# OpenAIChatCompletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id | 
**created** | **str** | The created date | 
**model_name** | **str** | The model name | 
**choices** | [**List[OpenAIChatCompletionPayloadMessagesInner]**](OpenAIChatCompletionPayloadMessagesInner.md) |  | 

## Example

```python
from guardrails_api_client.models.open_ai_chat_completion import OpenAIChatCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIChatCompletion from a JSON string
open_ai_chat_completion_instance = OpenAIChatCompletion.from_json(json)
# print the JSON string representation of the object
print(OpenAIChatCompletion.to_json())

# convert the object into a dict
open_ai_chat_completion_dict = open_ai_chat_completion_instance.to_dict()
# create an instance of OpenAIChatCompletion from a dict
open_ai_chat_completion_from_dict = OpenAIChatCompletion.from_dict(open_ai_chat_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


