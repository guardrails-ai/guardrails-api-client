from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_metadata import DocumentMetadata
    from ..models.document_pages import DocumentPages


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """
    Attributes:
        id (Union[Unset, str]):
        pages (Union[Unset, DocumentPages]):
        metadata (Union[Unset, DocumentMetadata]):
    """

    id: Union[Unset, str] = UNSET
    pages: Union[Unset, "DocumentPages"] = UNSET
    metadata: Union[Unset, "DocumentMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        pages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pages, Unset):
            pages = self.pages.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if pages is not UNSET:
            field_dict["pages"] = pages
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_metadata import DocumentMetadata
        from ..models.document_pages import DocumentPages

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _pages = d.pop("pages", UNSET)
        pages: Union[Unset, DocumentPages]
        if isinstance(_pages, Unset):
            pages = UNSET
        else:
            pages = DocumentPages.from_dict(_pages)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, DocumentMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DocumentMetadata.from_dict(_metadata)

        document = cls(
            id=id,
            pages=pages,
            metadata=metadata,
        )

        document.additional_properties = d
        return document

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
