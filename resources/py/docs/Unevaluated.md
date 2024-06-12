# Unevaluated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unevaluated_items** | **object** |  | [optional] 
**unevaluated_properties** | **object** |  | [optional] 

## Example

```python
from guardrails_api_client.models.unevaluated import Unevaluated

# TODO update the JSON string below
json = "{}"
# create an instance of Unevaluated from a JSON string
unevaluated_instance = Unevaluated.from_json(json)
# print the JSON string representation of the object
print(Unevaluated.to_json())

# convert the object into a dict
unevaluated_dict = unevaluated_instance.to_dict()
# create an instance of Unevaluated from a dict
unevaluated_from_dict = Unevaluated.from_dict(unevaluated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


