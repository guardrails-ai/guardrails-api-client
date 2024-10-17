[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ValidatorReference

# Interface: ValidatorReference

**`Export`**

ValidatorReference

## Table of contents

### Properties

- [args](ValidatorReference.md#args)
- [id](ValidatorReference.md#id)
- [kwargs](ValidatorReference.md#kwargs)
- [on](ValidatorReference.md#on)
- [onFail](ValidatorReference.md#onfail)

## Properties

### args

• `Optional` **args**: `any`[]

**`Memberof`**

ValidatorReference

#### Defined in

src/models/ValidatorReference.ts:44

___

### id

• **id**: `any`

The unique identifier for this Validator.  Often the hub id; e.g. guardrails/regex_match

**`Memberof`**

ValidatorReference

#### Defined in

src/models/ValidatorReference.ts:26

___

### kwargs

• `Optional` **kwargs**: `Object`

**`Memberof`**

ValidatorReference

#### Index signature

▪ [key: `string`]: `any`

#### Defined in

src/models/ValidatorReference.ts:50

___

### on

• `Optional` **on**: `string`

A reference to the property this validator should be applied against.  Can be a valid JSON path or a meta-property such as "messages" or "output"

**`Memberof`**

ValidatorReference

#### Defined in

src/models/ValidatorReference.ts:32

___

### onFail

• `Optional` **onFail**: [`ValidatorReferenceOnFailEnum`](../modules.md#validatorreferenceonfailenum)

**`Memberof`**

ValidatorReference

#### Defined in

src/models/ValidatorReference.ts:38
