# ValidatorLogInstanceId

A unique identifier for the validator that produced this log within the session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from guardrails_api_client.models.validator_log_instance_id import ValidatorLogInstanceId

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatorLogInstanceId from a JSON string
validator_log_instance_id_instance = ValidatorLogInstanceId.from_json(json)
# print the JSON string representation of the object
print(ValidatorLogInstanceId.to_json())

# convert the object into a dict
validator_log_instance_id_dict = validator_log_instance_id_instance.to_dict()
# create an instance of ValidatorLogInstanceId from a dict
validator_log_instance_id_from_dict = ValidatorLogInstanceId.from_dict(validator_log_instance_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


