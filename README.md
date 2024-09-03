# guardrails-api-client
OpenAPI Specifications and scripts for generating SDKs for the various Guardrails services.

## Auto Generated Libraries

### Python
PyPI Page: https://pypi.org/project/guardrails-api-client
API Ref: https://github.com/guardrails-ai/guardrails-api-client/blob/main/resources/py/README.md#documentation-for-models

### Typescript/Javascript
NPM Page: https://www.npmjs.com/package/@guardrails-ai/api-client
API Ref: https://github.com/guardrails-ai/guardrails-api-client/blob/HEAD/resources/ts/docs/modules.md

## Local Development

### Repository Structure & Code Generation Process

#### TL;DR;
Go to the `package.json` and follow the code path for `npm run build`.


#### Long Explanation
OpenAPI Specifications are stored in the `service-specs` directory. Currently this is only the specification for the `guardrails-api`.

The shell scripts in root directory are orchestrator scripts used in the build process.  They primarily handle filesystem and environment changes and handoff more specific jobs to the scripts located in variours subdirectores of `resources`.

General, non-language specific scripts are located in `./resources/scripts`. These primarily deal with discrepancies between JSON Schema Draft 2020-12 and OpenAPI Specification 3.1.

`resources/scripts/gen-openapi-spec.js`, takes the OpenAPI Specification, hydrates it with remote references, hoists sub-schemas and fixes their relative reference paths, downgrades some keywords to a dialect that [openapi-generator](https://openapi-generator.tech/) understands (e.g. `$defs` vs `definitions`), then writes out the OpenAPI Specification as JSON to `./build/openapi-spec.json`.

This OpenAPI Specification is then used by [openapi-generator](https://openapi-generator.tech/) to generate types, interfaces, or classes along with a REST client for any given language we want to support; currently this includes Python and Typescript.  This generated code is close but not perfect so we do employ some custom post-processing scripts to make inline fixes.

Scripts for making inline fixes for a particular language's generated code, as well as some boilerplate files for defining the publishable libraries, can be found within the language code directories under the `resources` directory: e.g. `./resources/py` and `./resources/ts`.  Each has a `resources/{lang-code}/scripts/prebuild.js` script where these inline fixes are written.  Generally, these fixes are things like making types for specific, fixing property names that would otherwise be considered reserved keywors, etc..  These scripts, as well as the general scripts under `./resources/scripts`, are written using javascript for two primary reasons:
1. Javascript has more advanced regex support.
2. Javascript has better JSON Schema and OpenAPI Specification tooling (like the `@hyperjump` packages).

We also employ linter/formatters to standardize the final generated code.  For Python we use [ruff](https://docs.astral.sh/ruff/).  For Tyescript we use [prettier](https://prettier.io/).


###  Getting Setup For Local Development
What you'll need:
- [Java](https://formulae.brew.sh/formula/openjdk)
- [NodeJs](https://formulae.brew.sh/formula/node)
- [Python](https://docs.brew.sh/Homebrew-and-Python)

Install dependencies with `npm ci`

Try running `npm run build` and address an issues you may encounter.

For example, dependening on your specific machine you may need to setup some environment variables for Java:
```bash
# Java/OpenJDK
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"
export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
```


### Testing Changes Locally
1. Make your changes to the OpenAPI Specification or related JSON Schemas in the [interfaces](https://github.com/guardrails-ai/interfaces) repository.
2. `npm run build`
3. Install the lang-code directory of whichever language you're testing in the consuming project. For example, install `./resources/py` with pip via it's absolute path into the guardrails open source package.
