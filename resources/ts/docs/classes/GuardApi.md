[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / GuardApi

# Class: GuardApi

## Hierarchy

- [`BaseAPI`](BaseAPI.md)

  ↳ **`GuardApi`**

## Implements

- [`GuardApiInterface`](../interfaces/GuardApiInterface.md)

## Table of contents

### Constructors

- [constructor](GuardApi.md#constructor)

### Properties

- [configuration](GuardApi.md#configuration)

### Methods

- [createGuard](GuardApi.md#createguard)
- [createGuardRaw](GuardApi.md#createguardraw)
- [deleteGuard](GuardApi.md#deleteguard)
- [deleteGuardRaw](GuardApi.md#deleteguardraw)
- [getGuard](GuardApi.md#getguard)
- [getGuardHistory](GuardApi.md#getguardhistory)
- [getGuardHistoryRaw](GuardApi.md#getguardhistoryraw)
- [getGuardRaw](GuardApi.md#getguardraw)
- [getGuards](GuardApi.md#getguards)
- [getGuardsRaw](GuardApi.md#getguardsraw)
- [isJsonMime](GuardApi.md#isjsonmime)
- [request](GuardApi.md#request)
- [updateGuard](GuardApi.md#updateguard)
- [updateGuardRaw](GuardApi.md#updateguardraw)
- [withMiddleware](GuardApi.md#withmiddleware)
- [withPostMiddleware](GuardApi.md#withpostmiddleware)
- [withPreMiddleware](GuardApi.md#withpremiddleware)

## Constructors

### constructor

• **new GuardApi**(`configuration?`): [`GuardApi`](GuardApi.md)

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `configuration` | [`Configuration`](Configuration.md) | `DefaultConfig` |

#### Returns

[`GuardApi`](GuardApi.md)

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

### createGuard

▸ **createGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](../interfaces/Guard.md)\>

Creates a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`CreateGuardRequest`](../interfaces/CreateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](../interfaces/Guard.md)\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[createGuard](../interfaces/GuardApiInterface.md#createguard)

#### Defined in

src/apis/GuardApi.ts:232

___

### createGuardRaw

▸ **createGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

Creates a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`CreateGuardRequest`](../interfaces/CreateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[createGuardRaw](../interfaces/GuardApiInterface.md#createguardraw)

#### Defined in

src/apis/GuardApi.ts:183

___

### deleteGuard

▸ **deleteGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](../interfaces/Guard.md)\>

Deletes a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`DeleteGuardRequest`](../interfaces/DeleteGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](../interfaces/Guard.md)\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[deleteGuard](../interfaces/GuardApiInterface.md#deleteguard)

#### Defined in

src/apis/GuardApi.ts:295

___

### deleteGuardRaw

▸ **deleteGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

Deletes a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`DeleteGuardRequest`](../interfaces/DeleteGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[deleteGuardRaw](../interfaces/GuardApiInterface.md#deleteguardraw)

#### Defined in

src/apis/GuardApi.ts:246

___

### getGuard

▸ **getGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](../interfaces/Guard.md)\>

Fetches a specific Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardRequest`](../interfaces/GetGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](../interfaces/Guard.md)\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[getGuard](../interfaces/GuardApiInterface.md#getguard)

#### Defined in

src/apis/GuardApi.ts:364

___

### getGuardHistory

▸ **getGuardHistory**(`requestParameters`, `initOverrides?`): `Promise`\<[`Call`](../interfaces/Call.md)[]\>

Fetches the history for a specific Guard execution by using the id for the most recent Call

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardHistoryRequest`](../interfaces/GetGuardHistoryRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Call`](../interfaces/Call.md)[]\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[getGuardHistory](../interfaces/GuardApiInterface.md#getguardhistory)

#### Defined in

src/apis/GuardApi.ts:436

___

### getGuardHistoryRaw

▸ **getGuardHistoryRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Call`](../interfaces/Call.md)[]\>\>

Fetches the history for a specific Guard execution by using the id for the most recent Call

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardHistoryRequest`](../interfaces/GetGuardHistoryRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Call`](../interfaces/Call.md)[]\>\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[getGuardHistoryRaw](../interfaces/GuardApiInterface.md#getguardhistoryraw)

#### Defined in

src/apis/GuardApi.ts:375

___

### getGuardRaw

▸ **getGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

Fetches a specific Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardRequest`](../interfaces/GetGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[getGuardRaw](../interfaces/GuardApiInterface.md#getguardraw)

#### Defined in

src/apis/GuardApi.ts:309

___

### getGuards

▸ **getGuards**(`initOverrides?`): `Promise`\<[`Guard`](../interfaces/Guard.md)[]\>

Fetches the configuration for all Guards the user has access to.

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](../interfaces/Guard.md)[]\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[getGuards](../interfaces/GuardApiInterface.md#getguards)

#### Defined in

src/apis/GuardApi.ts:488

___

### getGuardsRaw

▸ **getGuardsRaw**(`initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)[]\>\>

Fetches the configuration for all Guards the user has access to.

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)[]\>\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[getGuardsRaw](../interfaces/GuardApiInterface.md#getguardsraw)

#### Defined in

src/apis/GuardApi.ts:450

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

### updateGuard

▸ **updateGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](../interfaces/Guard.md)\>

Updates a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`UpdateGuardRequest`](../interfaces/UpdateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](../interfaces/Guard.md)\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[updateGuard](../interfaces/GuardApiInterface.md#updateguard)

#### Defined in

src/apis/GuardApi.ts:557

___

### updateGuardRaw

▸ **updateGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

Updates a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`UpdateGuardRequest`](../interfaces/UpdateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](../interfaces/ApiResponse.md)\<[`Guard`](../interfaces/Guard.md)\>\>

#### Implementation of

[GuardApiInterface](../interfaces/GuardApiInterface.md).[updateGuardRaw](../interfaces/GuardApiInterface.md#updateguardraw)

#### Defined in

src/apis/GuardApi.ts:498

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
