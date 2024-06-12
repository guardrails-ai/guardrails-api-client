[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Inputs

# Interface: Inputs

**`Export`**

Inputs

## Table of contents

### Properties

- [fullSchemaReask](Inputs.md#fullschemareask)
- [instructions](Inputs.md#instructions)
- [llmApi](Inputs.md#llmapi)
- [llmOutput](Inputs.md#llmoutput)
- [metadata](Inputs.md#metadata)
- [msgHistory](Inputs.md#msghistory)
- [numReasks](Inputs.md#numreasks)
- [prompt](Inputs.md#prompt)
- [promptParams](Inputs.md#promptparams)

## Properties

### fullSchemaReask

• `Optional` **fullSchemaReask**: `boolean`

Whether to perform reasks for the entire schema rather than for individual fields.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:74

___

### instructions

• `Optional` **instructions**: `string`

The instructions for chat models.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:38

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

### metadata

• `Optional` **metadata**: `Object`

Additional data to be used by Validators during execution time.

**`Memberof`**

Inputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/Inputs.ts:68

___

### msgHistory

• `Optional` **msgHistory**: \{ `[key: string]`: `any`;  }[]

The message history for chat models.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:50

___

### numReasks

• `Optional` **numReasks**: `number`

The total number of times the LLM can be called to correct output excluding the initial call.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:62

___

### prompt

• `Optional` **prompt**: `string`

The prompt for the LLM.

**`Memberof`**

Inputs

#### Defined in

src/models/Inputs.ts:44

___

### promptParams

• `Optional` **promptParams**: `Object`

Parameters to be formatted into the prompt.

**`Memberof`**

Inputs

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/Inputs.ts:56
