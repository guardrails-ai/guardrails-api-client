import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.on_fail_options import OnFailOptions
from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validator_run_metric_details_parameters import ValidatorRunMetricDetailsParameters


T = TypeVar("T", bound="ValidatorRunMetrics")


@_attrs_define
class ValidatorRunMetrics:
    """
    Attributes:
        instance_id (str):
        name (str):
        request_id (str):
        guard_name (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        duration_in_millis (float):
        input_ (str):
        output (str):
        status (Status):
        step_number (int):
        result_type (str):
        fail_action (OnFailOptions):
        parameters (ValidatorRunMetricDetailsParameters):
        tokens (Union[Unset, float]): The number of tokens consumed if the validator calls an LLM. Only applies to
            validators that call LLMs.
    """

    instance_id: str
    name: str
    request_id: str
    guard_name: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    duration_in_millis: float
    input_: str
    output: str
    status: Status
    step_number: int
    result_type: str
    fail_action: OnFailOptions
    parameters: "ValidatorRunMetricDetailsParameters"
    tokens: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instance_id = self.instance_id

        name = self.name

        request_id = self.request_id

        guard_name = self.guard_name

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        duration_in_millis = self.duration_in_millis

        input_ = self.input_

        output = self.output

        status = self.status.value

        step_number = self.step_number

        result_type = self.result_type

        fail_action = self.fail_action.value

        parameters = self.parameters.to_dict()

        tokens = self.tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instanceId": instance_id,
                "name": name,
                "requestId": request_id,
                "guardName": guard_name,
                "startTime": start_time,
                "endTime": end_time,
                "durationInMillis": duration_in_millis,
                "input": input_,
                "output": output,
                "status": status,
                "stepNumber": step_number,
                "resultType": result_type,
                "failAction": fail_action,
                "parameters": parameters,
            }
        )
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validator_run_metric_details_parameters import ValidatorRunMetricDetailsParameters

        d = src_dict.copy()
        instance_id = d.pop("instanceId")

        name = d.pop("name")

        request_id = d.pop("requestId")

        guard_name = d.pop("guardName")

        start_time = isoparse(d.pop("startTime"))

        end_time = isoparse(d.pop("endTime"))

        duration_in_millis = d.pop("durationInMillis")

        input_ = d.pop("input")

        output = d.pop("output")

        status = Status(d.pop("status"))

        step_number = d.pop("stepNumber")

        result_type = d.pop("resultType")

        fail_action = OnFailOptions(d.pop("failAction"))

        parameters = ValidatorRunMetricDetailsParameters.from_dict(d.pop("parameters"))

        tokens = d.pop("tokens", UNSET)

        validator_run_metrics = cls(
            instance_id=instance_id,
            name=name,
            request_id=request_id,
            guard_name=guard_name,
            start_time=start_time,
            end_time=end_time,
            duration_in_millis=duration_in_millis,
            input_=input_,
            output=output,
            status=status,
            step_number=step_number,
            result_type=result_type,
            fail_action=fail_action,
            parameters=parameters,
            tokens=tokens,
        )

        validator_run_metrics.additional_properties = d
        return validator_run_metrics

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
