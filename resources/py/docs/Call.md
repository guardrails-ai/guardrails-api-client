# Call


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for this Call.  Can be used as an identifier for a specific execution of a Guard. | 
**iterations** | [**List[Iteration]**](Iteration.md) |  | [optional] [default to []]
**inputs** | [**CallInputs**](CallInputs.md) |  | [optional] 
**exception** | **str** |  | [optional] 

## Example

```python
from guardrails_api_client.models.call import Call

# TODO update the JSON string below
json = "{}"
# create an instance of Call from a JSON string
call_instance = Call.from_json(json)
# print the JSON string representation of the object
print(Call.to_json())

# convert the object into a dict
call_dict = call_instance.to_dict()
# create an instance of Call from a dict
call_from_dict = Call.from_dict(call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


