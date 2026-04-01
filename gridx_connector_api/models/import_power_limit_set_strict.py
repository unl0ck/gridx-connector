from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_power_limit_set_strict_number_of_phases import ImportPowerLimitSetStrictNumberOfPhases
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportPowerLimitSetStrict")


@_attrs_define
class ImportPowerLimitSetStrict:
    """
    Attributes:
        number_of_phases (ImportPowerLimitSetStrictNumberOfPhases | Unset): Number of phases the import power limit is
            set for. 1 or 3. Default is 3. Default: ImportPowerLimitSetStrictNumberOfPhases.VALUE_3. Example: 3.
        max_import_total (int | Unset): Maximum total import power in W. Default: 0.
        max_import_l1 (int | Unset): Maximum total import power in the first phase in W. Default: 0.
        max_import_l2 (int | Unset): Maximum total import power in the second phase in W. Default: 0.
        max_import_l3 (int | Unset): Maximum total import power in the third phase in W. Default: 0.
        import_ev_margin_total (int | Unset): Maximum import power margin in W. This is the safety margin to the limit.
            Default: 0.
        import_ev_margin_phase (int | Unset):
        max_import_ev_margin_l1 (int | Unset): Maximum import power margin in the first phase in W. This is the safety
            margin to the limit. Default: 0.
        max_import_ev_margin_l2 (int | Unset): Maximum import power margin in the second phase in W. This is the safety
            margin to the limit. Default: 0.
        max_import_ev_margin_l3 (int | Unset): Maximum import power margin in the third phase in W. This is the safety
            margin to the limit. Default: 0.
        max_import_ev_worst_case (int | Unset): The assumed maximum charging power in W for all EVs in case the
            connection to the grid connection point meter is lost. Default: 0.
        max_import_ev_worst_case_l1 (int | Unset): The assumed maximum charging power in W for all EVs in case the
            connection to the grid connection point meter is lost for the first phase. Default: 0.
        max_import_ev_worst_case_l2 (int | Unset): The assumed maximum charging power in W for all EVs in case the
            connection to the grid connection point meter is lost for the second phase. Default: 0.
        max_import_ev_worst_case_l3 (int | Unset): The assumed maximum charging power in W for all EVs in case the
            connection to the grid connection point meter is lost for the third phase. Default: 0.
    """

    number_of_phases: ImportPowerLimitSetStrictNumberOfPhases | Unset = ImportPowerLimitSetStrictNumberOfPhases.VALUE_3
    max_import_total: int | Unset = 0
    max_import_l1: int | Unset = 0
    max_import_l2: int | Unset = 0
    max_import_l3: int | Unset = 0
    import_ev_margin_total: int | Unset = 0
    import_ev_margin_phase: int | Unset = UNSET
    max_import_ev_margin_l1: int | Unset = 0
    max_import_ev_margin_l2: int | Unset = 0
    max_import_ev_margin_l3: int | Unset = 0
    max_import_ev_worst_case: int | Unset = 0
    max_import_ev_worst_case_l1: int | Unset = 0
    max_import_ev_worst_case_l2: int | Unset = 0
    max_import_ev_worst_case_l3: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number_of_phases: int | Unset = UNSET
        if not isinstance(self.number_of_phases, Unset):
            number_of_phases = self.number_of_phases.value

        max_import_total = self.max_import_total

        max_import_l1 = self.max_import_l1

        max_import_l2 = self.max_import_l2

        max_import_l3 = self.max_import_l3

        import_ev_margin_total = self.import_ev_margin_total

        import_ev_margin_phase = self.import_ev_margin_phase

        max_import_ev_margin_l1 = self.max_import_ev_margin_l1

        max_import_ev_margin_l2 = self.max_import_ev_margin_l2

        max_import_ev_margin_l3 = self.max_import_ev_margin_l3

        max_import_ev_worst_case = self.max_import_ev_worst_case

        max_import_ev_worst_case_l1 = self.max_import_ev_worst_case_l1

        max_import_ev_worst_case_l2 = self.max_import_ev_worst_case_l2

        max_import_ev_worst_case_l3 = self.max_import_ev_worst_case_l3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number_of_phases is not UNSET:
            field_dict["numberOfPhases"] = number_of_phases
        if max_import_total is not UNSET:
            field_dict["maxImportTotal"] = max_import_total
        if max_import_l1 is not UNSET:
            field_dict["maxImportL1"] = max_import_l1
        if max_import_l2 is not UNSET:
            field_dict["maxImportL2"] = max_import_l2
        if max_import_l3 is not UNSET:
            field_dict["maxImportL3"] = max_import_l3
        if import_ev_margin_total is not UNSET:
            field_dict["importEVMarginTotal"] = import_ev_margin_total
        if import_ev_margin_phase is not UNSET:
            field_dict["importEVMarginPhase"] = import_ev_margin_phase
        if max_import_ev_margin_l1 is not UNSET:
            field_dict["maxImportEVMarginL1"] = max_import_ev_margin_l1
        if max_import_ev_margin_l2 is not UNSET:
            field_dict["maxImportEVMarginL2"] = max_import_ev_margin_l2
        if max_import_ev_margin_l3 is not UNSET:
            field_dict["maxImportEVMarginL3"] = max_import_ev_margin_l3
        if max_import_ev_worst_case is not UNSET:
            field_dict["maxImportEVWorstCase"] = max_import_ev_worst_case
        if max_import_ev_worst_case_l1 is not UNSET:
            field_dict["maxImportEVWorstCaseL1"] = max_import_ev_worst_case_l1
        if max_import_ev_worst_case_l2 is not UNSET:
            field_dict["maxImportEVWorstCaseL2"] = max_import_ev_worst_case_l2
        if max_import_ev_worst_case_l3 is not UNSET:
            field_dict["maxImportEVWorstCaseL3"] = max_import_ev_worst_case_l3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _number_of_phases = d.pop("numberOfPhases", UNSET)
        number_of_phases: ImportPowerLimitSetStrictNumberOfPhases | Unset
        if isinstance(_number_of_phases, Unset):
            number_of_phases = UNSET
        else:
            number_of_phases = ImportPowerLimitSetStrictNumberOfPhases(_number_of_phases)

        max_import_total = d.pop("maxImportTotal", UNSET)

        max_import_l1 = d.pop("maxImportL1", UNSET)

        max_import_l2 = d.pop("maxImportL2", UNSET)

        max_import_l3 = d.pop("maxImportL3", UNSET)

        import_ev_margin_total = d.pop("importEVMarginTotal", UNSET)

        import_ev_margin_phase = d.pop("importEVMarginPhase", UNSET)

        max_import_ev_margin_l1 = d.pop("maxImportEVMarginL1", UNSET)

        max_import_ev_margin_l2 = d.pop("maxImportEVMarginL2", UNSET)

        max_import_ev_margin_l3 = d.pop("maxImportEVMarginL3", UNSET)

        max_import_ev_worst_case = d.pop("maxImportEVWorstCase", UNSET)

        max_import_ev_worst_case_l1 = d.pop("maxImportEVWorstCaseL1", UNSET)

        max_import_ev_worst_case_l2 = d.pop("maxImportEVWorstCaseL2", UNSET)

        max_import_ev_worst_case_l3 = d.pop("maxImportEVWorstCaseL3", UNSET)

        import_power_limit_set_strict = cls(
            number_of_phases=number_of_phases,
            max_import_total=max_import_total,
            max_import_l1=max_import_l1,
            max_import_l2=max_import_l2,
            max_import_l3=max_import_l3,
            import_ev_margin_total=import_ev_margin_total,
            import_ev_margin_phase=import_ev_margin_phase,
            max_import_ev_margin_l1=max_import_ev_margin_l1,
            max_import_ev_margin_l2=max_import_ev_margin_l2,
            max_import_ev_margin_l3=max_import_ev_margin_l3,
            max_import_ev_worst_case=max_import_ev_worst_case,
            max_import_ev_worst_case_l1=max_import_ev_worst_case_l1,
            max_import_ev_worst_case_l2=max_import_ev_worst_case_l2,
            max_import_ev_worst_case_l3=max_import_ev_worst_case_l3,
        )

        import_power_limit_set_strict.additional_properties = d
        return import_power_limit_set_strict

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
