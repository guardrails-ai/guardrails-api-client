# Guardrails API Client

Client libray for utilizing Guardrails AI via the API

## Installation
```sh
pip install guardrails-api-client
```

## Development
```sh
git clone https://github.com/guardrails-ai/guardrails-api-client.git

cd guardrails-api-client

npm ci

cp ./service-specs/guardrails-service-spec.yml ./open-api-spec.yml

npm run openapi-gen

bash ./py-build.sh
```

## Documentation For Models

 - [AnyType](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/AnyType.md);
 - [Applicator](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Applicator.md);
 - [ArgsAndKwargs](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ArgsAndKwargs.md);
 - [ArraysInner](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ArraysInner.md);
 - [Call](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Call.md);
 - [CallInputs](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/CallInputs.md);
 - [Content](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Content.md);
 - [Core](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Core.md);
 - [ErrorSpan](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ErrorSpan.md);
 - [FailResult](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/FailResult.md);
 - [FormatAnnotation](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/FormatAnnotation.md);
 - [Guard](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Guard.md);
 - [GuardApi](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/GuardApi.md);
 - [HealthCheck](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/HealthCheck.md);
 - [HttpError](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/HttpError.md);
 - [Inputs](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Inputs.md);
 - [Iteration](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Iteration.md);
 - [LLMResource](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/LLMResource.md);
 - [LLMResponse](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/LLMResponse.md);
 - [MetaData](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/MetaData.md);
 - [ModelSchema](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ModelSchema.md);
 - [Outputs](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Outputs.md);
 - [OutputsParsedOutput](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/OutputsParsedOutput.md);
 - [OutputsValidationResponse](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/OutputsValidationResponse.md);
 - [PassResult](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/PassResult.md);
 - [Primitives](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Primitives.md);
 - [Reask](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Reask.md);
 - [ServiceHealthApi](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ServiceHealthApi.md);
 - [SimpleTypes](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/SimpleTypes.md);
 - [Unevaluated](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Unevaluated.md);
 - [ValidateApi](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidateApi.md);
 - [ValidatePayload](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidatePayload.md);
 - [Validation](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/Validation.md);
 - [ValidationOutcome](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidationOutcome.md);
 - [ValidationOutcomeValidatedOutput](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidationOutcomeValidatedOutput.md);
 - [ValidationResult](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidationResult.md);
 - [ValidationType](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidationType.md);
 - [ValidatorLog](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidatorLog.md);
 - [ValidatorLogInstanceId](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidatorLogInstanceId.md);
 - [ValidatorLogValidationResult](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidatorLogValidationResult.md);
 - [ValidatorReference](https://github.com/guardrails-ai/guardrails-api-client/tree/main/resources/py/docs/ValidatorReference.md);
  