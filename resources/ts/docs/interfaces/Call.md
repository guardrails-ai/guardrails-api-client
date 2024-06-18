[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Call

# Interface: Call

**`Export`**

Call

## Table of contents

### Properties

- [exception](Call.md#exception)
- [id](Call.md#id)
- [inputs](Call.md#inputs)
- [iterations](Call.md#iterations)

## Properties

### exception

• `Optional` **exception**: `string` \| [`CallException`](CallException.md)

**`Memberof`**

Call

#### Defined in

src/models/Call.ts:51

___

### id

• **id**: `string`

The unique identifier for this Call.  Can be used as an identifier for a specific execution of a Guard.

**`Memberof`**

Call

#### Defined in

src/models/Call.ts:33

___

### inputs

• `Optional` **inputs**: [`CallInputs`](CallInputs.md)

**`Memberof`**

Call

#### Defined in

src/models/Call.ts:45

___

### iterations

• `Optional` **iterations**: [`Iteration`](Iteration.md)[]

**`Memberof`**

Call

#### Defined in

src/models/Call.ts:39
