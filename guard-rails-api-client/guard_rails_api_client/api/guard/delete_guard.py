from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.guard import Guard
from ...types import Response


def _get_kwargs(
    guard_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/guards/{guard_name}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Guard]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Guard.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Guard]:
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
) -> Response[Guard]:
    """Deletes a Guard

    Args:
        guard_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Guard]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guard_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Guard]:
    """Deletes a Guard

    Args:
        guard_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Guard
    """

    return sync_detailed(
        guard_name=guard_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    guard_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Guard]:
    """Deletes a Guard

    Args:
        guard_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Guard]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guard_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Guard]:
    """Deletes a Guard

    Args:
        guard_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Guard
    """

    return (
        await asyncio_detailed(
            guard_name=guard_name,
            client=client,
        )
    ).parsed
