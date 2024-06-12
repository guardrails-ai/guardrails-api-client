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
- [CallException](interfaces/CallException.md)
- [CallExceptionAnyOf](interfaces/CallExceptionAnyOf.md)
- [CallInputs](interfaces/CallInputs.md)
- [ConfigurationParameters](interfaces/ConfigurationParameters.md)
- [Consume](interfaces/Consume.md)
- [Content](interfaces/Content.md)
- [Core](interfaces/Core.md)
- [CreateGuardRequest](interfaces/CreateGuardRequest.md)
- [DeleteGuardRequest](interfaces/DeleteGuardRequest.md)
- [ErrorContext](interfaces/ErrorContext.md)
- [FailResult](interfaces/FailResult.md)
- [FetchParams](interfaces/FetchParams.md)
- [FormatAnnotation](interfaces/FormatAnnotation.md)
- [GetGuardRequest](interfaces/GetGuardRequest.md)
- [Guard](interfaces/Guard.md)
- [GuardApiInterface](interfaces/GuardApiInterface.md)
- [GuardHistory](interfaces/GuardHistory.md)
- [GuardHistoryAnyOfInner](interfaces/GuardHistoryAnyOfInner.md)
- [HealthCheck](interfaces/HealthCheck.md)
- [HttpError](interfaces/HttpError.md)
- [Inputs](interfaces/Inputs.md)
- [Iteration](interfaces/Iteration.md)
- [LLMResponse](interfaces/LLMResponse.md)
- [MetaData](interfaces/MetaData.md)
- [Middleware](interfaces/Middleware.md)
- [Outputs](interfaces/Outputs.md)
- [OutputsException](interfaces/OutputsException.md)
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
- [ValidatorLogValidationResultOutcomeEnum](modules.md#validatorlogvalidationresultoutcomeenum)
- [ValidatorReferenceOnFailEnum](modules.md#validatorreferenceonfailenum)

### Variables

- [BASE\_PATH](modules.md#base_path)
- [COLLECTION\_FORMATS](modules.md#collection_formats)
- [DefaultConfig](modules.md#defaultconfig)
- [LLMResource](modules.md#llmresource-1)
- [SimpleTypes](modules.md#simpletypes-1)
- [ValidationResultOutcomeEnum](modules.md#validationresultoutcomeenum-1)
- [ValidatorLogValidationResultOutcomeEnum](modules.md#validatorlogvalidationresultoutcomeenum-1)
- [ValidatorReferenceOnFailEnum](modules.md#validatorreferenceonfailenum-1)

### Functions

- [AnyTypeFromJSON](modules.md#anytypefromjson)
- [AnyTypeFromJSONTyped](modules.md#anytypefromjsontyped)
- [AnyTypeToJSON](modules.md#anytypetojson)
- [ApplicatorFromJSON](modules.md#applicatorfromjson)
- [ApplicatorFromJSONTyped](modules.md#applicatorfromjsontyped)
- [ApplicatorToJSON](modules.md#applicatortojson)
- [ArgsAndKwargsFromJSON](modules.md#argsandkwargsfromjson)
- [ArgsAndKwargsFromJSONTyped](modules.md#argsandkwargsfromjsontyped)
- [ArgsAndKwargsToJSON](modules.md#argsandkwargstojson)
- [ArraysInnerFromJSON](modules.md#arraysinnerfromjson)
- [ArraysInnerFromJSONTyped](modules.md#arraysinnerfromjsontyped)
- [ArraysInnerToJSON](modules.md#arraysinnertojson)
- [CallExceptionAnyOfFromJSON](modules.md#callexceptionanyoffromjson)
- [CallExceptionAnyOfFromJSONTyped](modules.md#callexceptionanyoffromjsontyped)
- [CallExceptionAnyOfToJSON](modules.md#callexceptionanyoftojson)
- [CallExceptionFromJSON](modules.md#callexceptionfromjson)
- [CallExceptionFromJSONTyped](modules.md#callexceptionfromjsontyped)
- [CallExceptionToJSON](modules.md#callexceptiontojson)
- [CallFromJSON](modules.md#callfromjson)
- [CallFromJSONTyped](modules.md#callfromjsontyped)
- [CallInputsFromJSON](modules.md#callinputsfromjson)
- [CallInputsFromJSONTyped](modules.md#callinputsfromjsontyped)
- [CallInputsToJSON](modules.md#callinputstojson)
- [CallToJSON](modules.md#calltojson)
- [ContentFromJSON](modules.md#contentfromjson)
- [ContentFromJSONTyped](modules.md#contentfromjsontyped)
- [ContentToJSON](modules.md#contenttojson)
- [CoreFromJSON](modules.md#corefromjson)
- [CoreFromJSONTyped](modules.md#corefromjsontyped)
- [CoreToJSON](modules.md#coretojson)
- [FailResultFromJSON](modules.md#failresultfromjson)
- [FailResultFromJSONTyped](modules.md#failresultfromjsontyped)
- [FailResultToJSON](modules.md#failresulttojson)
- [FormatAnnotationFromJSON](modules.md#formatannotationfromjson)
- [FormatAnnotationFromJSONTyped](modules.md#formatannotationfromjsontyped)
- [FormatAnnotationToJSON](modules.md#formatannotationtojson)
- [GuardFromJSON](modules.md#guardfromjson)
- [GuardFromJSONTyped](modules.md#guardfromjsontyped)
- [GuardHistoryAnyOfInnerFromJSON](modules.md#guardhistoryanyofinnerfromjson)
- [GuardHistoryAnyOfInnerFromJSONTyped](modules.md#guardhistoryanyofinnerfromjsontyped)
- [GuardHistoryAnyOfInnerToJSON](modules.md#guardhistoryanyofinnertojson)
- [GuardHistoryFromJSON](modules.md#guardhistoryfromjson)
- [GuardHistoryFromJSONTyped](modules.md#guardhistoryfromjsontyped)
- [GuardHistoryToJSON](modules.md#guardhistorytojson)
- [GuardToJSON](modules.md#guardtojson)
- [HealthCheckFromJSON](modules.md#healthcheckfromjson)
- [HealthCheckFromJSONTyped](modules.md#healthcheckfromjsontyped)
- [HealthCheckToJSON](modules.md#healthchecktojson)
- [HttpErrorFromJSON](modules.md#httperrorfromjson)
- [HttpErrorFromJSONTyped](modules.md#httperrorfromjsontyped)
- [HttpErrorToJSON](modules.md#httperrortojson)
- [InputsFromJSON](modules.md#inputsfromjson)
- [InputsFromJSONTyped](modules.md#inputsfromjsontyped)
- [InputsToJSON](modules.md#inputstojson)
- [IterationFromJSON](modules.md#iterationfromjson)
- [IterationFromJSONTyped](modules.md#iterationfromjsontyped)
- [IterationToJSON](modules.md#iterationtojson)
- [LLMResourceFromJSON](modules.md#llmresourcefromjson)
- [LLMResourceFromJSONTyped](modules.md#llmresourcefromjsontyped)
- [LLMResourceToJSON](modules.md#llmresourcetojson)
- [LLMResponseFromJSON](modules.md#llmresponsefromjson)
- [LLMResponseFromJSONTyped](modules.md#llmresponsefromjsontyped)
- [LLMResponseToJSON](modules.md#llmresponsetojson)
- [MetaDataFromJSON](modules.md#metadatafromjson)
- [MetaDataFromJSONTyped](modules.md#metadatafromjsontyped)
- [MetaDataToJSON](modules.md#metadatatojson)
- [OutputsExceptionFromJSON](modules.md#outputsexceptionfromjson)
- [OutputsExceptionFromJSONTyped](modules.md#outputsexceptionfromjsontyped)
- [OutputsExceptionToJSON](modules.md#outputsexceptiontojson)
- [OutputsFromJSON](modules.md#outputsfromjson)
- [OutputsFromJSONTyped](modules.md#outputsfromjsontyped)
- [OutputsParsedOutputFromJSON](modules.md#outputsparsedoutputfromjson)
- [OutputsParsedOutputFromJSONTyped](modules.md#outputsparsedoutputfromjsontyped)
- [OutputsParsedOutputToJSON](modules.md#outputsparsedoutputtojson)
- [OutputsToJSON](modules.md#outputstojson)
- [OutputsValidationResponseFromJSON](modules.md#outputsvalidationresponsefromjson)
- [OutputsValidationResponseFromJSONTyped](modules.md#outputsvalidationresponsefromjsontyped)
- [OutputsValidationResponseToJSON](modules.md#outputsvalidationresponsetojson)
- [PassResultFromJSON](modules.md#passresultfromjson)
- [PassResultFromJSONTyped](modules.md#passresultfromjsontyped)
- [PassResultToJSON](modules.md#passresulttojson)
- [PrimitivesFromJSON](modules.md#primitivesfromjson)
- [PrimitivesFromJSONTyped](modules.md#primitivesfromjsontyped)
- [PrimitivesToJSON](modules.md#primitivestojson)
- [ReaskFromJSON](modules.md#reaskfromjson)
- [ReaskFromJSONTyped](modules.md#reaskfromjsontyped)
- [ReaskToJSON](modules.md#reasktojson)
- [SchemaFromJSON](modules.md#schemafromjson)
- [SchemaFromJSONTyped](modules.md#schemafromjsontyped)
- [SchemaToJSON](modules.md#schematojson)
- [SimpleTypesFromJSON](modules.md#simpletypesfromjson)
- [SimpleTypesFromJSONTyped](modules.md#simpletypesfromjsontyped)
- [SimpleTypesToJSON](modules.md#simpletypestojson)
- [UnevaluatedFromJSON](modules.md#unevaluatedfromjson)
- [UnevaluatedFromJSONTyped](modules.md#unevaluatedfromjsontyped)
- [UnevaluatedToJSON](modules.md#unevaluatedtojson)
- [ValidatePayloadFromJSON](modules.md#validatepayloadfromjson)
- [ValidatePayloadFromJSONTyped](modules.md#validatepayloadfromjsontyped)
- [ValidatePayloadToJSON](modules.md#validatepayloadtojson)
- [ValidationFromJSON](modules.md#validationfromjson)
- [ValidationFromJSONTyped](modules.md#validationfromjsontyped)
- [ValidationOutcomeFromJSON](modules.md#validationoutcomefromjson)
- [ValidationOutcomeFromJSONTyped](modules.md#validationoutcomefromjsontyped)
- [ValidationOutcomeToJSON](modules.md#validationoutcometojson)
- [ValidationOutcomeValidatedOutputFromJSON](modules.md#validationoutcomevalidatedoutputfromjson)
- [ValidationOutcomeValidatedOutputFromJSONTyped](modules.md#validationoutcomevalidatedoutputfromjsontyped)
- [ValidationOutcomeValidatedOutputToJSON](modules.md#validationoutcomevalidatedoutputtojson)
- [ValidationResultFromJSON](modules.md#validationresultfromjson)
- [ValidationResultFromJSONTyped](modules.md#validationresultfromjsontyped)
- [ValidationResultToJSON](modules.md#validationresulttojson)
- [ValidationToJSON](modules.md#validationtojson)
- [ValidationTypeFromJSON](modules.md#validationtypefromjson)
- [ValidationTypeFromJSONTyped](modules.md#validationtypefromjsontyped)
- [ValidationTypeToJSON](modules.md#validationtypetojson)
- [ValidatorLogFromJSON](modules.md#validatorlogfromjson)
- [ValidatorLogFromJSONTyped](modules.md#validatorlogfromjsontyped)
- [ValidatorLogInstanceIdFromJSON](modules.md#validatorloginstanceidfromjson)
- [ValidatorLogInstanceIdFromJSONTyped](modules.md#validatorloginstanceidfromjsontyped)
- [ValidatorLogInstanceIdToJSON](modules.md#validatorloginstanceidtojson)
- [ValidatorLogToJSON](modules.md#validatorlogtojson)
- [ValidatorLogValidationResultFromJSON](modules.md#validatorlogvalidationresultfromjson)
- [ValidatorLogValidationResultFromJSONTyped](modules.md#validatorlogvalidationresultfromjsontyped)
- [ValidatorLogValidationResultToJSON](modules.md#validatorlogvalidationresulttojson)
- [ValidatorReferenceFromJSON](modules.md#validatorreferencefromjson)
- [ValidatorReferenceFromJSONTyped](modules.md#validatorreferencefromjsontyped)
- [ValidatorReferenceToJSON](modules.md#validatorreferencetojson)
- [canConsumeForm](modules.md#canconsumeform)
- [instanceOfAnyType](modules.md#instanceofanytype)
- [instanceOfApplicator](modules.md#instanceofapplicator)
- [instanceOfArgsAndKwargs](modules.md#instanceofargsandkwargs)
- [instanceOfArraysInner](modules.md#instanceofarraysinner)
- [instanceOfCall](modules.md#instanceofcall)
- [instanceOfCallException](modules.md#instanceofcallexception)
- [instanceOfCallExceptionAnyOf](modules.md#instanceofcallexceptionanyof)
- [instanceOfCallInputs](modules.md#instanceofcallinputs)
- [instanceOfContent](modules.md#instanceofcontent)
- [instanceOfCore](modules.md#instanceofcore)
- [instanceOfFailResult](modules.md#instanceoffailresult)
- [instanceOfFormatAnnotation](modules.md#instanceofformatannotation)
- [instanceOfGuard](modules.md#instanceofguard)
- [instanceOfGuardHistory](modules.md#instanceofguardhistory)
- [instanceOfGuardHistoryAnyOfInner](modules.md#instanceofguardhistoryanyofinner)
- [instanceOfHealthCheck](modules.md#instanceofhealthcheck)
- [instanceOfHttpError](modules.md#instanceofhttperror)
- [instanceOfInputs](modules.md#instanceofinputs)
- [instanceOfIteration](modules.md#instanceofiteration)
- [instanceOfLLMResource](modules.md#instanceofllmresource)
- [instanceOfLLMResponse](modules.md#instanceofllmresponse)
- [instanceOfMetaData](modules.md#instanceofmetadata)
- [instanceOfOutputs](modules.md#instanceofoutputs)
- [instanceOfOutputsException](modules.md#instanceofoutputsexception)
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

src/models/ValidatorReference.ts:115

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

src/models/ValidationResult.ts:38

src/models/ValidationResult.ts:42

___

### ValidatorLogValidationResultOutcomeEnum

Ƭ **ValidatorLogValidationResultOutcomeEnum**: typeof [`ValidatorLogValidationResultOutcomeEnum`](modules.md#validatorlogvalidationresultoutcomeenum-1)[keyof typeof [`ValidatorLogValidationResultOutcomeEnum`](modules.md#validatorlogvalidationresultoutcomeenum-1)]

#### Defined in

src/models/ValidatorLogValidationResult.ts:56

src/models/ValidatorLogValidationResult.ts:60

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

src/models/ValidationResult.ts:38

src/models/ValidationResult.ts:42

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

src/models/ValidatorLogValidationResult.ts:56

src/models/ValidatorLogValidationResult.ts:60

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

▸ **AnyTypeToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`AnyType`](interfaces/AnyType.md) |

#### Returns

`any`

#### Defined in

src/models/AnyType.ts:40

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

▸ **ApplicatorToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Applicator`](interfaces/Applicator.md) |

#### Returns

`any`

#### Defined in

src/models/Applicator.ts:156

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

▸ **ArgsAndKwargsToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ArgsAndKwargs`](interfaces/ArgsAndKwargs.md) |

#### Returns

`any`

#### Defined in

src/models/ArgsAndKwargs.ts:59

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

▸ **ArraysInnerToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ArraysInner`](interfaces/ArraysInner.md) |

#### Returns

`any`

#### Defined in

src/models/ArraysInner.ts:40

___

### CallExceptionAnyOfFromJSON

▸ **CallExceptionAnyOfFromJSON**(`json`): [`CallExceptionAnyOf`](interfaces/CallExceptionAnyOf.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`CallExceptionAnyOf`](interfaces/CallExceptionAnyOf.md)

#### Defined in

src/models/CallExceptionAnyOf.ts:37

___

### CallExceptionAnyOfFromJSONTyped

▸ **CallExceptionAnyOfFromJSONTyped**(`json`, `ignoreDiscriminator`): [`CallExceptionAnyOf`](interfaces/CallExceptionAnyOf.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`CallExceptionAnyOf`](interfaces/CallExceptionAnyOf.md)

#### Defined in

src/models/CallExceptionAnyOf.ts:41

___

### CallExceptionAnyOfToJSON

▸ **CallExceptionAnyOfToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`CallExceptionAnyOf`](interfaces/CallExceptionAnyOf.md) |

#### Returns

`any`

#### Defined in

src/models/CallExceptionAnyOf.ts:54

___

### CallExceptionFromJSON

▸ **CallExceptionFromJSON**(`json`): `string` \| [`CallException`](interfaces/CallException.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `string` \| \{ `[key: string]`: `any`;  } |

#### Returns

`string` \| [`CallException`](interfaces/CallException.md)

#### Defined in

src/models/CallException.ts:47

___

### CallExceptionFromJSONTyped

▸ **CallExceptionFromJSONTyped**(`json`, `ignoreDiscriminator`): `string` \| [`CallException`](interfaces/CallException.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `string` \| \{ `[key: string]`: `any`;  } |
| `ignoreDiscriminator` | `boolean` |

#### Returns

`string` \| [`CallException`](interfaces/CallException.md)

#### Defined in

src/models/CallException.ts:53

___

### CallExceptionToJSON

▸ **CallExceptionToJSON**(`value?`): `string` \| \{ `[key: string]`: `any`;  } \| ``null`` \| `undefined`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| `string` \| [`CallException`](interfaces/CallException.md) |

#### Returns

`string` \| \{ `[key: string]`: `any`;  } \| ``null`` \| `undefined`

#### Defined in

src/models/CallException.ts:72

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

src/models/Call.ts:55

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

src/models/Call.ts:59

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

src/models/CallInputs.ts:96

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

src/models/CallInputs.ts:100

___

### CallInputsToJSON

▸ **CallInputsToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`CallInputs`](interfaces/CallInputs.md) |

#### Returns

`any`

#### Defined in

src/models/CallInputs.ts:125

___

### CallToJSON

▸ **CallToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Call`](interfaces/Call.md) |

#### Returns

`any`

#### Defined in

src/models/Call.ts:80

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

▸ **ContentToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Content`](interfaces/Content.md) |

#### Returns

`any`

#### Defined in

src/models/Content.ts:69

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

▸ **CoreToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Core`](interfaces/Core.md) |

#### Returns

`any`

#### Defined in

src/models/Core.ts:95

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

src/models/FailResult.ts:54

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

src/models/FailResult.ts:58

___

### FailResultToJSON

▸ **FailResultToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`FailResult`](interfaces/FailResult.md) |

#### Returns

`any`

#### Defined in

src/models/FailResult.ts:74

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

src/models/FormatAnnotation.ts:36

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

src/models/FormatAnnotation.ts:40

___

### FormatAnnotationToJSON

▸ **FormatAnnotationToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`FormatAnnotation`](interfaces/FormatAnnotation.md) |

#### Returns

`any`

#### Defined in

src/models/FormatAnnotation.ts:52

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

src/models/Guard.ts:79

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

src/models/Guard.ts:83

___

### GuardHistoryAnyOfInnerFromJSON

▸ **GuardHistoryAnyOfInnerFromJSON**(`json`): [`GuardHistoryAnyOfInner`](interfaces/GuardHistoryAnyOfInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`GuardHistoryAnyOfInner`](interfaces/GuardHistoryAnyOfInner.md)

#### Defined in

src/models/GuardHistoryAnyOfInner.ts:36

___

### GuardHistoryAnyOfInnerFromJSONTyped

▸ **GuardHistoryAnyOfInnerFromJSONTyped**(`json`, `ignoreDiscriminator`): [`GuardHistoryAnyOfInner`](interfaces/GuardHistoryAnyOfInner.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`GuardHistoryAnyOfInner`](interfaces/GuardHistoryAnyOfInner.md)

#### Defined in

src/models/GuardHistoryAnyOfInner.ts:42

___

### GuardHistoryAnyOfInnerToJSON

▸ **GuardHistoryAnyOfInnerToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`GuardHistoryAnyOfInner`](interfaces/GuardHistoryAnyOfInner.md) |

#### Returns

`any`

#### Defined in

src/models/GuardHistoryAnyOfInner.ts:54

___

### GuardHistoryFromJSON

▸ **GuardHistoryFromJSON**(`json`): [`GuardHistory`](interfaces/GuardHistory.md) \| [`Call`](interfaces/Call.md)[]

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`GuardHistory`](interfaces/GuardHistory.md) \| [`Call`](interfaces/Call.md)[]

#### Defined in

src/models/GuardHistory.ts:39

___

### GuardHistoryFromJSONTyped

▸ **GuardHistoryFromJSONTyped**(`json`, `ignoreDiscriminator`): [`GuardHistory`](interfaces/GuardHistory.md) \| [`Call`](interfaces/Call.md)[]

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`GuardHistory`](interfaces/GuardHistory.md) \| [`Call`](interfaces/Call.md)[]

#### Defined in

src/models/GuardHistory.ts:43

___

### GuardHistoryToJSON

▸ **GuardHistoryToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`GuardHistory`](interfaces/GuardHistory.md) \| [`Call`](interfaces/Call.md)[] |

#### Returns

`any`

#### Defined in

src/models/GuardHistory.ts:57

___

### GuardToJSON

▸ **GuardToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Guard`](interfaces/Guard.md) |

#### Returns

`any`

#### Defined in

src/models/Guard.ts:109

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

▸ **HealthCheckToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`HealthCheck`](interfaces/HealthCheck.md) |

#### Returns

`any`

#### Defined in

src/models/HealthCheck.ts:61

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

▸ **HttpErrorToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`HttpError`](interfaces/HttpError.md) |

#### Returns

`any`

#### Defined in

src/models/HttpError.ts:82

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

src/models/Inputs.ts:84

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

src/models/Inputs.ts:88

___

### InputsToJSON

▸ **InputsToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Inputs`](interfaces/Inputs.md) |

#### Returns

`any`

#### Defined in

src/models/Inputs.ts:111

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

src/models/Iteration.ts:47

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

src/models/Iteration.ts:51

___

### IterationToJSON

▸ **IterationToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Iteration`](interfaces/Iteration.md) |

#### Returns

`any`

#### Defined in

src/models/Iteration.ts:65

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

src/models/LLMResource.ts:35

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

src/models/LLMResource.ts:39

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

src/models/LLMResource.ts:46

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

src/models/LLMResponse.ts:54

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

src/models/LLMResponse.ts:58

___

### LLMResponseToJSON

▸ **LLMResponseToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`LLMResponse`](interfaces/LLMResponse.md) |

#### Returns

`any`

#### Defined in

src/models/LLMResponse.ts:78

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

▸ **MetaDataToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`MetaData`](interfaces/MetaData.md) |

#### Returns

`any`

#### Defined in

src/models/MetaData.ts:94

___

### OutputsExceptionFromJSON

▸ **OutputsExceptionFromJSON**(`json`): [`OutputsException`](interfaces/OutputsException.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |

#### Returns

[`OutputsException`](interfaces/OutputsException.md)

#### Defined in

src/models/OutputsException.ts:37

___

### OutputsExceptionFromJSONTyped

▸ **OutputsExceptionFromJSONTyped**(`json`, `ignoreDiscriminator`): [`OutputsException`](interfaces/OutputsException.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `json` | `any` |
| `ignoreDiscriminator` | `boolean` |

#### Returns

[`OutputsException`](interfaces/OutputsException.md)

#### Defined in

src/models/OutputsException.ts:41

___

### OutputsExceptionToJSON

▸ **OutputsExceptionToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`OutputsException`](interfaces/OutputsException.md) |

#### Returns

`any`

#### Defined in

src/models/OutputsException.ts:54

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

src/models/Outputs.ts:104

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

src/models/Outputs.ts:108

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

src/models/OutputsParsedOutput.ts:29

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

src/models/OutputsParsedOutput.ts:33

___

### OutputsParsedOutputToJSON

▸ **OutputsParsedOutputToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`OutputsParsedOutput`](interfaces/OutputsParsedOutput.md) |

#### Returns

`any`

#### Defined in

src/models/OutputsParsedOutput.ts:40

___

### OutputsToJSON

▸ **OutputsToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Outputs`](interfaces/Outputs.md) |

#### Returns

`any`

#### Defined in

src/models/Outputs.ts:149

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

src/models/PassResult.ts:48

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

src/models/PassResult.ts:52

___

### PassResultToJSON

▸ **PassResultToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`PassResult`](interfaces/PassResult.md) |

#### Returns

`any`

#### Defined in

src/models/PassResult.ts:67

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

▸ **PrimitivesToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Primitives`](interfaces/Primitives.md) |

#### Returns

`any`

#### Defined in

src/models/Primitives.ts:40

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

src/models/Reask.ts:45

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

src/models/Reask.ts:49

___

### ReaskToJSON

▸ **ReaskToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Reask`](interfaces/Reask.md) |

#### Returns

`any`

#### Defined in

src/models/Reask.ts:66

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

▸ **SchemaToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Schema`](interfaces/Schema.md) |

#### Returns

`any`

#### Defined in

src/models/Schema.ts:468

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

src/models/SimpleTypes.ts:34

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

src/models/SimpleTypes.ts:38

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

src/models/SimpleTypes.ts:45

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

▸ **UnevaluatedToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Unevaluated`](interfaces/Unevaluated.md) |

#### Returns

`any`

#### Defined in

src/models/Unevaluated.ts:63

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

src/models/ValidatePayload.ts:58

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

src/models/ValidatePayload.ts:62

___

### ValidatePayloadToJSON

▸ **ValidatePayloadToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidatePayload`](interfaces/ValidatePayload.md) |

#### Returns

`any`

#### Defined in

src/models/ValidatePayload.ts:80

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

src/models/ValidationOutcome.ts:67

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

src/models/ValidationOutcome.ts:71

___

### ValidationOutcomeToJSON

▸ **ValidationOutcomeToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidationOutcome`](interfaces/ValidationOutcome.md) |

#### Returns

`any`

#### Defined in

src/models/ValidationOutcome.ts:92

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

▸ **ValidationOutcomeValidatedOutputToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidationOutcomeValidatedOutput`](interfaces/ValidationOutcomeValidatedOutput.md) |

#### Returns

`any`

#### Defined in

src/models/ValidationOutcomeValidatedOutput.ts:44

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

src/models/ValidationResult.ts:52

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

src/models/ValidationResult.ts:56

___

### ValidationResultToJSON

▸ **ValidationResultToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidationResult`](interfaces/ValidationResult.md) |

#### Returns

`any`

#### Defined in

src/models/ValidationResult.ts:69

___

### ValidationToJSON

▸ **ValidationToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`Validation`](interfaces/Validation.md) |

#### Returns

`any`

#### Defined in

src/models/Validation.ts:194

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

src/models/ValidationType.ts:29

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

src/models/ValidationType.ts:33

___

### ValidationTypeToJSON

▸ **ValidationTypeToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidationType`](interfaces/ValidationType.md) |

#### Returns

`any`

#### Defined in

src/models/ValidationType.ts:40

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

src/models/ValidatorLog.ts:90

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

src/models/ValidatorLog.ts:94

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

src/models/ValidatorLogInstanceId.ts:29

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

src/models/ValidatorLogInstanceId.ts:35

___

### ValidatorLogInstanceIdToJSON

▸ **ValidatorLogInstanceIdToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidatorLogInstanceId`](interfaces/ValidatorLogInstanceId.md) |

#### Returns

`any`

#### Defined in

src/models/ValidatorLogInstanceId.ts:42

___

### ValidatorLogToJSON

▸ **ValidatorLogToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidatorLog`](interfaces/ValidatorLog.md) |

#### Returns

`any`

#### Defined in

src/models/ValidatorLog.ts:127

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

src/models/ValidatorLogValidationResult.ts:70

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

src/models/ValidatorLogValidationResult.ts:76

___

### ValidatorLogValidationResultToJSON

▸ **ValidatorLogValidationResultToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidatorLogValidationResult`](interfaces/ValidatorLogValidationResult.md) |

#### Returns

`any`

#### Defined in

src/models/ValidatorLogValidationResult.ts:94

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

src/models/ValidatorReference.ts:77

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

src/models/ValidatorReference.ts:81

___

### ValidatorReferenceToJSON

▸ **ValidatorReferenceToJSON**(`value?`): `any`

#### Parameters

| Name | Type |
| :------ | :------ |
| `value?` | ``null`` \| [`ValidatorReference`](interfaces/ValidatorReference.md) |

#### Returns

`any`

#### Defined in

src/models/ValidatorReference.ts:97

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

src/runtime.ts:442

___

### instanceOfAnyType

▸ **instanceOfAnyType**(`value`): `boolean`

Check if a given object implements the AnyType interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/AnyType.ts:25

___

### instanceOfApplicator

▸ **instanceOfApplicator**(`value`): `boolean`

Check if a given object implements the Applicator interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Applicator.ts:116

___

### instanceOfArgsAndKwargs

▸ **instanceOfArgsAndKwargs**(`value`): `boolean`

Check if a given object implements the ArgsAndKwargs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ArgsAndKwargs.ts:38

___

### instanceOfArraysInner

▸ **instanceOfArraysInner**(`value`): `boolean`

Check if a given object implements the ArraysInner interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ArraysInner.ts:25

___

### instanceOfCall

▸ **instanceOfCall**(`value`): `boolean`

Check if a given object implements the Call interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Call.ts:51

___

### instanceOfCallException

▸ **instanceOfCallException**(`value`): `boolean`

Check if a given object implements the CallException interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `string` \| \{ `[key: string]`: `any`;  } |

#### Returns

`boolean`

#### Defined in

src/models/CallException.ts:32

___

### instanceOfCallExceptionAnyOf

▸ **instanceOfCallExceptionAnyOf**(`value`): `boolean`

Check if a given object implements the CallExceptionAnyOf interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/CallExceptionAnyOf.ts:33

___

### instanceOfCallInputs

▸ **instanceOfCallInputs**(`value`): `boolean`

Check if a given object implements the CallInputs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/CallInputs.ts:92

___

### instanceOfContent

▸ **instanceOfContent**(`value`): `boolean`

Check if a given object implements the Content interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Content.ts:44

___

### instanceOfCore

▸ **instanceOfCore**(`value`): `boolean`

Check if a given object implements the Core interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Core.ts:68

___

### instanceOfFailResult

▸ **instanceOfFailResult**(`value`): `boolean`

Check if a given object implements the FailResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/FailResult.ts:50

___

### instanceOfFormatAnnotation

▸ **instanceOfFormatAnnotation**(`value`): `boolean`

Check if a given object implements the FormatAnnotation interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/FormatAnnotation.ts:32

___

### instanceOfGuard

▸ **instanceOfGuard**(`value`): `boolean`

Check if a given object implements the Guard interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Guard.ts:73

___

### instanceOfGuardHistory

▸ **instanceOfGuardHistory**(`value`): `boolean`

Check if a given object implements the GuardHistory interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `Object` |

#### Returns

`boolean`

#### Defined in

src/models/GuardHistory.ts:35

___

### instanceOfGuardHistoryAnyOfInner

▸ **instanceOfGuardHistoryAnyOfInner**(`value`): `boolean`

Check if a given object implements the GuardHistoryAnyOfInner interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/GuardHistoryAnyOfInner.ts:32

___

### instanceOfHealthCheck

▸ **instanceOfHealthCheck**(`value`): `boolean`

Check if a given object implements the HealthCheck interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/HealthCheck.ts:38

___

### instanceOfHttpError

▸ **instanceOfHttpError**(`value`): `boolean`

Check if a given object implements the HttpError interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/HttpError.ts:56

___

### instanceOfInputs

▸ **instanceOfInputs**(`value`): `boolean`

Check if a given object implements the Inputs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Inputs.ts:80

___

### instanceOfIteration

▸ **instanceOfIteration**(`value`): `boolean`

Check if a given object implements the Iteration interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Iteration.ts:43

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

▸ **instanceOfLLMResponse**(`value`): `boolean`

Check if a given object implements the LLMResponse interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/LLMResponse.ts:50

___

### instanceOfMetaData

▸ **instanceOfMetaData**(`value`): `boolean`

Check if a given object implements the MetaData interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/MetaData.ts:68

___

### instanceOfOutputs

▸ **instanceOfOutputs**(`value`): `boolean`

Check if a given object implements the Outputs interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Outputs.ts:100

___

### instanceOfOutputsException

▸ **instanceOfOutputsException**(`value`): `boolean`

Check if a given object implements the OutputsException interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/OutputsException.ts:33

___

### instanceOfOutputsParsedOutput

▸ **instanceOfOutputsParsedOutput**(`value`): `boolean`

Check if a given object implements the OutputsParsedOutput interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

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

▸ **instanceOfPassResult**(`value`): `boolean`

Check if a given object implements the PassResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/PassResult.ts:44

___

### instanceOfPrimitives

▸ **instanceOfPrimitives**(`value`): `boolean`

Check if a given object implements the Primitives interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Primitives.ts:25

___

### instanceOfReask

▸ **instanceOfReask**(`value`): `boolean`

Check if a given object implements the Reask interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Reask.ts:41

___

### instanceOfSchema

▸ **instanceOfSchema**(`value`): `boolean`

Check if a given object implements the Schema interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

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

▸ **instanceOfUnevaluated**(`value`): `boolean`

Check if a given object implements the Unevaluated interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Unevaluated.ts:38

___

### instanceOfValidatePayload

▸ **instanceOfValidatePayload**(`value`): `boolean`

Check if a given object implements the ValidatePayload interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidatePayload.ts:54

___

### instanceOfValidation

▸ **instanceOfValidation**(`value`): `boolean`

Check if a given object implements the Validation interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/Validation.ts:149

___

### instanceOfValidationOutcome

▸ **instanceOfValidationOutcome**(`value`): `boolean`

Check if a given object implements the ValidationOutcome interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidationOutcome.ts:63

___

### instanceOfValidationOutcomeValidatedOutput

▸ **instanceOfValidationOutcomeValidatedOutput**(`value`): `boolean`

Check if a given object implements the ValidationOutcomeValidatedOutput interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidationOutcomeValidatedOutput.ts:25

___

### instanceOfValidationResult

▸ **instanceOfValidationResult**(`value`): `boolean`

Check if a given object implements the ValidationResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidationResult.ts:48

___

### instanceOfValidationType

▸ **instanceOfValidationType**(`value`): `boolean`

Check if a given object implements the ValidationType interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidationType.ts:25

___

### instanceOfValidatorLog

▸ **instanceOfValidatorLog**(`value`): `boolean`

Check if a given object implements the ValidatorLog interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidatorLog.ts:86

___

### instanceOfValidatorLogInstanceId

▸ **instanceOfValidatorLogInstanceId**(`value`): `boolean`

Check if a given object implements the ValidatorLogInstanceId interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidatorLogInstanceId.ts:25

___

### instanceOfValidatorLogValidationResult

▸ **instanceOfValidatorLogValidationResult**(`value`): `boolean`

Check if a given object implements the ValidatorLogValidationResult interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

#### Defined in

src/models/ValidatorLogValidationResult.ts:66

___

### instanceOfValidatorReference

▸ **instanceOfValidatorReference**(`value`): `boolean`

Check if a given object implements the ValidatorReference interface.

#### Parameters

| Name | Type |
| :------ | :------ |
| `value` | `object` |

#### Returns

`boolean`

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

src/runtime.ts:435

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
