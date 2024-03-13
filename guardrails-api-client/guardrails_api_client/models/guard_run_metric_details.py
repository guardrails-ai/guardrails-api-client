from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.guard_run_step import GuardRunStep


T = TypeVar("T", bound="GuardRunMetricDetails")


@_attrs_define
class GuardRunMetricDetails:
    """
    Attributes:
        steps (List['GuardRunStep']):
        prompt (Union[Unset, str]):
        instructions (Union[Unset, str]):
    """

    steps: List["GuardRunStep"]
    prompt: Union[Unset, str] = UNSET
    instructions: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        prompt = self.prompt

        instructions = self.instructions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
            }
        )
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.guard_run_step import GuardRunStep

        d = src_dict.copy()
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = GuardRunStep.from_dict(steps_item_data)

            steps.append(steps_item)

        prompt = d.pop("prompt", UNSET)

        instructions = d.pop("instructions", UNSET)

        guard_run_metric_details = cls(
            steps=steps,
            prompt=prompt,
            instructions=instructions,
        )

        guard_run_metric_details.additional_properties = d
        return guard_run_metric_details

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
