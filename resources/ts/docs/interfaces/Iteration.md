[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Iteration

# Interface: Iteration

**`Export`**

Iteration

## Table of contents

### Properties

- [callId](Iteration.md#callid)
- [id](Iteration.md#id)
- [index](Iteration.md#index)
- [inputs](Iteration.md#inputs)
- [outputs](Iteration.md#outputs)

## Properties

### callId

• **callId**: `string`

The unique identifier for the Call that this iteration is a part of.

**`Memberof`**

Iteration

#### Defined in

src/models/Iteration.ts:43

___

### id

• **id**: `string`

The unique identifier for this Call.  Can be used as an identifier for a specific execution of a Guard.

**`Memberof`**

Iteration

#### Defined in

src/models/Iteration.ts:31

___

### index

• **index**: `number`

The zero-based index of this iteration within the current Call.

**`Memberof`**

Iteration

#### Defined in

src/models/Iteration.ts:37

___

### inputs

• `Optional` **inputs**: [`Inputs`](Inputs.md)

**`Memberof`**

Iteration

#### Defined in

src/models/Iteration.ts:49

___

### outputs

• `Optional` **outputs**: [`Outputs`](Outputs.md)

**`Memberof`**

Iteration

#### Defined in

src/models/Iteration.ts:55
