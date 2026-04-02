from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.put_systems_system_id_gateways_gateway_id_import_power_limit_response_201_number_of_phases import (
    PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201NumberOfPhases,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201")


@_attrs_define
class PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201:
    """
    Attributes:
        number_of_phases (PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201NumberOfPhases): Number of
            phases the import power limit is set for. 1 or 3. Default is 3. Default:
            PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201NumberOfPhases.VALUE_3. Example: 3.
        max_import_total (int): Maximum total import power in W. Default: 0.
        max_import_l1 (int): Maximum total import power in the first phase in W. Default: 0.
        max_import_l2 (int): Maximum total import power in the second phase in W. Default: 0.
        max_import_l3 (int): Maximum total import power in the third phase in W. Default: 0.
        import_ev_margin_total (int): Maximum import power margin in W. This is the safety margin to the limit. Default:
            0.
        max_import_ev_margin_l1 (int): Maximum import power margin in the first phase in W. This is the safety margin to
            the limit. Default: 0.
        max_import_ev_margin_l2 (int): Maximum import power margin in the second phase in W. This is the safety margin
            to the limit. Default: 0.
        max_import_ev_margin_l3 (int): Maximum import power margin in the third phase in W. This is the safety margin to
            the limit. Default: 0.
        max_import_ev_worst_case (int): The assumed maximum charging power in W for all EVs in case the connection to
            the grid connection point meter is lost. Default: 0.
        max_import_ev_worst_case_l1 (int): The assumed maximum charging power in W for all EVs in case the connection to
            the grid connection point meter is lost for the first phase. Default: 0.
        max_import_ev_worst_case_l2 (int): The assumed maximum charging power in W for all EVs in case the connection to
            the grid connection point meter is lost for the second phase. Default: 0.
        max_import_ev_worst_case_l3 (int): The assumed maximum charging power in W for all EVs in case the connection to
            the grid connection point meter is lost for the third phase. Default: 0.
        internal_device_id (str): Unique ID to identify the gateway the import power limit belongs to. Example:
            aeb639cf0793e81f0804c6647af7f0900a847921c0596726f1afdfd04a3a3186.
        created_at (datetime.datetime): Time at which the import power limit was created in UTC using the RFC3339
            format. Example: 2021-10-10T23:20:50Z.
        updated_at (datetime.datetime): Time at which the import power limit was updated in UTC using the RFC3339
            format. Example: 2021-10-10T23:20:50Z.
        import_ev_margin_phase (int | Unset):
    """

    internal_device_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    number_of_phases: PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201NumberOfPhases = (
        PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201NumberOfPhases.VALUE_3
    )
    max_import_total: int = 0
    max_import_l1: int = 0
    max_import_l2: int = 0
    max_import_l3: int = 0
    import_ev_margin_total: int = 0
    max_import_ev_margin_l1: int = 0
    max_import_ev_margin_l2: int = 0
    max_import_ev_margin_l3: int = 0
    max_import_ev_worst_case: int = 0
    max_import_ev_worst_case_l1: int = 0
    max_import_ev_worst_case_l2: int = 0
    max_import_ev_worst_case_l3: int = 0
    import_ev_margin_phase: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number_of_phases = self.number_of_phases.value

        max_import_total = self.max_import_total

        max_import_l1 = self.max_import_l1

        max_import_l2 = self.max_import_l2

        max_import_l3 = self.max_import_l3

        import_ev_margin_total = self.import_ev_margin_total

        max_import_ev_margin_l1 = self.max_import_ev_margin_l1

        max_import_ev_margin_l2 = self.max_import_ev_margin_l2

        max_import_ev_margin_l3 = self.max_import_ev_margin_l3

        max_import_ev_worst_case = self.max_import_ev_worst_case

        max_import_ev_worst_case_l1 = self.max_import_ev_worst_case_l1

        max_import_ev_worst_case_l2 = self.max_import_ev_worst_case_l2

        max_import_ev_worst_case_l3 = self.max_import_ev_worst_case_l3

        internal_device_id = self.internal_device_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        import_ev_margin_phase = self.import_ev_margin_phase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numberOfPhases": number_of_phases,
                "maxImportTotal": max_import_total,
                "maxImportL1": max_import_l1,
                "maxImportL2": max_import_l2,
                "maxImportL3": max_import_l3,
                "importEVMarginTotal": import_ev_margin_total,
                "maxImportEVMarginL1": max_import_ev_margin_l1,
                "maxImportEVMarginL2": max_import_ev_margin_l2,
                "maxImportEVMarginL3": max_import_ev_margin_l3,
                "maxImportEVWorstCase": max_import_ev_worst_case,
                "maxImportEVWorstCaseL1": max_import_ev_worst_case_l1,
                "maxImportEVWorstCaseL2": max_import_ev_worst_case_l2,
                "maxImportEVWorstCaseL3": max_import_ev_worst_case_l3,
                "internalDeviceID": internal_device_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if import_ev_margin_phase is not UNSET:
            field_dict["importEVMarginPhase"] = import_ev_margin_phase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_phases = PutSystemsSystemIDGatewaysGatewayIDImportPowerLimitResponse201NumberOfPhases(
            d.pop("numberOfPhases")
        )

        max_import_total = d.pop("maxImportTotal")

        max_import_l1 = d.pop("maxImportL1")

        max_import_l2 = d.pop("maxImportL2")

        max_import_l3 = d.pop("maxImportL3")

        import_ev_margin_total = d.pop("importEVMarginTotal")

        max_import_ev_margin_l1 = d.pop("maxImportEVMarginL1")

        max_import_ev_margin_l2 = d.pop("maxImportEVMarginL2")

        max_import_ev_margin_l3 = d.pop("maxImportEVMarginL3")

        max_import_ev_worst_case = d.pop("maxImportEVWorstCase")

        max_import_ev_worst_case_l1 = d.pop("maxImportEVWorstCaseL1")

        max_import_ev_worst_case_l2 = d.pop("maxImportEVWorstCaseL2")

        max_import_ev_worst_case_l3 = d.pop("maxImportEVWorstCaseL3")

        internal_device_id = d.pop("internalDeviceID")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        import_ev_margin_phase = d.pop("importEVMarginPhase", UNSET)

        put_systems_system_id_gateways_gateway_id_import_power_limit_response_201 = cls(
            number_of_phases=number_of_phases,
            max_import_total=max_import_total,
            max_import_l1=max_import_l1,
            max_import_l2=max_import_l2,
            max_import_l3=max_import_l3,
            import_ev_margin_total=import_ev_margin_total,
            max_import_ev_margin_l1=max_import_ev_margin_l1,
            max_import_ev_margin_l2=max_import_ev_margin_l2,
            max_import_ev_margin_l3=max_import_ev_margin_l3,
            max_import_ev_worst_case=max_import_ev_worst_case,
            max_import_ev_worst_case_l1=max_import_ev_worst_case_l1,
            max_import_ev_worst_case_l2=max_import_ev_worst_case_l2,
            max_import_ev_worst_case_l3=max_import_ev_worst_case_l3,
            internal_device_id=internal_device_id,
            created_at=created_at,
            updated_at=updated_at,
            import_ev_margin_phase=import_ev_margin_phase,
        )

        put_systems_system_id_gateways_gateway_id_import_power_limit_response_201.additional_properties = d
        return put_systems_system_id_gateways_gateway_id_import_power_limit_response_201

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
