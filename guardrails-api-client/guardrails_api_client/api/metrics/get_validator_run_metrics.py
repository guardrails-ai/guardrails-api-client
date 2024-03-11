from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validator_run_metrics import ValidatorRunMetrics
from ...types import Response


def _get_kwargs(
    validator_name: str,
    request_id: str,
    validator_instance_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/validators/{validator_name}/runs/{request_id}/instances/{validator_instance_id}/metrics",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ValidatorRunMetrics"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ValidatorRunMetrics.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ValidatorRunMetrics"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    validator_name: str,
    request_id: str,
    validator_instance_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["ValidatorRunMetrics"]]:
    """Returns an arary of ValidatorRunMetrics for a given request.

    Args:
        validator_name (str):
        request_id (str):
        validator_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ValidatorRunMetrics']]
    """

    kwargs = _get_kwargs(
        validator_name=validator_name,
        request_id=request_id,
        validator_instance_id=validator_instance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    validator_name: str,
    request_id: str,
    validator_instance_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["ValidatorRunMetrics"]]:
    """Returns an arary of ValidatorRunMetrics for a given request.

    Args:
        validator_name (str):
        request_id (str):
        validator_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ValidatorRunMetrics']
    """

    return sync_detailed(
        validator_name=validator_name,
        request_id=request_id,
        validator_instance_id=validator_instance_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    validator_name: str,
    request_id: str,
    validator_instance_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["ValidatorRunMetrics"]]:
    """Returns an arary of ValidatorRunMetrics for a given request.

    Args:
        validator_name (str):
        request_id (str):
        validator_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ValidatorRunMetrics']]
    """

    kwargs = _get_kwargs(
        validator_name=validator_name,
        request_id=request_id,
        validator_instance_id=validator_instance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    validator_name: str,
    request_id: str,
    validator_instance_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["ValidatorRunMetrics"]]:
    """Returns an arary of ValidatorRunMetrics for a given request.

    Args:
        validator_name (str):
        request_id (str):
        validator_instance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ValidatorRunMetrics']
    """

    return (
        await asyncio_detailed(
            validator_name=validator_name,
            request_id=request_id,
            validator_instance_id=validator_instance_id,
            client=client,
        )
    ).parsed
