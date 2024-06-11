[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ErrorContext

# Interface: ErrorContext

## Table of contents

### Properties

- [error](ErrorContext.md#error)
- [fetch](ErrorContext.md#fetch)
- [init](ErrorContext.md#init)
- [response](ErrorContext.md#response)
- [url](ErrorContext.md#url)

## Properties

### error

• **error**: `unknown`

#### Defined in

src/runtime.ts:472

___

### fetch

• **fetch**: (`input`: `RequestInfo` \| `URL`, `init?`: `RequestInit`) => `Promise`\<`Response`\>

#### Type declaration

▸ (`input`, `init?`): `Promise`\<`Response`\>

[MDN Reference](https://developer.mozilla.org/docs/Web/API/fetch)

##### Parameters

| Name | Type |
| :------ | :------ |
| `input` | `RequestInfo` \| `URL` |
| `init?` | `RequestInit` |

##### Returns

`Promise`\<`Response`\>

#### Defined in

src/runtime.ts:469

___

### init

• **init**: `RequestInit`

#### Defined in

src/runtime.ts:471

___

### response

• `Optional` **response**: `Response`

#### Defined in

src/runtime.ts:473

___

### url

• **url**: `string`

#### Defined in

src/runtime.ts:470
