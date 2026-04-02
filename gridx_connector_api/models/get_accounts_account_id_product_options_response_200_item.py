from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_accounts_account_id_product_options_response_200_item_functionalities_item import (
        GetAccountsAccountIDProductOptionsResponse200ItemFunctionalitiesItem,
    )
    from ..models.get_accounts_account_id_product_options_response_200_item_hide_functionalities_item import (
        GetAccountsAccountIDProductOptionsResponse200ItemHideFunctionalitiesItem,
    )
    from ..models.get_accounts_account_id_product_options_response_200_item_show_functionalities_item import (
        GetAccountsAccountIDProductOptionsResponse200ItemShowFunctionalitiesItem,
    )


T = TypeVar("T", bound="GetAccountsAccountIDProductOptionsResponse200Item")


@_attrs_define
class GetAccountsAccountIDProductOptionsResponse200Item:
    """
    Attributes:
        name (str): Name of the product option. Example: Default Product Option.
        id (UUID): Unique identifier of the product option. Example: d5166f02-8b56-4200-90bd-35d3d17391b4.
        account_id (UUID): Unique identifier of the account that owns the product option. Example: d73b6749-2c32-4bca-
            ab73-50d8e3744edf.
        is_default (bool): Indicates whether the product option should be assigned by default to all systems of the
            owning account.
        functionalities (list[GetAccountsAccountIDProductOptionsResponse200ItemFunctionalitiesItem]): The default
            functionalities that a product option restricts access to. Deprecated - Use `showFunctionalities` and
            `hideFunctionalities` instead.
        hide_functionalities (list[GetAccountsAccountIDProductOptionsResponse200ItemHideFunctionalitiesItem]): The
            default functionalities that a product option restricts access to. Must be of type `hide=true`.
        show_functionalities (list[GetAccountsAccountIDProductOptionsResponse200ItemShowFunctionalitiesItem]): The extra
            functionalities that a product option grants access to. Must be of type `hide=false`.
        description (str | Unset): Describes the purpose of the product option.
    """

    name: str
    id: UUID
    account_id: UUID
    is_default: bool
    functionalities: list[GetAccountsAccountIDProductOptionsResponse200ItemFunctionalitiesItem]
    hide_functionalities: list[GetAccountsAccountIDProductOptionsResponse200ItemHideFunctionalitiesItem]
    show_functionalities: list[GetAccountsAccountIDProductOptionsResponse200ItemShowFunctionalitiesItem]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        account_id = str(self.account_id)

        is_default = self.is_default

        functionalities = []
        for functionalities_item_data in self.functionalities:
            functionalities_item = functionalities_item_data.to_dict()
            functionalities.append(functionalities_item)

        hide_functionalities = []
        for hide_functionalities_item_data in self.hide_functionalities:
            hide_functionalities_item = hide_functionalities_item_data.to_dict()
            hide_functionalities.append(hide_functionalities_item)

        show_functionalities = []
        for show_functionalities_item_data in self.show_functionalities:
            show_functionalities_item = show_functionalities_item_data.to_dict()
            show_functionalities.append(show_functionalities_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "accountID": account_id,
                "isDefault": is_default,
                "functionalities": functionalities,
                "hideFunctionalities": hide_functionalities,
                "showFunctionalities": show_functionalities,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_accounts_account_id_product_options_response_200_item_functionalities_item import (
            GetAccountsAccountIDProductOptionsResponse200ItemFunctionalitiesItem,
        )
        from ..models.get_accounts_account_id_product_options_response_200_item_hide_functionalities_item import (
            GetAccountsAccountIDProductOptionsResponse200ItemHideFunctionalitiesItem,
        )
        from ..models.get_accounts_account_id_product_options_response_200_item_show_functionalities_item import (
            GetAccountsAccountIDProductOptionsResponse200ItemShowFunctionalitiesItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        account_id = UUID(d.pop("accountID"))

        is_default = d.pop("isDefault")

        functionalities = []
        _functionalities = d.pop("functionalities")
        for functionalities_item_data in _functionalities:
            functionalities_item = GetAccountsAccountIDProductOptionsResponse200ItemFunctionalitiesItem.from_dict(
                functionalities_item_data
            )

            functionalities.append(functionalities_item)

        hide_functionalities = []
        _hide_functionalities = d.pop("hideFunctionalities")
        for hide_functionalities_item_data in _hide_functionalities:
            hide_functionalities_item = (
                GetAccountsAccountIDProductOptionsResponse200ItemHideFunctionalitiesItem.from_dict(
                    hide_functionalities_item_data
                )
            )

            hide_functionalities.append(hide_functionalities_item)

        show_functionalities = []
        _show_functionalities = d.pop("showFunctionalities")
        for show_functionalities_item_data in _show_functionalities:
            show_functionalities_item = (
                GetAccountsAccountIDProductOptionsResponse200ItemShowFunctionalitiesItem.from_dict(
                    show_functionalities_item_data
                )
            )

            show_functionalities.append(show_functionalities_item)

        description = d.pop("description", UNSET)

        get_accounts_account_id_product_options_response_200_item = cls(
            name=name,
            id=id,
            account_id=account_id,
            is_default=is_default,
            functionalities=functionalities,
            hide_functionalities=hide_functionalities,
            show_functionalities=show_functionalities,
            description=description,
        )

        get_accounts_account_id_product_options_response_200_item.additional_properties = d
        return get_accounts_account_id_product_options_response_200_item

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
