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
    description="Guardrails API Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8, <4",
    install_requires=[${requirements}],
    package_data={"guardrails_api_client": ["py.typed", "openapi-spec.json"]},
)
  `;

  fs.writeFileSync(
    path.resolve('./setup.py'),
    setupPy
  )
}



function fixValidationResult() {
  const validationResultsFilePath = path.resolve('./guardrails_api_client/models/validation_result.py');
  const validationResultsFile = fs.readFileSync(validationResultsFilePath).toString();
  const validationResults = validationResultsFile
    .replace(
      '_obj = cls.model_validate({',
      '_obj = cls.model_validate({\n\t\t\t"metadata": obj.get("metadata"),'
    )
    
  if (validationResultsFile === validationResults) {
    console.warn("Fixes in fixValidationResults may no longer be necessary!")
  }

  fs.writeFileSync(validationResultsFilePath, validationResults)
}

function fixPassResult() {
  const passResultFilePath = path.resolve('./guardrails_api_client/models/pass_result.py');
  const passResultFile = fs.readFileSync(passResultFilePath).toString();
  const passResult = passResultFile
    .replace(
      '_obj = cls.model_validate({',
      '_obj = cls.model_validate({\n\t\t\t"metadata": obj.get("metadata"),\n\t\t\t"value_override": obj.get("value_override"),'
    )
    
  if (passResultFile === passResult) {
    console.warn("Fixes in fixPassResult may no longer be necessary!")
  }

  fs.writeFileSync(passResultFilePath, passResult)
}

function fixFailResult() {
  const failResultFilePath = path.resolve('./guardrails_api_client/models/fail_result.py');
  const failResultFile = fs.readFileSync(failResultFilePath).toString();
  const failResult = failResultFile
  .replace(
    '_obj = cls.model_validate({',
    '_obj = cls.model_validate({\n\t\t\t"error_message": obj.get("error_message"),\n\t\t\t"fix_value": obj.get("fix_value"),\n\t\t\t"error_spans": [ErrorSpan.from_dict(es) for es in obj.get("error_spans", [])],\n\t\t\t"metadata": obj.get("metadata"),'
  )

  if (failResultFile === failResult) {
    console.warn("Fixes in fixFailResult may no longer be necessary!")
  }

  fs.writeFileSync(failResultFilePath, failResult)
}

function fixValidationResults() {
  fixValidationResult();
  fixPassResult();
  fixFailResult();
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

function fixCallException () {
  const callFilePath = path.resolve('./guardrails_api_client/models/call.py');
  const callFile = fs.readFileSync(callFilePath).toString();
  const call = callFile
    .replace(
      'from pydantic import BaseModel, ConfigDict',
      'from pydantic import BaseModel, ConfigDict, Field'
    )
    .replace(
      'exception: Optional[CallException] = None',
      'i_exception: Optional[CallException] = Field(default=None, alias="exception")'
    )
    .replace(
      /self.exception/g,
      'self.i_exception'
    )
    
  if (callFile === call) {
    console.warn("Fixes in fixCallException may no longer be necessary!")
  }

  fs.writeFileSync(callFilePath, call)
}

function fixValidatorReferenceTypes () {
  const validatorReferenceFilePath = path.resolve('./guardrails_api_client/models/validator_reference.py');
  const validatorReferenceFile = fs.readFileSync(validatorReferenceFilePath).toString();
  const validatorReference = validatorReferenceFile
    .replace(
      'id: Optional[Any] = Field(description="The unique identifier for this Validator.  Often the hub id; e.g. guardrails/regex_match")',
      'id: Optional[str] = Field(description="The unique identifier for this Validator.  Often the hub id; e.g. guardrails/regex_match")'
    )
    .replace(
      'on: Optional[Any] = Field(default=None, description="A reference to the property this validator should be applied against.  Can be a valid JSON path or a meta-property such as \\"prompt\\" or \\"output\\"")',
      'on: Optional[str] = Field(default=None, description="A reference to the property this validator should be applied against.  Can be a valid JSON path or a meta-property such as \\"prompt\\" or \\"output\\"")'
    )
    .replace(
      'on_fail: Optional[Any] = Field(default=None, alias="onFail")',
      'on_fail: Optional[str] = Field(default=None, alias="onFail")'
    )
    .replace(
      '"args": obj.get("args"),',
      '**obj,\n"args": obj.get("args"),'
    )
    
  if (validatorReferenceFile === validatorReference) {
    console.warn("Fixes in fixValidatorReferenceTypes may no longer be necessary!")
  }

  fs.writeFileSync(validatorReferenceFilePath, validatorReference)
}

function exportAll (filePath) {
  const initFilePath = path.resolve(filePath);
  const initFile = fs.readFileSync(initFilePath).toString();

  if (!initFile.includes('__all__')) {
    const importMatches = initFile.matchAll(/from (?:\S)+ import (?<exportName>(\S)+)/g);
  
    const allExports = [];
    
    for (const match of importMatches) {
      allExports.push(match.groups.exportName);
    }
  
    const init = `${initFile}\n\n__all__ = [\n${allExports.map(e => `\t"${e}"`).join(',\n')}\n]\n`;
  
    
    
    fs.writeFileSync(initFilePath, init)
  } else {
    console.warn(`Fixes in fixInits may no longer be necessary for file ${filePath}!`)
  }
}


function fixInits () {
  exportAll('./guardrails_api_client/__init__.py');
  exportAll('./guardrails_api_client/models/__init__.py');
  exportAll('./guardrails_api_client/api/__init__.py');
}

function hotFixes () {
  fixValidatorLogValidationResult();
  fixValidationResults();
  fixModelSchemaDefaults();
  fixCallException();
  fixValidatorReferenceTypes();
  fixInits();
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
        .replace(
          '"args": [object.from_dict(_item) for _item in obj["args"]] if obj.get("args") is not None else None,',
          '"args": obj.get("args"),'
        )
        // TODO: Find a regex for these
        .replace(
          '"validated_chunk": object.from_dict(obj["validated_chunk"]) if obj.get("validated_chunk") is not None else None',
          '"validated_chunk": obj.get("validated_chunk")'
        )
        .replace(
          '"incorrectValue": object.from_dict(obj["incorrectValue"]) if obj.get("incorrectValue") is not None else None,',
          '"incorrectValue": obj.get("incorrectValue"),'
        )
        .replace(
          '"valueBeforeValidation": object.from_dict(obj["valueBeforeValidation"]) if obj.get("valueBeforeValidation") is not None else None,',
          '"valueBeforeValidation": obj.get("valueBeforeValidation"),'
        )
        .replace(
          '"valueAfterValidation": object.from_dict(obj["valueAfterValidation"]) if obj.get("valueAfterValidation") is not None else None,',
          '"valueAfterValidation": obj.get("valueAfterValidation"),'
        )
        .replace(
          '_items.append(_item.to_dict())',
          '_items.append(_item.to_dict() if hasattr(_item, "to_dict") and callable(_item.to_dict) else _item)'
        )
        .replace(
          "_dict['validated_chunk'] = self.validated_chunk.to_dict()",
          "_dict['validated_chunk'] = self.validated_chunk"
        )
        .replace(
          "_dict['incorrectValue'] = self.incorrect_value.to_dict()",
          "_dict['incorrectValue'] = self.incorrect_value"
        )
        .replace(
          "_dict['valueBeforeValidation'] = self.value_before_validation.to_dict()",
          "_dict['valueBeforeValidation'] = self.value_before_validation"
        )
        .replace(
          "_dict['valueAfterValidation'] = self.valueAfterValidation.to_dict()",
          "_dict['valueAfterValidation'] = self.valueAfterValidation"
        )
        .replace(
          "_dict['valueAfterValidation'] = self.value_after_validation.to_dict()",
          "_dict['valueAfterValidation'] = self.value_after_validation"
        )
        .replace(
          'error_message: Optional[Any] = Field(alias="errorMessage")',
          'error_message: Optional[str] = Field(alias="errorMessage")'
        )
        .replace(
          'outcome: Optional[Any]',
          'outcome: Optional[str]'
        )
        .replace(
          /\: StrictStr/g,
          ': str'
        )
        .replace(
          /\[StrictStr]/g,
          '[str]'
        )
        .replace(
          /\: StrictBool/g,
          ': bool'
        )
        .replace(
          /\[StrictBool]/g,
          '[bool]'
        )
        .replace(
          /\: StrictInt/g,
          ': int'
        )
        .replace(
          /\[StrictInt]/g,
          '[int]'
        )
        .replace(
          /\: StrictFloat/g,
          ': float'
        )
        .replace(
          /\[StrictFloat]/g,
          '[float]'
        )
        .replace(
          'start_time: Optional[datetime] = Field(default=None, alias="startTime")',
          'start_time: Optional[str] = Field(default=None, alias="startTime")'
        )
        .replace(
          'end_time: Optional[datetime] = Field(default=None, alias="endTime")',
          'end_time: Optional[str] = Field(default=None, alias="endTime")'
        )
        
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