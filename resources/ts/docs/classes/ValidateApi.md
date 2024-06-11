[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ValidateApi

# Class: ValidateApi

## Hierarchy

- [`BaseAPI`](BaseAPI.md)

  ↳ **`ValidateApi`**

## Implements

- [`ValidateApiInterface`](../interfaces/ValidateApiInterface.md)

## Table of contents

### Constructors

- [constructor](ValidateApi.md#constructor)

### Properties

- [configuration](ValidateApi.md#configuration)

### Methods

- [isJsonMime](ValidateApi.md#isjsonmime)
- [request](ValidateApi.md#request)
- [validate](ValidateApi.md#validate)
- [validateRaw](ValidateApi.md#validateraw)
- [withMiddleware](ValidateApi.md#withmiddleware)
- [withPostMiddleware](ValidateApi.md#withpostmiddleware)
- [withPreMiddleware](ValidateApi.md#withpremiddleware)

## Constructors

### constructor

• **new ValidateApi**(`configuration?`): [`ValidateApi`](ValidateApi.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `configuration` | [`Configuration`](Configuration.md) | `DefaultConfig` |

#### Returns

[`ValidateApi`](ValidateApi.md)

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

### validate

▸ **validate**(`requestParameters`, `initOverrides?`): `Promise`\<[`ValidationOutcome`](../interfaces/ValidationOutcome.md)\>

Runs the validations specified in a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`ValidateRequest`](../interfaces/ValidateRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ValidationOutcome`](../interfaces/ValidationOutcome.md)\>

#### Implementation of

[ValidateApiInterface](../interfaces/ValidateApiInterface.md).[validate](../interfaces/ValidateApiInterface.md#validate)

#### Defined in

src/apis/ValidateApi.ts:134

___

### validateRaw

▸ **validateRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`ValidationOutcome`](../interfaces/ValidationOutcome.md)\>\>

Runs the validations specified in a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`ValidateRequest`](../interfaces/ValidateRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`ValidationOutcome`](../interfaces/ValidationOutcome.md)\>\>

#### Implementation of

[ValidateApiInterface](../interfaces/ValidateApiInterface.md).[validateRaw](../interfaces/ValidateApiInterface.md#validateraw)

#### Defined in

src/apis/ValidateApi.ts:69

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
