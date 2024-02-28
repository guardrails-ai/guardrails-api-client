from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_object import AnyObject


T = TypeVar("T", bound="Reask")


@_attrs_define
class Reask:
    """
    Attributes:
        incorrect_value (Union['AnyObject', List[Union['AnyObject', List[Union['AnyObject', bool, float, int, str]],
            bool, float, int, str]], Unset, bool, float, int, str]):
        error_message (Union[Unset, str]):
        fix_value (Union['AnyObject', List[Union['AnyObject', List[Union['AnyObject', bool, float, int, str]], bool,
            float, int, str]], Unset, bool, float, int, str]):
        path (Union[Unset, List[Union['AnyObject', List[Union['AnyObject', List[Union['AnyObject', bool, float, int,
            str]], bool, float, int, str]], bool, float, int, str]]]):
    """

    incorrect_value: Union[
        "AnyObject",
        List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
        Unset,
        bool,
        float,
        int,
        str,
    ] = UNSET
    error_message: Union[Unset, str] = UNSET
    fix_value: Union[
        "AnyObject",
        List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
        Unset,
        bool,
        float,
        int,
        str,
    ] = UNSET
    path: Union[
        Unset,
        List[
            Union[
                "AnyObject",
                List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
                bool,
                float,
                int,
                str,
            ]
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_object import AnyObject

        incorrect_value: Union[
            Dict[str, Any],
            List[Union[Dict[str, Any], List[Union[Dict[str, Any], bool, float, int, str]], bool, float, int, str]],
            Unset,
            bool,
            float,
            int,
            str,
        ]
        if isinstance(self.incorrect_value, Unset):
            incorrect_value = UNSET
        elif isinstance(self.incorrect_value, list):
            incorrect_value = []
            for componentsschemas_any_array_item_data in self.incorrect_value:
                componentsschemas_any_array_item: Union[
                    Dict[str, Any], List[Union[Dict[str, Any], bool, float, int, str]], bool, float, int, str
                ]
                if isinstance(componentsschemas_any_array_item_data, AnyObject):
                    componentsschemas_any_array_item = componentsschemas_any_array_item_data.to_dict()
                elif isinstance(componentsschemas_any_array_item_data, list):
                    componentsschemas_any_array_item = []
                    for componentsschemas_any_array_item_type_2_item_data in componentsschemas_any_array_item_data:
                        componentsschemas_any_array_item_type_2_item: Union[Dict[str, Any], bool, float, int, str]
                        if isinstance(componentsschemas_any_array_item_type_2_item_data, AnyObject):
                            componentsschemas_any_array_item_type_2_item = (
                                componentsschemas_any_array_item_type_2_item_data.to_dict()
                            )
                        else:
                            componentsschemas_any_array_item_type_2_item = (
                                componentsschemas_any_array_item_type_2_item_data
                            )
                        componentsschemas_any_array_item.append(componentsschemas_any_array_item_type_2_item)

                else:
                    componentsschemas_any_array_item = componentsschemas_any_array_item_data
                incorrect_value.append(componentsschemas_any_array_item)

        elif isinstance(self.incorrect_value, AnyObject):
            incorrect_value = self.incorrect_value.to_dict()
        else:
            incorrect_value = self.incorrect_value

        error_message = self.error_message

        fix_value: Union[
            Dict[str, Any],
            List[Union[Dict[str, Any], List[Union[Dict[str, Any], bool, float, int, str]], bool, float, int, str]],
            Unset,
            bool,
            float,
            int,
            str,
        ]
        if isinstance(self.fix_value, Unset):
            fix_value = UNSET
        elif isinstance(self.fix_value, list):
            fix_value = []
            for componentsschemas_any_array_item_data in self.fix_value:
                componentsschemas_any_array_item: Union[
                    Dict[str, Any], List[Union[Dict[str, Any], bool, float, int, str]], bool, float, int, str
                ]
                if isinstance(componentsschemas_any_array_item_data, AnyObject):
                    componentsschemas_any_array_item = componentsschemas_any_array_item_data.to_dict()
                elif isinstance(componentsschemas_any_array_item_data, list):
                    componentsschemas_any_array_item = []
                    for componentsschemas_any_array_item_type_2_item_data in componentsschemas_any_array_item_data:
                        componentsschemas_any_array_item_type_2_item: Union[Dict[str, Any], bool, float, int, str]
                        if isinstance(componentsschemas_any_array_item_type_2_item_data, AnyObject):
                            componentsschemas_any_array_item_type_2_item = (
                                componentsschemas_any_array_item_type_2_item_data.to_dict()
                            )
                        else:
                            componentsschemas_any_array_item_type_2_item = (
                                componentsschemas_any_array_item_type_2_item_data
                            )
                        componentsschemas_any_array_item.append(componentsschemas_any_array_item_type_2_item)

                else:
                    componentsschemas_any_array_item = componentsschemas_any_array_item_data
                fix_value.append(componentsschemas_any_array_item)

        elif isinstance(self.fix_value, AnyObject):
            fix_value = self.fix_value.to_dict()
        else:
            fix_value = self.fix_value

        path: Union[
            Unset,
            List[
                Union[
                    Dict[str, Any],
                    List[
                        Union[Dict[str, Any], List[Union[Dict[str, Any], bool, float, int, str]], bool, float, int, str]
                    ],
                    bool,
                    float,
                    int,
                    str,
                ]
            ],
        ] = UNSET
        if not isinstance(self.path, Unset):
            path = []
            for path_item_data in self.path:
                path_item: Union[
                    Dict[str, Any],
                    List[
                        Union[Dict[str, Any], List[Union[Dict[str, Any], bool, float, int, str]], bool, float, int, str]
                    ],
                    bool,
                    float,
                    int,
                    str,
                ]
                if isinstance(path_item_data, list):
                    path_item = []
                    for componentsschemas_any_array_item_data in path_item_data:
                        componentsschemas_any_array_item: Union[
                            Dict[str, Any], List[Union[Dict[str, Any], bool, float, int, str]], bool, float, int, str
                        ]
                        if isinstance(componentsschemas_any_array_item_data, AnyObject):
                            componentsschemas_any_array_item = componentsschemas_any_array_item_data.to_dict()
                        elif isinstance(componentsschemas_any_array_item_data, list):
                            componentsschemas_any_array_item = []
                            for (
                                componentsschemas_any_array_item_type_2_item_data
                            ) in componentsschemas_any_array_item_data:
                                componentsschemas_any_array_item_type_2_item: Union[
                                    Dict[str, Any], bool, float, int, str
                                ]
                                if isinstance(componentsschemas_any_array_item_type_2_item_data, AnyObject):
                                    componentsschemas_any_array_item_type_2_item = (
                                        componentsschemas_any_array_item_type_2_item_data.to_dict()
                                    )
                                else:
                                    componentsschemas_any_array_item_type_2_item = (
                                        componentsschemas_any_array_item_type_2_item_data
                                    )
                                componentsschemas_any_array_item.append(componentsschemas_any_array_item_type_2_item)

                        else:
                            componentsschemas_any_array_item = componentsschemas_any_array_item_data
                        path_item.append(componentsschemas_any_array_item)

                elif isinstance(path_item_data, AnyObject):
                    path_item = path_item_data.to_dict()
                else:
                    path_item = path_item_data
                path.append(path_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incorrect_value is not UNSET:
            field_dict["incorrect_value"] = incorrect_value
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if fix_value is not UNSET:
            field_dict["fix_value"] = fix_value
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_object import AnyObject

        d = src_dict.copy()

        def _parse_incorrect_value(
            data: object,
        ) -> Union[
            "AnyObject",
            List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
            Unset,
            bool,
            float,
            int,
            str,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_any_type_0 = []
                _componentsschemas_any_type_0 = data
                for componentsschemas_any_array_item_data in _componentsschemas_any_type_0:

                    def _parse_componentsschemas_any_array_item(
                        data: object,
                    ) -> Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_any_array_item_type_0 = AnyObject.from_dict(data)

                            return componentsschemas_any_array_item_type_0
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, list):
                                raise TypeError()
                            componentsschemas_any_array_item_type_2 = []
                            _componentsschemas_any_array_item_type_2 = data
                            for (
                                componentsschemas_any_array_item_type_2_item_data
                            ) in _componentsschemas_any_array_item_type_2:

                                def _parse_componentsschemas_any_array_item_type_2_item(
                                    data: object,
                                ) -> Union["AnyObject", bool, float, int, str]:
                                    try:
                                        if not isinstance(data, dict):
                                            raise TypeError()
                                        componentsschemas_any_array_item_type_2_item_type_0 = AnyObject.from_dict(data)

                                        return componentsschemas_any_array_item_type_2_item_type_0
                                    except:  # noqa: E722
                                        pass
                                    return cast(Union["AnyObject", bool, float, int, str], data)

                                componentsschemas_any_array_item_type_2_item = (
                                    _parse_componentsschemas_any_array_item_type_2_item(
                                        componentsschemas_any_array_item_type_2_item_data
                                    )
                                )

                                componentsschemas_any_array_item_type_2.append(
                                    componentsschemas_any_array_item_type_2_item
                                )

                            return componentsschemas_any_array_item_type_2
                        except:  # noqa: E722
                            pass
                        return cast(
                            Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str],
                            data,
                        )

                    componentsschemas_any_array_item = _parse_componentsschemas_any_array_item(
                        componentsschemas_any_array_item_data
                    )

                    componentsschemas_any_type_0.append(componentsschemas_any_array_item)

                return componentsschemas_any_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_any_type_1 = AnyObject.from_dict(data)

                return componentsschemas_any_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "AnyObject",
                    List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
                    Unset,
                    bool,
                    float,
                    int,
                    str,
                ],
                data,
            )

        incorrect_value = _parse_incorrect_value(d.pop("incorrect_value", UNSET))

        error_message = d.pop("error_message", UNSET)

        def _parse_fix_value(
            data: object,
        ) -> Union[
            "AnyObject",
            List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
            Unset,
            bool,
            float,
            int,
            str,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_any_type_0 = []
                _componentsschemas_any_type_0 = data
                for componentsschemas_any_array_item_data in _componentsschemas_any_type_0:

                    def _parse_componentsschemas_any_array_item(
                        data: object,
                    ) -> Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_any_array_item_type_0 = AnyObject.from_dict(data)

                            return componentsschemas_any_array_item_type_0
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, list):
                                raise TypeError()
                            componentsschemas_any_array_item_type_2 = []
                            _componentsschemas_any_array_item_type_2 = data
                            for (
                                componentsschemas_any_array_item_type_2_item_data
                            ) in _componentsschemas_any_array_item_type_2:

                                def _parse_componentsschemas_any_array_item_type_2_item(
                                    data: object,
                                ) -> Union["AnyObject", bool, float, int, str]:
                                    try:
                                        if not isinstance(data, dict):
                                            raise TypeError()
                                        componentsschemas_any_array_item_type_2_item_type_0 = AnyObject.from_dict(data)

                                        return componentsschemas_any_array_item_type_2_item_type_0
                                    except:  # noqa: E722
                                        pass
                                    return cast(Union["AnyObject", bool, float, int, str], data)

                                componentsschemas_any_array_item_type_2_item = (
                                    _parse_componentsschemas_any_array_item_type_2_item(
                                        componentsschemas_any_array_item_type_2_item_data
                                    )
                                )

                                componentsschemas_any_array_item_type_2.append(
                                    componentsschemas_any_array_item_type_2_item
                                )

                            return componentsschemas_any_array_item_type_2
                        except:  # noqa: E722
                            pass
                        return cast(
                            Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str],
                            data,
                        )

                    componentsschemas_any_array_item = _parse_componentsschemas_any_array_item(
                        componentsschemas_any_array_item_data
                    )

                    componentsschemas_any_type_0.append(componentsschemas_any_array_item)

                return componentsschemas_any_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_any_type_1 = AnyObject.from_dict(data)

                return componentsschemas_any_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "AnyObject",
                    List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
                    Unset,
                    bool,
                    float,
                    int,
                    str,
                ],
                data,
            )

        fix_value = _parse_fix_value(d.pop("fix_value", UNSET))

        path = []
        _path = d.pop("path", UNSET)
        for path_item_data in _path or []:

            def _parse_path_item(
                data: object,
            ) -> Union[
                "AnyObject",
                List[Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]],
                bool,
                float,
                int,
                str,
            ]:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    componentsschemas_any_type_0 = []
                    _componentsschemas_any_type_0 = data
                    for componentsschemas_any_array_item_data in _componentsschemas_any_type_0:

                        def _parse_componentsschemas_any_array_item(
                            data: object,
                        ) -> Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]:
                            try:
                                if not isinstance(data, dict):
                                    raise TypeError()
                                componentsschemas_any_array_item_type_0 = AnyObject.from_dict(data)

                                return componentsschemas_any_array_item_type_0
                            except:  # noqa: E722
                                pass
                            try:
                                if not isinstance(data, list):
                                    raise TypeError()
                                componentsschemas_any_array_item_type_2 = []
                                _componentsschemas_any_array_item_type_2 = data
                                for (
                                    componentsschemas_any_array_item_type_2_item_data
                                ) in _componentsschemas_any_array_item_type_2:

                                    def _parse_componentsschemas_any_array_item_type_2_item(
                                        data: object,
                                    ) -> Union["AnyObject", bool, float, int, str]:
                                        try:
                                            if not isinstance(data, dict):
                                                raise TypeError()
                                            componentsschemas_any_array_item_type_2_item_type_0 = AnyObject.from_dict(
                                                data
                                            )

                                            return componentsschemas_any_array_item_type_2_item_type_0
                                        except:  # noqa: E722
                                            pass
                                        return cast(Union["AnyObject", bool, float, int, str], data)

                                    componentsschemas_any_array_item_type_2_item = (
                                        _parse_componentsschemas_any_array_item_type_2_item(
                                            componentsschemas_any_array_item_type_2_item_data
                                        )
                                    )

                                    componentsschemas_any_array_item_type_2.append(
                                        componentsschemas_any_array_item_type_2_item
                                    )

                                return componentsschemas_any_array_item_type_2
                            except:  # noqa: E722
                                pass
                            return cast(
                                Union[
                                    "AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str
                                ],
                                data,
                            )

                        componentsschemas_any_array_item = _parse_componentsschemas_any_array_item(
                            componentsschemas_any_array_item_data
                        )

                        componentsschemas_any_type_0.append(componentsschemas_any_array_item)

                    return componentsschemas_any_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_any_type_1 = AnyObject.from_dict(data)

                    return componentsschemas_any_type_1
                except:  # noqa: E722
                    pass
                return cast(
                    Union[
                        "AnyObject",
                        List[
                            Union["AnyObject", List[Union["AnyObject", bool, float, int, str]], bool, float, int, str]
                        ],
                        bool,
                        float,
                        int,
                        str,
                    ],
                    data,
                )

            path_item = _parse_path_item(path_item_data)

            path.append(path_item)

        reask = cls(
            incorrect_value=incorrect_value,
            error_message=error_message,
            fix_value=fix_value,
            path=path,
        )

        reask.additional_properties = d
        return reask

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
