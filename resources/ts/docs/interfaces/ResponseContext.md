[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ResponseContext

# Interface: ResponseContext

## Table of contents

### Properties

- [fetch](ResponseContext.md#fetch)
- [init](ResponseContext.md#init)
- [response](ResponseContext.md#response)
- [url](ResponseContext.md#url)

## Properties

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

src/runtime.ts:462

___

### init

• **init**: `RequestInit`

#### Defined in

src/runtime.ts:464

___

### response

• **response**: `Response`

#### Defined in

src/runtime.ts:465

___

### url

• **url**: `string`

#### Defined in

src/runtime.ts:463
