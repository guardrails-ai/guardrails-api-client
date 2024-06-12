[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ValidatePayload

# Interface: ValidatePayload

**`Export`**

ValidatePayload

## Indexable

▪ [key: `string`]: `any` \| `any`

## Table of contents

### Properties

- [llmApi](ValidatePayload.md#llmapi)
- [llmOutput](ValidatePayload.md#llmoutput)
- [numReasks](ValidatePayload.md#numreasks)
- [promptParams](ValidatePayload.md#promptparams)

## Properties

### llmApi

• `Optional` **llmApi**: [`LLMResource`](../modules.md#llmresource)

**`Memberof`**

ValidatePayload

#### Defined in

src/models/ValidatePayload.ts:48

___

### llmOutput

• `Optional` **llmOutput**: `any`

The LLM output as a string or the input prompts for the LLM

**`Memberof`**

ValidatePayload

#### Defined in

src/models/ValidatePayload.ts:30

___

### numReasks

• `Optional` **numReasks**: `any`

An override for the number of re-asks to perform

**`Memberof`**

ValidatePayload

#### Defined in

src/models/ValidatePayload.ts:36

___

### promptParams

• `Optional` **promptParams**: `Object`

additional params for llm prompts

**`Memberof`**

ValidatePayload

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/ValidatePayload.ts:42
