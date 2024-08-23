# guardrails_api_client.OpenaiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openai_chat_completion**](OpenaiApi.md#openai_chat_completion) | **POST** /guards/{guardName}/openai/v1/chat/completions | OpenAI SDK compatible endpoint for Chat Completions


# **openai_chat_completion**
> OpenAIChatCompletion openai_chat_completion(guard_name, open_ai_chat_completion_payload)

OpenAI SDK compatible endpoint for Chat Completions

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import guardrails_api_client
from guardrails_api_client.models.open_ai_chat_completion import OpenAIChatCompletion
from guardrails_api_client.models.open_ai_chat_completion_payload import OpenAIChatCompletionPayload
from guardrails_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = guardrails_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = guardrails_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with guardrails_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = guardrails_api_client.OpenaiApi(api_client)
    guard_name = 'guard_name_example' # str | Guard name
    open_ai_chat_completion_payload = guardrails_api_client.OpenAIChatCompletionPayload() # OpenAIChatCompletionPayload | 

    try:
        # OpenAI SDK compatible endpoint for Chat Completions
        api_response = api_instance.openai_chat_completion(guard_name, open_ai_chat_completion_payload)
        print("The response of OpenaiApi->openai_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->openai_chat_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_name** | **str**| Guard name | 
 **open_ai_chat_completion_payload** | [**OpenAIChatCompletionPayload**](OpenAIChatCompletionPayload.md)|  | 

### Return type

[**OpenAIChatCompletion**](OpenAIChatCompletion.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The output of the completion |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

