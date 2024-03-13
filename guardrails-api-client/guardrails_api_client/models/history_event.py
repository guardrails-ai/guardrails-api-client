from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_object import AnyObject
    from ..models.history_event_prompt import HistoryEventPrompt
    from ..models.history_event_reasks_item import HistoryEventReasksItem


T = TypeVar("T", bound="HistoryEvent")


@_attrs_define
class HistoryEvent:
    """
    Attributes:
        instructions (Union[Unset, str]):
        output (Union[Unset, str]):
        parsed_output (Union['AnyObject', Unset, str]):
        prompt (Union[Unset, HistoryEventPrompt]):
        reasks (Union[Unset, List['HistoryEventReasksItem']]):
        validated_output (Union['AnyObject', Unset, str]):
    """

    instructions: Union[Unset, str] = UNSET
    output: Union[Unset, str] = UNSET
    parsed_output: Union["AnyObject", Unset, str] = UNSET
    prompt: Union[Unset, "HistoryEventPrompt"] = UNSET
    reasks: Union[Unset, List["HistoryEventReasksItem"]] = UNSET
    validated_output: Union["AnyObject", Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_object import AnyObject

        instructions = self.instructions

        output = self.output

        parsed_output: Union[Dict[str, Any], Unset, str]
        if isinstance(self.parsed_output, Unset):
            parsed_output = UNSET
        elif isinstance(self.parsed_output, AnyObject):
            parsed_output = self.parsed_output.to_dict()
        else:
            parsed_output = self.parsed_output

        prompt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prompt, Unset):
            prompt = self.prompt.to_dict()

        reasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reasks, Unset):
            reasks = []
            for reasks_item_data in self.reasks:
                reasks_item = reasks_item_data.to_dict()
                reasks.append(reasks_item)

        validated_output: Union[Dict[str, Any], Unset, str]
        if isinstance(self.validated_output, Unset):
            validated_output = UNSET
        elif isinstance(self.validated_output, AnyObject):
            validated_output = self.validated_output.to_dict()
        else:
            validated_output = self.validated_output

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if output is not UNSET:
            field_dict["output"] = output
        if parsed_output is not UNSET:
            field_dict["parsedOutput"] = parsed_output
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if reasks is not UNSET:
            field_dict["reasks"] = reasks
        if validated_output is not UNSET:
            field_dict["validatedOutput"] = validated_output

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_object import AnyObject
        from ..models.history_event_prompt import HistoryEventPrompt
        from ..models.history_event_reasks_item import HistoryEventReasksItem

        d = src_dict.copy()
        instructions = d.pop("instructions", UNSET)

        output = d.pop("output", UNSET)

        def _parse_parsed_output(data: object) -> Union["AnyObject", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parsed_output_type_0 = AnyObject.from_dict(data)

                return parsed_output_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AnyObject", Unset, str], data)

        parsed_output = _parse_parsed_output(d.pop("parsedOutput", UNSET))

        _prompt = d.pop("prompt", UNSET)
        prompt: Union[Unset, HistoryEventPrompt]
        if isinstance(_prompt, Unset):
            prompt = UNSET
        else:
            prompt = HistoryEventPrompt.from_dict(_prompt)

        reasks = []
        _reasks = d.pop("reasks", UNSET)
        for reasks_item_data in _reasks or []:
            reasks_item = HistoryEventReasksItem.from_dict(reasks_item_data)

            reasks.append(reasks_item)

        def _parse_validated_output(data: object) -> Union["AnyObject", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                validated_output_type_0 = AnyObject.from_dict(data)

                return validated_output_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AnyObject", Unset, str], data)

        validated_output = _parse_validated_output(d.pop("validatedOutput", UNSET))

        history_event = cls(
            instructions=instructions,
            output=output,
            parsed_output=parsed_output,
            prompt=prompt,
            reasks=reasks,
            validated_output=validated_output,
        )

        history_event.additional_properties = d
        return history_event

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
