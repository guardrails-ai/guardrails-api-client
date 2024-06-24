# ValidatorLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validator_name** | **str** | The class name of the validator. | 
**registered_name** | **str** | The registry id of the validator. | 
**instance_id** | [**ValidatorLogInstanceId**](ValidatorLogInstanceId.md) |  | [optional] 
**property_path** | **str** | The JSON path to the property which was validated that produced this log. | 
**value_before_validation** | [**object**](AnyType.md) |  | 
**value_after_validation** | [**object**](AnyType.md) |  | [optional] 
**validation_result** | [**ValidatorLogValidationResult**](ValidatorLogValidationResult.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 

## Example

```python
from guardrails_api_client.models.validator_log import ValidatorLog

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatorLog from a JSON string
validator_log_instance = ValidatorLog.from_json(json)
# print the JSON string representation of the object
print(ValidatorLog.to_json())

# convert the object into a dict
validator_log_dict = validator_log_instance.to_dict()
# create an instance of ValidatorLog from a dict
validator_log_from_dict = ValidatorLog.from_dict(validator_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


