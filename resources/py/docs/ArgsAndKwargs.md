# ArgsAndKwargs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | [**List[object]**](AnyType.md) |  | [optional] 
**kwargs** | **Dict[str, object]** |  | [optional] 

## Example

```python
from guardrails_api_client.models.args_and_kwargs import ArgsAndKwargs

# TODO update the JSON string below
json = "{}"
# create an instance of ArgsAndKwargs from a JSON string
args_and_kwargs_instance = ArgsAndKwargs.from_json(json)
# print the JSON string representation of the object
print(ArgsAndKwargs.to_json())

# convert the object into a dict
args_and_kwargs_dict = args_and_kwargs_instance.to_dict()
# create an instance of ArgsAndKwargs from a dict
args_and_kwargs_from_dict = ArgsAndKwargs.from_dict(args_and_kwargs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


