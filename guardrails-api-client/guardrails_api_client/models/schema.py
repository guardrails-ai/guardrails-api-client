from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_type import DataType
    from ..models.json_schema import JsonSchema


T = TypeVar("T", bound="Schema")


@_attrs_define
class Schema:
    """
    Attributes:
        schema (Union['DataType', 'JsonSchema']):
    """

    schema: Union["DataType", "JsonSchema"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.json_schema import JsonSchema

        schema: Dict[str, Any]
        if isinstance(self.schema, JsonSchema):
            schema = self.schema.to_dict()
        else:
            schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema": schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_type import DataType
        from ..models.json_schema import JsonSchema

        d = src_dict.copy()

        def _parse_schema(data: object) -> Union["DataType", "JsonSchema"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = JsonSchema.from_dict(data)

                return schema_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            schema_type_1 = DataType.from_dict(data)

            return schema_type_1

        schema = _parse_schema(d.pop("schema"))

        schema = cls(
            schema=schema,
        )

        schema.additional_properties = d
        return schema

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
