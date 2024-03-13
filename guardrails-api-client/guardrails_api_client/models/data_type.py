from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_type_children import DataTypeChildren
    from ..models.schema_element import SchemaElement


T = TypeVar("T", bound="DataType")


@_attrs_define
class DataType:
    """
    Attributes:
        element (SchemaElement):
        children (Union[Unset, DataTypeChildren]):
        formatters (Union[Unset, List[str]]):
        plugins (Union[Unset, List[str]]):
    """

    element: "SchemaElement"
    children: Union[Unset, "DataTypeChildren"] = UNSET
    formatters: Union[Unset, List[str]] = UNSET
    plugins: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        element = self.element.to_dict()

        children: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

        formatters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.formatters, Unset):
            formatters = self.formatters

        plugins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.plugins, Unset):
            plugins = self.plugins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "element": element,
            }
        )
        if children is not UNSET:
            field_dict["children"] = children
        if formatters is not UNSET:
            field_dict["formatters"] = formatters
        if plugins is not UNSET:
            field_dict["plugins"] = plugins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_type_children import DataTypeChildren
        from ..models.schema_element import SchemaElement

        d = src_dict.copy()
        element = SchemaElement.from_dict(d.pop("element"))

        _children = d.pop("children", UNSET)
        children: Union[Unset, DataTypeChildren]
        if isinstance(_children, Unset):
            children = UNSET
        else:
            children = DataTypeChildren.from_dict(_children)

        formatters = cast(List[str], d.pop("formatters", UNSET))

        plugins = cast(List[str], d.pop("plugins", UNSET))

        data_type = cls(
            element=element,
            children=children,
            formatters=formatters,
            plugins=plugins,
        )

        data_type.additional_properties = d
        return data_type

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
