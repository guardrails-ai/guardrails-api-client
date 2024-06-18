[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / GuardApiInterface

# Interface: GuardApiInterface

GuardApi - interface

**`Export`**

GuardApiInterface

## Implemented by

- [`GuardApi`](../classes/GuardApi.md)

## Table of contents

### Methods

- [createGuard](GuardApiInterface.md#createguard)
- [createGuardRaw](GuardApiInterface.md#createguardraw)
- [deleteGuard](GuardApiInterface.md#deleteguard)
- [deleteGuardRaw](GuardApiInterface.md#deleteguardraw)
- [getGuard](GuardApiInterface.md#getguard)
- [getGuardHistory](GuardApiInterface.md#getguardhistory)
- [getGuardHistoryRaw](GuardApiInterface.md#getguardhistoryraw)
- [getGuardRaw](GuardApiInterface.md#getguardraw)
- [getGuards](GuardApiInterface.md#getguards)
- [getGuardsRaw](GuardApiInterface.md#getguardsraw)
- [updateGuard](GuardApiInterface.md#updateguard)
- [updateGuardRaw](GuardApiInterface.md#updateguardraw)

## Methods

### createGuard

▸ **createGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](Guard.md)\>

Creates a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`CreateGuardRequest`](CreateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](Guard.md)\>

#### Defined in

src/apis/GuardApi.ts:65

___

### createGuardRaw

▸ **createGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`CreateGuardRequest`](CreateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

**`Summary`**

Creates a Guard

**`Throws`**

**`Memberof`**

GuardApiInterface

#### Defined in

src/apis/GuardApi.ts:57

___

### deleteGuard

▸ **deleteGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](Guard.md)\>

Deletes a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`DeleteGuardRequest`](DeleteGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](Guard.md)\>

#### Defined in

src/apis/GuardApi.ts:86

___

### deleteGuardRaw

▸ **deleteGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`DeleteGuardRequest`](DeleteGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

**`Summary`**

Deletes a Guard

**`Throws`**

**`Memberof`**

GuardApiInterface

#### Defined in

src/apis/GuardApi.ts:78

___

### getGuard

▸ **getGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](Guard.md)\>

Fetches a specific Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardRequest`](GetGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](Guard.md)\>

#### Defined in

src/apis/GuardApi.ts:108

___

### getGuardHistory

▸ **getGuardHistory**(`requestParameters`, `initOverrides?`): `Promise`\<[`Call`](Call.md)[]\>

Fetches the history for a specific Guard execution by using the id for the most recent Call

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardHistoryRequest`](GetGuardHistoryRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Call`](Call.md)[]\>

#### Defined in

src/apis/GuardApi.ts:130

___

### getGuardHistoryRaw

▸ **getGuardHistoryRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Call`](Call.md)[]\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardHistoryRequest`](GetGuardHistoryRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Call`](Call.md)[]\>\>

**`Summary`**

Fetches the history for a specific Guard execution by using the id for the most recent Call

**`Throws`**

**`Memberof`**

GuardApiInterface

#### Defined in

src/apis/GuardApi.ts:122

___

### getGuardRaw

▸ **getGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`GetGuardRequest`](GetGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

**`Summary`**

Fetches a specific Guard

**`Throws`**

**`Memberof`**

GuardApiInterface

#### Defined in

src/apis/GuardApi.ts:100

___

### getGuards

▸ **getGuards**(`initOverrides?`): `Promise`\<[`Guard`](Guard.md)[]\>

Fetches the configuration for all Guards the user has access to.

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](Guard.md)[]\>

#### Defined in

src/apis/GuardApi.ts:149

___

### getGuardsRaw

▸ **getGuardsRaw**(`initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)[]\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)[]\>\>

**`Summary`**

Fetches the configuration for all Guards the user has access to.

**`Throws`**

**`Memberof`**

GuardApiInterface

#### Defined in

src/apis/GuardApi.ts:142

___

### updateGuard

▸ **updateGuard**(`requestParameters`, `initOverrides?`): `Promise`\<[`Guard`](Guard.md)\>

Updates a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`UpdateGuardRequest`](UpdateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`Guard`](Guard.md)\>

#### Defined in

src/apis/GuardApi.ts:170

___

### updateGuardRaw

▸ **updateGuardRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`UpdateGuardRequest`](UpdateGuardRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`Guard`](Guard.md)\>\>

**`Summary`**

Updates a Guard

**`Throws`**

**`Memberof`**

GuardApiInterface

#### Defined in

src/apis/GuardApi.ts:162
