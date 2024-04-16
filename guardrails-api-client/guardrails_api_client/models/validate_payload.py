from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_payload_llm_api import ValidatePayloadLlmApi
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validate_payload_prompt_params import ValidatePayloadPromptParams


T = TypeVar("T", bound="ValidatePayload")


@_attrs_define
class ValidatePayload:
    """
    Attributes:
        llm_output (Union[Unset, str]): The LLM output as a string or the input prompts for the LLM Example: stubbed llm
            output.
        num_reasks (Union[Unset, int]): An override for the number of re-asks to perform
        prompt_params (Union[Unset, ValidatePayloadPromptParams]): additional params for llm prompts
        llm_api (Union[Unset, ValidatePayloadLlmApi]):
    """

    llm_output: Union[Unset, str] = UNSET
    num_reasks: Union[Unset, int] = UNSET
    prompt_params: Union[Unset, "ValidatePayloadPromptParams"] = UNSET
    llm_api: Union[Unset, ValidatePayloadLlmApi] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        llm_output = self.llm_output

        num_reasks = self.num_reasks

        prompt_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prompt_params, Unset):
            prompt_params = self.prompt_params.to_dict()

        llm_api: Union[Unset, str] = UNSET
        if not isinstance(self.llm_api, Unset):
            llm_api = self.llm_api.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if llm_output is not UNSET:
            field_dict["llmOutput"] = llm_output
        if num_reasks is not UNSET:
            field_dict["numReasks"] = num_reasks
        if prompt_params is not UNSET:
            field_dict["promptParams"] = prompt_params
        if llm_api is not UNSET:
            field_dict["llmApi"] = llm_api

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validate_payload_prompt_params import ValidatePayloadPromptParams

        d = src_dict.copy()
        llm_output = d.pop("llmOutput", UNSET)

        num_reasks = d.pop("numReasks", UNSET)

        _prompt_params = d.pop("promptParams", UNSET)
        prompt_params: Union[Unset, ValidatePayloadPromptParams]
        if isinstance(_prompt_params, Unset):
            prompt_params = UNSET
        else:
            prompt_params = ValidatePayloadPromptParams.from_dict(_prompt_params)

        _llm_api = d.pop("llmApi", UNSET)
        llm_api: Union[Unset, ValidatePayloadLlmApi]
        if isinstance(_llm_api, Unset):
            llm_api = UNSET
        else:
            llm_api = ValidatePayloadLlmApi(_llm_api)

        validate_payload = cls(
            llm_output=llm_output,
            num_reasks=num_reasks,
            prompt_params=prompt_params,
            llm_api=llm_api,
        )

        validate_payload.additional_properties = d
        return validate_payload

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
