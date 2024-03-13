from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.guard_run_metrics import GuardRunMetrics
from ...types import Response


def _get_kwargs(
    guard_name: str,
    request_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/guards/{guard_name}/runs/{request_id}/metrics",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["GuardRunMetrics"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GuardRunMetrics.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["GuardRunMetrics"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guard_name: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["GuardRunMetrics"]]:
    """Returns an instance of GuardRunMetrics for a given request.

    Args:
        guard_name (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GuardRunMetrics']]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guard_name: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["GuardRunMetrics"]]:
    """Returns an instance of GuardRunMetrics for a given request.

    Args:
        guard_name (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GuardRunMetrics']
    """

    return sync_detailed(
        guard_name=guard_name,
        request_id=request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    guard_name: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["GuardRunMetrics"]]:
    """Returns an instance of GuardRunMetrics for a given request.

    Args:
        guard_name (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['GuardRunMetrics']]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guard_name: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["GuardRunMetrics"]]:
    """Returns an instance of GuardRunMetrics for a given request.

    Args:
        guard_name (str):
        request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['GuardRunMetrics']
    """

    return (
        await asyncio_detailed(
            guard_name=guard_name,
            request_id=request_id,
            client=client,
        )
    ).parsed
