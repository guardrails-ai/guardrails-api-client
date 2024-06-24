# ErrorSpan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | 
**end** | **int** |  | 
**reason** | **str** | The reason validation failed, specific to this chunk. | 

## Example

```python
from guardrails_api_client.models.error_span import ErrorSpan

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorSpan from a JSON string
error_span_instance = ErrorSpan.from_json(json)
# print the JSON string representation of the object
print(ErrorSpan.to_json())

# convert the object into a dict
error_span_dict = error_span_instance.to_dict()
# create an instance of ErrorSpan from a dict
error_span_from_dict = ErrorSpan.from_dict(error_span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


