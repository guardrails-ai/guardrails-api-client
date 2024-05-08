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
  // Assign generic type on Set in Schema.ts
  const validatorLogValidationResultFilePath = path.resolve('./guardrails_api_client/models/validator_log_validation_result.py');
  const validatorLogValidationResultFile = fs.readFileSync(validatorLogValidationResultFilePath).toString();
  const validatorLogValidationResult = validatorLogValidationResultFile
    .replace('instance = ValidatorLogValidationResult.model_construct()', '');
    
  if (validatorLogValidationResultFile === validatorLogValidationResult) {
    console.warn("Fixes in fixValidatorLogValidationResult may no longer be necessary!")
  }

  fs.writeFileSync(validatorLogValidationResultFilePath, validatorLogValidationResult)
}

function hotFixes () {
  fixValidatorLogValidationResult();
}

function main () {
  hotFixes();
  buildReadme();
  updateDependencies();
  buildSetupPy();
}
main();