[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ServiceHealthApiInterface

# Interface: ServiceHealthApiInterface

ServiceHealthApi - interface

**`Export`**

ServiceHealthApiInterface

## Implemented by

- [`ServiceHealthApi`](../classes/ServiceHealthApi.md)

## Table of contents

### Methods

- [healthCheckGet](ServiceHealthApiInterface.md#healthcheckget)
- [healthCheckGetRaw](ServiceHealthApiInterface.md#healthcheckgetraw)

## Methods

### healthCheckGet

▸ **healthCheckGet**(`initOverrides?`): `Promise`\<[`HealthCheck`](HealthCheck.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`HealthCheck`](HealthCheck.md)\>

#### Defined in

src/apis/ServiceHealthApi.ts:38

___

### healthCheckGetRaw

▸ **healthCheckGetRaw**(`initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`HealthCheck`](HealthCheck.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`HealthCheck`](HealthCheck.md)\>\>

**`Throws`**

**`Memberof`**

ServiceHealthApiInterface

#### Defined in

src/apis/ServiceHealthApi.ts:32
