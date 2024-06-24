[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Outputs

# Interface: Outputs

**`Export`**

Outputs

## Table of contents

### Properties

- [error](Outputs.md#error)
- [guardedOutput](Outputs.md#guardedoutput)
- [llmResponseInfo](Outputs.md#llmresponseinfo)
- [parsedOutput](Outputs.md#parsedoutput)
- [rawOutput](Outputs.md#rawoutput)
- [reasks](Outputs.md#reasks)
- [validationResponse](Outputs.md#validationresponse)
- [validatorLogs](Outputs.md#validatorlogs)

## Properties

### error

• `Optional` **error**: `string`

The error message from any exception which interrupted the Guard execution process.

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:83

___

### guardedOutput

• `Optional` **guardedOutput**: `string` \| `Record`\<`string`, `any`\>

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:65

___

### llmResponseInfo

• `Optional` **llmResponseInfo**: [`LLMResponse`](LLMResponse.md)

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:41

___

### parsedOutput

• `Optional` **parsedOutput**: `string` \| `Record`\<`string`, `any`\>

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:53

___

### rawOutput

• `Optional` **rawOutput**: `string`

The string content from the LLM response.

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:47

___

### reasks

• `Optional` **reasks**: [`Reask`](Reask.md)[]

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:71

___

### validationResponse

• `Optional` **validationResponse**: `string` \| [`Reask`](Reask.md) \| `Record`\<`string`, `any`\>

@@type {string | Reask | Record<string, any>}

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:59

___

### validatorLogs

• `Optional` **validatorLogs**: [`ValidatorLog`](ValidatorLog.md)[]

**`Memberof`**

Outputs

#### Defined in

src/models/Outputs.ts:77
