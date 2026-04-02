from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_systems_system_id_timeofuse_decisions_response_200_decisions_item_insight_motives_item import (
    GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItemInsightMotivesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItemInsight")


@_attrs_define
class GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItemInsight:
    """
    Attributes:
        motives (list[GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItemInsightMotivesItem] | Unset):
            Identifies the motivation behind a ToU decision. The following insights are implemented:
            1. `BATTERY_CHARGE_TO_COVER_LOAD`: Charge the battery in low `import_price` to cover load at higher import
            prices (> `break_even_import_price`) between `start_time` and `end_time`.
            2. `BATTERY_CHARGE_TO_DISCHARGE_TO_GRID`: Charge the battery in low `import_price` to discharge to grid at
            higher export prices (> `break_even_export_price`) between `start_time` and `end_time`.
            3. `BATTERY_CHARGE_SURPLUS_TO_COVER_LOAD`: Charge the battery from surplus to cover load later at higher import
            prices.
            4. `BATTERY_CHARGE_SURPLUS_TO_DISCHARGE_TO_GRID`: Charge the battery from surplus to discharge to grid at higher
            export prices.
            5. `BATTERY_KEEP_TO_COVER_LOAD`: Delay battery discharge to cover load at higher import prices (>
            `break_even_import_price`) between `start_time` and `end_time`.
            6. `BATTERY_KEEP_TO_DISCHARGE_TO_GRID`: Delay battery discharge to the grid at higher export prices (>
            `break_even_export_price`) between `start_time` and `end_time`.
            7. `BATTERY_DISCHARGE_TO_GRID`: Discharge the battery into the grid to benefit from high export prices.
            8. `EV_CHARGE_IN_LOW_PRICES`: Charge the EV earlier in low `import_price`. The desired SoC expected to be met at
            `end_time`.
            9. `EV_CHARGE_TO_SATISFY_DESIRED_SOC`: Force Charge the EV from grid to ensure that the desired SoC at pre-
            defined departure time (regardless of prices).
            10. `EV_KEEP_TO_EXPORT_SURPLUS_AND_CHARGE_FROM_GRID_LATER`: Prevent EV charge to allow PV surplus export at high
            export prices, and charge EV from grid later at lower import prices.
            11. `EV_DELAY_CHARGE_TO_LOW_PRICES`: Charge EV later at lower import prices.
            12. `EV_DELAY_CHARGE_TO_SURPLUS`: Charge EV later from PV surplus.
            13. `HEAT_PUMP_RECOMMEND_ON_MOTIVE`: Request increased heat pump operation, to avoid potential higher price
            periods or to use PV surplus.
             Example: ['BATTERY_CHARGE_TO_COVER_LOAD'].
        import_price (float | Unset): Current import price at which the decision is taken.
             Example: 0.1.
        break_even_import_price (float | Unset): Refers to the minimum import price at which using the stored energy
            later becomes more profitable than importing from grid, while accounting for battery efficiency losses.
             Example: 0.1.
        average_import_price (float | Unset): Average import price at which the stored energy was utilized.
             Example: 0.1.
        export_price (float | Unset): Current export price at which the decision is taken.
             Example: 0.1.
        break_even_export_price (float | Unset): Refers to the minimum export price at which selling the stored energy
            to grid later becomes profitable, while accounting for battery efficiency losses.
             Example: 0.1.
        average_export_price (float | Unset): Average export price at which the stored energy was utilized.
             Example: 0.1.
        from_ (datetime.datetime | Unset): Refers to the start time of an upcoming event justifying the current decision
            (e.g., start of battery discharge to cover load / to grid).
             Example: 2020-09-21T00:00:00Z.
        to (datetime.datetime | Unset): Refers to the end time of an upcoming event justifying the current decision
            (e.g., end of battery discharge to cover load / to grid).
             Example: 2020-09-21T01:00:00Z.
    """

    motives: list[GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItemInsightMotivesItem] | Unset = UNSET
    import_price: float | Unset = UNSET
    break_even_import_price: float | Unset = UNSET
    average_import_price: float | Unset = UNSET
    export_price: float | Unset = UNSET
    break_even_export_price: float | Unset = UNSET
    average_export_price: float | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        motives: list[str] | Unset = UNSET
        if not isinstance(self.motives, Unset):
            motives = []
            for motives_item_data in self.motives:
                motives_item = motives_item_data.value
                motives.append(motives_item)

        import_price = self.import_price

        break_even_import_price = self.break_even_import_price

        average_import_price = self.average_import_price

        export_price = self.export_price

        break_even_export_price = self.break_even_export_price

        average_export_price = self.average_export_price

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if motives is not UNSET:
            field_dict["motives"] = motives
        if import_price is not UNSET:
            field_dict["importPrice"] = import_price
        if break_even_import_price is not UNSET:
            field_dict["breakEvenImportPrice"] = break_even_import_price
        if average_import_price is not UNSET:
            field_dict["averageImportPrice"] = average_import_price
        if export_price is not UNSET:
            field_dict["exportPrice"] = export_price
        if break_even_export_price is not UNSET:
            field_dict["breakEvenExportPrice"] = break_even_export_price
        if average_export_price is not UNSET:
            field_dict["averageExportPrice"] = average_export_price
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _motives = d.pop("motives", UNSET)
        motives: list[GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItemInsightMotivesItem] | Unset = UNSET
        if _motives is not UNSET:
            motives = []
            for motives_item_data in _motives:
                motives_item = GetSystemsSystemIDTimeofuseDecisionsResponse200DecisionsItemInsightMotivesItem(
                    motives_item_data
                )

                motives.append(motives_item)

        import_price = d.pop("importPrice", UNSET)

        break_even_import_price = d.pop("breakEvenImportPrice", UNSET)

        average_import_price = d.pop("averageImportPrice", UNSET)

        export_price = d.pop("exportPrice", UNSET)

        break_even_export_price = d.pop("breakEvenExportPrice", UNSET)

        average_export_price = d.pop("averageExportPrice", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        get_systems_system_id_timeofuse_decisions_response_200_decisions_item_insight = cls(
            motives=motives,
            import_price=import_price,
            break_even_import_price=break_even_import_price,
            average_import_price=average_import_price,
            export_price=export_price,
            break_even_export_price=break_even_export_price,
            average_export_price=average_export_price,
            from_=from_,
            to=to,
        )

        get_systems_system_id_timeofuse_decisions_response_200_decisions_item_insight.additional_properties = d
        return get_systems_system_id_timeofuse_decisions_response_200_decisions_item_insight

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
