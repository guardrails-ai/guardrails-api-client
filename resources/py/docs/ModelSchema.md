# ModelSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definitions** | **Dict[str, object]** |  | [optional] 
**dependencies** | [**Dict[str, AnyOfAnyTypeset]**](AnyOfAnyTypeset.md) |  | [optional] 
**anchor** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**dynamic_ref** | **str** |  | [optional] 
**dynamic_anchor** | **str** |  | [optional] 
**vocabulary** | **Dict[str, object]** |  | [optional] 
**comment** | **str** |  | [optional] 
**defs** | **Dict[str, object]** |  | [optional] 
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
**unevaluated_items** | **object** |  | [optional] 
**unevaluated_properties** | **object** |  | [optional] 
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
**required** | **List[object]** |  | [optional] [default to []]
**dependent_required** | **Dict[str, List[str]]** |  | [optional] 
**const** | **object** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**type** | [**ValidationType**](ValidationType.md) |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**default** | **object** |  | [optional] 
**deprecated** | **bool** |  | [optional] [default to False]
**read_only** | **bool** |  | [optional] [default to False]
**write_only** | **bool** |  | [optional] [default to False]
**examples** | **List[object]** |  | [optional] 
**format** | **str** |  | [optional] 
**content_media_type** | **str** |  | [optional] 
**content_encoding** | **str** |  | [optional] 
**content_schema** | **object** |  | [optional] 

## Example

```python
from guardrails_api_client.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print(ModelSchema.to_json())

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_from_dict = ModelSchema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


