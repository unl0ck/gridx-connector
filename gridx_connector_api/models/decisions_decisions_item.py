from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.decisions_decisions_item_case_name import DecisionsDecisionsItemCaseName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decisions_decisions_item_insight import DecisionsDecisionsItemInsight


T = TypeVar("T", bound="DecisionsDecisionsItem")


@_attrs_define
class DecisionsDecisionsItem:
    """
    Attributes:
        from_ (datetime.datetime):
        to (datetime.datetime):
        case_name (DecisionsDecisionsItemCaseName): Identifies underlying the decision case that this decision is based
            on.
            The following cases are implemented:
            1. `BATTERY_SELF_CONSUMPTION`: No time-of-use decision applied for the battery. In this case, the default
            self-consumption maximization logic applies to the battery.
            2. `BATTERY_NO_DISCHARGE`: Do not discharge the battery, even if there is demand and no PV surplus.
            Demand is served with power from the grid, instead of discharging the battery.
            3. `BATTERY_CHARGE_FROM_GRID`: Charge the battery with power from the grid, instead of only
            charging the PV surplus. The battery is forced to charge with maximum charging power.
            4. `BATTERY_CHARGE_FROM_SURPLUS`: Charge the battery with power from the surplus.
            5. `BATTERY_DISCHARGE_TO_GRID`: Discharge the battery into the grid, instead of only discharging to serve
            demand.
            Discharge of the battery may coincide with PV surplus, to benefit from high grid export prices charging the PV
            surplus. The battery is forced to discharge with maximum power.
            6. `BATTERY_NO_CHARGE`: Do not charge the battery, even if there is PV surplus. PV surplus is injected
            into the grid, instead of charging the battery.
            7. `BATTERY_NO_CHARGE_NO_DISCHARGE`: Do not charge or discharge the battery, regardless of PV surplus
            or insufficient PV production to meet demand.
            8. `BATTERY_LIMIT_CHARGE`: Limit the charging power of the battery, even if there is additional PV surplus.
            9. `BATTERY_LIMIT_DISCHARGE`: Limit the discharging power of the battery, even if there is additional demand.
            10. `BATTERY_UNDEFINED_DECISION`: Decision applied to the battery, but the decision cannot be mapped to any
            other decision case. This case is used as a fallback for newly implemented decision cases.
            self-consumption maximization logic applies to the battery.
            11. `EV_NO_DECISION`: No time-of-use decision applied for the EV. In this case, the default
            charge logic applies to the EV, depending on the charge mode.
            12. `EV_CHARGE_FROM_GRID`: Charge the EV with power for the grid, instead of only
            charging the PV surplus. The EV is forced to charge with maximum charging power.
            13. `EV_NO_CHARGE`: Do not charge the EV, even if there is PV surplus.
            14. `EV_LIMIT_CHARGE`: Limit the charging power of the EV.
            15. `EV_LIMIT_DISCHARGE`: Limit the discharging power of the EV.
            16. `EV_UNDEFINED_DECISION`: Decision applied to the EV, but the decision cannot be mapped to any
            other decision case. This case is used as a fallback for newly implemented decision cases.
            17. `HEATPUMP_RECOMMEND_ON`: Recommending the heat pump to switch on.
            18. `HEATPUMP_AUTO`: The heat pump is set to run in its energy-efficient normal mode.
            19. `PV_CURTAILMENT`: The PV production is curtailed to avoid grid export during periods of negative feed-in
            prices.
            20. `PV_NO_DECISION`: No time-of-use decision applied for the PV.
             Example: BATTERY_CHARGE_FROM_GRID.
        is_price_based_optimization (bool): Indicates if the decision is based on price. In most cases, decisions not
            based on price correspond to the "default" decision for a particular appliance type.
        insight (DecisionsDecisionsItemInsight | Unset):
    """

    from_: datetime.datetime
    to: datetime.datetime
    case_name: DecisionsDecisionsItemCaseName
    is_price_based_optimization: bool
    insight: DecisionsDecisionsItemInsight | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        case_name = self.case_name.value

        is_price_based_optimization = self.is_price_based_optimization

        insight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insight, Unset):
            insight = self.insight.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "case_name": case_name,
                "isPriceBasedOptimization": is_price_based_optimization,
            }
        )
        if insight is not UNSET:
            field_dict["insight"] = insight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decisions_decisions_item_insight import DecisionsDecisionsItemInsight

        d = dict(src_dict)
        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        case_name = DecisionsDecisionsItemCaseName(d.pop("case_name"))

        is_price_based_optimization = d.pop("isPriceBasedOptimization")

        _insight = d.pop("insight", UNSET)
        insight: DecisionsDecisionsItemInsight | Unset
        if isinstance(_insight, Unset):
            insight = UNSET
        else:
            insight = DecisionsDecisionsItemInsight.from_dict(_insight)

        decisions_decisions_item = cls(
            from_=from_,
            to=to,
            case_name=case_name,
            is_price_based_optimization=is_price_based_optimization,
            insight=insight,
        )

        decisions_decisions_item.additional_properties = d
        return decisions_decisions_item

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
