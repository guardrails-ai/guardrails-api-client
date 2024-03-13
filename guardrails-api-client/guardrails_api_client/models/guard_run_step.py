from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.validator_metrics import ValidatorMetrics


T = TypeVar("T", bound="GuardRunStep")


@_attrs_define
class GuardRunStep:
    """
    Attributes:
        step_number (float):
        validator_metrics (List['ValidatorMetrics']):
    """

    step_number: float
    validator_metrics: List["ValidatorMetrics"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step_number = self.step_number

        validator_metrics = []
        for validator_metrics_item_data in self.validator_metrics:
            validator_metrics_item = validator_metrics_item_data.to_dict()
            validator_metrics.append(validator_metrics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stepNumber": step_number,
                "validatorMetrics": validator_metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validator_metrics import ValidatorMetrics

        d = src_dict.copy()
        step_number = d.pop("stepNumber")

        validator_metrics = []
        _validator_metrics = d.pop("validatorMetrics")
        for validator_metrics_item_data in _validator_metrics:
            validator_metrics_item = ValidatorMetrics.from_dict(validator_metrics_item_data)

            validator_metrics.append(validator_metrics_item)

        guard_run_step = cls(
            step_number=step_number,
            validator_metrics=validator_metrics,
        )

        guard_run_step.additional_properties = d
        return guard_run_step

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
