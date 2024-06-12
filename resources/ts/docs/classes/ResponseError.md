[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ResponseError

# Class: ResponseError

## Hierarchy

- `Error`

  ↳ **`ResponseError`**

## Table of contents

### Constructors

- [constructor](ResponseError.md#constructor)

### Properties

- [cause](ResponseError.md#cause)
- [message](ResponseError.md#message)
- [name](ResponseError.md#name)
- [response](ResponseError.md#response)
- [stack](ResponseError.md#stack)
- [prepareStackTrace](ResponseError.md#preparestacktrace)
- [stackTraceLimit](ResponseError.md#stacktracelimit)

### Methods

- [captureStackTrace](ResponseError.md#capturestacktrace)

## Constructors

### constructor

• **new ResponseError**(`response`, `msg?`): [`ResponseError`](ResponseError.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `response` | `Response` |
| `msg?` | `string` |

#### Returns

[`ResponseError`](ResponseError.md)

#### Overrides

Error.constructor

#### Defined in

src/runtime.ts:307

## Properties

### cause

• `Optional` **cause**: `unknown`

#### Inherited from

Error.cause

#### Defined in

node_modules/typescript/lib/lib.es2022.error.d.ts:24

___

### message

• **message**: `string`

#### Inherited from

Error.message

#### Defined in

node_modules/typescript/lib/lib.es5.d.ts:1077

___

### name

• **name**: ``"ResponseError"``

#### Overrides

Error.name

#### Defined in

src/runtime.ts:306

___

### response

• **response**: `Response`

#### Defined in

src/runtime.ts:308

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
