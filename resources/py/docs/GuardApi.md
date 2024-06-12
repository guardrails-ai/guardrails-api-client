# guardrails_api_client.GuardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_guard**](GuardApi.md#create_guard) | **POST** /guards | Creates a Guard
[**delete_guard**](GuardApi.md#delete_guard) | **DELETE** /guards/{guardName} | Deletes a Guard
[**get_guard**](GuardApi.md#get_guard) | **GET** /guards/{guardName} | Fetches a specific Guard
[**get_guards**](GuardApi.md#get_guards) | **GET** /guards | Fetches the configuration for all Guards the user has access to.
[**update_guard**](GuardApi.md#update_guard) | **PUT** /guards/{guardName} | Updates a Guard


# **create_guard**
> Guard create_guard(body)

Creates a Guard

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import guardrails_api_client
from guardrails_api_client.models.guard import Guard
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
    api_instance = guardrails_api_client.GuardApi(api_client)
    body = guardrails_api_client.Guard() # Guard | 

    try:
        # Creates a Guard
        api_response = api_instance.create_guard(body)
        print("The response of GuardApi->create_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardApi->create_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Guard**|  | 

### Return type

[**Guard**](Guard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the new Guard |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guard**
> Guard delete_guard(guard_name)

Deletes a Guard

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import guardrails_api_client
from guardrails_api_client.models.guard import Guard
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
    api_instance = guardrails_api_client.GuardApi(api_client)
    guard_name = 'guard_name_example' # str | Guard name

    try:
        # Deletes a Guard
        api_response = api_instance.delete_guard(guard_name)
        print("The response of GuardApi->delete_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardApi->delete_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_name** | **str**| Guard name | 

### Return type

[**Guard**](Guard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the deleted Guard |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guard**
> Guard get_guard(guard_name, as_of=as_of)

Fetches a specific Guard

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import guardrails_api_client
from guardrails_api_client.models.guard import Guard
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
    api_instance = guardrails_api_client.GuardApi(api_client)
    guard_name = 'guard_name_example' # str | Guard name
    as_of = '2013-10-20T19:20:30+01:00' # datetime | Used to query for data as it existed at this date and time (optional)

    try:
        # Fetches a specific Guard
        api_response = api_instance.get_guard(guard_name, as_of=as_of)
        print("The response of GuardApi->get_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardApi->get_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_name** | **str**| Guard name | 
 **as_of** | **datetime**| Used to query for data as it existed at this date and time | [optional] 

### Return type

[**Guard**](Guard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the fetched Guard |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_guards**
> List[Guard] get_guards()

Fetches the configuration for all Guards the user has access to.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import guardrails_api_client
from guardrails_api_client.models.guard import Guard
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
    api_instance = guardrails_api_client.GuardApi(api_client)

    try:
        # Fetches the configuration for all Guards the user has access to.
        api_response = api_instance.get_guards()
        print("The response of GuardApi->get_guards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardApi->get_guards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Guard]**](Guard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Guards. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guard**
> Guard update_guard(guard_name, body)

Updates a Guard

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import guardrails_api_client
from guardrails_api_client.models.guard import Guard
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
    api_instance = guardrails_api_client.GuardApi(api_client)
    guard_name = 'guard_name_example' # str | Guard name
    body = guardrails_api_client.Guard() # Guard | 

    try:
        # Updates a Guard
        api_response = api_instance.update_guard(guard_name, body)
        print("The response of GuardApi->update_guard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuardApi->update_guard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guard_name** | **str**| Guard name | 
 **body** | **Guard**|  | 

### Return type

[**Guard**](Guard.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the updated Guard |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

