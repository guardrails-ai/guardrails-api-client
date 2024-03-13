from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="IngestionPayload")


@_attrs_define
class IngestionPayload:
    """
    Attributes:
        articles (Union[Unset, Document]):
        guard_id (Union[Unset, str]):
        validator_id (Union[Unset, str]):
        chunk_id (Union[Unset, str]):
    """

    articles: Union[Unset, "Document"] = UNSET
    guard_id: Union[Unset, str] = UNSET
    validator_id: Union[Unset, str] = UNSET
    chunk_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        articles: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.articles, Unset):
            articles = self.articles.to_dict()

        guard_id = self.guard_id

        validator_id = self.validator_id

        chunk_id = self.chunk_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if articles is not UNSET:
            field_dict["articles"] = articles
        if guard_id is not UNSET:
            field_dict["guardId"] = guard_id
        if validator_id is not UNSET:
            field_dict["validatorId"] = validator_id
        if chunk_id is not UNSET:
            field_dict["chunkId"] = chunk_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document import Document

        d = src_dict.copy()
        _articles = d.pop("articles", UNSET)
        articles: Union[Unset, Document]
        if isinstance(_articles, Unset):
            articles = UNSET
        else:
            articles = Document.from_dict(_articles)

        guard_id = d.pop("guardId", UNSET)

        validator_id = d.pop("validatorId", UNSET)

        chunk_id = d.pop("chunkId", UNSET)

        ingestion_payload = cls(
            articles=articles,
            guard_id=guard_id,
            validator_id=validator_id,
            chunk_id=chunk_id,
        )

        ingestion_payload.additional_properties = d
        return ingestion_payload

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
