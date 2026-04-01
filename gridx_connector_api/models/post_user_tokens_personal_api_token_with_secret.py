from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostUserTokensPersonalAPITokenWithSecret")


@_attrs_define
class PostUserTokensPersonalAPITokenWithSecret:
    """
    Attributes:
        token (str): This token can be used for authenticating further requests as an alternative to Bearer
            Authentication.

            Example: Set the header field `Authorization` to `Token gxp_SUDJmIoABC1337JiAuKBZuauC0ff331HNPR0`.
            The permissions of this tokens are the same as the user that created it.

            **ATTENTION** - Please keep the token secret and treat it like a password! The token is only available
            immediately after creation and can not be retrieved again afterwards.
             Example: gxp_SUDJmIoABC1337JiAuKBZuauC0ff331HNPR0.
    """

    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        post_user_tokens_personal_api_token_with_secret = cls(
            token=token,
        )

        post_user_tokens_personal_api_token_with_secret.additional_properties = d
        return post_user_tokens_personal_api_token_with_secret

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
