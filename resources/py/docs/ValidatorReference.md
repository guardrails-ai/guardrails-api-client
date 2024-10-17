# ValidatorReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | The unique identifier for this Validator.  Often the hub id; e.g. guardrails/regex_match | 
**on** | [**AnyOfAnyTypeAnyType**](AnyOfAnyTypeAnyType.md) | A reference to the property this validator should be applied against.  Can be a valid JSON path or a meta-property such as \&quot;messages\&quot; or \&quot;output\&quot; | [optional] 
**on_fail** | **object** |  | [optional] 
**args** | [**List[object]**](AnyType.md) |  | [optional] 
**kwargs** | **Dict[str, object]** |  | [optional] 

## Example

```python
from guardrails_api_client.models.validator_reference import ValidatorReference

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatorReference from a JSON string
validator_reference_instance = ValidatorReference.from_json(json)
# print the JSON string representation of the object
print(ValidatorReference.to_json())

# convert the object into a dict
validator_reference_dict = validator_reference_instance.to_dict()
# create an instance of ValidatorReference from a dict
validator_reference_from_dict = ValidatorReference.from_dict(validator_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


