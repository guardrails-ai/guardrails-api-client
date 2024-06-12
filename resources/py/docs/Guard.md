# Guard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the Guard. | 
**name** | **str** | The name for the Guard. | 
**description** | **str** | A description that concisely states the expected behaviour or purpose of the Guard. | [optional] 
**validators** | [**List[ValidatorReference]**](ValidatorReference.md) |  | [optional] 
**output_schema** | [**ModelSchema**](ModelSchema.md) |  | [optional] 
**history** | [**GuardHistory**](GuardHistory.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.guard import Guard

# TODO update the JSON string below
json = "{}"
# create an instance of Guard from a JSON string
guard_instance = Guard.from_json(json)
# print the JSON string representation of the object
print(Guard.to_json())

# convert the object into a dict
guard_dict = guard_instance.to_dict()
# create an instance of Guard from a dict
guard_from_dict = Guard.from_dict(guard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


