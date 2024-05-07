import _ from 'lodash';

// We have to break the JSON schemas to get them to work with the generators specific understanding of OpenAPI Specification 3.1
function breakToFix (schema) {  
  return Object.entries(schema)
    .reduce((acc, [key, value]) => {
      if (key !== '$id' && key !== "$schema") { // We have to remove $id and $schema
        if (key === "$defs") { // switch from $defs to definitions
          key = "definitions"
        } else if (key == "$ref" && _.isString(value)) {
          value = value.startsWith("#/$defs") ?
            value.replace("#/$defs", `#/components/schemas`) : // Use hoisted $defs, now named schemas
            value.replace("#/", `#/components/schemas/`) // Fix relative references wrt OpenAPI Spec
          
          value = value.includes("/$defs/") ?
            value.replace("/$defs/", "/definitions/") :
            value;
        }

        if (_.isPlainObject(value)) {
          acc[key] = breakToFix(value);
        } else if (Array.isArray(value) && _.isPlainObject(value.at(0))) {
          acc[key] = value.map(v => breakToFix(v));
        } else {
          acc[key] = value;
        }
      }
      return acc
    }, {});
}

function updateSchemas (schema, schemaName) {
  const { $defs } = schema;
  if ($defs) {
    delete schema.$defs;
  }

  const schemas = {
    [schemaName]: schema,
    ...$defs
  }
  
  return breakToFix(
    schemas
  );
}
export function bundleOpenApiSpec (openApiSpec) {
  const schemas = _.cloneDeep(openApiSpec.components.schemas);
  openApiSpec.components.schemas = Object.entries(schemas).reduce((acc, [schemaName, schema]) => {
    const updatedSchemas = updateSchemas(schema, schemaName);
    acc = {
      ...acc,
      ...updatedSchemas
    }
    return acc;
  }, {});
  return openApiSpec;
}