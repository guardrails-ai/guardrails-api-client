# OpenAIChatCompletionPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The model to use for the completion | [optional] 
**messages** | [**List[OpenAIChatCompletionPayloadMessagesInner]**](OpenAIChatCompletionPayloadMessagesInner.md) | The messages to use for the completion | [optional] 
**max_tokens** | **int** | The maximum number of tokens to generate | [optional] 
**temperature** | **float** | The sampling temperature | [optional] 

## Example

```python
from guardrails_api_client.models.open_ai_chat_completion_payload import OpenAIChatCompletionPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIChatCompletionPayload from a JSON string
open_ai_chat_completion_payload_instance = OpenAIChatCompletionPayload.from_json(json)
# print the JSON string representation of the object
print(OpenAIChatCompletionPayload.to_json())

# convert the object into a dict
open_ai_chat_completion_payload_dict = open_ai_chat_completion_payload_instance.to_dict()
# create an instance of OpenAIChatCompletionPayload from a dict
open_ai_chat_completion_payload_from_dict = OpenAIChatCompletionPayload.from_dict(open_ai_chat_completion_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


