from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.on_fail import OnFail


T = TypeVar("T", bound="SchemaElement")


@_attrs_define
class SchemaElement:
    """
    Attributes:
        type (str):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        strict (Union[Unset, bool]):
        date_format (Union[Unset, str]):
        time_format (Union[Unset, str]):
        on_fail (Union[Unset, str]):
        on_fails (Union[Unset, List['OnFail']]):
        model (Union[Unset, str]):
    """

    type: str
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    strict: Union[Unset, bool] = UNSET
    date_format: Union[Unset, str] = UNSET
    time_format: Union[Unset, str] = UNSET
    on_fail: Union[Unset, str] = UNSET
    on_fails: Union[Unset, List["OnFail"]] = UNSET
    model: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        name = self.name

        description = self.description

        strict = self.strict

        date_format = self.date_format

        time_format = self.time_format

        on_fail = self.on_fail

        on_fails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.on_fails, Unset):
            on_fails = []
            for on_fails_item_data in self.on_fails:
                on_fails_item = on_fails_item_data.to_dict()
                on_fails.append(on_fails_item)

        model = self.model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if strict is not UNSET:
            field_dict["strict"] = strict
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if time_format is not UNSET:
            field_dict["timeFormat"] = time_format
        if on_fail is not UNSET:
            field_dict["onFail"] = on_fail
        if on_fails is not UNSET:
            field_dict["onFails"] = on_fails
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.on_fail import OnFail

        d = src_dict.copy()
        type = d.pop("type")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        strict = d.pop("strict", UNSET)

        date_format = d.pop("dateFormat", UNSET)

        time_format = d.pop("timeFormat", UNSET)

        on_fail = d.pop("onFail", UNSET)

        on_fails = []
        _on_fails = d.pop("onFails", UNSET)
        for on_fails_item_data in _on_fails or []:
            on_fails_item = OnFail.from_dict(on_fails_item_data)

            on_fails.append(on_fails_item)

        model = d.pop("model", UNSET)

        schema_element = cls(
            type=type,
            name=name,
            description=description,
            strict=strict,
            date_format=date_format,
            time_format=time_format,
            on_fail=on_fail,
            on_fails=on_fails,
            model=model,
        )

        schema_element.additional_properties = d
        return schema_element

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
