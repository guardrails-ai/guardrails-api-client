# CallInputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_api** | **str** | The LLM resource targeted by the user. e.g. openai.chat.completions.create | [optional] 
**llm_output** | **str** | The string output from an external LLM call provided by the user via Guard.parse. | [optional] 
**instructions** | **str** | The instructions for chat models. | [optional] 
**prompt** | **str** | The prompt for the LLM. | [optional] 
**msg_history** | **List[Dict[str, object]]** | The message history for chat models. | [optional] 
**prompt_params** | **Dict[str, object]** | Parameters to be formatted into the prompt. | [optional] 
**num_reasks** | **int** | The total number of times the LLM can be called to correct output excluding the initial call. | [optional] 
**metadata** | **Dict[str, object]** | Additional data to be used by Validators during execution time. | [optional] 
**full_schema_reask** | **bool** | Whether to perform reasks for the entire schema rather than for individual fields. | [optional] 
**stream** | **bool** | Whether to use streaming. | [optional] 
**args** | [**List[object]**](AnyType.md) |  | [optional] 
**kwargs** | **Dict[str, object]** |  | [optional] 

## Example

```python
from guardrails_api_client.models.call_inputs import CallInputs

# TODO update the JSON string below
json = "{}"
# create an instance of CallInputs from a JSON string
call_inputs_instance = CallInputs.from_json(json)
# print the JSON string representation of the object
print(CallInputs.to_json())

# convert the object into a dict
call_inputs_dict = call_inputs_instance.to_dict()
# create an instance of CallInputs from a dict
call_inputs_from_dict = CallInputs.from_dict(call_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


