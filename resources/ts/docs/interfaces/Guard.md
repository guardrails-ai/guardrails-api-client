[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Guard

# Interface: Guard

**`Export`**

Guard

## Table of contents

### Properties

- [description](Guard.md#description)
- [history](Guard.md#history)
- [id](Guard.md#id)
- [name](Guard.md#name)
- [outputSchema](Guard.md#outputschema)
- [validators](Guard.md#validators)

## Properties

### description

• `Optional` **description**: `string`

A description that concisely states the expected behaviour or purpose of the Guard.

**`Memberof`**

Guard

#### Defined in

src/models/Guard.ts:49

___

### history

• `Optional` **history**: [`GuardHistory`](GuardHistory.md) \| [`Call`](Call.md)[]

**`Memberof`**

Guard

#### Defined in

src/models/Guard.ts:67

___

### id

• **id**: `string`

The unique identifier for the Guard.

**`Memberof`**

Guard

#### Defined in

src/models/Guard.ts:37

___

### name

• **name**: `string`

The name for the Guard.

**`Memberof`**

Guard

#### Defined in

src/models/Guard.ts:43

___

### outputSchema

• `Optional` **outputSchema**: [`Schema`](Schema.md)

**`Memberof`**

Guard

#### Defined in

src/models/Guard.ts:61

___

### validators

• `Optional` **validators**: [`ValidatorReference`](ValidatorReference.md)[]

**`Memberof`**

Guard

#### Defined in

src/models/Guard.ts:55
