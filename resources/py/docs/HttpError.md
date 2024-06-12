# HttpError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | A valid http status code | 
**message** | **str** | A message explaining the status | 
**cause** | **str** | Used to describe the origin of an error if that original error has meaning to the client.  This field should add specificity to &#39;message&#39;. | [optional] 
**fields** | **Dict[str, List[str]]** | Used to identify specific fields in a JSON body that caused the error.  Typically only used for 4xx type responses.  The key should be the json path to the invalid property and the value should be a list of error messages specific to that property. | [optional] 
**context** | **str** | Used to identify what part of the request caused the error for non-JSON payloads. | [optional] 

## Example

```python
from guardrails_api_client.models.http_error import HttpError

# TODO update the JSON string below
json = "{}"
# create an instance of HttpError from a JSON string
http_error_instance = HttpError.from_json(json)
# print the JSON string representation of the object
print(HttpError.to_json())

# convert the object into a dict
http_error_dict = http_error_instance.to_dict()
# create an instance of HttpError from a dict
http_error_from_dict = HttpError.from_dict(http_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


