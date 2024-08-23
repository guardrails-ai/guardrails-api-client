# OpenAIChatCompletionPayloadMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role of the message | [optional] 
**content** | **str** | The content of the message | [optional] 

## Example

```python
from guardrails_api_client.models.open_ai_chat_completion_payload_messages_inner import OpenAIChatCompletionPayloadMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIChatCompletionPayloadMessagesInner from a JSON string
open_ai_chat_completion_payload_messages_inner_instance = OpenAIChatCompletionPayloadMessagesInner.from_json(json)
# print the JSON string representation of the object
print(OpenAIChatCompletionPayloadMessagesInner.to_json())

# convert the object into a dict
open_ai_chat_completion_payload_messages_inner_dict = open_ai_chat_completion_payload_messages_inner_instance.to_dict()
# create an instance of OpenAIChatCompletionPayloadMessagesInner from a dict
open_ai_chat_completion_payload_messages_inner_from_dict = OpenAIChatCompletionPayloadMessagesInner.from_dict(open_ai_chat_completion_payload_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


