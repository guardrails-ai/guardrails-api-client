import fs  from 'fs';
import { resolve }  from 'path';
import { validate }  from '@hyperjump/json-schema/draft-2020-12';

async function main () {
  const [
    _execPath,
    _thisFile,
    filepath
  ] = process.argv;

  if (!filepath) throw new Error("A filepath is required as the first argument for this script!");

  const schema = JSON.parse(
    fs.readFileSync(
      resolve(filepath)
    ).toString()
  );

  const output = await validate("https://json-schema.org/draft/2020-12/schema", schema, "DETAILED");
  if (output.valid) {
    console.info(`JSON Schema: ${filepath} - Ok`)
    process.exit(0);
  } else {
    console.error(`The schema located at ${filepath} is not compliant with JSON schema Draft 2020-12!`);
    console.error("Validation Output: \n", JSON.stringify(output, null, 2));
    process.exit(1);
  }
}
main()