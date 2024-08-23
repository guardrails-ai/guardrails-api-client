[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / OpenaiApi

# Class: OpenaiApi

## Hierarchy

- [`BaseAPI`](BaseAPI.md)

  ↳ **`OpenaiApi`**

## Implements

- [`OpenaiApiInterface`](../interfaces/OpenaiApiInterface.md)

## Table of contents

### Constructors

- [constructor](OpenaiApi.md#constructor)

### Properties

- [configuration](OpenaiApi.md#configuration)

### Methods

- [isJsonMime](OpenaiApi.md#isjsonmime)
- [openaiChatCompletion](OpenaiApi.md#openaichatcompletion)
- [openaiChatCompletionRaw](OpenaiApi.md#openaichatcompletionraw)
- [request](OpenaiApi.md#request)
- [withMiddleware](OpenaiApi.md#withmiddleware)
- [withPostMiddleware](OpenaiApi.md#withpostmiddleware)
- [withPreMiddleware](OpenaiApi.md#withpremiddleware)

## Constructors

### constructor

• **new OpenaiApi**(`configuration?`): [`OpenaiApi`](OpenaiApi.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `configuration` | [`Configuration`](Configuration.md) | `DefaultConfig` |

#### Returns

[`OpenaiApi`](OpenaiApi.md)

#### Inherited from

[BaseAPI](BaseAPI.md).[constructor](BaseAPI.md#constructor)

#### Defined in

src/runtime.ts:110

## Properties

### configuration

• `Protected` **configuration**: [`Configuration`](Configuration.md) = `DefaultConfig`

#### Inherited from

[BaseAPI](BaseAPI.md).[configuration](BaseAPI.md#configuration)

#### Defined in

src/runtime.ts:110

## Methods

### isJsonMime

▸ **isJsonMime**(`mime`): `boolean`

Check if the given MIME is a JSON MIME.
JSON MIME examples:
  application/json
  application/json; charset=UTF8
  APPLICATION/JSON
  application/vnd.company+json

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `mime` | `undefined` \| ``null`` \| `string` | MIME (Multipurpose Internet Mail Extensions) |

#### Returns

`boolean`

True if the given MIME is JSON, false otherwise.

#### Inherited from

[BaseAPI](BaseAPI.md).[isJsonMime](BaseAPI.md#isjsonmime)

#### Defined in

src/runtime.ts:146

___

### openaiChatCompletion

▸ **openaiChatCompletion**(`requestParameters`, `initOverrides?`): `Promise`\<[`OpenAIChatCompletion`](../interfaces/OpenAIChatCompletion.md)\>

OpenAI SDK compatible endpoint for Chat Completions

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`OpenaiChatCompletionRequest`](../interfaces/OpenaiChatCompletionRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`OpenAIChatCompletion`](../interfaces/OpenAIChatCompletion.md)\>

#### Implementation of

[OpenaiApiInterface](../interfaces/OpenaiApiInterface.md).[openaiChatCompletion](../interfaces/OpenaiApiInterface.md#openaichatcompletion)

#### Defined in

src/apis/OpenaiApi.ts:128

___

### openaiChatCompletionRaw

▸ **openaiChatCompletionRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`OpenAIChatCompletion`](../interfaces/OpenAIChatCompletion.md)\>\>

OpenAI SDK compatible endpoint for Chat Completions

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`OpenaiChatCompletionRequest`](../interfaces/OpenaiChatCompletionRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`OpenAIChatCompletion`](../interfaces/OpenAIChatCompletion.md)\>\>

#### Implementation of

[OpenaiApiInterface](../interfaces/OpenaiApiInterface.md).[openaiChatCompletionRaw](../interfaces/OpenaiApiInterface.md#openaichatcompletionraw)

#### Defined in

src/apis/OpenaiApi.ts:67

___

### request

▸ **request**(`context`, `initOverrides?`): `Promise`\<`Response`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `context` | [`RequestOpts`](../interfaces/RequestOpts.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<`Response`\>

#### Inherited from

[BaseAPI](BaseAPI.md).[request](BaseAPI.md#request)

#### Defined in

src/runtime.ts:153

___

### withMiddleware

▸ **withMiddleware**\<`T`\>(`this`, `...middlewares`): `T`

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | extends [`BaseAPI`](BaseAPI.md) |

#### Parameters

| Name | Type |
| :------ | :------ |
| `this` | `T` |
| `...middlewares` | [`Middleware`](../interfaces/Middleware.md)[] |

#### Returns

`T`

#### Inherited from

[BaseAPI](BaseAPI.md).[withMiddleware](BaseAPI.md#withmiddleware)

#### Defined in

src/runtime.ts:114

___

### withPostMiddleware

▸ **withPostMiddleware**\<`T`\>(`this`, `...postMiddlewares`): `T`

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | extends [`BaseAPI`](BaseAPI.md) |

#### Parameters

| Name | Type |
| :------ | :------ |
| `this` | `T` |
| `...postMiddlewares` | (`undefined` \| (`context`: [`ResponseContext`](../interfaces/ResponseContext.md)) => `Promise`\<`void` \| `Response`\>)[] |

#### Returns

`T`

#### Inherited from

[BaseAPI](BaseAPI.md).[withPostMiddleware](BaseAPI.md#withpostmiddleware)

#### Defined in

src/runtime.ts:128

___

### withPreMiddleware

▸ **withPreMiddleware**\<`T`\>(`this`, `...preMiddlewares`): `T`

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | extends [`BaseAPI`](BaseAPI.md) |

#### Parameters

| Name | Type |
| :------ | :------ |
| `this` | `T` |
| `...preMiddlewares` | (`undefined` \| (`context`: [`RequestContext`](../interfaces/RequestContext.md)) => `Promise`\<`void` \| [`FetchParams`](../interfaces/FetchParams.md)\>)[] |

#### Returns

`T`

#### Inherited from

[BaseAPI](BaseAPI.md).[withPreMiddleware](BaseAPI.md#withpremiddleware)

#### Defined in

src/runtime.ts:120
