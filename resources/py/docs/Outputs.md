# Outputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_response_info** | [**LLMResponse**](LLMResponse.md) |  | [optional] 
**raw_output** | **str** | The string content from the LLM response. | [optional] 
**parsed_output** | [**OutputsParsedOutput**](OutputsParsedOutput.md) |  | [optional] 
**validation_response** | [**OutputsValidationResponse**](OutputsValidationResponse.md) |  | [optional] 
**guarded_output** | [**OutputsParsedOutput**](OutputsParsedOutput.md) |  | [optional] 
**reasks** | [**List[Reask]**](Reask.md) |  | [optional] 
**validator_logs** | [**List[ValidatorLog]**](ValidatorLog.md) |  | [optional] 
**error** | **str** | The error message from any exception which interrupted the Guard execution process. | [optional] 
**exception** | [**OutputsException**](OutputsException.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.outputs import Outputs

# TODO update the JSON string below
json = "{}"
# create an instance of Outputs from a JSON string
outputs_instance = Outputs.from_json(json)
# print the JSON string representation of the object
print(Outputs.to_json())

# convert the object into a dict
outputs_dict = outputs_instance.to_dict()
# create an instance of Outputs from a dict
outputs_from_dict = Outputs.from_dict(outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


