[@guardrails-ai/api-client](README.md) / Exports

# @guardrails-ai/api-client

## Table of contents

### Classes

- [BaseAPI](classes/BaseAPI.md)
- [BlobApiResponse](classes/BlobApiResponse.md)
- [Configuration](classes/Configuration.md)
- [FetchError](classes/FetchError.md)
- [GuardApi](classes/GuardApi.md)
- [JSONApiResponse](classes/JSONApiResponse.md)
- [OpenaiApi](classes/OpenaiApi.md)
- [RequiredError](classes/RequiredError.md)
- [ResponseError](classes/ResponseError.md)
- [ServiceHealthApi](classes/ServiceHealthApi.md)
- [TextApiResponse](classes/TextApiResponse.md)
- [ValidateApi](classes/ValidateApi.md)
- [VoidApiResponse](classes/VoidApiResponse.md)

### Interfaces

- [AnyType](interfaces/AnyType.md)
- [ApiResponse](interfaces/ApiResponse.md)
- [Applicator](interfaces/Applicator.md)
- [ArgsAndKwargs](interfaces/ArgsAndKwargs.md)
- [ArraysInner](interfaces/ArraysInner.md)
- [Call](interfaces/Call.md)
- [CallInputs](interfaces/CallInputs.md)
- [ConfigurationParameters](interfaces/ConfigurationParameters.md)
- [Consume](interfaces/Consume.md)
- [Content](interfaces/Content.md)
- [Core](interfaces/Core.md)
- [CreateGuardRequest](interfaces/CreateGuardRequest.md)
- [DeleteGuardRequest](interfaces/DeleteGuardRequest.md)
- [ErrorContext](interfaces/ErrorContext.md)
- [ErrorSpan](interfaces/ErrorSpan.md)
- [FailResult](interfaces/FailResult.md)
- [FetchParams](interfaces/FetchParams.md)
- [FormatAnnotation](interfaces/FormatAnnotation.md)
- [GetGuardHistoryRequest](interfaces/GetGuardHistoryRequest.md)
- [GetGuardRequest](interfaces/GetGuardRequest.md)
- [Guard](interfaces/Guard.md)
- [GuardApiInterface](interfaces/GuardApiInterface.md)
- [HealthCheck](interfaces/HealthCheck.md)
- [HttpError](interfaces/HttpError.md)
- [Inputs](interfaces/Inputs.md)
- [Iteration](interfaces/Iteration.md)
- [LLMResponse](interfaces/LLMResponse.md)
- [MetaData](interfaces/MetaData.md)
- [Middleware](interfaces/Middleware.md)
- [OpenAIChatCompletion](interfaces/OpenAIChatCompletion.md)
- [OpenAIChatCompletionPayload](interfaces/OpenAIChatCompletionPayload.md)
- [OpenAIChatCompletionPayloadMessagesInner](interfaces/OpenAIChatCompletionPayloadMessagesInner.md)
- [OpenaiApiInterface](interfaces/OpenaiApiInterface.md)
- [OpenaiChatCompletionRequest](interfaces/OpenaiChatCompletionRequest.md)
- [Outputs](interfaces/Outputs.md)
- [OutputsParsedOutput](interfaces/OutputsParsedOutput.md)
- [OutputsValidationResponse](interfaces/OutputsValidationResponse.md)
- [PassResult](interfaces/PassResult.md)
- [Primitives](interfaces/Primitives.md)
- [Reask](interfaces/Reask.md)
- [RequestContext](interfaces/RequestContext.md)
- [RequestOpts](interfaces/RequestOpts.md)
- [ResponseContext](interfaces/ResponseContext.md)
- [ResponseTransformer](interfaces/ResponseTransformer.md)
- [Schema](interfaces/Schema.md)
- [ServiceHealthApiInterface](interfaces/ServiceHealthApiInterface.md)
- [Unevaluated](interfaces/Unevaluated.md)
- [UpdateGuardRequest](interfaces/UpdateGuardRequest.md)
- [ValidateApiInterface](interfaces/ValidateApiInterface.md)
- [ValidatePayload](interfaces/ValidatePayload.md)
- [ValidateRequest](interfaces/ValidateRequest.md)
- [Validation](interfaces/Validation.md)
- [ValidationOutcome](interfaces/ValidationOutcome.md)
- [ValidationOutcomeValidatedOutput](interfaces/ValidationOutcomeValidatedOutput.md)
- [ValidationResult](interfaces/ValidationResult.md)
- [ValidationSummary](interfaces/ValidationSummary.md)
- [ValidationType](interfaces/ValidationType.md)
- [ValidatorLog](interfaces/ValidatorLog.md)
- [ValidatorLogInstanceId](interfaces/ValidatorLogInstanceId.md)
- [ValidatorLogValidationResult](interfaces/ValidatorLogValidationResult.md)
- [ValidatorReference](interfaces/ValidatorReference.md)

### Type Aliases

