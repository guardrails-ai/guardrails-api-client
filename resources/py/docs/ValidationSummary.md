# ValidationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validator_name** | **str** | The class name of the validator. | 
**validator_status** | **str** |  | 
**property_path** | **str** | The JSON path to the property which was validated that produced this log. | [optional] 
**failure_reason** | **str** | The error message indicating why validation failed. | [optional] 
**error_spans** | [**List[ErrorSpan]**](ErrorSpan.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.validation_summary import ValidationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationSummary from a JSON string
validation_summary_instance = ValidationSummary.from_json(json)
# print the JSON string representation of the object
print(ValidationSummary.to_json())

# convert the object into a dict
validation_summary_dict = validation_summary_instance.to_dict()
# create an instance of ValidationSummary from a dict
validation_summary_from_dict = ValidationSummary.from_dict(validation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


