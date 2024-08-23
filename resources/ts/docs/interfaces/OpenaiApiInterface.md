[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / OpenaiApiInterface

# Interface: OpenaiApiInterface

OpenaiApi - interface

**`Export`**

OpenaiApiInterface

## Implemented by

- [`OpenaiApi`](../classes/OpenaiApi.md)

## Table of contents

### Methods

- [openaiChatCompletion](OpenaiApiInterface.md#openaichatcompletion)
- [openaiChatCompletionRaw](OpenaiApiInterface.md#openaichatcompletionraw)

## Methods

### openaiChatCompletion

▸ **openaiChatCompletion**(`requestParameters`, `initOverrides?`): `Promise`\<[`OpenAIChatCompletion`](OpenAIChatCompletion.md)\>

OpenAI SDK compatible endpoint for Chat Completions

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`OpenaiChatCompletionRequest`](OpenaiChatCompletionRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`OpenAIChatCompletion`](OpenAIChatCompletion.md)\>

#### Defined in

src/apis/OpenaiApi.ts:54

___

### openaiChatCompletionRaw

▸ **openaiChatCompletionRaw**(`requestParameters`, `initOverrides?`): `Promise`\<[`ApiResponse`](ApiResponse.md)\<[`OpenAIChatCompletion`](OpenAIChatCompletion.md)\>\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `requestParameters` | [`OpenaiChatCompletionRequest`](OpenaiChatCompletionRequest.md) |
| `initOverrides?` | `RequestInit` \| [`InitOverrideFunction`](../modules.md#initoverridefunction) |

#### Returns

`Promise`\<[`ApiResponse`](ApiResponse.md)\<[`OpenAIChatCompletion`](OpenAIChatCompletion.md)\>\>

**`Summary`**

OpenAI SDK compatible endpoint for Chat Completions

**`Throws`**

**`Memberof`**

OpenaiApiInterface

#### Defined in

src/apis/OpenaiApi.ts:46
