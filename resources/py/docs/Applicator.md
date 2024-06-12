# Applicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix_items** | **List[object]** |  | [optional] 
**items** | **object** |  | [optional] 
**contains** | **object** |  | [optional] 
**additional_properties** | **object** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 
**pattern_properties** | **Dict[str, object]** |  | [optional] 
**dependent_schemas** | **Dict[str, object]** |  | [optional] 
**property_names** | **object** |  | [optional] 
**var_if** | **object** |  | [optional] 
**then** | **object** |  | [optional] 
**var_else** | **object** |  | [optional] 
**all_of** | **List[object]** |  | [optional] 
**any_of** | **List[object]** |  | [optional] 
**one_of** | **List[object]** |  | [optional] 
**var_not** | **object** |  | [optional] 

## Example

```python
from guardrails_api_client.models.applicator import Applicator

# TODO update the JSON string below
json = "{}"
# create an instance of Applicator from a JSON string
applicator_instance = Applicator.from_json(json)
# print the JSON string representation of the object
print(Applicator.to_json())

# convert the object into a dict
applicator_dict = applicator_instance.to_dict()
# create an instance of Applicator from a dict
applicator_from_dict = Applicator.from_dict(applicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


