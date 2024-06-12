const fs = require('fs');
const path = require('path');

function globalReplacements () {
  const files = [
    ...fs.readdirSync('./src/apis').map(file => `./apis/${file}`),
    ...fs.readdirSync('./src/models').map(file => `./models/${file}`),
  ];

  for (const file of files) {
    const filePath = path.resolve('./src', file);
    let fileContent = fs.readFileSync(filePath).toString();
    
    fs.writeFileSync(
      filePath,
      fileContent
        // .replace(/: object/g, ': { [key: string]: any }')  // This is a case of the generators author not following proper typing; should probably submit a PR for this one.
        // .replace(/{object}/g, ': {{ [key: string]: any }}')
        .replace(/.map\(anyFromJSON\)/g, '')
        .replace(/.map\(anyToJSON\)/g, '')
        .replace(/anyFromJSON/g, '')
        .replace(/anyToJSON/g, '')
    );
  }
}

function fixSchema () {
  // Assign generic type on Set in Schema.ts
  const schemaFilePath = path.resolve('./src/models/Schema.ts');
  const schemaFile = fs.readFileSync(schemaFilePath).toString();
  const schema = schemaFile
    .replace('dependencies?: { [key: string]: Set; };', 'dependencies?: { [key: string]: Set<any>; };')
    .replace('@type {{ [key: string]: Set; }}', '@type {{ [key: string]: Set<any>; }}');
    
  if (schemaFile === schema) {
    console.warn("Fixes in fixSchema may no longer be necessary!")
  }

  fs.writeFileSync(schemaFilePath, schema)
}

function fixValidatorReference () {
  // Give ValidatorReference.on a proper unioned type
  const validatorReferenceFilePath = path.resolve('./src/models/ValidatorReference.ts');
  const validatorReference = fs.readFileSync(validatorReferenceFilePath)
    .toString()
    .replace(/ FromJSON/g, ' ')
    .replace(/ ToJSON/g, ' ')
    .replace('on?: ;', 'on?: OnType;')
    .replace('* @type {}', '* @type {OnType}')
    .concat(`
  /**
  * @export
  */
  export type OnType = 'prompt' | 'instructions' | 'msg_history' | 'output' | '$.foo.bar' | string;
  `);
  
  fs.writeFileSync(validatorReferenceFilePath, validatorReference)
}

function fixCall () {
  const callException = fs.readFileSync(
    path.resolve('./templates/CallException.ts')
  ).toString();
  fs.writeFileSync(path.resolve('./src/models/CallException.ts'), callException)

  const callFilePath = path.resolve('./src/models/Call.ts');
  const callFile = fs.readFileSync(callFilePath).toString();
  const call = callFile
    .replace('exception?: CallException;', 'exception?: string | CallException;')
    .replace('@type {CallException}', '@type {string | CallException}');

  if (callFile === call) {
    console.warn("Fixes in fixCall may no longer be necessary!")
  }

  fs.writeFileSync(callFilePath, call);
}

function fixGuard () {
  const guardHistory = fs.readFileSync(
    path.resolve('./templates/GuardHistory.ts')
  ).toString();
  fs.writeFileSync(path.resolve('./src/models/GuardHistory.ts'), guardHistory)

  const guardFilePath = path.resolve('./src/models/Guard.ts');
  const guardFile = fs.readFileSync(guardFilePath).toString();
  const guard = guardFile
    .replace('import type { GuardHistory } from \'./GuardHistory\';', 'import type { Call } from "./Call";\nimport type { GuardHistory } from "./GuardHistory";')
    .replace('history?: GuardHistory;', 'history?: Call[] | GuardHistory;')
    .replace('@type {GuardHistory}', '@type {Call[] | GuardHistory}');
    
  if (guardFile === guard) {
    console.warn("Fixes in fixGuard may no longer be necessary!")
  }

  fs.writeFileSync(guardFilePath, guard);
}

function fixOutputs () {
  const outputsValidationResponse = fs.readFileSync(
    path.resolve('./templates/OutputsValidationResponse.ts')
  ).toString();
  fs.writeFileSync(path.resolve('./src/models/OutputsValidationResponse.ts'), outputsValidationResponse)

  // Replace useless interfaces with string or json union
  const outputsFilePath = path.resolve('./src/models/Outputs.ts');
  const outputsFile = fs.readFileSync(outputsFilePath).toString();
  const outputs = outputsFile
    .replace('parsedOutput?: OutputsParsedOutput;', 'parsedOutput?: string | Record<string, any>;')
    .replace('guardedOutput?: OutputsParsedOutput;', 'guardedOutput?: string | Record<string, any>;')
    .replace(/@type {OutputsParsedOutput}/g, '@type {string | Record<string, any>}')
    .replace('validationResponse?: OutputsValidationResponse;', 'validationResponse?: string | Reask | Record<string, any>;')
    .replace('type {OutputsValidationResponse}', '@type {string | Reask | Record<string, any>}')
    
  if (outputsFile === outputs) {
    console.warn("Fixes in fixOutputs may no longer be necessary!")
  }

  fs.writeFileSync(outputsFilePath, outputs)
}

function fixValidationOutcome () {
  // Replace useless interfaces with string or json union
  const validationOutcomeFilePath = path.resolve('./src/models/ValidationOutcome.ts');
  const validationOutcomeFile = fs.readFileSync(validationOutcomeFilePath).toString();
  const validationOutcome = validationOutcomeFile
    .replace('validatedOutput?: ValidationOutcomeValidatedOutput;', 'validatedOutput?: string | Record<string, any>;')
    .replace('@type {ValidationOutcomeValidatedOutput}', '@type {string | Record<string, any>}');
    
  if (validationOutcomeFile === validationOutcome) {
    console.warn("Fixes in fixValidationOutcome may no longer be necessary!")
  }
  
  fs.writeFileSync(validationOutcomeFilePath, validationOutcome)
}

function fixValidatorLog () {
  // Replace useless interfaces with string or int union
  const validatorLogFilePath = path.resolve('./src/models/ValidatorLog.ts');
  const validatorLogFile = fs.readFileSync(validatorLogFilePath).toString();
  const validatorLog = validatorLogFile
    .replace('instanceId?: ValidatorLogInstanceId;', 'instanceId?: string | number;')
    .replace('@type {ValidatorLogInstanceId}', '@type {string | number}')
    .replace('ValidatorLogInstanceIdToJSON(value[\'instanceId\'])', 'value["instanceId"]')
    .replace('ValidatorLogInstanceIdFromJSON(json[\'instanceId\'])', 'json["instanceId"]');

  if (validatorLogFile === validatorLog) {
    console.warn("Fixes in fixValidatorLog may no longer be necessary!")
  }

    // TODO: validationResult
    
  
  fs.writeFileSync(validatorLogFilePath, validatorLog)
}

function hotFixes () {
  fixSchema();
  fixValidatorReference();
  fixCall();
  fixGuard();
  fixOutputs();
  fixValidationOutcome();
  fixValidatorLog();
}


function main () {
  globalReplacements();
  hotFixes();
}
main();