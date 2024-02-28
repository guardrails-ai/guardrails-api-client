from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_fail_options import OnFailOptions

if TYPE_CHECKING:
    from ..models.validator_run_metric_details_parameters import ValidatorRunMetricDetailsParameters


T = TypeVar("T", bound="ValidatorRunMetricDetails")


@_attrs_define
class ValidatorRunMetricDetails:
    """
    Attributes:
        step_number (int):
        result_type (str):
        fail_action (OnFailOptions):
        parameters (ValidatorRunMetricDetailsParameters):
    """

    step_number: int
    result_type: str
    fail_action: OnFailOptions
    parameters: "ValidatorRunMetricDetailsParameters"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step_number = self.step_number

        result_type = self.result_type

        fail_action = self.fail_action.value

        parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stepNumber": step_number,
                "resultType": result_type,
                "failAction": fail_action,
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validator_run_metric_details_parameters import ValidatorRunMetricDetailsParameters

        d = src_dict.copy()
        step_number = d.pop("stepNumber")

        result_type = d.pop("resultType")

        fail_action = OnFailOptions(d.pop("failAction"))

        parameters = ValidatorRunMetricDetailsParameters.from_dict(d.pop("parameters"))

        validator_run_metric_details = cls(
            step_number=step_number,
            result_type=result_type,
            fail_action=fail_action,
            parameters=parameters,
        )

        validator_run_metric_details.additional_properties = d
        return validator_run_metric_details

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
