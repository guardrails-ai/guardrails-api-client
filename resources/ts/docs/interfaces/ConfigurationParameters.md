[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ConfigurationParameters

# Interface: ConfigurationParameters

## Table of contents

### Properties

- [accessToken](ConfigurationParameters.md#accesstoken)
- [apiKey](ConfigurationParameters.md#apikey)
- [basePath](ConfigurationParameters.md#basepath)
- [credentials](ConfigurationParameters.md#credentials)
- [fetchApi](ConfigurationParameters.md#fetchapi)
- [headers](ConfigurationParameters.md#headers)
- [middleware](ConfigurationParameters.md#middleware)
- [password](ConfigurationParameters.md#password)
- [queryParamsStringify](ConfigurationParameters.md#queryparamsstringify)
- [username](ConfigurationParameters.md#username)

## Properties

### accessToken

• `Optional` **accessToken**: `string` \| `Promise`\<`string`\> \| (`name?`: `string`, `scopes?`: `string`[]) => `string` \| `Promise`\<`string`\>

#### Defined in

src/runtime.ts:28

___

### apiKey

• `Optional` **apiKey**: `string` \| `Promise`\<`string`\> \| (`name`: `string`) => `string` \| `Promise`\<`string`\>

#### Defined in

src/runtime.ts:24

___

### basePath

• `Optional` **basePath**: `string`

#### Defined in

src/runtime.ts:18

___

### credentials

• `Optional` **credentials**: `RequestCredentials`

#### Defined in

src/runtime.ts:33

___

### fetchApi

• `Optional` **fetchApi**: (`input`: `RequestInfo` \| `URL`, `init?`: `RequestInit`) => `Promise`\<`Response`\>

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

src/runtime.ts:19

___

### headers

• `Optional` **headers**: [`HTTPHeaders`](../modules.md#httpheaders)

#### Defined in

src/runtime.ts:32

___

### middleware

• `Optional` **middleware**: [`Middleware`](Middleware.md)[]

#### Defined in

src/runtime.ts:20

___

### password

• `Optional` **password**: `string`

#### Defined in

src/runtime.ts:23

___

### queryParamsStringify

• `Optional` **queryParamsStringify**: (`params`: [`HTTPQuery`](../modules.md#httpquery)) => `string`

#### Type declaration

▸ (`params`): `string`

##### Parameters

| Name | Type |
| :------ | :------ |
| `params` | [`HTTPQuery`](../modules.md#httpquery) |

##### Returns

`string`

#### Defined in

src/runtime.ts:21

___

### username

• `Optional` **username**: `string`

#### Defined in

src/runtime.ts:22
