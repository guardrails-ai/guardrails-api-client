[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / CallInputs

# Interface: CallInputs

**`Export`**

CallInputs

## Table of contents

### Properties

- [args](CallInputs.md#args)
- [fullSchemaReask](CallInputs.md#fullschemareask)
- [instructions](CallInputs.md#instructions)
- [kwargs](CallInputs.md#kwargs)
- [llmApi](CallInputs.md#llmapi)
- [llmOutput](CallInputs.md#llmoutput)
- [metadata](CallInputs.md#metadata)
- [msgHistory](CallInputs.md#msghistory)
- [numReasks](CallInputs.md#numreasks)
- [prompt](CallInputs.md#prompt)
- [promptParams](CallInputs.md#promptparams)

## Properties

### args

• `Optional` **args**: `any`[]

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:80

___

### fullSchemaReask

• `Optional` **fullSchemaReask**: `boolean`

Whether to perform reasks for the entire schema rather than for individual fields.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:74

___

### instructions

• `Optional` **instructions**: `string`

The instructions for chat models.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:38

___

### kwargs

• `Optional` **kwargs**: `Object`

**`Memberof`**

CallInputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/CallInputs.ts:86

___

### llmApi

• `Optional` **llmApi**: `string`

The LLM resource targeted by the user. e.g. openai.chat.completions.create

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:26

___

### llmOutput

• `Optional` **llmOutput**: `string`

The string output from an external LLM call provided by the user via Guard.parse.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:32

___

### metadata

• `Optional` **metadata**: `Object`

Additional data to be used by Validators during execution time.

**`Memberof`**

CallInputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/CallInputs.ts:68

___

### msgHistory

• `Optional` **msgHistory**: \{ `[key: string]`: `any`;  }[]

The message history for chat models.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:50

___

### numReasks

• `Optional` **numReasks**: `number`

The total number of times the LLM can be called to correct output excluding the initial call.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:62

___

### prompt

• `Optional` **prompt**: `string`

The prompt for the LLM.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:44

___

### promptParams

• `Optional` **promptParams**: `Object`

Parameters to be formatted into the prompt.

**`Memberof`**

CallInputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/CallInputs.ts:56
