# OutputsValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incorrect_value** | [**object**](AnyType.md) |  | [optional] 
**fail_results** | [**List[FailResult]**](FailResult.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.outputs_validation_response import OutputsValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutputsValidationResponse from a JSON string
outputs_validation_response_instance = OutputsValidationResponse.from_json(json)
# print the JSON string representation of the object
print(OutputsValidationResponse.to_json())

# convert the object into a dict
outputs_validation_response_dict = outputs_validation_response_instance.to_dict()
# create an instance of OutputsValidationResponse from a dict
outputs_validation_response_from_dict = OutputsValidationResponse.from_dict(outputs_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


