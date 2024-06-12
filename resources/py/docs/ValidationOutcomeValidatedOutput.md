# ValidationOutcomeValidatedOutput

The validated, and potentially fixed, output from the LLM call after undergoing validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from guardrails_api_client.models.validation_outcome_validated_output import ValidationOutcomeValidatedOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationOutcomeValidatedOutput from a JSON string
validation_outcome_validated_output_instance = ValidationOutcomeValidatedOutput.from_json(json)
# print the JSON string representation of the object
print(ValidationOutcomeValidatedOutput.to_json())

# convert the object into a dict
validation_outcome_validated_output_dict = validation_outcome_validated_output_instance.to_dict()
# create an instance of ValidationOutcomeValidatedOutput from a dict
validation_outcome_validated_output_from_dict = ValidationOutcomeValidatedOutput.from_dict(validation_outcome_validated_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


