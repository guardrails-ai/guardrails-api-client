from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Projection")


@_attrs_define
class Projection:
    """
    Attributes:
        id (Union[Unset, str]):
        guard_id (Union[Unset, str]):
        validator_id (Union[Unset, str]):
        document_id (Union[Unset, str]):
        page_id (Union[Unset, str]):
        chunk_id (Union[Unset, str]):
        projection (Union[Unset, List[float]]):
    """

    id: Union[Unset, str] = UNSET
    guard_id: Union[Unset, str] = UNSET
    validator_id: Union[Unset, str] = UNSET
    document_id: Union[Unset, str] = UNSET
    page_id: Union[Unset, str] = UNSET
    chunk_id: Union[Unset, str] = UNSET
    projection: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        guard_id = self.guard_id

        validator_id = self.validator_id

        document_id = self.document_id

        page_id = self.page_id

        chunk_id = self.chunk_id

        projection: Union[Unset, List[float]] = UNSET
        if not isinstance(self.projection, Unset):
            projection = self.projection

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if guard_id is not UNSET:
            field_dict["guardId"] = guard_id
        if validator_id is not UNSET:
            field_dict["validatorId"] = validator_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if page_id is not UNSET:
            field_dict["pageId"] = page_id
        if chunk_id is not UNSET:
            field_dict["chunkId"] = chunk_id
        if projection is not UNSET:
            field_dict["projection"] = projection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        guard_id = d.pop("guardId", UNSET)

        validator_id = d.pop("validatorId", UNSET)

        document_id = d.pop("documentId", UNSET)

        page_id = d.pop("pageId", UNSET)

        chunk_id = d.pop("chunkId", UNSET)

        projection = cast(List[float], d.pop("projection", UNSET))

        projection = cls(
            id=id,
            guard_id=guard_id,
            validator_id=validator_id,
            document_id=document_id,
            page_id=page_id,
            chunk_id=chunk_id,
            projection=projection,
        )

        projection.additional_properties = d
        return projection

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
