# ValidatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_output** | **object** | The LLM output as a string or the input prompts for the LLM | [optional] 
**num_reasks** | **object** | An override for the number of re-asks to perform | [optional] 
**prompt_params** | **Dict[str, object]** | additional params for llm prompts | [optional] 
**llm_api** | [**LLMResource**](LLMResource.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.validate_payload import ValidatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePayload from a JSON string
validate_payload_instance = ValidatePayload.from_json(json)
# print the JSON string representation of the object
print(ValidatePayload.to_json())

# convert the object into a dict
validate_payload_dict = validate_payload_instance.to_dict()
# create an instance of ValidatePayload from a dict
validate_payload_from_dict = ValidatePayload.from_dict(validate_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


