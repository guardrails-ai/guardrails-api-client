import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validator_metrics import ValidatorMetrics
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/validators/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ValidatorMetrics"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ValidatorMetrics.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ValidatorMetrics"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 0,
) -> Response[List["ValidatorMetrics"]]:
    """Returns an array of ValidatorMetrics for a given time range.  If startTime or endTime are ommitted,
    a five minute duration is used by default.  Default page size is 10, but this page size applied to
    guard steps not validator metrics. Have to think this one out a little more.

    Args:
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ValidatorMetrics']]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 0,
) -> Optional[List["ValidatorMetrics"]]:
    """Returns an array of ValidatorMetrics for a given time range.  If startTime or endTime are ommitted,
    a five minute duration is used by default.  Default page size is 10, but this page size applied to
    guard steps not validator metrics. Have to think this one out a little more.

    Args:
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ValidatorMetrics']
    """

    return sync_detailed(
        client=client,
        start_time=start_time,
        end_time=end_time,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 0,
) -> Response[List["ValidatorMetrics"]]:
    """Returns an array of ValidatorMetrics for a given time range.  If startTime or endTime are ommitted,
    a five minute duration is used by default.  Default page size is 10, but this page size applied to
    guard steps not validator metrics. Have to think this one out a little more.

    Args:
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ValidatorMetrics']]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 0,
) -> Optional[List["ValidatorMetrics"]]:
    """Returns an array of ValidatorMetrics for a given time range.  If startTime or endTime are ommitted,
    a five minute duration is used by default.  Default page size is 10, but this page size applied to
    guard steps not validator metrics. Have to think this one out a little more.

    Args:
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ValidatorMetrics']
    """

    return (
        await asyncio_detailed(
            client=client,
            start_time=start_time,
            end_time=end_time,
            page=page,
        )
    ).parsed
