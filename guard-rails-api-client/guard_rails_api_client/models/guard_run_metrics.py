import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.guard_run_step import GuardRunStep


T = TypeVar("T", bound="GuardRunMetrics")


@_attrs_define
class GuardRunMetrics:
    """
    Attributes:
        request_id (str): The id of the request this metric entry is for (i.e. the specific call to
            /guards/{guardName}/validate)
        guard_name (str): The name of the Guard
        timestamp (datetime.datetime): The start time of the span the metrics were captured within (ISO 8601 format; See
            https://www.rfc-editor.org/rfc/rfc3339#section-5.6)
        run_duration (float): The total span duration of the guard run in seconds
        status (Status):
        reasks (float): The number of times the LLM was reasked
        tokens (float): The number of tokens used
        raw_llm_ouput (str): The unaltered output from the LLM
        validated_output (str): The potentially altered output from validation
        steps (List['GuardRunStep']):
        prompt (Union[Unset, str]):
        instructions (Union[Unset, str]):
    """

    request_id: str
    guard_name: str
    timestamp: datetime.datetime
    run_duration: float
    status: Status
    reasks: float
    tokens: float
    raw_llm_ouput: str
    validated_output: str
    steps: List["GuardRunStep"]
    prompt: Union[Unset, str] = UNSET
    instructions: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id

        guard_name = self.guard_name

        timestamp = self.timestamp.isoformat()

        run_duration = self.run_duration

        status = self.status.value

        reasks = self.reasks

        tokens = self.tokens

        raw_llm_ouput = self.raw_llm_ouput

        validated_output = self.validated_output

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
                "requestId": request_id,
                "guardName": guard_name,
                "timestamp": timestamp,
                "runDuration": run_duration,
                "status": status,
                "reasks": reasks,
                "tokens": tokens,
                "rawLlmOuput": raw_llm_ouput,
                "validatedOutput": validated_output,
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
        request_id = d.pop("requestId")

        guard_name = d.pop("guardName")

        timestamp = isoparse(d.pop("timestamp"))

        run_duration = d.pop("runDuration")

        status = Status(d.pop("status"))

        reasks = d.pop("reasks")

        tokens = d.pop("tokens")

        raw_llm_ouput = d.pop("rawLlmOuput")

        validated_output = d.pop("validatedOutput")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = GuardRunStep.from_dict(steps_item_data)

            steps.append(steps_item)

        prompt = d.pop("prompt", UNSET)

        instructions = d.pop("instructions", UNSET)

        guard_run_metrics = cls(
            request_id=request_id,
            guard_name=guard_name,
            timestamp=timestamp,
            run_duration=run_duration,
            status=status,
            reasks=reasks,
            tokens=tokens,
            raw_llm_ouput=raw_llm_ouput,
            validated_output=validated_output,
            steps=steps,
            prompt=prompt,
            instructions=instructions,
        )

        guard_run_metrics.additional_properties = d
        return guard_run_metrics

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
