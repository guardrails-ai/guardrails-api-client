[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ValidateApiInterface

# Interface: ValidateApiInterface

ValidateApi - interface

**`Export`**

ValidateApiInterface

## Implemented by

- [`ValidateApi`](../classes/ValidateApi.md)

## Table of contents

### Methods

- [validate](ValidateApiInterface.md#validate)
- [validateRaw](ValidateApiInterface.md#validateraw)

## Methods

### validate

▸ **validate**(`requestParameters`, `initOverrides?`): `Promise`\<[`ValidationOutcome`](ValidationOutcome.md)\>

Runs the validations specified in a Guard

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`ValidateRequest`](ValidateRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ValidationOutcome`](ValidationOutcome.md)\>

#### Defined in

src/apis/ValidateApi.ts:53

___

### validateRaw

▸ **validateRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`ValidationOutcome`](ValidationOutcome.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`ValidateRequest`](ValidateRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`ValidationOutcome`](ValidationOutcome.md)\>\>

**`Summary`**

Runs the validations specified in a Guard

**`Throws`**

**`Memberof`**

ValidateApiInterface

#### Defined in

src/apis/ValidateApi.ts:45
