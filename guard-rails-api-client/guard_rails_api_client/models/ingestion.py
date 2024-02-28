from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingestion_metadata import IngestionMetadata


T = TypeVar("T", bound="Ingestion")


@_attrs_define
class Ingestion:
    """
    Attributes:
        id (Union[Unset, str]):
        guard_id (Union[Unset, str]):
        embeddings (Union[Unset, List[List[float]]]):
        document_id (Union[Unset, str]):
        metadata (Union[Unset, IngestionMetadata]):
        validator_id (Union[Unset, str]):
        page_id (Union[Unset, str]):
        chunk_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    guard_id: Union[Unset, str] = UNSET
    embeddings: Union[Unset, List[List[float]]] = UNSET
    document_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, "IngestionMetadata"] = UNSET
    validator_id: Union[Unset, str] = UNSET
    page_id: Union[Unset, str] = UNSET
    chunk_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        guard_id = self.guard_id

        embeddings: Union[Unset, List[List[float]]] = UNSET
        if not isinstance(self.embeddings, Unset):
            embeddings = []
            for embeddings_item_data in self.embeddings:
                embeddings_item = embeddings_item_data

                embeddings.append(embeddings_item)

        document_id = self.document_id

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        validator_id = self.validator_id

        page_id = self.page_id

        chunk_id = self.chunk_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if guard_id is not UNSET:
            field_dict["guardId"] = guard_id
        if embeddings is not UNSET:
            field_dict["embeddings"] = embeddings
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if validator_id is not UNSET:
            field_dict["validatorId"] = validator_id
        if page_id is not UNSET:
            field_dict["pageId"] = page_id
        if chunk_id is not UNSET:
            field_dict["chunkId"] = chunk_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ingestion_metadata import IngestionMetadata

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        guard_id = d.pop("guardId", UNSET)

        embeddings = []
        _embeddings = d.pop("embeddings", UNSET)
        for embeddings_item_data in _embeddings or []:
            embeddings_item = cast(List[float], embeddings_item_data)

            embeddings.append(embeddings_item)

        document_id = d.pop("documentId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, IngestionMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = IngestionMetadata.from_dict(_metadata)

        validator_id = d.pop("validatorId", UNSET)

        page_id = d.pop("pageId", UNSET)

        chunk_id = d.pop("chunkId", UNSET)

        ingestion = cls(
            id=id,
            guard_id=guard_id,
            embeddings=embeddings,
            document_id=document_id,
            metadata=metadata,
            validator_id=validator_id,
            page_id=page_id,
            chunk_id=chunk_id,
        )

        ingestion.additional_properties = d
        return ingestion

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
