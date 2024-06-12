# CallException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | [optional] 

## Example

```python
from guardrails_api_client.models.call_exception import CallException

# TODO update the JSON string below
json = "{}"
# create an instance of CallException from a JSON string
call_exception_instance = CallException.from_json(json)
# print the JSON string representation of the object
print(CallException.to_json())

# convert the object into a dict
call_exception_dict = call_exception_instance.to_dict()
# create an instance of CallException from a dict
call_exception_from_dict = CallException.from_dict(call_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


