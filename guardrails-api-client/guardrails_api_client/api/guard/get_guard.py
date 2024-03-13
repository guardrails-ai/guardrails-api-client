import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.guard import Guard
from ...types import UNSET, Response, Unset


def _get_kwargs(
    guard_name: str,
    *,
    as_of: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_as_of: Union[Unset, str] = UNSET
    if not isinstance(as_of, Unset):
        json_as_of = as_of.isoformat()
    params["asOf"] = json_as_of

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/guards/{guard_name}",
        "params": params,
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
    as_of: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Guard]:
    """Fetches a specific Guard

    Args:
        guard_name (str):
        as_of (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Guard]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        as_of=as_of,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guard_name: str,
    *,
    client: AuthenticatedClient,
    as_of: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Guard]:
    """Fetches a specific Guard

    Args:
        guard_name (str):
        as_of (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Guard
    """

    return sync_detailed(
        guard_name=guard_name,
        client=client,
        as_of=as_of,
    ).parsed


async def asyncio_detailed(
    guard_name: str,
    *,
    client: AuthenticatedClient,
    as_of: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Guard]:
    """Fetches a specific Guard

    Args:
        guard_name (str):
        as_of (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Guard]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        as_of=as_of,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guard_name: str,
    *,
    client: AuthenticatedClient,
    as_of: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Guard]:
    """Fetches a specific Guard

    Args:
        guard_name (str):
        as_of (Union[Unset, datetime.datetime]):

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
            as_of=as_of,
        )
    ).parsed
