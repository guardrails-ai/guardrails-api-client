from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.projection import Projection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    guard_name: str,
    *,
    validator_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["validatorId"] = validator_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/embeddings/{guard_name}/projections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Projection"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Projection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Projection"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guard_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    validator_id: Union[Unset, str] = UNSET,
) -> Response[List["Projection"]]:
    """Creates of updates projection for a given Guard id

    Args:
        guard_name (str):
        validator_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Projection']]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        validator_id=validator_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    guard_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    validator_id: Union[Unset, str] = UNSET,
) -> Optional[List["Projection"]]:
    """Creates of updates projection for a given Guard id

    Args:
        guard_name (str):
        validator_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Projection']
    """

    return sync_detailed(
        guard_name=guard_name,
        client=client,
        validator_id=validator_id,
    ).parsed


async def asyncio_detailed(
    guard_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    validator_id: Union[Unset, str] = UNSET,
) -> Response[List["Projection"]]:
    """Creates of updates projection for a given Guard id

    Args:
        guard_name (str):
        validator_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Projection']]
    """

    kwargs = _get_kwargs(
        guard_name=guard_name,
        validator_id=validator_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    guard_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    validator_id: Union[Unset, str] = UNSET,
) -> Optional[List["Projection"]]:
    """Creates of updates projection for a given Guard id

    Args:
        guard_name (str):
        validator_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Projection']
    """

    return (
        await asyncio_detailed(
            guard_name=guard_name,
            client=client,
            validator_id=validator_id,
        )
    ).parsed
