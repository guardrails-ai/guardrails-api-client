from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validate_payload import ValidatePayload
from ...models.validation_output import ValidationOutput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    guard_name: str,
    *,
    body: ValidatePayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_openai_api_key, Unset):
        headers["x-openai-api-key"] = x_openai_api_key

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/guards/{guard_name}/validate",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ValidationOutput]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ValidationOutput.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ValidationOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guard_name: str,
    *,
    client: AuthenticatedClient,
    body: ValidatePayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Response[ValidationOutput]:
    """Runs the validations specified in a Guard

    Args:
        guard_name (str):
        x_openai_api_key (Union[Unset, str]):
        body (ValidatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidationOutput]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        body=body,
        x_openai_api_key=x_openai_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guard_name: str,
    *,
    client: AuthenticatedClient,
    body: ValidatePayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Optional[ValidationOutput]:
    """Runs the validations specified in a Guard

    Args:
        guard_name (str):
        x_openai_api_key (Union[Unset, str]):
        body (ValidatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidationOutput
    """

    return sync_detailed(
        guard_name=guard_name,
        client=client,
        body=body,
        x_openai_api_key=x_openai_api_key,
    ).parsed


async def asyncio_detailed(
    guard_name: str,
    *,
    client: AuthenticatedClient,
    body: ValidatePayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Response[ValidationOutput]:
    """Runs the validations specified in a Guard

    Args:
        guard_name (str):
        x_openai_api_key (Union[Unset, str]):
        body (ValidatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidationOutput]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        body=body,
        x_openai_api_key=x_openai_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guard_name: str,
    *,
    client: AuthenticatedClient,
    body: ValidatePayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Optional[ValidationOutput]:
    """Runs the validations specified in a Guard

    Args:
        guard_name (str):
        x_openai_api_key (Union[Unset, str]):
        body (ValidatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidationOutput
    """

    return (
        await asyncio_detailed(
            guard_name=guard_name,
            client=client,
            body=body,
            x_openai_api_key=x_openai_api_key,
        )
    ).parsed
