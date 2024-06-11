[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ServiceHealthApi

# Class: ServiceHealthApi

## Hierarchy

- [`BaseAPI`](BaseAPI.md)

  ↳ **`ServiceHealthApi`**

## Implements

- [`ServiceHealthApiInterface`](../interfaces/ServiceHealthApiInterface.md)

## Table of contents

### Constructors

- [constructor](ServiceHealthApi.md#constructor)

### Properties

- [configuration](ServiceHealthApi.md#configuration)

### Methods

- [healthCheckGet](ServiceHealthApi.md#healthcheckget)
- [healthCheckGetRaw](ServiceHealthApi.md#healthcheckgetraw)
- [isJsonMime](ServiceHealthApi.md#isjsonmime)
- [request](ServiceHealthApi.md#request)
- [withMiddleware](ServiceHealthApi.md#withmiddleware)
- [withPostMiddleware](ServiceHealthApi.md#withpostmiddleware)
- [withPreMiddleware](ServiceHealthApi.md#withpremiddleware)

## Constructors

### constructor

• **new ServiceHealthApi**(`configuration?`): [`ServiceHealthApi`](ServiceHealthApi.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `configuration` | [`Configuration`](Configuration.md) | `DefaultConfig` |

#### Returns

[`ServiceHealthApi`](ServiceHealthApi.md)

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

### healthCheckGet

▸ **healthCheckGet**(`initOverrides?`): `Promise`\<[`HealthCheck`](../interfaces/HealthCheck.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`HealthCheck`](../interfaces/HealthCheck.md)\>

#### Implementation of

[ServiceHealthApiInterface](../interfaces/ServiceHealthApiInterface.md).[healthCheckGet](../interfaces/ServiceHealthApiInterface.md#healthcheckget)

#### Defined in

src/apis/ServiceHealthApi.ts:89

___

### healthCheckGetRaw

▸ **healthCheckGetRaw**(`initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`HealthCheck`](../interfaces/HealthCheck.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`HealthCheck`](../interfaces/HealthCheck.md)\>\>

#### Implementation of

[ServiceHealthApiInterface](../interfaces/ServiceHealthApiInterface.md).[healthCheckGetRaw](../interfaces/ServiceHealthApiInterface.md#healthcheckgetraw)

#### Defined in

src/apis/ServiceHealthApi.ts:52

___

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
