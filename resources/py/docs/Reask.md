# Reask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incorrect_value** | [**object**](AnyType.md) |  | [optional] 
**fail_results** | [**List[FailResult]**](FailResult.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.reask import Reask

# TODO update the JSON string below
json = "{}"
# create an instance of Reask from a JSON string
reask_instance = Reask.from_json(json)
# print the JSON string representation of the object
print(Reask.to_json())

# convert the object into a dict
reask_dict = reask_instance.to_dict()
# create an instance of Reask from a dict
reask_from_dict = Reask.from_dict(reask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


