[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / FetchError

# Class: FetchError

## Hierarchy

- `Error`

  ↳ **`FetchError`**

## Table of contents

### Constructors

- [constructor](FetchError.md#constructor)

### Properties

- [cause](FetchError.md#cause)
- [message](FetchError.md#message)
- [name](FetchError.md#name)
- [stack](FetchError.md#stack)
- [prepareStackTrace](FetchError.md#preparestacktrace)
- [stackTraceLimit](FetchError.md#stacktracelimit)

### Methods

- [captureStackTrace](FetchError.md#capturestacktrace)

## Constructors

### constructor

• **new FetchError**(`cause`, `msg?`): [`FetchError`](FetchError.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `cause` | `Error` |
| `msg?` | `string` |

#### Returns

[`FetchError`](FetchError.md)

#### Overrides

Error.constructor

#### Defined in

src/runtime.ts:317

## Properties

### cause

• **cause**: `Error`

#### Inherited from

Error.cause

#### Defined in

src/runtime.ts:318

___

### message

• **message**: `string`

#### Inherited from

Error.message

#### Defined in

node_modules/typescript/lib/lib.es5.d.ts:1077

___

### name

• **name**: ``"FetchError"``

#### Overrides

Error.name

#### Defined in

src/runtime.ts:316

___

### stack

• `Optional` **stack**: `string`

#### Inherited from

Error.stack

#### Defined in

node_modules/typescript/lib/lib.es5.d.ts:1078

___

### prepareStackTrace

▪ `Static` `Optional` **prepareStackTrace**: (`err`: `Error`, `stackTraces`: `CallSite`[]) => `any`

Optional override for formatting stack traces

**`See`**

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Type declaration

▸ (`err`, `stackTraces`): `any`

##### Parameters

| Name | Type |
| :------ | :------ |
| `err` | `Error` |
| `stackTraces` | `CallSite`[] |

##### Returns

`any`

#### Inherited from

Error.prepareStackTrace

#### Defined in

node_modules/@types/node/globals.d.ts:28

___

### stackTraceLimit

▪ `Static` **stackTraceLimit**: `number`

#### Inherited from

Error.stackTraceLimit

#### Defined in

node_modules/@types/node/globals.d.ts:30

## Methods

### captureStackTrace

▸ **captureStackTrace**(`targetObject`, `constructorOpt?`): `void`

Create .stack property on a target object

#### Parameters

| Name | Type |
| :------ | :------ |
| `targetObject` | `object` |
| `constructorOpt?` | `Function` |

#### Returns

`void`

#### Inherited from

Error.captureStackTrace

#### Defined in

node_modules/@types/node/globals.d.ts:21
