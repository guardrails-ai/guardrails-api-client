# Validation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_of** | **float** |  | [optional] 
**maximum** | **float** |  | [optional] 
**exclusive_maximum** | **float** |  | [optional] 
**minimum** | **float** |  | [optional] 
**exclusive_minimum** | **float** |  | [optional] 
**max_length** | **int** |  | [optional] 
**min_length** | **int** |  | [optional] 
**pattern** | **str** |  | [optional] 
**max_items** | **int** |  | [optional] 
**min_items** | **int** |  | [optional] 
**unique_items** | **bool** |  | [optional] [default to False]
**max_contains** | **int** |  | [optional] 
**min_contains** | **int** |  | [optional] 
**max_properties** | **int** |  | [optional] 
**min_properties** | **int** |  | [optional] 
**required** | **List[str]** |  | [optional] [default to []]
**dependent_required** | **Dict[str, List[str]]** |  | [optional] 
**const** | **object** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**type** | [**ValidationType**](ValidationType.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.validation import Validation

# TODO update the JSON string below
json = "{}"
# create an instance of Validation from a JSON string
validation_instance = Validation.from_json(json)
# print the JSON string representation of the object
print(Validation.to_json())

# convert the object into a dict
validation_dict = validation_instance.to_dict()
# create an instance of Validation from a dict
validation_from_dict = Validation.from_dict(validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


