[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Middleware

# Interface: Middleware

## Table of contents

### Methods

- [onError](Middleware.md#onerror)
- [post](Middleware.md#post)
- [pre](Middleware.md#pre)

## Methods

### onError

▸ **onError**(`context`): `Promise`\<`void` \| `Response`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `context` | [`ErrorContext`](ErrorContext.md) |

#### Returns

`Promise`\<`void` \| `Response`\>

#### Defined in

src/runtime.ts:479

___

### post

▸ **post**(`context`): `Promise`\<`void` \| `Response`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `context` | [`ResponseContext`](ResponseContext.md) |

#### Returns

`Promise`\<`void` \| `Response`\>

#### Defined in

src/runtime.ts:478

___

### pre

▸ **pre**(`context`): `Promise`\<`void` \| [`FetchParams`](FetchParams.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `context` | [`RequestContext`](RequestContext.md) |

#### Returns

`Promise`\<`void` \| [`FetchParams`](FetchParams.md)\>

#### Defined in

src/runtime.ts:477
