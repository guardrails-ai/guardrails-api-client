[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / JSONApiResponse

# Class: JSONApiResponse\<T\>

## Type parameters

| Name |
| :------ |
| `T` |

## Table of contents

### Constructors

- [constructor](JSONApiResponse.md#constructor)

### Properties

- [raw](JSONApiResponse.md#raw)
- [transformer](JSONApiResponse.md#transformer)

### Methods

- [value](JSONApiResponse.md#value)

## Constructors

### constructor

• **new JSONApiResponse**\<`T`\>(`raw`, `transformer?`): [`JSONApiResponse`](JSONApiResponse.md)\<`T`\>

#### Type parameters

| Name |
| :------ |
| `T` |

#### Parameters

| Name | Type |
| :------ | :------ |
| `raw` | `Response` |
| `transformer` | [`ResponseTransformer`](../interfaces/ResponseTransformer.md)\<`T`\> |

#### Returns

[`JSONApiResponse`](JSONApiResponse.md)\<`T`\>

#### Defined in

src/runtime.ts:492

## Properties

### raw

• **raw**: `Response`

#### Defined in

src/runtime.ts:493

___

### transformer

• `Private` **transformer**: [`ResponseTransformer`](../interfaces/ResponseTransformer.md)\<`T`\>

#### Defined in

src/runtime.ts:494

## Methods

### value

▸ **value**(): `Promise`\<`T`\>

#### Returns

`Promise`\<`T`\>

#### Defined in

src/runtime.ts:497
