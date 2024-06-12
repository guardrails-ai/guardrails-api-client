[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / Configuration

# Class: Configuration

## Table of contents

### Constructors

- [constructor](Configuration.md#constructor)

### Properties

- [configuration](Configuration.md#configuration)

### Accessors

- [accessToken](Configuration.md#accesstoken)
- [apiKey](Configuration.md#apikey)
- [basePath](Configuration.md#basepath)
- [config](Configuration.md#config)
- [credentials](Configuration.md#credentials)
- [fetchApi](Configuration.md#fetchapi)
- [headers](Configuration.md#headers)
- [middleware](Configuration.md#middleware)
- [password](Configuration.md#password)
- [queryParamsStringify](Configuration.md#queryparamsstringify)
- [username](Configuration.md#username)

## Constructors

### constructor

• **new Configuration**(`configuration?`): [`Configuration`](Configuration.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `configuration` | [`ConfigurationParameters`](../interfaces/ConfigurationParameters.md) |

#### Returns

[`Configuration`](Configuration.md)

#### Defined in

src/runtime.ts:37

## Properties

### configuration

• `Private` **configuration**: [`ConfigurationParameters`](../interfaces/ConfigurationParameters.md) = `{}`

#### Defined in

src/runtime.ts:37

## Accessors

### accessToken

• `get` **accessToken**(): `undefined` \| (`name?`: `string`, `scopes?`: `string`[]) => `string` \| `Promise`\<`string`\>

#### Returns

`undefined` \| (`name?`: `string`, `scopes?`: `string`[]) => `string` \| `Promise`\<`string`\>

#### Defined in

src/runtime.ts:77

___

### apiKey

• `get` **apiKey**(): `undefined` \| (`name`: `string`) => `string` \| `Promise`\<`string`\>

#### Returns

`undefined` \| (`name`: `string`) => `string` \| `Promise`\<`string`\>

#### Defined in

src/runtime.ts:69

___

### basePath

• `get` **basePath**(): `string`

#### Returns

`string`

#### Defined in

src/runtime.ts:43

___

### config

• `set` **config**(`configuration`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `configuration` | [`Configuration`](Configuration.md) |

#### Returns

`void`

#### Defined in

src/runtime.ts:39

___

### credentials

• `get` **credentials**(): `undefined` \| `RequestCredentials`

#### Returns

`undefined` \| `RequestCredentials`

#### Defined in

src/runtime.ts:93

___

### fetchApi

• `get` **fetchApi**(): `undefined` \| (`input`: `RequestInfo` \| `URL`, `init?`: `RequestInit`) => `Promise`\<`Response`\>

#### Returns

`undefined` \| (`input`: `RequestInfo` \| `URL`, `init?`: `RequestInit`) => `Promise`\<`Response`\>

#### Defined in

src/runtime.ts:49

___

### headers

• `get` **headers**(): `undefined` \| [`HTTPHeaders`](../modules.md#httpheaders)

#### Returns

`undefined` \| [`HTTPHeaders`](../modules.md#httpheaders)

#### Defined in

src/runtime.ts:89

___

### middleware

• `get` **middleware**(): [`Middleware`](../interfaces/Middleware.md)[]

#### Returns

[`Middleware`](../interfaces/Middleware.md)[]

#### Defined in

src/runtime.ts:53

___

### password

• `get` **password**(): `undefined` \| `string`

#### Returns

`undefined` \| `string`

#### Defined in

src/runtime.ts:65

___

### queryParamsStringify

• `get` **queryParamsStringify**(): (`params`: [`HTTPQuery`](../modules.md#httpquery)) => `string`

#### Returns

`fn`

▸ (`params`): `string`

##### Parameters

| Name | Type |
| :------ | :------ |
| `params` | [`HTTPQuery`](../modules.md#httpquery) |

##### Returns

`string`

#### Defined in

src/runtime.ts:57

___

### username

• `get` **username**(): `undefined` \| `string`

#### Returns

`undefined` \| `string`

#### Defined in

src/runtime.ts:61
