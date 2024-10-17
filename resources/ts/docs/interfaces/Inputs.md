[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Inputs

# Interface: Inputs

**`Export`**

Inputs

## Table of contents

### Properties

- [fullSchemaReask](Inputs.md#fullschemareask)
- [llmApi](Inputs.md#llmapi)
- [llmOutput](Inputs.md#llmoutput)
- [messages](Inputs.md#messages)
- [metadata](Inputs.md#metadata)
- [numReasks](Inputs.md#numreasks)
- [promptParams](Inputs.md#promptparams)
- [stream](Inputs.md#stream)

## Properties

### fullSchemaReask

• `Optional` **fullSchemaReask**: `boolean`

Whether to perform reasks for the entire schema rather than for individual fields.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:62

___

### llmApi

• `Optional` **llmApi**: `string`

The LLM resource targeted by the user. e.g. openai.chat.completions.create

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:26

___

### llmOutput

• `Optional` **llmOutput**: `string`

The string output from an external LLM call provided by the user via Guard.parse.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:32

___

### messages

• `Optional` **messages**: \{ `[key: string]`: `any`;  }[]

The messages for chat models.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:38

___

### metadata

• `Optional` **metadata**: `Object`

Additional data to be used by Validators during execution time.

**`Memberof`**

Inputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/Inputs.ts:56

___

### numReasks

• `Optional` **numReasks**: `number`

The total number of times the LLM can be called to correct output excluding the initial call.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:50

___

### promptParams

• `Optional` **promptParams**: `Object`

Parameters to be formatted into the messages.

**`Memberof`**

Inputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/Inputs.ts:44

___

### stream

• `Optional` **stream**: `boolean`

Whether to use streaming.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:68
