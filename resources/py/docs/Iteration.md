# Iteration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for this Call.  Can be used as an identifier for a specific execution of a Guard. | 
**index** | **int** | The zero-based index of this iteration within the current Call. | 
**call_id** | **str** | The unique identifier for the Call that this iteration is a part of. | 
**inputs** | [**Inputs**](Inputs.md) |  | [optional] 
**outputs** | [**Outputs**](Outputs.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.iteration import Iteration

# TODO update the JSON string below
json = "{}"
# create an instance of Iteration from a JSON string
iteration_instance = Iteration.from_json(json)
# print the JSON string representation of the object
print(Iteration.to_json())

# convert the object into a dict
iteration_dict = iteration_instance.to_dict()
# create an instance of Iteration from a dict
iteration_from_dict = Iteration.from_dict(iteration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


