# ValidationOutcome

The output from a Guard execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_llm_output** | **str** | The raw, unchanged string content from the LLM call. | [optional] 
**validated_output** | [**ValidationOutcomeValidatedOutput**](ValidationOutcomeValidatedOutput.md) |  | [optional] 
**reask** | [**Reask**](Reask.md) | If validation continuously fails and all allocated reasks are used, this field will contain the final reask that would have been sent to the LLM if additional reasks were available. | [optional] 
**validation_passed** | **bool** | A boolean to indicate whether or not the LLM output passed validation.  If this is False, the validated_output may be invalid. | [optional] 
**error** | **str** | If the validation process raised a handleable exception, this field will contain the error message. | [optional] 

## Example

```python
from guardrails_api_client.models.validation_outcome import ValidationOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationOutcome from a JSON string
validation_outcome_instance = ValidationOutcome.from_json(json)
# print the JSON string representation of the object
print(ValidationOutcome.to_json())

# convert the object into a dict
validation_outcome_dict = validation_outcome_instance.to_dict()
# create an instance of ValidationOutcome from a dict
validation_outcome_from_dict = ValidationOutcome.from_dict(validation_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


