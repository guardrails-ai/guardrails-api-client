[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / HttpError

# Interface: HttpError

**`Export`**

HttpError

## Table of contents

### Properties

- [cause](HttpError.md#cause)
- [context](HttpError.md#context)
- [fields](HttpError.md#fields)
- [message](HttpError.md#message)
- [status](HttpError.md#status)

## Properties

### cause

• `Optional` **cause**: `string`

Used to describe the origin of an error if that original error has meaning to the client.  This field should add specificity to 'message'.

**`Memberof`**

HttpError

#### Defined in

src/models/HttpError.ts:38

___

### context

• `Optional` **context**: `string`

Used to identify what part of the request caused the error for non-JSON payloads.

**`Memberof`**

HttpError

#### Defined in

src/models/HttpError.ts:50

___

### fields

• `Optional` **fields**: `Object`

Used to identify specific fields in a JSON body that caused the error.  Typically only used for 4xx type responses.  The key should be the json path to the invalid property and the value should be a list of error messages specific to that property.

**`Memberof`**

HttpError

#### Index signature

▪ [key: `string`]: `string`[]

#### Defined in

src/models/HttpError.ts:44

___

### message

• **message**: `string`

A message explaining the status

**`Memberof`**

HttpError

#### Defined in

src/models/HttpError.ts:32

___

### status

• **status**: `number`

A valid http status code

**`Memberof`**

HttpError

#### Defined in

src/models/HttpError.ts:26
