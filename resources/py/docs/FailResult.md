# FailResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **object** |  | [optional] 
**error_message** | **object** |  | [optional] 
**fix_value** | [**object**](AnyType.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from guardrails_api_client.models.fail_result import FailResult

# TODO update the JSON string below
json = "{}"
# create an instance of FailResult from a JSON string
fail_result_instance = FailResult.from_json(json)
# print the JSON string representation of the object
print(FailResult.to_json())

# convert the object into a dict
fail_result_dict = fail_result_instance.to_dict()
# create an instance of FailResult from a dict
fail_result_from_dict = FailResult.from_dict(fail_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


