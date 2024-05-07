import { bundle }  from '@hyperjump/json-schema/bundle';
import _ from 'lodash';


function useDefs (property) {
  if (property.$ref) {
    if (_.isString(property.$ref)) {
      // Replace absolute URI's with $def reference
      if (property.$ref.startsWith("https")) {
        property.$ref = `#/$defs/${property.$ref.split("/").at(-1).split(".json").at(0)}`
      } else if (property.$ref.startsWith("meta/")) {
        property.$ref = `#/$defs/${property.$ref.split("meta/").at(-1)}`
      }

      const realtiveRefClosures = property.$ref.split("#");
      if (realtiveRefClosures.length > 2) {
        property.$ref = `#${realtiveRefClosures.join("")}`;
      }

    } else {
      property.$ref = useDefs(property.$ref);
    }
  }

  // This is a hack; some tools don't support dynamicRef's yet
  // if (property.$dynamicRef && property.$dynamicRef === '#meta') {
    // This is what we want to do, but many tools also can't support circular structures 
    // property.$ref = "#/$defs/schema";
    
    // Since most of the dynamicRef's are to say that additionalProperties should be a schema,
    //    we can just remove it and let it be an anonymous object.
    // delete property.$dynamicRef;
  // }
  
  if (property.properties) {
    property.properties = updateRefs(property.properties)
  }
  
  if (property.additionalProperties) {
    property.additionalProperties = useDefs(property.additionalProperties)
  }

  if (property.items) {
    property.items = useDefs(property.items)
  }

  if (property.allOf) {
    property.allOf = property.allOf.map(useDefs)
  }

  if (property.anyOf) {
    property.anyOf = property.anyOf.map(useDefs)
  }

  if (property.oneOf) {
    property.oneOf = property.oneOf.map(useDefs)
  }

  return property;
}

function updateRefs (properties) {
  return Object.fromEntries(
    Object.entries(properties)
      .map(([key, value]) => {
        // if (key === "$dynamicRef") {
        //   return 
        // }
        return [key, useDefs(value)]
      })
  );
}

function updateDefs (schema) {
  return Object.fromEntries(
    Object.entries(schema.$defs)
      .map(([key, value]) => {
        if (key.endsWith(".json")) {
          key = key.split(".json").at(0);
          value.$id = key;
        } 
        if (key.startsWith("https")) {
          key = key.split("/").at(-1);
          value.$id = key;
        }
        return [key, value];
      })
  );
}

function hoistDefs (schema) {
  const hoistedDefs = Object.values(schema.$defs)
    .reduce((acc, value) => {
      if (value.$defs) {
        Object.entries(value.$defs).forEach(([key, value]) => {
          acc[key] = value;
        });
      }
      return acc;
    }, {});
  return {
    ...hoistedDefs,
    ...schema.$defs
  };
}

export async function bundleJsonSchema (schemaId) {
  let bundledSchema = await bundle(schemaId);
  bundledSchema.$id = schemaId;

  if (bundledSchema.$defs) {
    bundledSchema.$defs = hoistDefs(bundledSchema);
    bundledSchema.$defs = updateDefs(bundledSchema);
    bundledSchema.$defs = updateRefs(bundledSchema.$defs);
  }
  
  if (bundledSchema.properties) {
    bundledSchema.properties = updateRefs(bundledSchema.properties);
  } else {
    bundledSchema = useDefs(bundledSchema);
  }

  return bundledSchema;
}


