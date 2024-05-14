import YAML from 'yaml';
import contentTypeParser from 'content-type';
import { mkdirSync, readFileSync, writeFileSync } from 'fs';
import { resolve } from 'path';
import { bundle }  from '@hyperjump/json-schema/bundle';
import { validate as validateJsonSchema, registerSchema }  from '@hyperjump/json-schema/draft-2020-12';
import { validate as validateOpenAPISpec } from '@hyperjump/json-schema/openapi-3-1';
import { addMediaTypePlugin } from '@hyperjump/browser';
import { buildSchemaDocument } from '@hyperjump/json-schema/experimental';
import { bundleOpenApiSpec } from './openapi-spec-bundler.js';
import { bundleJsonSchema } from './json-schema-bundler.js';

async function bundleSchema (schemaId) {
  addMediaTypePlugin('text/plain', {
    parse: async (response) => {
      const contentType = contentTypeParser.parse(response.headers.get('content-type') ?? '');
      const contextDialectId = contentType.parameters.schema ?? contentType.parameters.profile;
      
      const responseBody = JSON.parse(await response.text());
      return buildSchemaDocument(responseBody, response.url, contextDialectId);
    }
  });

  // This works for the Typescript generator out of the box
  // return bundle(manifestSchema.$id);

  // We have to use these customizations for the Python generator
  return bundleJsonSchema(schemaId);
}

async function validateSchema (schema, schemaId) {
  const output = await validateJsonSchema('https://json-schema.org/draft/2020-12/schema', schema, 'BASIC');
  if (output.valid) {
    console.info('JSON Schema - Ok');
  } else {
    console.error(`The JSON schema provided is not compliant with JSON schema Draft 2020-12!`);
    console.info('Schema Id: ', schemaId);
    console.info('Validation Output: \n', JSON.stringify(output, null, 2));
    process.exit(1);
  }
}

async function validateApiSpec (openApiSpec) {
  const output = await validateOpenAPISpec("https://spec.openapis.org/oas/3.1/schema-base", openApiSpec, 'BASIC');
  if (output.valid) {
    console.info('OpenAPI Specificaiton - Ok');
  } else {
    console.error(`The OpenAPI Specificaiton provided is not compliant with OpenAPI Specification 3.1!`);
    console.info('Validation Output: \n', JSON.stringify(output, null, 2));
    process.exit(1);
  }
}

async function main () {
  mkdirSync('./build', { recursive: true });

  const openApiSpec = YAML.parse(
    readFileSync('./open-api-spec.yml').toString()
  );
  
  let updatedSchemas = {}
  
  for (const [key, schema] of Object.entries(openApiSpec.components.schemas)) {
    // Get or create schemaId
    const schemaId = schema.$id || `urn:${key}`;
  
    schema.$schema = schema.$schema || 'https://json-schema.org/draft/2020-12/schema';
  
    registerSchema(schema, schemaId);
    
    const bundledSchema = await bundleSchema(schemaId);

    if (!bundledSchema) {
      console.error("Empty schema! ", schemaId);
    }

    writeFileSync(resolve(`./build/${key}.json`), JSON.stringify(bundledSchema, null, 2));
    
    await validateSchema(bundledSchema, schemaId);
    
    // OpenAPI doesn't like this keyword for some reason.
    delete bundledSchema.$schema;
  
    updatedSchemas[key] = bundledSchema;
  }

  openApiSpec.components.schemas = updatedSchemas;

  // The Typescript generator could use the above api spec directly,
  // but the Python generator needs to use some older syntax and more direct references.
  const bundledOpenApiSpec = bundleOpenApiSpec(openApiSpec)

  writeFileSync(resolve('./build/openapi-spec.json'), JSON.stringify(bundledOpenApiSpec, null, 2));
  
  await validateApiSpec(bundledOpenApiSpec);
  
  writeFileSync(resolve('./build/openapi-spec.json'), JSON.stringify(bundledOpenApiSpec, null, 2));
}
main();