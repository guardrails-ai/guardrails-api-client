# OutputsException

The exception which interrupted the Guard execution process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** |  | [optional] 

## Example

```python
from guardrails_api_client.models.outputs_exception import OutputsException

# TODO update the JSON string below
json = "{}"
# create an instance of OutputsException from a JSON string
outputs_exception_instance = OutputsException.from_json(json)
# print the JSON string representation of the object
print(OutputsException.to_json())

# convert the object into a dict
outputs_exception_dict = outputs_exception_instance.to_dict()
# create an instance of OutputsException from a dict
outputs_exception_from_dict = OutputsException.from_dict(outputs_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


