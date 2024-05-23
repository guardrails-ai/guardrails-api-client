import fs from 'fs';
import path from 'path';

function buildReadme () {
  const files = fs.readdirSync('./docs');
  const readme = `# Guardrails API Client

Client libray for utilizing Guardrails AI via the API

## Installation
\`\`\`sh
pip install guardrails-api-client
\`\`\`

## Development
\`\`\`sh
git clone https://github.com/guardrails-ai/guardrails-api-client.git

cd guardrails-api-client

npm ci

cp ./service-specs/guardrails-service-spec.yml ./open-api-spec.yml

npm run openapi-gen

bash ./py-build.sh
\`\`\`

## Documentation For Models

${
  files
    .map(f => f.split('.').at(0))
    .map(f => ` - [${f}](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/${f}.md);`)
    .join('\n')
}
  `;

  fs.writeFileSync(path.resolve('./README.md'), readme);
}

function updateDependencies () {
  const pyProjectToml = fs.readFileSync(
    path.resolve('./pyproject.toml.template')
  ).toString();
  const requirementsTxt = fs.readFileSync(
    path.resolve('./requirements.txt')
  ).toString();
  const requirements = requirementsTxt.split('\n');

  const dependencies = `dependencies = [
${
  requirements
    .map(r => `"${r.trim().split('\s').join('')}"`)
    .join('\n')
}
]`;

  pyProjectToml.replace('dependencies = []', dependencies)

  

  fs.writeFileSync(
    path.resolve('./pyproject.toml'),
    pyProjectToml
  );
}

function buildSetupPy () {
  const requirementsTxt = fs.readFileSync(
    path.resolve('./requirements.txt')
  ).toString();
  const requirements = requirementsTxt
    .split('\n')
    .map(r => r.trim())
    .filter(r => r.length > 0)
    .map(r => `"${r}"`)
    .join(', ');
  const setupPy = `import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="guardrails-api-client",
    version="0.3.0",
    description="Guardrails API Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8, <4",
    install_requires=[${requirements}],
    package_data={"guardrails_api_client": ["py.typed"]},
)
  `;

  fs.writeFileSync(
    path.resolve('./setup.py'),
    setupPy
  )
}

function fixValidatorLogValidationResult () {
  const validatorLogValidationResultFilePath = path.resolve('./guardrails_api_client/models/validator_log_validation_result.py');
  const validatorLogValidationResultFile = fs.readFileSync(validatorLogValidationResultFilePath).toString();
  const validatorLogValidationResult = validatorLogValidationResultFile
    .replace('instance = ValidatorLogValidationResult.model_construct()', '');
    
  if (validatorLogValidationResultFile === validatorLogValidationResult) {
    console.warn("Fixes in fixValidatorLogValidationResult may no longer be necessary!")
  }

  fs.writeFileSync(validatorLogValidationResultFilePath, validatorLogValidationResult)
}

function fixModelSchemaDefaults () {
  // Assign generic type on Set in Schema.ts
  const modelSchemaFilePath = path.resolve('./guardrails_api_client/models/model_schema.py');
  const modelSchemaFile = fs.readFileSync(modelSchemaFilePath).toString();
  const modelSchema = modelSchemaFile
    .replace(
      'unique_items: Optional[StrictBool] = Field(default=False, alias="uniqueItems")',
      'unique_items: Optional[bool] = Field(default=None, alias="uniqueItems")'
    )
    .replace(
      '"uniqueItems": obj.get("uniqueItems") if obj.get("uniqueItems") is not None else False,',
      '"uniqueItems": obj.get("uniqueItems"),'
    )
    .replace(
      'deprecated: Optional[StrictBool] = False',
      'deprecated: Optional[bool] = None'
    )
    .replace(
      '"deprecated": obj.get("deprecated") if obj.get("deprecated") is not None else False,',
      '"deprecated": obj.get("deprecated"),'
    )
    .replace(
      'read_only: Optional[StrictBool] = Field(default=False, alias="readOnly")',
      'read_only: Optional[bool] = Field(default=None, alias="readOnly")'
    )
    .replace(
      '"readOnly": obj.get("readOnly") if obj.get("readOnly") is not None else False,',
      '"readOnly": obj.get("readOnly"),'
    )
    .replace(
      'write_only: Optional[StrictBool] = Field(default=False, alias="writeOnly")',
      'write_only: Optional[bool] = Field(default=None, alias="writeOnly")'
    )
    .replace(
      '"writeOnly": obj.get("writeOnly") if obj.get("writeOnly") is not None else False,',
      '"writeOnly": obj.get("writeOnly"),'
    )
    .replace(
      '_obj = cls.model_validate({',
      '_obj = cls.model_validate({\n\t\t\t**obj,',
    )
    
  if (modelSchemaFile === modelSchema) {
    console.warn("Fixes in fixModelSchemaDefaults may no longer be necessary!")
  }

  fs.writeFileSync(modelSchemaFilePath, modelSchema)
}

function fixGuardHistory () {
  // Assign generic type on Set in Schema.ts
  const guardFilePath = path.resolve('./guardrails_api_client/models/guard.py');
  const guardFile = fs.readFileSync(guardFilePath).toString();
  const guard = guardFile
    .replace(
      'history: Optional[GuardHistory] = None',
      'i_history: Optional[GuardHistory] = Field(default=None, alias="history")'
    )
    
  if (guardFile === guard) {
    console.warn("Fixes in fixGuardHistory may no longer be necessary!")
  }

  fs.writeFileSync(guardFilePath, guard)
}

function hotFixes () {
  fixValidatorLogValidationResult();
  fixModelSchemaDefaults();
  fixGuardHistory();
}

function globalReplacements () {
  const files = [
    ...fs.readdirSync('./guardrails_api_client/models').map(file => `./models/${file}`),
  ];

  for (const file of files) {
    const filePath = path.resolve('./guardrails_api_client', file);
    let fileContent = fs.readFileSync(filePath).toString();

    fs.writeFileSync(
      filePath,
      fileContent
        .replace(/from guardrails_api_client.models.object import object/g, '')
    );
  }
}

function main () {
  globalReplacements();
  hotFixes();
  buildReadme();
  updateDependencies();
  buildSetupPy();
}
main();