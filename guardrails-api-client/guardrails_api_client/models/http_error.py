from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_error_fields import HttpErrorFields


T = TypeVar("T", bound="HttpError")


@_attrs_define
class HttpError:
    """
    Attributes:
        status (int): A valid http status code
        message (str): A message explaining the status
        cause (Union[Unset, str]): Used to describe the origin of an error if that original error has meaning to the
            client.  This field should add specificity to 'message'.
        fields (Union[Unset, HttpErrorFields]): Used to identify specific fields in a JSON body that caused the error.
            Typically only used for 4xx type responses.  The key should be the json path to the invalid property and the
            value should be a list of error messages specific to that property.
        context (Union[Unset, str]): Used to identify what part of the request caused the error for non-JSON payloads.
    """

    status: int
    message: str
    cause: Union[Unset, str] = UNSET
    fields: Union[Unset, "HttpErrorFields"] = UNSET
    context: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        message = self.message

        cause = self.cause

        fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        context = self.context

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "message": message,
            }
        )
        if cause is not UNSET:
            field_dict["cause"] = cause
        if fields is not UNSET:
            field_dict["fields"] = fields
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_error_fields import HttpErrorFields

        d = src_dict.copy()
        status = d.pop("status")

        message = d.pop("message")

        cause = d.pop("cause", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, HttpErrorFields]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = HttpErrorFields.from_dict(_fields)

        context = d.pop("context", UNSET)

        http_error = cls(
            status=status,
            message=message,
            cause=cause,
            fields=fields,
            context=context,
        )

        http_error.additional_properties = d
        return http_error

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
