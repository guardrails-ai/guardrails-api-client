[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / CallInputs

# Interface: CallInputs

**`Export`**

CallInputs

## Table of contents

### Properties

- [args](CallInputs.md#args)
- [fullSchemaReask](CallInputs.md#fullschemareask)
- [kwargs](CallInputs.md#kwargs)
- [llmApi](CallInputs.md#llmapi)
- [llmOutput](CallInputs.md#llmoutput)
- [messages](CallInputs.md#messages)
- [metadata](CallInputs.md#metadata)
- [numReasks](CallInputs.md#numreasks)
- [promptParams](CallInputs.md#promptparams)
- [stream](CallInputs.md#stream)

## Properties

### args

• `Optional` **args**: `any`[]

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:74

___

### fullSchemaReask

• `Optional` **fullSchemaReask**: `boolean`

Whether to perform reasks for the entire schema rather than for individual fields.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:62

___

### kwargs

• `Optional` **kwargs**: `Object`

**`Memberof`**

CallInputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/CallInputs.ts:80

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

### messages

• `Optional` **messages**: \{ `[key: string]`: `any`;  }[]

The messages for chat models.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:38

___

### metadata

• `Optional` **metadata**: `Object`

Additional data to be used by Validators during execution time.

**`Memberof`**

CallInputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/CallInputs.ts:56

___

### numReasks

• `Optional` **numReasks**: `number`

The total number of times the LLM can be called to correct output excluding the initial call.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:50

___

### promptParams

• `Optional` **promptParams**: `Object`

Parameters to be formatted into the messages.

**`Memberof`**

CallInputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/CallInputs.ts:44

___

### stream

• `Optional` **stream**: `boolean`

Whether to use streaming.

**`Memberof`**

CallInputs

#### Defined in

src/models/CallInputs.ts:68
