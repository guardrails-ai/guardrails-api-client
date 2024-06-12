# ValidatorLogValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **str** |  | [optional] 
**value_override** | [**object**](AnyType.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**error_message** | **object** |  | [optional] 
**fix_value** | [**object**](AnyType.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.validator_log_validation_result import ValidatorLogValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatorLogValidationResult from a JSON string
validator_log_validation_result_instance = ValidatorLogValidationResult.from_json(json)
# print the JSON string representation of the object
print(ValidatorLogValidationResult.to_json())

# convert the object into a dict
validator_log_validation_result_dict = validator_log_validation_result_instance.to_dict()
# create an instance of ValidatorLogValidationResult from a dict
validator_log_validation_result_from_dict = ValidatorLogValidationResult.from_dict(validator_log_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


