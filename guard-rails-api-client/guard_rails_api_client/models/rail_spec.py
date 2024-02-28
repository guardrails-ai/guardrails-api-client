from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rail_spec_version import RailSpecVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema import Schema


T = TypeVar("T", bound="RailSpec")


@_attrs_define
class RailSpec:
    """A JSONified version of the user provided railspec.

    Attributes:
        output_schema (Schema):
        prompt (str):
        version (RailSpecVersion):  Default: RailSpecVersion.VALUE_0.
        input_schema (Union[Unset, Schema]):
        instructions (Union[Unset, str]):
    """

    output_schema: "Schema"
    prompt: str
    version: RailSpecVersion = RailSpecVersion.VALUE_0
    input_schema: Union[Unset, "Schema"] = UNSET
    instructions: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        output_schema = self.output_schema.to_dict()

        prompt = self.prompt

        version = self.version.value

        input_schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.input_schema, Unset):
            input_schema = self.input_schema.to_dict()

        instructions = self.instructions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outputSchema": output_schema,
                "prompt": prompt,
                "version": version,
            }
        )
        if input_schema is not UNSET:
            field_dict["inputSchema"] = input_schema
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema import Schema

        d = src_dict.copy()
        output_schema = Schema.from_dict(d.pop("outputSchema"))

        prompt = d.pop("prompt")

        version = RailSpecVersion(d.pop("version"))

        _input_schema = d.pop("inputSchema", UNSET)
        input_schema: Union[Unset, Schema]
        if isinstance(_input_schema, Unset):
            input_schema = UNSET
        else:
            input_schema = Schema.from_dict(_input_schema)

        instructions = d.pop("instructions", UNSET)

        rail_spec = cls(
            output_schema=output_schema,
            prompt=prompt,
            version=version,
            input_schema=input_schema,
            instructions=instructions,
        )

        rail_spec.additional_properties = d
        return rail_spec

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
