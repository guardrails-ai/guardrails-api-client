from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.guard_guard_config import GuardGuardConfig
    from ..models.rail_spec import RailSpec


T = TypeVar("T", bound="Guard")


@_attrs_define
class Guard:
    """
    Attributes:
        name (str): A unique name for this guard.
        railspec (RailSpec): A JSONified version of the user provided railspec.
        description (Union[Unset, str]): A description of this guard.
        num_reasks (Union[Unset, int]): The number of re-asks to perform during validation when a validation fails.
        guard_config (Union[Unset, GuardGuardConfig]): Addtional guard configuration attributes.
        llm_endpoint (Union[Unset, str]): The endpoint for the targetted LLM.
    """

    name: str
    railspec: "RailSpec"
    description: Union[Unset, str] = UNSET
    num_reasks: Union[Unset, int] = UNSET
    guard_config: Union[Unset, "GuardGuardConfig"] = UNSET
    llm_endpoint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        railspec = self.railspec.to_dict()

        description = self.description

        num_reasks = self.num_reasks

        guard_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guard_config, Unset):
            guard_config = self.guard_config.to_dict()

        llm_endpoint = self.llm_endpoint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "railspec": railspec,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if num_reasks is not UNSET:
            field_dict["numReasks"] = num_reasks
        if guard_config is not UNSET:
            field_dict["guardConfig"] = guard_config
        if llm_endpoint is not UNSET:
            field_dict["llmEndpoint"] = llm_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.guard_guard_config import GuardGuardConfig
        from ..models.rail_spec import RailSpec

        d = src_dict.copy()
        name = d.pop("name")

        railspec = RailSpec.from_dict(d.pop("railspec"))

        description = d.pop("description", UNSET)

        num_reasks = d.pop("numReasks", UNSET)

        _guard_config = d.pop("guardConfig", UNSET)
        guard_config: Union[Unset, GuardGuardConfig]
        if isinstance(_guard_config, Unset):
            guard_config = UNSET
        else:
            guard_config = GuardGuardConfig.from_dict(_guard_config)

        llm_endpoint = d.pop("llmEndpoint", UNSET)

        guard = cls(
            name=name,
            railspec=railspec,
            description=description,
            num_reasks=num_reasks,
            guard_config=guard_config,
            llm_endpoint=llm_endpoint,
        )

        guard.additional_properties = d
        return guard

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
