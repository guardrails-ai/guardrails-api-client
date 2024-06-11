# Core


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**dynamic_ref** | **str** |  | [optional] 
**dynamic_anchor** | **str** |  | [optional] 
**vocabulary** | **Dict[str, bool]** |  | [optional] 
**comment** | **str** |  | [optional] 
**defs** | **Dict[str, object]** |  | [optional] 

## Example

```python
from guardrails_api_client.models.core import Core

# TODO update the JSON string below
json = "{}"
# create an instance of Core from a JSON string
core_instance = Core.from_json(json)
# print the JSON string representation of the object
print(Core.to_json())

# convert the object into a dict
core_dict = core_instance.to_dict()
# create an instance of Core from a dict
core_from_dict = Core.from_dict(core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


