from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_object import AnyObject
    from ..models.history import History


T = TypeVar("T", bound="ValidationOutput")


@_attrs_define
class ValidationOutput:
    """
    Attributes:
        result (bool): Whether the validation passed or failed
        validated_output (Union['AnyObject', Unset, str]):
        session_history (Union[Unset, List['History']]):
        raw_llm_response (Union[Unset, str]):
    """

    result: bool
    validated_output: Union["AnyObject", Unset, str] = UNSET
    session_history: Union[Unset, List["History"]] = UNSET
    raw_llm_response: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_object import AnyObject

        result = self.result

        validated_output: Union[Dict[str, Any], Unset, str]
        if isinstance(self.validated_output, Unset):
            validated_output = UNSET
        elif isinstance(self.validated_output, AnyObject):
            validated_output = self.validated_output.to_dict()
        else:
            validated_output = self.validated_output

        session_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.session_history, Unset):
            session_history = []
            for session_history_item_data in self.session_history:
                session_history_item = session_history_item_data.to_dict()
                session_history.append(session_history_item)

        raw_llm_response = self.raw_llm_response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
            }
        )
        if validated_output is not UNSET:
            field_dict["validatedOutput"] = validated_output
        if session_history is not UNSET:
            field_dict["sessionHistory"] = session_history
        if raw_llm_response is not UNSET:
            field_dict["rawLlmResponse"] = raw_llm_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_object import AnyObject
        from ..models.history import History

        d = src_dict.copy()
        result = d.pop("result")

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

        session_history = []
        _session_history = d.pop("sessionHistory", UNSET)
        for session_history_item_data in _session_history or []:
            session_history_item = History.from_dict(session_history_item_data)

            session_history.append(session_history_item)

        raw_llm_response = d.pop("rawLlmResponse", UNSET)

        validation_output = cls(
            result=result,
            validated_output=validated_output,
            session_history=session_history,
            raw_llm_response=raw_llm_response,
        )

        validation_output.additional_properties = d
        return validation_output

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