- [FetchAPI](modules.md#fetchapi)
- [HTTPBody](modules.md#httpbody)
- [HTTPHeaders](modules.md#httpheaders)
- [HTTPMethod](modules.md#httpmethod)
- [HTTPQuery](modules.md#httpquery)
- [HTTPRequestInit](modules.md#httprequestinit)
- [InitOverrideFunction](modules.md#initoverridefunction)
- [Json](modules.md#json)
- [LLMResource](modules.md#llmresource)
- [ModelPropertyNaming](modules.md#modelpropertynaming)
- [OnType](modules.md#ontype)
- [SimpleTypes](modules.md#simpletypes)
- [ValidationResultOutcomeEnum](modules.md#validationresultoutcomeenum)
- [ValidationSummaryValidatorStatusEnum](modules.md#validationsummaryvalidatorstatusenum)
- [ValidatorLogValidationResultOutcomeEnum](modules.md#validatorlogvalidationresultoutcomeenum)
- [ValidatorReferenceOnFailEnum](modules.md#validatorreferenceonfailenum)

### Variables

- [BASE\_PATH](modules.md#base_path)
- [COLLECTION\_FORMATS](modules.md#collection_formats)
- [DefaultConfig](modules.md#defaultconfig)
- [LLMResource](modules.md#llmresource-1)
- [SimpleTypes](modules.md#simpletypes-1)
- [ValidationResultOutcomeEnum](modules.md#validationresultoutcomeenum-1)
- [ValidationSummaryValidatorStatusEnum](modules.md#validationsummaryvalidatorstatusenum-1)
- [ValidatorLogValidationResultOutcomeEnum](modules.md#validatorlogvalidationresultoutcomeenum-1)
- [ValidatorReferenceOnFailEnum](modules.md#validatorreferenceonfailenum-1)

### Functions

- [AnyTypeFromJSON](modules.md#anytypefromjson)
- [AnyTypeFromJSONTyped](modules.md#anytypefromjsontyped)
- [AnyTypeToJSON](modules.md#anytypetojson)
- [AnyTypeToJSONTyped](modules.md#anytypetojsontyped)
- [ApplicatorFromJSON](modules.md#applicatorfromjson)
- [ApplicatorFromJSONTyped](modules.md#applicatorfromjsontyped)
- [ApplicatorToJSON](modules.md#applicatortojson)
- [ApplicatorToJSONTyped](modules.md#applicatortojsontyped)
- [ArgsAndKwargsFromJSON](modules.md#argsandkwargsfromjson)
- [ArgsAndKwargsFromJSONTyped](modules.md#argsandkwargsfromjsontyped)
- [ArgsAndKwargsToJSON](modules.md#argsandkwargstojson)
- [ArgsAndKwargsToJSONTyped](modules.md#argsandkwargstojsontyped)
- [ArraysInnerFromJSON](modules.md#arraysinnerfromjson)
- [ArraysInnerFromJSONTyped](modules.md#arraysinnerfromjsontyped)
- [ArraysInnerToJSON](modules.md#arraysinnertojson)
- [ArraysInnerToJSONTyped](modules.md#arraysinnertojsontyped)
- [CallFromJSON](modules.md#callfromjson)
- [CallFromJSONTyped](modules.md#callfromjsontyped)
- [CallInputsFromJSON](modules.md#callinputsfromjson)
- [CallInputsFromJSONTyped](modules.md#callinputsfromjsontyped)
- [CallInputsToJSON](modules.md#callinputstojson)
- [CallInputsToJSONTyped](modules.md#callinputstojsontyped)
- [CallToJSON](modules.md#calltojson)
- [CallToJSONTyped](modules.md#calltojsontyped)
- [ContentFromJSON](modules.md#contentfromjson)
- [ContentFromJSONTyped](modules.md#contentfromjsontyped)
- [ContentToJSON](modules.md#contenttojson)
- [ContentToJSONTyped](modules.md#contenttojsontyped)
- [CoreFromJSON](modules.md#corefromjson)
- [CoreFromJSONTyped](modules.md#corefromjsontyped)
- [CoreToJSON](modules.md#coretojson)
- [CoreToJSONTyped](modules.md#coretojsontyped)
- [ErrorSpanFromJSON](modules.md#errorspanfromjson)
- [ErrorSpanFromJSONTyped](modules.md#errorspanfromjsontyped)
- [ErrorSpanToJSON](modules.md#errorspantojson)
- [ErrorSpanToJSONTyped](modules.md#errorspantojsontyped)
- [FailResultFromJSON](modules.md#failresultfromjson)
- [FailResultFromJSONTyped](modules.md#failresultfromjsontyped)
- [FailResultToJSON](modules.md#failresulttojson)
- [FailResultToJSONTyped](modules.md#failresulttojsontyped)
- [FormatAnnotationFromJSON](modules.md#formatannotationfromjson)
- [FormatAnnotationFromJSONTyped](modules.md#formatannotationfromjsontyped)
- [FormatAnnotationToJSON](modules.md#formatannotationtojson)
- [FormatAnnotationToJSONTyped](modules.md#formatannotationtojsontyped)
- [GuardFromJSON](modules.md#guardfromjson)
- [GuardFromJSONTyped](modules.md#guardfromjsontyped)
- [GuardToJSON](modules.md#guardtojson)
- [GuardToJSONTyped](modules.md#guardtojsontyped)
- [HealthCheckFromJSON](modules.md#healthcheckfromjson)
- [HealthCheckFromJSONTyped](modules.md#healthcheckfromjsontyped)
- [HealthCheckToJSON](modules.md#healthchecktojson)
- [HealthCheckToJSONTyped](modules.md#healthchecktojsontyped)
- [HttpErrorFromJSON](modules.md#httperrorfromjson)
- [HttpErrorFromJSONTyped](modules.md#httperrorfromjsontyped)
- [HttpErrorToJSON](modules.md#httperrortojson)
- [HttpErrorToJSONTyped](modules.md#httperrortojsontyped)
- [InputsFromJSON](modules.md#inputsfromjson)
- [InputsFromJSONTyped](modules.md#inputsfromjsontyped)
- [InputsToJSON](modules.md#inputstojson)
- [InputsToJSONTyped](modules.md#inputstojsontyped)
- [IterationFromJSON](modules.md#iterationfromjson)
- [IterationFromJSONTyped](modules.md#iterationfromjsontyped)
- [IterationToJSON](modules.md#iterationtojson)
- [IterationToJSONTyped](modules.md#iterationtojsontyped)
- [LLMResourceFromJSON](modules.md#llmresourcefromjson)
- [LLMResourceFromJSONTyped](modules.md#llmresourcefromjsontyped)
- [LLMResourceToJSON](modules.md#llmresourcetojson)
- [LLMResourceToJSONTyped](modules.md#llmresourcetojsontyped)
- [LLMResponseFromJSON](modules.md#llmresponsefromjson)
- [LLMResponseFromJSONTyped](modules.md#llmresponsefromjsontyped)
- [LLMResponseToJSON](modules.md#llmresponsetojson)
- [LLMResponseToJSONTyped](modules.md#llmresponsetojsontyped)
- [MetaDataFromJSON](modules.md#metadatafromjson)
- [MetaDataFromJSONTyped](modules.md#metadatafromjsontyped)
- [MetaDataToJSON](modules.md#metadatatojson)
- [MetaDataToJSONTyped](modules.md#metadatatojsontyped)
- [OpenAIChatCompletionFromJSON](modules.md#openaichatcompletionfromjson)
- [OpenAIChatCompletionFromJSONTyped](modules.md#openaichatcompletionfromjsontyped)
- [OpenAIChatCompletionPayloadFromJSON](modules.md#openaichatcompletionpayloadfromjson)
- [OpenAIChatCompletionPayloadFromJSONTyped](modules.md#openaichatcompletionpayloadfromjsontyped)
- [OpenAIChatCompletionPayloadMessagesInnerFromJSON](modules.md#openaichatcompletionpayloadmessagesinnerfromjson)
- [OpenAIChatCompletionPayloadMessagesInnerFromJSONTyped](modules.md#openaichatcompletionpayloadmessagesinnerfromjsontyped)
- [OpenAIChatCompletionPayloadMessagesInnerToJSON](modules.md#openaichatcompletionpayloadmessagesinnertojson)
- [OpenAIChatCompletionPayloadMessagesInnerToJSONTyped](modules.md#openaichatcompletionpayloadmessagesinnertojsontyped)
- [OpenAIChatCompletionPayloadToJSON](modules.md#openaichatcompletionpayloadtojson)
- [OpenAIChatCompletionPayloadToJSONTyped](modules.md#openaichatcompletionpayloadtojsontyped)
- [OpenAIChatCompletionToJSON](modules.md#openaichatcompletiontojson)
- [OpenAIChatCompletionToJSONTyped](modules.md#openaichatcompletiontojsontyped)
- [OutputsFromJSON](modules.md#outputsfromjson)
- [OutputsFromJSONTyped](modules.md#outputsfromjsontyped)
- [OutputsParsedOutputFromJSON](modules.md#outputsparsedoutputfromjson)
- [OutputsParsedOutputFromJSONTyped](modules.md#outputsparsedoutputfromjsontyped)
- [OutputsParsedOutputToJSON](modules.md#outputsparsedoutputtojson)
- [OutputsParsedOutputToJSONTyped](modules.md#outputsparsedoutputtojsontyped)
- [OutputsToJSON](modules.md#outputstojson)
- [OutputsToJSONTyped](modules.md#outputstojsontyped)
- [OutputsValidationResponseFromJSON](modules.md#outputsvalidationresponsefromjson)
- [OutputsValidationResponseFromJSONTyped](modules.md#outputsvalidationresponsefromjsontyped)
- [OutputsValidationResponseToJSON](modules.md#outputsvalidationresponsetojson)
- [PassResultFromJSON](modules.md#passresultfromjson)
- [PassResultFromJSONTyped](modules.md#passresultfromjsontyped)
- [PassResultToJSON](modules.md#passresulttojson)
- [PassResultToJSONTyped](modules.md#passresulttojsontyped)
- [PrimitivesFromJSON](modules.md#primitivesfromjson)
- [PrimitivesFromJSONTyped](modules.md#primitivesfromjsontyped)
- [PrimitivesToJSON](modules.md#primitivestojson)
- [PrimitivesToJSONTyped](modules.md#primitivestojsontyped)
- [ReaskFromJSON](modules.md#reaskfromjson)
- [ReaskFromJSONTyped](modules.md#reaskfromjsontyped)
- [ReaskToJSON](modules.md#reasktojson)
- [ReaskToJSONTyped](modules.md#reasktojsontyped)
- [SchemaFromJSON](modules.md#schemafromjson)
- [SchemaFromJSONTyped](modules.md#schemafromjsontyped)
- [SchemaToJSON](modules.md#schematojson)
- [SchemaToJSONTyped](modules.md#schematojsontyped)
- [SimpleTypesFromJSON](modules.md#simpletypesfromjson)
- [SimpleTypesFromJSONTyped](modules.md#simpletypesfromjsontyped)
- [SimpleTypesToJSON](modules.md#simpletypestojson)
- [SimpleTypesToJSONTyped](modules.md#simpletypestojsontyped)
- [UnevaluatedFromJSON](modules.md#unevaluatedfromjson)
- [UnevaluatedFromJSONTyped](modules.md#unevaluatedfromjsontyped)
- [UnevaluatedToJSON](modules.md#unevaluatedtojson)
- [UnevaluatedToJSONTyped](modules.md#unevaluatedtojsontyped)
- [ValidatePayloadFromJSON](modules.md#validatepayloadfromjson)
- [ValidatePayloadFromJSONTyped](modules.md#validatepayloadfromjsontyped)
- [ValidatePayloadToJSON](modules.md#validatepayloadtojson)
- [ValidatePayloadToJSONTyped](modules.md#validatepayloadtojsontyped)
- [ValidationFromJSON](modules.md#validationfromjson)
- [ValidationFromJSONTyped](modules.md#validationfromjsontyped)
- [ValidationOutcomeFromJSON](modules.md#validationoutcomefromjson)
- [ValidationOutcomeFromJSONTyped](modules.md#validationoutcomefromjsontyped)
- [ValidationOutcomeToJSON](modules.md#validationoutcometojson)
- [ValidationOutcomeToJSONTyped](modules.md#validationoutcometojsontyped)
- [ValidationOutcomeValidatedOutputFromJSON](modules.md#validationoutcomevalidatedoutputfromjson)
- [ValidationOutcomeValidatedOutputFromJSONTyped](modules.md#validationoutcomevalidatedoutputfromjsontyped)
- [ValidationOutcomeValidatedOutputToJSON](modules.md#validationoutcomevalidatedoutputtojson)
- [ValidationOutcomeValidatedOutputToJSONTyped](modules.md#validationoutcomevalidatedoutputtojsontyped)
- [ValidationResultFromJSON](modules.md#validationresultfromjson)
- [ValidationResultFromJSONTyped](modules.md#validationresultfromjsontyped)
- [ValidationResultToJSON](modules.md#validationresulttojson)
- [ValidationResultToJSONTyped](modules.md#validationresulttojsontyped)
- [ValidationSummaryFromJSON](modules.md#validationsummaryfromjson)
- [ValidationSummaryFromJSONTyped](modules.md#validationsummaryfromjsontyped)
- [ValidationSummaryToJSON](modules.md#validationsummarytojson)
- [ValidationSummaryToJSONTyped](modules.md#validationsummarytojsontyped)
- [ValidationToJSON](modules.md#validationtojson)
- [ValidationToJSONTyped](modules.md#validationtojsontyped)
- [ValidationTypeFromJSON](modules.md#validationtypefromjson)
- [ValidationTypeFromJSONTyped](modules.md#validationtypefromjsontyped)
- [ValidationTypeToJSON](modules.md#validationtypetojson)
- [ValidationTypeToJSONTyped](modules.md#validationtypetojsontyped)
- [ValidatorLogFromJSON](modules.md#validatorlogfromjson)
- [ValidatorLogFromJSONTyped](modules.md#validatorlogfromjsontyped)
- [ValidatorLogInstanceIdFromJSON](modules.md#validatorloginstanceidfromjson)
- [ValidatorLogInstanceIdFromJSONTyped](modules.md#validatorloginstanceidfromjsontyped)
- [ValidatorLogInstanceIdToJSON](modules.md#validatorloginstanceidtojson)
- [ValidatorLogInstanceIdToJSONTyped](modules.md#validatorloginstanceidtojsontyped)
- [ValidatorLogToJSON](modules.md#validatorlogtojson)
- [ValidatorLogToJSONTyped](modules.md#validatorlogtojsontyped)
- [ValidatorLogValidationResultFromJSON](modules.md#validatorlogvalidationresultfromjson)
- [ValidatorLogValidationResultFromJSONTyped](modules.md#validatorlogvalidationresultfromjsontyped)
- [ValidatorLogValidationResultToJSON](modules.md#validatorlogvalidationresulttojson)
- [ValidatorLogValidationResultToJSONTyped](modules.md#validatorlogvalidationresulttojsontyped)
- [ValidatorReferenceFromJSON](modules.md#validatorreferencefromjson)
- [ValidatorReferenceFromJSONTyped](modules.md#validatorreferencefromjsontyped)
- [ValidatorReferenceToJSON](modules.md#validatorreferencetojson)
- [ValidatorReferenceToJSONTyped](modules.md#validatorreferencetojsontyped)
- [canConsumeForm](modules.md#canconsumeform)
- [exists](modules.md#exists)
- [instanceOfAnyType](modules.md#instanceofanytype)
- [instanceOfApplicator](modules.md#instanceofapplicator)
- [instanceOfArgsAndKwargs](modules.md#instanceofargsandkwargs)
- [instanceOfArraysInner](modules.md#instanceofarraysinner)
- [instanceOfCall](modules.md#instanceofcall)
- [instanceOfCallInputs](modules.md#instanceofcallinputs)
- [instanceOfContent](modules.md#instanceofcontent)
- [instanceOfCore](modules.md#instanceofcore)
- [instanceOfErrorSpan](modules.md#instanceoferrorspan)
- [instanceOfFailResult](modules.md#instanceoffailresult)
- [instanceOfFormatAnnotation](modules.md#instanceofformatannotation)
- [instanceOfGuard](modules.md#instanceofguard)
- [instanceOfHealthCheck](modules.md#instanceofhealthcheck)
- [instanceOfHttpError](modules.md#instanceofhttperror)
- [instanceOfInputs](modules.md#instanceofinputs)
- [instanceOfIteration](modules.md#instanceofiteration)
- [instanceOfLLMResource](modules.md#instanceofllmresource)
- [instanceOfLLMResponse](modules.md#instanceofllmresponse)
- [instanceOfMetaData](modules.md#instanceofmetadata)
- [instanceOfOpenAIChatCompletion](modules.md#instanceofopenaichatcompletion)
- [instanceOfOpenAIChatCompletionPayload](modules.md#instanceofopenaichatcompletionpayload)
- [instanceOfOpenAIChatCompletionPayloadMessagesInner](modules.md#instanceofopenaichatcompletionpayloadmessagesinner)
- [instanceOfOutputs](modules.md#instanceofoutputs)
- [instanceOfOutputsParsedOutput](modules.md#instanceofoutputsparsedoutput)
- [instanceOfOutputsValidationResponse](modules.md#instanceofoutputsvalidationresponse)
- [instanceOfPassResult](modules.md#instanceofpassresult)
- [instanceOfPrimitives](modules.md#instanceofprimitives)
- [instanceOfReask](modules.md#instanceofreask)
- [instanceOfSchema](modules.md#instanceofschema)
- [instanceOfSimpleTypes](modules.md#instanceofsimpletypes)
- [instanceOfUnevaluated](modules.md#instanceofunevaluated)
- [instanceOfValidatePayload](modules.md#instanceofvalidatepayload)
- [instanceOfValidation](modules.md#instanceofvalidation)
- [instanceOfValidationOutcome](modules.md#instanceofvalidationoutcome)
- [instanceOfValidationOutcomeValidatedOutput](modules.md#instanceofvalidationoutcomevalidatedoutput)
- [instanceOfValidationResult](modules.md#instanceofvalidationresult)
- [instanceOfValidationSummary](modules.md#instanceofvalidationsummary)
- [instanceOfValidationType](modules.md#instanceofvalidationtype)
- [instanceOfValidatorLog](modules.md#instanceofvalidatorlog)
- [instanceOfValidatorLogInstanceId](modules.md#instanceofvalidatorloginstanceid)
- [instanceOfValidatorLogValidationResult](modules.md#instanceofvalidatorlogvalidationresult)
- [instanceOfValidatorReference](modules.md#instanceofvalidatorreference)
- [mapValues](modules.md#mapvalues)
- [querystring](modules.md#querystring)

## Type Aliases

### FetchAPI

Ƭ **FetchAPI**: `WindowOrWorkerGlobalScope`[``"fetch"``]

#### Defined in

src/runtime.ts:342

___

### HTTPBody

Ƭ **HTTPBody**: [`Json`](modules.md#json) \| `FormData` \| `URLSearchParams`

#### Defined in

src/runtime.ts:364

___

### HTTPHeaders

Ƭ **HTTPHeaders**: `Object`

#### Index signature

▪ [key: `string`]: `string`

#### Defined in

src/runtime.ts:353

___

### HTTPMethod

Ƭ **HTTPMethod**: ``"GET"`` \| ``"POST"`` \| ``"PUT"`` \| ``"PATCH"`` \| ``"DELETE"`` \| ``"OPTIONS"`` \| ``"HEAD"``

#### Defined in

src/runtime.ts:345

___

### HTTPQuery

Ƭ **HTTPQuery**: `Object`

#### Index signature

▪ [key: `string`]: `string` \| `number` \| ``null`` \| `boolean` \| (`string` \| `number` \| ``null`` \| `boolean`)[] \| `Set`\<`string` \| `number` \| ``null`` \| `boolean`\> \| [`HTTPQuery`](modules.md#httpquery)

#### Defined in

src/runtime.ts:354

___

### HTTPRequestInit

Ƭ **HTTPRequestInit**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `body?` | [`HTTPBody`](modules.md#httpbody) |
| `credentials?` | `RequestCredentials` |
| `headers?` | [`HTTPHeaders`](modules.md#httpheaders) |
| `method` | [`HTTPMethod`](modules.md#httpmethod) |

#### Defined in

src/runtime.ts:365

___

### InitOverrideFunction

Ƭ **InitOverrideFunction**: (`requestContext`: \{ `context`: [`RequestOpts`](interfaces/RequestOpts.md) ; `init`: [`HTTPRequestInit`](modules.md#httprequestinit)  }) => `Promise`\<`RequestInit`\>

#### Type declaration

▸ (`requestContext`): `Promise`\<`RequestInit`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `requestContext` | `Object` |
| `requestContext.context` | [`RequestOpts`](interfaces/RequestOpts.md) |
| `requestContext.init` | [`HTTPRequestInit`](modules.md#httprequestinit) |

##### Returns

`Promise`\<`RequestInit`\>

#### Defined in

src/runtime.ts:377

___

### Json

Ƭ **Json**: `any`

#### Defined in

src/runtime.ts:344

___

### LLMResource

Ƭ **LLMResource**: typeof [`LLMResource`](modules.md#llmresource-1)[keyof typeof [`LLMResource`](modules.md#llmresource-1)]

#### Defined in

src/models/LLMResource.ts:19

src/models/LLMResource.ts:29

___

### ModelPropertyNaming

Ƭ **ModelPropertyNaming**: ``"camelCase"`` \| ``"snake_case"`` \| ``"PascalCase"`` \| ``"original"``

#### Defined in

src/runtime.ts:371

___

### OnType

Ƭ **OnType**: ``"prompt"`` \| ``"instructions"`` \| ``"msg_history"`` \| ``"output"`` \| ``"$.foo.bar"`` \| `string`

**`Export`**

#### Defined in

src/models/ValidatorReference.ts:123

___

### SimpleTypes

Ƭ **SimpleTypes**: typeof [`SimpleTypes`](modules.md#simpletypes-1)[keyof typeof [`SimpleTypes`](modules.md#simpletypes-1)]

#### Defined in

src/models/SimpleTypes.ts:19

src/models/SimpleTypes.ts:28

___

### ValidationResultOutcomeEnum

Ƭ **ValidationResultOutcomeEnum**: typeof [`ValidationResultOutcomeEnum`](modules.md#validationresultoutcomeenum-1)[keyof typeof [`ValidationResultOutcomeEnum`](modules.md#validationresultoutcomeenum-1)]

#### Defined in

src/models/ValidationResult.ts:44

src/models/ValidationResult.ts:48

___

### ValidationSummaryValidatorStatusEnum

Ƭ **ValidationSummaryValidatorStatusEnum**: typeof [`ValidationSummaryValidatorStatusEnum`](modules.md#validationsummaryvalidatorstatusenum-1)[keyof typeof [`ValidationSummaryValidatorStatusEnum`](modules.md#validationsummaryvalidatorstatusenum-1)]

#### Defined in

src/models/ValidationSummary.ts:59

src/models/ValidationSummary.ts:63

___

### ValidatorLogValidationResultOutcomeEnum

Ƭ **ValidatorLogValidationResultOutcomeEnum**: typeof [`ValidatorLogValidationResultOutcomeEnum`](modules.md#validatorlogvalidationresultoutcomeenum-1)[keyof typeof [`ValidatorLogValidationResultOutcomeEnum`](modules.md#validatorlogvalidationresultoutcomeenum-1)]

#### Defined in

src/models/ValidatorLogValidationResult.ts:71

src/models/ValidatorLogValidationResult.ts:75

___

### ValidatorReferenceOnFailEnum

Ƭ **ValidatorReferenceOnFailEnum**: typeof [`ValidatorReferenceOnFailEnum`](modules.md#validatorreferenceonfailenum-1)[keyof typeof [`ValidatorReferenceOnFailEnum`](modules.md#validatorreferenceonfailenum-1)]

#### Defined in

src/models/ValidatorReference.ts:56

src/models/ValidatorReference.ts:66

## Variables

### BASE\_PATH

• `Const` **BASE\_PATH**: `string`

Guardrails API
Guardrails CRUD API

The version of the OpenAPI document: 0.0.0

NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
https://openapi-generator.tech
Do not edit the class manually.

#### Defined in

src/runtime.ts:15

___

### COLLECTION\_FORMATS

• `Const` **COLLECTION\_FORMATS**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `csv` | `string` |
| `pipes` | `string` |
| `ssv` | `string` |
| `tsv` | `string` |

#### Defined in

src/runtime.ts:335

___

### DefaultConfig

• `Const` **DefaultConfig**: [`Configuration`](classes/Configuration.md)

#### Defined in

src/runtime.ts:98

___

### LLMResource

• `Const` **LLMResource**: `Object`

**`Export`**

#### Type declaration

| Name | Type |
| :------ | :------ |
| `LitellmAcompletion` | ``"litellm.acompletion"`` |
| `LitellmCompletion` | ``"litellm.completion"`` |
| `OpenaiChatCompletionAcreate` | ``"openai.ChatCompletion.acreate"`` |
| `OpenaiChatCompletionCreate` | ``"openai.ChatCompletion.create"`` |
| `OpenaiChatCompletionsCreate` | ``"openai.chat.completions.create"`` |
| `OpenaiCompletionAcreate` | ``"openai.Completion.acreate"`` |
| `OpenaiCompletionCreate` | ``"openai.Completion.create"`` |
| `OpenaiCompletionsCreate` | ``"openai.completions.create"`` |

#### Defined in

src/models/LLMResource.ts:19

src/models/LLMResource.ts:29

___

### SimpleTypes

• `Const` **SimpleTypes**: `Object`

**`Export`**

#### Type declaration

| Name | Type |
| :------ | :------ |
| `Array` | ``"array"`` |
| `Boolean` | ``"boolean"`` |
| `Integer` | ``"integer"`` |
| `Null` | ``"null"`` |
| `Number` | ``"number"`` |
| `Object` | ``"object"`` |
| `String` | ``"string"`` |

#### Defined in

src/models/SimpleTypes.ts:19

src/models/SimpleTypes.ts:28

___

### ValidationResultOutcomeEnum

• `Const` **ValidationResultOutcomeEnum**: `Object`

**`Export`**

#### Type declaration

| Name | Type |
| :------ | :------ |
| `Fail` | ``"fail"`` |
| `Pass` | ``"pass"`` |

#### Defined in

src/models/ValidationResult.ts:44

src/models/ValidationResult.ts:48

___

### ValidationSummaryValidatorStatusEnum

• `Const` **ValidationSummaryValidatorStatusEnum**: `Object`

**`Export`**

#### Type declaration

| Name | Type |
| :------ | :------ |
| `Fail` | ``"fail"`` |
| `Pass` | ``"pass"`` |

#### Defined in

src/models/ValidationSummary.ts:59

src/models/ValidationSummary.ts:63

___

### ValidatorLogValidationResultOutcomeEnum

• `Const` **ValidatorLogValidationResultOutcomeEnum**: `Object`

**`Export`**

#### Type declaration

| Name | Type |
| :------ | :------ |
| `Fail` | ``"fail"`` |
| `Pass` | ``"pass"`` |

#### Defined in

src/models/ValidatorLogValidationResult.ts:71

src/models/ValidatorLogValidationResult.ts:75

___

### ValidatorReferenceOnFailEnum

• `Const` **ValidatorReferenceOnFailEnum**: `Object`

**`Export`**

#### Type declaration

| Name | Type |
| :------ | :------ |
| `Custom` | ``"custom"`` |
| `Exception` | ``"exception"`` |
| `Filter` | ``"filter"`` |
| `Fix` | ``"fix"`` |
| `FixReask` | ``"fix_reask"`` |
| `Noop` | ``"noop"`` |
| `Reask` | ``"reask"`` |
| `Refrain` | ``"refrain"`` |

#### Defined in

src/models/ValidatorReference.ts:56

src/models/ValidatorReference.ts:66

## Functions

### AnyTypeFromJSON

▸ **AnyTypeFromJSON**(`json`): [`AnyType`](interfaces/AnyType.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`AnyType`](interfaces/AnyType.md)

#### Defined in

src/models/AnyType.ts:29

___

### AnyTypeFromJSONTyped

▸ **AnyTypeFromJSONTyped**(`json`, `ignoreDiscriminator`): [`AnyType`](interfaces/AnyType.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`AnyType`](interfaces/AnyType.md)

#### Defined in

src/models/AnyType.ts:33

___

### AnyTypeToJSON

▸ **AnyTypeToJSON**(`json`): [`AnyType`](interfaces/AnyType.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`AnyType`](interfaces/AnyType.md)

#### Defined in

src/models/AnyType.ts:40

___

### AnyTypeToJSONTyped

▸ **AnyTypeToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`AnyType`](interfaces/AnyType.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/AnyType.ts:44

___

### ApplicatorFromJSON

▸ **ApplicatorFromJSON**(`json`): [`Applicator`](interfaces/Applicator.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Applicator`](interfaces/Applicator.md)

#### Defined in

src/models/Applicator.ts:120

___

### ApplicatorFromJSONTyped

▸ **ApplicatorFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Applicator`](interfaces/Applicator.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Applicator`](interfaces/Applicator.md)

#### Defined in

src/models/Applicator.ts:124

___

### ApplicatorToJSON

▸ **ApplicatorToJSON**(`json`): [`Applicator`](interfaces/Applicator.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Applicator`](interfaces/Applicator.md)

#### Defined in

src/models/Applicator.ts:156

___

### ApplicatorToJSONTyped

▸ **ApplicatorToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Applicator`](interfaces/Applicator.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Applicator.ts:160

___

### ArgsAndKwargsFromJSON

▸ **ArgsAndKwargsFromJSON**(`json`): [`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md)

#### Defined in

src/models/ArgsAndKwargs.ts:42

___

### ArgsAndKwargsFromJSONTyped

▸ **ArgsAndKwargsFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md)

#### Defined in

src/models/ArgsAndKwargs.ts:46

___

### ArgsAndKwargsToJSON

▸ **ArgsAndKwargsToJSON**(`json`): [`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md)

#### Defined in

src/models/ArgsAndKwargs.ts:59

___

### ArgsAndKwargsToJSONTyped

▸ **ArgsAndKwargsToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ArgsAndKwargs.ts:63

___

### ArraysInnerFromJSON

▸ **ArraysInnerFromJSON**(`json`): [`ArraysInner`](interfaces/ArraysInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ArraysInner`](interfaces/ArraysInner.md)

#### Defined in

src/models/ArraysInner.ts:29

___

### ArraysInnerFromJSONTyped

▸ **ArraysInnerFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ArraysInner`](interfaces/ArraysInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ArraysInner`](interfaces/ArraysInner.md)

#### Defined in

src/models/ArraysInner.ts:33

___

### ArraysInnerToJSON

▸ **ArraysInnerToJSON**(`json`): [`ArraysInner`](interfaces/ArraysInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ArraysInner`](interfaces/ArraysInner.md)

#### Defined in

src/models/ArraysInner.ts:40

___

### ArraysInnerToJSONTyped

▸ **ArraysInnerToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ArraysInner`](interfaces/ArraysInner.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ArraysInner.ts:44

___

### CallFromJSON

▸ **CallFromJSON**(`json`): [`Call`](interfaces/Call.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Call`](interfaces/Call.md)

#### Defined in

src/models/Call.ts:60

___

### CallFromJSONTyped

▸ **CallFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Call`](interfaces/Call.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Call`](interfaces/Call.md)

#### Defined in

src/models/Call.ts:64

___

### CallInputsFromJSON

▸ **CallInputsFromJSON**(`json`): [`CallInputs`](interfaces/CallInputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`CallInputs`](interfaces/CallInputs.md)

#### Defined in

src/models/CallInputs.ts:90

___

### CallInputsFromJSONTyped

▸ **CallInputsFromJSONTyped**(`json`, `ignoreDiscriminator`): [`CallInputs`](interfaces/CallInputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`CallInputs`](interfaces/CallInputs.md)

#### Defined in

src/models/CallInputs.ts:94

___

### CallInputsToJSON

▸ **CallInputsToJSON**(`json`): [`CallInputs`](interfaces/CallInputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`CallInputs`](interfaces/CallInputs.md)

#### Defined in

src/models/CallInputs.ts:117

___

### CallInputsToJSONTyped

▸ **CallInputsToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`CallInputs`](interfaces/CallInputs.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/CallInputs.ts:121

___

### CallToJSON

▸ **CallToJSON**(`json`): [`Call`](interfaces/Call.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Call`](interfaces/Call.md)

#### Defined in

src/models/Call.ts:83

___

### CallToJSONTyped

▸ **CallToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Call`](interfaces/Call.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Call.ts:87

___

### ContentFromJSON

▸ **ContentFromJSON**(`json`): [`Content`](interfaces/Content.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Content`](interfaces/Content.md)

#### Defined in

src/models/Content.ts:48

___

### ContentFromJSONTyped

▸ **ContentFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Content`](interfaces/Content.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Content`](interfaces/Content.md)

#### Defined in

src/models/Content.ts:52

___

### ContentToJSON

▸ **ContentToJSON**(`json`): [`Content`](interfaces/Content.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Content`](interfaces/Content.md)

#### Defined in

src/models/Content.ts:69

___

### ContentToJSONTyped

▸ **ContentToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Content`](interfaces/Content.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Content.ts:73

___

### CoreFromJSON

▸ **CoreFromJSON**(`json`): [`Core`](interfaces/Core.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Core`](interfaces/Core.md)

#### Defined in

src/models/Core.ts:72

___

### CoreFromJSONTyped

▸ **CoreFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Core`](interfaces/Core.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Core`](interfaces/Core.md)

#### Defined in

src/models/Core.ts:76

___

### CoreToJSON

▸ **CoreToJSON**(`json`): [`Core`](interfaces/Core.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Core`](interfaces/Core.md)

#### Defined in

src/models/Core.ts:95

___

### CoreToJSONTyped

▸ **CoreToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Core`](interfaces/Core.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Core.ts:99

___

### ErrorSpanFromJSON

▸ **ErrorSpanFromJSON**(`json`): [`ErrorSpan`](interfaces/ErrorSpan.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ErrorSpan`](interfaces/ErrorSpan.md)

#### Defined in

src/models/ErrorSpan.ts:51

___

### ErrorSpanFromJSONTyped

▸ **ErrorSpanFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ErrorSpan`](interfaces/ErrorSpan.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ErrorSpan`](interfaces/ErrorSpan.md)

#### Defined in

src/models/ErrorSpan.ts:55

___

### ErrorSpanToJSON

▸ **ErrorSpanToJSON**(`json`): [`ErrorSpan`](interfaces/ErrorSpan.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ErrorSpan`](interfaces/ErrorSpan.md)

#### Defined in

src/models/ErrorSpan.ts:69

___

### ErrorSpanToJSONTyped

▸ **ErrorSpanToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ErrorSpan`](interfaces/ErrorSpan.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ErrorSpan.ts:73

___

### FailResultFromJSON

▸ **FailResultFromJSON**(`json`): [`FailResult`](interfaces/FailResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`FailResult`](interfaces/FailResult.md)

#### Defined in

src/models/FailResult.ts:72

___

### FailResultFromJSONTyped

▸ **FailResultFromJSONTyped**(`json`, `ignoreDiscriminator`): [`FailResult`](interfaces/FailResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`FailResult`](interfaces/FailResult.md)

#### Defined in

src/models/FailResult.ts:76

___

### FailResultToJSON

▸ **FailResultToJSON**(`json`): [`FailResult`](interfaces/FailResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`FailResult`](interfaces/FailResult.md)

#### Defined in

src/models/FailResult.ts:97

___

### FailResultToJSONTyped

▸ **FailResultToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`FailResult`](interfaces/FailResult.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/FailResult.ts:101

___

### FormatAnnotationFromJSON

▸ **FormatAnnotationFromJSON**(`json`): [`FormatAnnotation`](interfaces/FormatAnnotation.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`FormatAnnotation`](interfaces/FormatAnnotation.md)

#### Defined in

src/models/FormatAnnotation.ts:38

___

### FormatAnnotationFromJSONTyped

▸ **FormatAnnotationFromJSONTyped**(`json`, `ignoreDiscriminator`): [`FormatAnnotation`](interfaces/FormatAnnotation.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`FormatAnnotation`](interfaces/FormatAnnotation.md)

#### Defined in

src/models/FormatAnnotation.ts:42

___

### FormatAnnotationToJSON

▸ **FormatAnnotationToJSON**(`json`): [`FormatAnnotation`](interfaces/FormatAnnotation.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`FormatAnnotation`](interfaces/FormatAnnotation.md)

#### Defined in

src/models/FormatAnnotation.ts:54

___

### FormatAnnotationToJSONTyped

▸ **FormatAnnotationToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`FormatAnnotation`](interfaces/FormatAnnotation.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/FormatAnnotation.ts:58

___

### GuardFromJSON

▸ **GuardFromJSON**(`json`): [`Guard`](interfaces/Guard.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Guard`](interfaces/Guard.md)

#### Defined in

src/models/Guard.ts:78

___

### GuardFromJSONTyped

▸ **GuardFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Guard`](interfaces/Guard.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Guard`](interfaces/Guard.md)

#### Defined in

src/models/Guard.ts:82

___

### GuardToJSON

▸ **GuardToJSON**(`json`): [`Guard`](interfaces/Guard.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Guard`](interfaces/Guard.md)

#### Defined in

src/models/Guard.ts:108

___

### GuardToJSONTyped

▸ **GuardToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Guard`](interfaces/Guard.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Guard.ts:112

___

### HealthCheckFromJSON

▸ **HealthCheckFromJSON**(`json`): [`HealthCheck`](interfaces/HealthCheck.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`HealthCheck`](interfaces/HealthCheck.md)

#### Defined in

src/models/HealthCheck.ts:44

___

### HealthCheckFromJSONTyped

▸ **HealthCheckFromJSONTyped**(`json`, `ignoreDiscriminator`): [`HealthCheck`](interfaces/HealthCheck.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`HealthCheck`](interfaces/HealthCheck.md)

#### Defined in

src/models/HealthCheck.ts:48

___

### HealthCheckToJSON

▸ **HealthCheckToJSON**(`json`): [`HealthCheck`](interfaces/HealthCheck.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`HealthCheck`](interfaces/HealthCheck.md)

#### Defined in

src/models/HealthCheck.ts:61

___

### HealthCheckToJSONTyped

▸ **HealthCheckToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`HealthCheck`](interfaces/HealthCheck.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/HealthCheck.ts:65

___

### HttpErrorFromJSON

▸ **HttpErrorFromJSON**(`json`): [`HttpError`](interfaces/HttpError.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`HttpError`](interfaces/HttpError.md)

#### Defined in

src/models/HttpError.ts:62

___

### HttpErrorFromJSONTyped

▸ **HttpErrorFromJSONTyped**(`json`, `ignoreDiscriminator`): [`HttpError`](interfaces/HttpError.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`HttpError`](interfaces/HttpError.md)

#### Defined in

src/models/HttpError.ts:66

___

### HttpErrorToJSON

▸ **HttpErrorToJSON**(`json`): [`HttpError`](interfaces/HttpError.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`HttpError`](interfaces/HttpError.md)

#### Defined in

src/models/HttpError.ts:82

___

### HttpErrorToJSONTyped

▸ **HttpErrorToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`HttpError`](interfaces/HttpError.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/HttpError.ts:86

___

### InputsFromJSON

▸ **InputsFromJSON**(`json`): [`Inputs`](interfaces/Inputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Inputs`](interfaces/Inputs.md)

#### Defined in

src/models/Inputs.ts:78

___

### InputsFromJSONTyped

▸ **InputsFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Inputs`](interfaces/Inputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Inputs`](interfaces/Inputs.md)

#### Defined in

src/models/Inputs.ts:82

___

### InputsToJSON

▸ **InputsToJSON**(`json`): [`Inputs`](interfaces/Inputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Inputs`](interfaces/Inputs.md)

#### Defined in

src/models/Inputs.ts:103

___

### InputsToJSONTyped

▸ **InputsToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Inputs`](interfaces/Inputs.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Inputs.ts:107

___

### IterationFromJSON

▸ **IterationFromJSON**(`json`): [`Iteration`](interfaces/Iteration.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Iteration`](interfaces/Iteration.md)

#### Defined in

src/models/Iteration.ts:68

___

### IterationFromJSONTyped

▸ **IterationFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Iteration`](interfaces/Iteration.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Iteration`](interfaces/Iteration.md)

#### Defined in

src/models/Iteration.ts:72

___

### IterationToJSON

▸ **IterationToJSON**(`json`): [`Iteration`](interfaces/Iteration.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Iteration`](interfaces/Iteration.md)

#### Defined in

src/models/Iteration.ts:89

___

### IterationToJSONTyped

▸ **IterationToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Iteration`](interfaces/Iteration.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Iteration.ts:93

___

### LLMResourceFromJSON

▸ **LLMResourceFromJSON**(`json`): [`LLMResource`](modules.md#llmresource)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`LLMResource`](modules.md#llmresource)

#### Defined in

src/models/LLMResource.ts:42

___

### LLMResourceFromJSONTyped

▸ **LLMResourceFromJSONTyped**(`json`, `ignoreDiscriminator`): [`LLMResource`](modules.md#llmresource)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`LLMResource`](modules.md#llmresource)

#### Defined in

src/models/LLMResource.ts:46

___

### LLMResourceToJSON

▸ **LLMResourceToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`LLMResource`](modules.md#llmresource) |

#### Returns

`any`

#### Defined in

src/models/LLMResource.ts:53

___

### LLMResourceToJSONTyped

▸ **LLMResourceToJSONTyped**(`value`, `ignoreDiscriminator`): [`LLMResource`](modules.md#llmresource)

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`LLMResource`](modules.md#llmresource)

#### Defined in

src/models/LLMResource.ts:57

___

### LLMResponseFromJSON

▸ **LLMResponseFromJSON**(`json`): [`LLMResponse`](interfaces/LLMResponse.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`LLMResponse`](interfaces/LLMResponse.md)

#### Defined in

src/models/LLMResponse.ts:61

___

### LLMResponseFromJSONTyped

▸ **LLMResponseFromJSONTyped**(`json`, `ignoreDiscriminator`): [`LLMResponse`](interfaces/LLMResponse.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`LLMResponse`](interfaces/LLMResponse.md)

#### Defined in

src/models/LLMResponse.ts:65

___

### LLMResponseToJSON

▸ **LLMResponseToJSON**(`json`): [`LLMResponse`](interfaces/LLMResponse.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`LLMResponse`](interfaces/LLMResponse.md)

#### Defined in

src/models/LLMResponse.ts:87

___

### LLMResponseToJSONTyped

▸ **LLMResponseToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`LLMResponse`](interfaces/LLMResponse.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/LLMResponse.ts:91

___

### MetaDataFromJSON

▸ **MetaDataFromJSON**(`json`): [`MetaData`](interfaces/MetaData.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`MetaData`](interfaces/MetaData.md)

#### Defined in

src/models/MetaData.ts:72

___

### MetaDataFromJSONTyped

▸ **MetaDataFromJSONTyped**(`json`, `ignoreDiscriminator`): [`MetaData`](interfaces/MetaData.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`MetaData`](interfaces/MetaData.md)

#### Defined in

src/models/MetaData.ts:76

___

### MetaDataToJSON

▸ **MetaDataToJSON**(`json`): [`MetaData`](interfaces/MetaData.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`MetaData`](interfaces/MetaData.md)

#### Defined in

src/models/MetaData.ts:94

___

### MetaDataToJSONTyped

▸ **MetaDataToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`MetaData`](interfaces/MetaData.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/MetaData.ts:98

___

### OpenAIChatCompletionFromJSON

▸ **OpenAIChatCompletionFromJSON**(`json`): [`OpenAIChatCompletion`](interfaces/OpenAIChatCompletion.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OpenAIChatCompletion`](interfaces/OpenAIChatCompletion.md)

#### Defined in

src/models/OpenAIChatCompletion.ts:66

___

### OpenAIChatCompletionFromJSONTyped

▸ **OpenAIChatCompletionFromJSONTyped**(`json`, `ignoreDiscriminator`): [`OpenAIChatCompletion`](interfaces/OpenAIChatCompletion.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`OpenAIChatCompletion`](interfaces/OpenAIChatCompletion.md)

#### Defined in

src/models/OpenAIChatCompletion.ts:70

___

### OpenAIChatCompletionPayloadFromJSON

▸ **OpenAIChatCompletionPayloadFromJSON**(`json`): [`OpenAIChatCompletionPayload`](interfaces/OpenAIChatCompletionPayload.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OpenAIChatCompletionPayload`](interfaces/OpenAIChatCompletionPayload.md)

#### Defined in

src/models/OpenAIChatCompletionPayload.ts:62

___

### OpenAIChatCompletionPayloadFromJSONTyped

▸ **OpenAIChatCompletionPayloadFromJSONTyped**(`json`, `ignoreDiscriminator`): [`OpenAIChatCompletionPayload`](interfaces/OpenAIChatCompletionPayload.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`OpenAIChatCompletionPayload`](interfaces/OpenAIChatCompletionPayload.md)

#### Defined in

src/models/OpenAIChatCompletionPayload.ts:68

___

### OpenAIChatCompletionPayloadMessagesInnerFromJSON

▸ **OpenAIChatCompletionPayloadMessagesInnerFromJSON**(`json`): [`OpenAIChatCompletionPayloadMessagesInner`](interfaces/OpenAIChatCompletionPayloadMessagesInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OpenAIChatCompletionPayloadMessagesInner`](interfaces/OpenAIChatCompletionPayloadMessagesInner.md)

#### Defined in

src/models/OpenAIChatCompletionPayloadMessagesInner.ts:44

___

### OpenAIChatCompletionPayloadMessagesInnerFromJSONTyped

▸ **OpenAIChatCompletionPayloadMessagesInnerFromJSONTyped**(`json`, `ignoreDiscriminator`): [`OpenAIChatCompletionPayloadMessagesInner`](interfaces/OpenAIChatCompletionPayloadMessagesInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`OpenAIChatCompletionPayloadMessagesInner`](interfaces/OpenAIChatCompletionPayloadMessagesInner.md)

#### Defined in

src/models/OpenAIChatCompletionPayloadMessagesInner.ts:50

___

### OpenAIChatCompletionPayloadMessagesInnerToJSON

▸ **OpenAIChatCompletionPayloadMessagesInnerToJSON**(`json`): [`OpenAIChatCompletionPayloadMessagesInner`](interfaces/OpenAIChatCompletionPayloadMessagesInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OpenAIChatCompletionPayloadMessagesInner`](interfaces/OpenAIChatCompletionPayloadMessagesInner.md)

#### Defined in

src/models/OpenAIChatCompletionPayloadMessagesInner.ts:63

___

### OpenAIChatCompletionPayloadMessagesInnerToJSONTyped

▸ **OpenAIChatCompletionPayloadMessagesInnerToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`OpenAIChatCompletionPayloadMessagesInner`](interfaces/OpenAIChatCompletionPayloadMessagesInner.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/OpenAIChatCompletionPayloadMessagesInner.ts:69

___

### OpenAIChatCompletionPayloadToJSON

▸ **OpenAIChatCompletionPayloadToJSON**(`json`): [`OpenAIChatCompletionPayload`](interfaces/OpenAIChatCompletionPayload.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OpenAIChatCompletionPayload`](interfaces/OpenAIChatCompletionPayload.md)

#### Defined in

src/models/OpenAIChatCompletionPayload.ts:88

___

### OpenAIChatCompletionPayloadToJSONTyped

▸ **OpenAIChatCompletionPayloadToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`OpenAIChatCompletionPayload`](interfaces/OpenAIChatCompletionPayload.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/OpenAIChatCompletionPayload.ts:94

___

### OpenAIChatCompletionToJSON

▸ **OpenAIChatCompletionToJSON**(`json`): [`OpenAIChatCompletion`](interfaces/OpenAIChatCompletion.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OpenAIChatCompletion`](interfaces/OpenAIChatCompletion.md)

#### Defined in

src/models/OpenAIChatCompletion.ts:87

___

### OpenAIChatCompletionToJSONTyped

▸ **OpenAIChatCompletionToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`OpenAIChatCompletion`](interfaces/OpenAIChatCompletion.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/OpenAIChatCompletion.ts:91

___

### OutputsFromJSON

▸ **OutputsFromJSON**(`json`): [`Outputs`](interfaces/Outputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Outputs`](interfaces/Outputs.md)

#### Defined in

src/models/Outputs.ts:93

___

### OutputsFromJSONTyped

▸ **OutputsFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Outputs`](interfaces/Outputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Outputs`](interfaces/Outputs.md)

#### Defined in

src/models/Outputs.ts:97

___

### OutputsParsedOutputFromJSON

▸ **OutputsParsedOutputFromJSON**(`json`): [`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md)

#### Defined in

src/models/OutputsParsedOutput.ts:31

___

### OutputsParsedOutputFromJSONTyped

▸ **OutputsParsedOutputFromJSONTyped**(`json`, `ignoreDiscriminator`): [`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md)

#### Defined in

src/models/OutputsParsedOutput.ts:35

___

### OutputsParsedOutputToJSON

▸ **OutputsParsedOutputToJSON**(`json`): [`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md)

#### Defined in

src/models/OutputsParsedOutput.ts:42

___

### OutputsParsedOutputToJSONTyped

▸ **OutputsParsedOutputToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/OutputsParsedOutput.ts:46

___

### OutputsToJSON

▸ **OutputsToJSON**(`json`): [`Outputs`](interfaces/Outputs.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Outputs`](interfaces/Outputs.md)

#### Defined in

src/models/Outputs.ts:134

___

### OutputsToJSONTyped

▸ **OutputsToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Outputs`](interfaces/Outputs.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Outputs.ts:138

___

### OutputsValidationResponseFromJSON

▸ **OutputsValidationResponseFromJSON**(`json`): [`OutputsValidationResponse`](interfaces/OutputsValidationResponse.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OutputsValidationResponse`](interfaces/OutputsValidationResponse.md)

#### Defined in

src/models/OutputsValidationResponse.ts:32

___

### OutputsValidationResponseFromJSONTyped

▸ **OutputsValidationResponseFromJSONTyped**(`json`, `ignoreDiscriminator`): [`OutputsValidationResponse`](interfaces/OutputsValidationResponse.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`OutputsValidationResponse`](interfaces/OutputsValidationResponse.md)

#### Defined in

src/models/OutputsValidationResponse.ts:38

___

### OutputsValidationResponseToJSON

▸ **OutputsValidationResponseToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`OutputsValidationResponse`](interfaces/OutputsValidationResponse.md) |

#### Returns

`any`

#### Defined in

src/models/OutputsValidationResponse.ts:52

___

### PassResultFromJSON

▸ **PassResultFromJSON**(`json`): [`PassResult`](interfaces/PassResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`PassResult`](interfaces/PassResult.md)

#### Defined in

src/models/PassResult.ts:55

___

### PassResultFromJSONTyped

▸ **PassResultFromJSONTyped**(`json`, `ignoreDiscriminator`): [`PassResult`](interfaces/PassResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`PassResult`](interfaces/PassResult.md)

#### Defined in

src/models/PassResult.ts:59

___

### PassResultToJSON

▸ **PassResultToJSON**(`json`): [`PassResult`](interfaces/PassResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`PassResult`](interfaces/PassResult.md)

#### Defined in

src/models/PassResult.ts:76

___

### PassResultToJSONTyped

▸ **PassResultToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`PassResult`](interfaces/PassResult.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/PassResult.ts:80

___

### PrimitivesFromJSON

▸ **PrimitivesFromJSON**(`json`): [`Primitives`](interfaces/Primitives.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Primitives`](interfaces/Primitives.md)

#### Defined in

src/models/Primitives.ts:29

___

### PrimitivesFromJSONTyped

▸ **PrimitivesFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Primitives`](interfaces/Primitives.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Primitives`](interfaces/Primitives.md)

#### Defined in

src/models/Primitives.ts:33

___

### PrimitivesToJSON

▸ **PrimitivesToJSON**(`json`): [`Primitives`](interfaces/Primitives.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Primitives`](interfaces/Primitives.md)

#### Defined in

src/models/Primitives.ts:40

___

### PrimitivesToJSONTyped

▸ **PrimitivesToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Primitives`](interfaces/Primitives.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Primitives.ts:44

___

### ReaskFromJSON

▸ **ReaskFromJSON**(`json`): [`Reask`](interfaces/Reask.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Reask`](interfaces/Reask.md)

#### Defined in

src/models/Reask.ts:46

___

### ReaskFromJSONTyped

▸ **ReaskFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Reask`](interfaces/Reask.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Reask`](interfaces/Reask.md)

#### Defined in

src/models/Reask.ts:50

___

### ReaskToJSON

▸ **ReaskToJSON**(`json`): [`Reask`](interfaces/Reask.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Reask`](interfaces/Reask.md)

#### Defined in

src/models/Reask.ts:68

___

### ReaskToJSONTyped

▸ **ReaskToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Reask`](interfaces/Reask.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Reask.ts:72

___

### SchemaFromJSON

▸ **SchemaFromJSON**(`json`): [`Schema`](interfaces/Schema.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Schema`](interfaces/Schema.md)

#### Defined in

src/models/Schema.ts:375

___

### SchemaFromJSONTyped

▸ **SchemaFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Schema`](interfaces/Schema.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Schema`](interfaces/Schema.md)

#### Defined in

src/models/Schema.ts:379

___

### SchemaToJSON

▸ **SchemaToJSON**(`json`): [`Schema`](interfaces/Schema.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Schema`](interfaces/Schema.md)

#### Defined in

src/models/Schema.ts:468

___

### SchemaToJSONTyped

▸ **SchemaToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Schema`](interfaces/Schema.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Schema.ts:472

___

### SimpleTypesFromJSON

▸ **SimpleTypesFromJSON**(`json`): [`SimpleTypes`](modules.md#simpletypes)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`SimpleTypes`](modules.md#simpletypes)

#### Defined in

src/models/SimpleTypes.ts:41

___

### SimpleTypesFromJSONTyped

▸ **SimpleTypesFromJSONTyped**(`json`, `ignoreDiscriminator`): [`SimpleTypes`](modules.md#simpletypes)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`SimpleTypes`](modules.md#simpletypes)

#### Defined in

src/models/SimpleTypes.ts:45

___

### SimpleTypesToJSON

▸ **SimpleTypesToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`SimpleTypes`](modules.md#simpletypes) |

#### Returns

`any`

#### Defined in

src/models/SimpleTypes.ts:52

___

### SimpleTypesToJSONTyped

▸ **SimpleTypesToJSONTyped**(`value`, `ignoreDiscriminator`): [`SimpleTypes`](modules.md#simpletypes)

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`SimpleTypes`](modules.md#simpletypes)

#### Defined in

src/models/SimpleTypes.ts:56

___

### UnevaluatedFromJSON

▸ **UnevaluatedFromJSON**(`json`): [`Unevaluated`](interfaces/Unevaluated.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Unevaluated`](interfaces/Unevaluated.md)

#### Defined in

src/models/Unevaluated.ts:42

___

### UnevaluatedFromJSONTyped

▸ **UnevaluatedFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Unevaluated`](interfaces/Unevaluated.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Unevaluated`](interfaces/Unevaluated.md)

#### Defined in

src/models/Unevaluated.ts:46

___

### UnevaluatedToJSON

▸ **UnevaluatedToJSON**(`json`): [`Unevaluated`](interfaces/Unevaluated.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Unevaluated`](interfaces/Unevaluated.md)

#### Defined in

src/models/Unevaluated.ts:63

___

### UnevaluatedToJSONTyped

▸ **UnevaluatedToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Unevaluated`](interfaces/Unevaluated.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Unevaluated.ts:67

___

### ValidatePayloadFromJSON

▸ **ValidatePayloadFromJSON**(`json`): [`ValidatePayload`](interfaces/ValidatePayload.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatePayload`](interfaces/ValidatePayload.md)

#### Defined in

src/models/ValidatePayload.ts:60

___

### ValidatePayloadFromJSONTyped

▸ **ValidatePayloadFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidatePayload`](interfaces/ValidatePayload.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidatePayload`](interfaces/ValidatePayload.md)

#### Defined in

src/models/ValidatePayload.ts:64

___

### ValidatePayloadToJSON

▸ **ValidatePayloadToJSON**(`json`): [`ValidatePayload`](interfaces/ValidatePayload.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatePayload`](interfaces/ValidatePayload.md)

#### Defined in

src/models/ValidatePayload.ts:82

___

### ValidatePayloadToJSONTyped

▸ **ValidatePayloadToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidatePayload`](interfaces/ValidatePayload.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidatePayload.ts:86

___

### ValidationFromJSON

▸ **ValidationFromJSON**(`json`): [`Validation`](interfaces/Validation.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Validation`](interfaces/Validation.md)

#### Defined in

src/models/Validation.ts:153

___

### ValidationFromJSONTyped

▸ **ValidationFromJSONTyped**(`json`, `ignoreDiscriminator`): [`Validation`](interfaces/Validation.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`Validation`](interfaces/Validation.md)

#### Defined in

src/models/Validation.ts:157

___

### ValidationOutcomeFromJSON

▸ **ValidationOutcomeFromJSON**(`json`): [`ValidationOutcome`](interfaces/ValidationOutcome.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationOutcome`](interfaces/ValidationOutcome.md)

#### Defined in

src/models/ValidationOutcome.ts:87

___

### ValidationOutcomeFromJSONTyped

▸ **ValidationOutcomeFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidationOutcome`](interfaces/ValidationOutcome.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidationOutcome`](interfaces/ValidationOutcome.md)

#### Defined in

src/models/ValidationOutcome.ts:91

___

### ValidationOutcomeToJSON

▸ **ValidationOutcomeToJSON**(`json`): [`ValidationOutcome`](interfaces/ValidationOutcome.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationOutcome`](interfaces/ValidationOutcome.md)

#### Defined in

src/models/ValidationOutcome.ts:119

___

### ValidationOutcomeToJSONTyped

▸ **ValidationOutcomeToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidationOutcome`](interfaces/ValidationOutcome.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidationOutcome.ts:123

___

### ValidationOutcomeValidatedOutputFromJSON

▸ **ValidationOutcomeValidatedOutputFromJSON**(`json`): [`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md)

#### Defined in

src/models/ValidationOutcomeValidatedOutput.ts:31

___

### ValidationOutcomeValidatedOutputFromJSONTyped

▸ **ValidationOutcomeValidatedOutputFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md)

#### Defined in

src/models/ValidationOutcomeValidatedOutput.ts:37

___

### ValidationOutcomeValidatedOutputToJSON

▸ **ValidationOutcomeValidatedOutputToJSON**(`json`): [`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md)

#### Defined in

src/models/ValidationOutcomeValidatedOutput.ts:44

___

### ValidationOutcomeValidatedOutputToJSONTyped

▸ **ValidationOutcomeValidatedOutputToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidationOutcomeValidatedOutput.ts:50

___

### ValidationResultFromJSON

▸ **ValidationResultFromJSON**(`json`): [`ValidationResult`](interfaces/ValidationResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationResult`](interfaces/ValidationResult.md)

#### Defined in

src/models/ValidationResult.ts:61

___

### ValidationResultFromJSONTyped

▸ **ValidationResultFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidationResult`](interfaces/ValidationResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidationResult`](interfaces/ValidationResult.md)

#### Defined in

src/models/ValidationResult.ts:65

___

### ValidationResultToJSON

▸ **ValidationResultToJSON**(`json`): [`ValidationResult`](interfaces/ValidationResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationResult`](interfaces/ValidationResult.md)

#### Defined in

src/models/ValidationResult.ts:80

___

### ValidationResultToJSONTyped

▸ **ValidationResultToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidationResult`](interfaces/ValidationResult.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidationResult.ts:84

___

### ValidationSummaryFromJSON

▸ **ValidationSummaryFromJSON**(`json`): [`ValidationSummary`](interfaces/ValidationSummary.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationSummary`](interfaces/ValidationSummary.md)

#### Defined in

src/models/ValidationSummary.ts:79

___

### ValidationSummaryFromJSONTyped

▸ **ValidationSummaryFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidationSummary`](interfaces/ValidationSummary.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidationSummary`](interfaces/ValidationSummary.md)

#### Defined in

src/models/ValidationSummary.ts:83

___

### ValidationSummaryToJSON

▸ **ValidationSummaryToJSON**(`json`): [`ValidationSummary`](interfaces/ValidationSummary.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationSummary`](interfaces/ValidationSummary.md)

#### Defined in

src/models/ValidationSummary.ts:104

___

### ValidationSummaryToJSONTyped

▸ **ValidationSummaryToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidationSummary`](interfaces/ValidationSummary.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidationSummary.ts:108

___

### ValidationToJSON

▸ **ValidationToJSON**(`json`): [`Validation`](interfaces/Validation.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`Validation`](interfaces/Validation.md)

#### Defined in

src/models/Validation.ts:194

___

### ValidationToJSONTyped

▸ **ValidationToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`Validation`](interfaces/Validation.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/Validation.ts:198

___

### ValidationTypeFromJSON

▸ **ValidationTypeFromJSON**(`json`): [`ValidationType`](interfaces/ValidationType.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationType`](interfaces/ValidationType.md)

#### Defined in

src/models/ValidationType.ts:31

___

### ValidationTypeFromJSONTyped

▸ **ValidationTypeFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidationType`](interfaces/ValidationType.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidationType`](interfaces/ValidationType.md)

#### Defined in

src/models/ValidationType.ts:35

___

### ValidationTypeToJSON

▸ **ValidationTypeToJSON**(`json`): [`ValidationType`](interfaces/ValidationType.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidationType`](interfaces/ValidationType.md)

#### Defined in

src/models/ValidationType.ts:42

___

### ValidationTypeToJSONTyped

▸ **ValidationTypeToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidationType`](interfaces/ValidationType.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidationType.ts:46

___

### ValidatorLogFromJSON

▸ **ValidatorLogFromJSON**(`json`): [`ValidatorLog`](interfaces/ValidatorLog.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorLog`](interfaces/ValidatorLog.md)

#### Defined in

src/models/ValidatorLog.ts:101

___

### ValidatorLogFromJSONTyped

▸ **ValidatorLogFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidatorLog`](interfaces/ValidatorLog.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidatorLog`](interfaces/ValidatorLog.md)

#### Defined in

src/models/ValidatorLog.ts:105

___

### ValidatorLogInstanceIdFromJSON

▸ **ValidatorLogInstanceIdFromJSON**(`json`): [`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md)

#### Defined in

src/models/ValidatorLogInstanceId.ts:31

___

### ValidatorLogInstanceIdFromJSONTyped

▸ **ValidatorLogInstanceIdFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md)

#### Defined in

src/models/ValidatorLogInstanceId.ts:37

___

### ValidatorLogInstanceIdToJSON

▸ **ValidatorLogInstanceIdToJSON**(`json`): [`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md)

#### Defined in

src/models/ValidatorLogInstanceId.ts:44

___

### ValidatorLogInstanceIdToJSONTyped

▸ **ValidatorLogInstanceIdToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidatorLogInstanceId.ts:50

___

### ValidatorLogToJSON

▸ **ValidatorLogToJSON**(`json`): [`ValidatorLog`](interfaces/ValidatorLog.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorLog`](interfaces/ValidatorLog.md)

#### Defined in

src/models/ValidatorLog.ts:132

___

### ValidatorLogToJSONTyped

▸ **ValidatorLogToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidatorLog`](interfaces/ValidatorLog.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidatorLog.ts:136

___

### ValidatorLogValidationResultFromJSON

▸ **ValidatorLogValidationResultFromJSON**(`json`): [`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md)

#### Defined in

src/models/ValidatorLogValidationResult.ts:90

___

### ValidatorLogValidationResultFromJSONTyped

▸ **ValidatorLogValidationResultFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md)

#### Defined in

src/models/ValidatorLogValidationResult.ts:96

___

### ValidatorLogValidationResultToJSON

▸ **ValidatorLogValidationResultToJSON**(`json`): [`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md)

#### Defined in

src/models/ValidatorLogValidationResult.ts:119

___

### ValidatorLogValidationResultToJSONTyped

▸ **ValidatorLogValidationResultToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidatorLogValidationResult.ts:125

___

### ValidatorReferenceFromJSON

▸ **ValidatorReferenceFromJSON**(`json`): [`ValidatorReference`](interfaces/ValidatorReference.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorReference`](interfaces/ValidatorReference.md)

#### Defined in

src/models/ValidatorReference.ts:79

___

### ValidatorReferenceFromJSONTyped

▸ **ValidatorReferenceFromJSONTyped**(`json`, `ignoreDiscriminator`): [`ValidatorReference`](interfaces/ValidatorReference.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`ValidatorReference`](interfaces/ValidatorReference.md)

#### Defined in

src/models/ValidatorReference.ts:83

___

### ValidatorReferenceToJSON

▸ **ValidatorReferenceToJSON**(`json`): [`ValidatorReference`](interfaces/ValidatorReference.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`ValidatorReference`](interfaces/ValidatorReference.md)

#### Defined in

src/models/ValidatorReference.ts:99

___

### ValidatorReferenceToJSONTyped

▸ **ValidatorReferenceToJSONTyped**(`value?`, `ignoreDiscriminator?`): `any`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `value?` | ``null`` \| [`ValidatorReference`](interfaces/ValidatorReference.md) | `undefined` |
| `ignoreDiscriminator` | `boolean` | `false` |

#### Returns

`any`

#### Defined in

src/models/ValidatorReference.ts:103

___

### canConsumeForm

▸ **canConsumeForm**(`consumes`): `boolean`

#### Parameters

| Name | Type |
| :------ | :------ |
| `consumes` | [`Consume`](interfaces/Consume.md)[] |

#### Returns

`boolean`

#### Defined in

src/runtime.ts:448

___

### exists

▸ **exists**(`json`, `key`): `boolean`

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `key` | `string` |

#### Returns

`boolean`

#### Defined in

src/runtime.ts:435

___

### instanceOfAnyType

▸ **instanceOfAnyType**(`value`): value is AnyType

Check if a given object implements the AnyType interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is AnyType

#### Defined in

src/models/AnyType.ts:25

___

### instanceOfApplicator

▸ **instanceOfApplicator**(`value`): value is Applicator

Check if a given object implements the Applicator interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Applicator

#### Defined in

src/models/Applicator.ts:116

___

### instanceOfArgsAndKwargs

▸ **instanceOfArgsAndKwargs**(`value`): value is ArgsAndKwargs

Check if a given object implements the ArgsAndKwargs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ArgsAndKwargs

#### Defined in

src/models/ArgsAndKwargs.ts:38

___

### instanceOfArraysInner

▸ **instanceOfArraysInner**(`value`): value is ArraysInner

Check if a given object implements the ArraysInner interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ArraysInner

#### Defined in

src/models/ArraysInner.ts:25

___

### instanceOfCall

▸ **instanceOfCall**(`value`): value is Call

Check if a given object implements the Call interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Call

#### Defined in

src/models/Call.ts:55

___

### instanceOfCallInputs

▸ **instanceOfCallInputs**(`value`): value is CallInputs

Check if a given object implements the CallInputs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is CallInputs

#### Defined in

src/models/CallInputs.ts:86

___

### instanceOfContent

▸ **instanceOfContent**(`value`): value is Content

Check if a given object implements the Content interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Content

#### Defined in

src/models/Content.ts:44

___

### instanceOfCore

▸ **instanceOfCore**(`value`): value is Core

Check if a given object implements the Core interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Core

#### Defined in

src/models/Core.ts:68

___

### instanceOfErrorSpan

▸ **instanceOfErrorSpan**(`value`): value is ErrorSpan

Check if a given object implements the ErrorSpan interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ErrorSpan

#### Defined in

src/models/ErrorSpan.ts:44

___

### instanceOfFailResult

▸ **instanceOfFailResult**(`value`): value is FailResult

Check if a given object implements the FailResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is FailResult

#### Defined in

src/models/FailResult.ts:65

___

### instanceOfFormatAnnotation

▸ **instanceOfFormatAnnotation**(`value`): value is FormatAnnotation

Check if a given object implements the FormatAnnotation interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is FormatAnnotation

#### Defined in

src/models/FormatAnnotation.ts:32

___

### instanceOfGuard

▸ **instanceOfGuard**(`value`): value is Guard

Check if a given object implements the Guard interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Guard

#### Defined in

src/models/Guard.ts:72

___

### instanceOfHealthCheck

▸ **instanceOfHealthCheck**(`value`): value is HealthCheck

Check if a given object implements the HealthCheck interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is HealthCheck

#### Defined in

src/models/HealthCheck.ts:38

___

### instanceOfHttpError

▸ **instanceOfHttpError**(`value`): value is HttpError

Check if a given object implements the HttpError interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is HttpError

#### Defined in

src/models/HttpError.ts:56

___

### instanceOfInputs

▸ **instanceOfInputs**(`value`): value is Inputs

Check if a given object implements the Inputs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Inputs

#### Defined in

src/models/Inputs.ts:74

___

### instanceOfIteration

▸ **instanceOfIteration**(`value`): value is Iteration

Check if a given object implements the Iteration interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Iteration

#### Defined in

src/models/Iteration.ts:61

___

### instanceOfLLMResource

▸ **instanceOfLLMResource**(`value`): `boolean`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `any` |

#### Returns

`boolean`

#### Defined in

src/models/LLMResource.ts:31

___

### instanceOfLLMResponse

▸ **instanceOfLLMResponse**(`value`): value is LLMResponse

Check if a given object implements the LLMResponse interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is LLMResponse

#### Defined in

src/models/LLMResponse.ts:56

___

### instanceOfMetaData

▸ **instanceOfMetaData**(`value`): value is MetaData

Check if a given object implements the MetaData interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is MetaData

#### Defined in

src/models/MetaData.ts:68

___

### instanceOfOpenAIChatCompletion

▸ **instanceOfOpenAIChatCompletion**(`value`): value is OpenAIChatCompletion

Check if a given object implements the OpenAIChatCompletion interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is OpenAIChatCompletion

#### Defined in

src/models/OpenAIChatCompletion.ts:56

___

### instanceOfOpenAIChatCompletionPayload

▸ **instanceOfOpenAIChatCompletionPayload**(`value`): value is OpenAIChatCompletionPayload

Check if a given object implements the OpenAIChatCompletionPayload interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is OpenAIChatCompletionPayload

#### Defined in

src/models/OpenAIChatCompletionPayload.ts:56

___

### instanceOfOpenAIChatCompletionPayloadMessagesInner

▸ **instanceOfOpenAIChatCompletionPayloadMessagesInner**(`value`): value is OpenAIChatCompletionPayloadMessagesInner

Check if a given object implements the OpenAIChatCompletionPayloadMessagesInner interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is OpenAIChatCompletionPayloadMessagesInner

#### Defined in

src/models/OpenAIChatCompletionPayloadMessagesInner.ts:38

___

### instanceOfOutputs

▸ **instanceOfOutputs**(`value`): value is Outputs

Check if a given object implements the Outputs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Outputs

#### Defined in

src/models/Outputs.ts:89

___

### instanceOfOutputsParsedOutput

▸ **instanceOfOutputsParsedOutput**(`value`): value is OutputsParsedOutput

Check if a given object implements the OutputsParsedOutput interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is OutputsParsedOutput

#### Defined in

src/models/OutputsParsedOutput.ts:25

___

### instanceOfOutputsValidationResponse

▸ **instanceOfOutputsValidationResponse**(`value`): `boolean`

Check if a given object implements the OutputsValidationResponse interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/OutputsValidationResponse.ts:28

___

### instanceOfPassResult

▸ **instanceOfPassResult**(`value`): value is PassResult

Check if a given object implements the PassResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is PassResult

#### Defined in

src/models/PassResult.ts:50

___

### instanceOfPrimitives

▸ **instanceOfPrimitives**(`value`): value is Primitives

Check if a given object implements the Primitives interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Primitives

#### Defined in

src/models/Primitives.ts:25

___

### instanceOfReask

▸ **instanceOfReask**(`value`): value is Reask

Check if a given object implements the Reask interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Reask

#### Defined in

src/models/Reask.ts:42

___

### instanceOfSchema

▸ **instanceOfSchema**(`value`): value is Schema

Check if a given object implements the Schema interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Schema

#### Defined in

src/models/Schema.ts:371

___

### instanceOfSimpleTypes

▸ **instanceOfSimpleTypes**(`value`): `boolean`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `any` |

#### Returns

`boolean`

#### Defined in

src/models/SimpleTypes.ts:30

___

### instanceOfUnevaluated

▸ **instanceOfUnevaluated**(`value`): value is Unevaluated

Check if a given object implements the Unevaluated interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Unevaluated

#### Defined in

src/models/Unevaluated.ts:38

___

### instanceOfValidatePayload

▸ **instanceOfValidatePayload**(`value`): value is ValidatePayload

Check if a given object implements the ValidatePayload interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidatePayload

#### Defined in

src/models/ValidatePayload.ts:54

___

### instanceOfValidation

▸ **instanceOfValidation**(`value`): value is Validation

Check if a given object implements the Validation interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is Validation

#### Defined in

src/models/Validation.ts:149

___

### instanceOfValidationOutcome

▸ **instanceOfValidationOutcome**(`value`): value is ValidationOutcome

Check if a given object implements the ValidationOutcome interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidationOutcome

#### Defined in

src/models/ValidationOutcome.ts:80

___

### instanceOfValidationOutcomeValidatedOutput

▸ **instanceOfValidationOutcomeValidatedOutput**(`value`): value is ValidationOutcomeValidatedOutput

Check if a given object implements the ValidationOutcomeValidatedOutput interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidationOutcomeValidatedOutput

#### Defined in

src/models/ValidationOutcomeValidatedOutput.ts:25

___

### instanceOfValidationResult

▸ **instanceOfValidationResult**(`value`): value is ValidationResult

Check if a given object implements the ValidationResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidationResult

#### Defined in

src/models/ValidationResult.ts:54

___

### instanceOfValidationSummary

▸ **instanceOfValidationSummary**(`value`): value is ValidationSummary

Check if a given object implements the ValidationSummary interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidationSummary

#### Defined in

src/models/ValidationSummary.ts:69

___

### instanceOfValidationType

▸ **instanceOfValidationType**(`value`): value is ValidationType

Check if a given object implements the ValidationType interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidationType

#### Defined in

src/models/ValidationType.ts:25

___

### instanceOfValidatorLog

▸ **instanceOfValidatorLog**(`value`): value is ValidatorLog

Check if a given object implements the ValidatorLog interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:86

___

### instanceOfValidatorLogInstanceId

▸ **instanceOfValidatorLogInstanceId**(`value`): value is ValidatorLogInstanceId

Check if a given object implements the ValidatorLogInstanceId interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidatorLogInstanceId

#### Defined in

src/models/ValidatorLogInstanceId.ts:25

___

### instanceOfValidatorLogValidationResult

▸ **instanceOfValidatorLogValidationResult**(`value`): value is ValidatorLogValidationResult

Check if a given object implements the ValidatorLogValidationResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidatorLogValidationResult

#### Defined in

src/models/ValidatorLogValidationResult.ts:81

___

### instanceOfValidatorReference

▸ **instanceOfValidatorReference**(`value`): value is ValidatorReference

Check if a given object implements the ValidatorReference interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

value is ValidatorReference

#### Defined in

src/models/ValidatorReference.ts:72

___

### mapValues

▸ **mapValues**(`data`, `fn`): `Object`

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |
| `fn` | (`item`: `any`) => `any` |

#### Returns

`Object`

#### Defined in

src/runtime.ts:440

___

### querystring

▸ **querystring**(`params`, `prefix?`): `string`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `params` | [`HTTPQuery`](modules.md#httpquery) | `undefined` |
| `prefix` | `string` | `""` |

#### Returns

`string`

#### Defined in

src/runtime.ts:395
