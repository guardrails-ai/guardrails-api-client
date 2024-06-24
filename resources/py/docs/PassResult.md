# PassResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **object** |  | 
**value_override** | [**object**](AnyType.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**validated_chunk** | [**object**](AnyType.md) |  | [optional] 

## Example

```python
from guardrails_api_client.models.pass_result import PassResult

# TODO update the JSON string below
json = "{}"
# create an instance of PassResult from a JSON string
pass_result_instance = PassResult.from_json(json)
# print the JSON string representation of the object
print(PassResult.to_json())

# convert the object into a dict
pass_result_dict = pass_result_instance.to_dict()
# create an instance of PassResult from a dict
pass_result_from_dict = PassResult.from_dict(pass_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


