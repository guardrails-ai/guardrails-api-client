from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ingestion import Ingestion
from ...models.ingestion_payload import IngestionPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    document_id: str,
    *,
    body: IngestionPayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_openai_api_key, Unset):
        headers["x-openai-api-key"] = x_openai_api_key

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/embeddings/{document_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["Ingestion"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Ingestion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["Ingestion"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IngestionPayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Response[List["Ingestion"]]:
    """Updates embeddings for a given documentId

    Args:
        document_id (str):
        x_openai_api_key (Union[Unset, str]):
        body (IngestionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Ingestion']]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        body=body,
        x_openai_api_key=x_openai_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IngestionPayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Optional[List["Ingestion"]]:
    """Updates embeddings for a given documentId

    Args:
        document_id (str):
        x_openai_api_key (Union[Unset, str]):
        body (IngestionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Ingestion']
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
        body=body,
        x_openai_api_key=x_openai_api_key,
    ).parsed


async def asyncio_detailed(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IngestionPayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Response[List["Ingestion"]]:
    """Updates embeddings for a given documentId

    Args:
        document_id (str):
        x_openai_api_key (Union[Unset, str]):
        body (IngestionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Ingestion']]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        body=body,
        x_openai_api_key=x_openai_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IngestionPayload,
    x_openai_api_key: Union[Unset, str] = UNSET,
) -> Optional[List["Ingestion"]]:
    """Updates embeddings for a given documentId

    Args:
        document_id (str):
        x_openai_api_key (Union[Unset, str]):
        body (IngestionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Ingestion']
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
            body=body,
            x_openai_api_key=x_openai_api_key,
        )
    ).parsed
