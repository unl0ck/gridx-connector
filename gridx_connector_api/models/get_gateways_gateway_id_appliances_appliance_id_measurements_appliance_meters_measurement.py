from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement")


@_attrs_define
class GetGatewaysGatewayIDAppliancesApplianceIDMeasurementsApplianceMetersMeasurement:
    """
    Attributes:
        measured_at (datetime.datetime | Unset): Time when the data was measured.
        l_1_active_power (int | Unset): L1 Active Power in mW.
        l_1_active_power_reading_positive (int | Unset): L1 Active Power Reading (Imported Energy) in Ws.
        l_1_active_power_reading_negative (int | Unset): L2 Active Power Reading (Exported Energy) in Ws.
        l_1_reactive_power (int | Unset): L1 Reactive Power in VAr.
        l_1_reactive_power_reading_positive (int | Unset): L1 Reactive Power Reading (Imported Energy) in VArs.
        l_1_reactive_power_reading_negative (int | Unset): L1 Reactive Power Reading (Exported Energy) in VArs.
        l_1_apparent_power (int | Unset): L1 Apparent Power in VA.
        l_1_apparent_power_reading_positive (int | Unset): L1 Apparent Power Reading (Imported Energy) in VAs.
        l_1_apparent_power_reading_negative (int | Unset): L1 Apparent Power Reading (Exported Energy) in VAs.
        l_1_current (int | Unset): L1 Current in mA.
        l_1_voltage (int | Unset): L1 Voltage in mV.
        l_1_import_power_limit (int | Unset): L1 maximum imported power in mW.
        l_2_active_power (int | Unset): L2 Active Power in mW.
        l_2_active_power_reading_positive (int | Unset): L2 Active Power Reading (Imported Energy) in Ws.
        l_2_active_power_reading_negative (int | Unset): L2 Active Power Reading (Exported Energy) in Ws.
        l_2_reactive_power (int | Unset): L2 Reactive Power in VAr.
        l_2_reactive_power_reading_positive (int | Unset): L2 Reactive Power Reading (Imported Energy) in VArs.
        l_2_reactive_power_reading_negative (int | Unset): L2 Reactive Power Reading (Exported Energy) in VArs.
        l_2_apparent_power (int | Unset): L2 Apparent Power in VA.
        l_2_apparent_power_reading_positive (int | Unset): L2 Apparent Power Reading (Imported Energy) in VAs.
        l_2_apparent_power_reading_negative (int | Unset): L2 Apparent Power Reading (Exported Energy) in VAs.
        l_2_current (int | Unset): L2 Current in mA.
        l_2_voltage (int | Unset): L2 Voltage in mV.
        l_2_import_power_limit (int | Unset): L2 maximum imported power in mW.
        l_3_active_power (int | Unset): L3 Active Power in mW.
        l_3_active_power_reading_positive (int | Unset): L3 Active Power Reading (Imported Energy) in Ws.
        l_3_active_power_reading_negative (int | Unset): L3 Active Power Reading (Exported Energy) in Ws.
        l_3_reactive_power (int | Unset): L3 Reactive Power in VAr.
        l_3_reactive_power_reading_positive (int | Unset): L3 Reactive Power Reading (Imported Energy) in VArs.
        l_3_reactive_power_reading_negative (int | Unset): L3 Reactive Power Reading (Exported Energy) in VArs.
        l_3_apparent_power (int | Unset): L3 Apparent Power in VA.
        l_3_apparent_power_reading_positive (int | Unset): L3 Apparent Power Reading (Imported Energy) in VAs.
        l_3_apparent_power_reading_negative (int | Unset): L3 Apparent Power Reading (Exported Energy) in VAs.
        l_3_current (int | Unset): L3 Current in mA.
        l_3_voltage (int | Unset): L3 Voltage in mV.
        l_3_import_power_limit (int | Unset): L3 maximum imported power in mW.
        sum_active_power (int | Unset): Sum Active Power in mW.
        sum_active_power_reading_positive (int | Unset): Sum Active Power Reading (Imported Energy) in Ws.
        sum_active_power_reading_negative (int | Unset): Sum Active Power Reading (Exported Energy) in Ws.
        sum_apparent_power (int | Unset): Sum Apparent Power in VA.
        sum_apparent_power_reading_positive (int | Unset): Sum Apparent Power Reading (Imported Energy) in VAs.
        sum_apparent_power_reading_negative (int | Unset): Sum Apparent Power Reading (Exported Energy) in VAs.
        sum_reactive_power (int | Unset): Sum Reactive Power in VA.
        sum_reactive_power_reading_positive (int | Unset): Sum Reactive Power Reading (Imported Energy) in VAs.
        sum_reactive_power_reading_negative (int | Unset): Sum Reactive Power Reading (Exported Energy) in VAs.
        sum_import_power_limit (int | Unset): Sum Maximum imported power in mW.
        sum_power_factor (int | Unset): Power factor in deg.
    """

    measured_at: datetime.datetime | Unset = UNSET
    l_1_active_power: int | Unset = UNSET
    l_1_active_power_reading_positive: int | Unset = UNSET
    l_1_active_power_reading_negative: int | Unset = UNSET
    l_1_reactive_power: int | Unset = UNSET
    l_1_reactive_power_reading_positive: int | Unset = UNSET
    l_1_reactive_power_reading_negative: int | Unset = UNSET
    l_1_apparent_power: int | Unset = UNSET
    l_1_apparent_power_reading_positive: int | Unset = UNSET
    l_1_apparent_power_reading_negative: int | Unset = UNSET
    l_1_current: int | Unset = UNSET
    l_1_voltage: int | Unset = UNSET
    l_1_import_power_limit: int | Unset = UNSET
    l_2_active_power: int | Unset = UNSET
    l_2_active_power_reading_positive: int | Unset = UNSET
    l_2_active_power_reading_negative: int | Unset = UNSET
    l_2_reactive_power: int | Unset = UNSET
    l_2_reactive_power_reading_positive: int | Unset = UNSET
    l_2_reactive_power_reading_negative: int | Unset = UNSET
    l_2_apparent_power: int | Unset = UNSET
    l_2_apparent_power_reading_positive: int | Unset = UNSET
    l_2_apparent_power_reading_negative: int | Unset = UNSET
    l_2_current: int | Unset = UNSET
    l_2_voltage: int | Unset = UNSET
    l_2_import_power_limit: int | Unset = UNSET
    l_3_active_power: int | Unset = UNSET
    l_3_active_power_reading_positive: int | Unset = UNSET
    l_3_active_power_reading_negative: int | Unset = UNSET
    l_3_reactive_power: int | Unset = UNSET
    l_3_reactive_power_reading_positive: int | Unset = UNSET
    l_3_reactive_power_reading_negative: int | Unset = UNSET
    l_3_apparent_power: int | Unset = UNSET
    l_3_apparent_power_reading_positive: int | Unset = UNSET
    l_3_apparent_power_reading_negative: int | Unset = UNSET
    l_3_current: int | Unset = UNSET
    l_3_voltage: int | Unset = UNSET
    l_3_import_power_limit: int | Unset = UNSET
    sum_active_power: int | Unset = UNSET
    sum_active_power_reading_positive: int | Unset = UNSET
    sum_active_power_reading_negative: int | Unset = UNSET
    sum_apparent_power: int | Unset = UNSET
    sum_apparent_power_reading_positive: int | Unset = UNSET
    sum_apparent_power_reading_negative: int | Unset = UNSET
    sum_reactive_power: int | Unset = UNSET
    sum_reactive_power_reading_positive: int | Unset = UNSET
    sum_reactive_power_reading_negative: int | Unset = UNSET
    sum_import_power_limit: int | Unset = UNSET
    sum_power_factor: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at: str | Unset = UNSET
        if not isinstance(self.measured_at, Unset):
            measured_at = self.measured_at.isoformat()

        l_1_active_power = self.l_1_active_power

        l_1_active_power_reading_positive = self.l_1_active_power_reading_positive

        l_1_active_power_reading_negative = self.l_1_active_power_reading_negative

        l_1_reactive_power = self.l_1_reactive_power

        l_1_reactive_power_reading_positive = self.l_1_reactive_power_reading_positive

        l_1_reactive_power_reading_negative = self.l_1_reactive_power_reading_negative

        l_1_apparent_power = self.l_1_apparent_power

        l_1_apparent_power_reading_positive = self.l_1_apparent_power_reading_positive

        l_1_apparent_power_reading_negative = self.l_1_apparent_power_reading_negative

        l_1_current = self.l_1_current

        l_1_voltage = self.l_1_voltage

        l_1_import_power_limit = self.l_1_import_power_limit

        l_2_active_power = self.l_2_active_power

        l_2_active_power_reading_positive = self.l_2_active_power_reading_positive

        l_2_active_power_reading_negative = self.l_2_active_power_reading_negative

        l_2_reactive_power = self.l_2_reactive_power

        l_2_reactive_power_reading_positive = self.l_2_reactive_power_reading_positive

        l_2_reactive_power_reading_negative = self.l_2_reactive_power_reading_negative

        l_2_apparent_power = self.l_2_apparent_power

        l_2_apparent_power_reading_positive = self.l_2_apparent_power_reading_positive

        l_2_apparent_power_reading_negative = self.l_2_apparent_power_reading_negative

        l_2_current = self.l_2_current

        l_2_voltage = self.l_2_voltage

        l_2_import_power_limit = self.l_2_import_power_limit

        l_3_active_power = self.l_3_active_power

        l_3_active_power_reading_positive = self.l_3_active_power_reading_positive

        l_3_active_power_reading_negative = self.l_3_active_power_reading_negative

        l_3_reactive_power = self.l_3_reactive_power

        l_3_reactive_power_reading_positive = self.l_3_reactive_power_reading_positive

        l_3_reactive_power_reading_negative = self.l_3_reactive_power_reading_negative

        l_3_apparent_power = self.l_3_apparent_power

        l_3_apparent_power_reading_positive = self.l_3_apparent_power_reading_positive

        l_3_apparent_power_reading_negative = self.l_3_apparent_power_reading_negative

        l_3_current = self.l_3_current

        l_3_voltage = self.l_3_voltage

        l_3_import_power_limit = self.l_3_import_power_limit

        sum_active_power = self.sum_active_power

        sum_active_power_reading_positive = self.sum_active_power_reading_positive

        sum_active_power_reading_negative = self.sum_active_power_reading_negative

        sum_apparent_power = self.sum_apparent_power

        sum_apparent_power_reading_positive = self.sum_apparent_power_reading_positive

        sum_apparent_power_reading_negative = self.sum_apparent_power_reading_negative

        sum_reactive_power = self.sum_reactive_power

        sum_reactive_power_reading_positive = self.sum_reactive_power_reading_positive

        sum_reactive_power_reading_negative = self.sum_reactive_power_reading_negative

        sum_import_power_limit = self.sum_import_power_limit

        sum_power_factor = self.sum_power_factor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measured_at is not UNSET:
            field_dict["measuredAt"] = measured_at
        if l_1_active_power is not UNSET:
            field_dict["l1ActivePower"] = l_1_active_power
        if l_1_active_power_reading_positive is not UNSET:
            field_dict["l1ActivePowerReadingPositive"] = l_1_active_power_reading_positive
        if l_1_active_power_reading_negative is not UNSET:
            field_dict["l1ActivePowerReadingNegative"] = l_1_active_power_reading_negative
        if l_1_reactive_power is not UNSET:
            field_dict["l1ReactivePower"] = l_1_reactive_power
        if l_1_reactive_power_reading_positive is not UNSET:
            field_dict["l1ReactivePowerReadingPositive"] = l_1_reactive_power_reading_positive
        if l_1_reactive_power_reading_negative is not UNSET:
            field_dict["l1ReactivePowerReadingNegative"] = l_1_reactive_power_reading_negative
        if l_1_apparent_power is not UNSET:
            field_dict["l1ApparentPower"] = l_1_apparent_power
        if l_1_apparent_power_reading_positive is not UNSET:
            field_dict["l1ApparentPowerReadingPositive"] = l_1_apparent_power_reading_positive
        if l_1_apparent_power_reading_negative is not UNSET:
            field_dict["l1ApparentPowerReadingNegative"] = l_1_apparent_power_reading_negative
        if l_1_current is not UNSET:
            field_dict["l1Current"] = l_1_current
        if l_1_voltage is not UNSET:
            field_dict["l1Voltage"] = l_1_voltage
        if l_1_import_power_limit is not UNSET:
            field_dict["l1ImportPowerLimit"] = l_1_import_power_limit
        if l_2_active_power is not UNSET:
            field_dict["l2ActivePower"] = l_2_active_power
        if l_2_active_power_reading_positive is not UNSET:
            field_dict["l2ActivePowerReadingPositive"] = l_2_active_power_reading_positive
        if l_2_active_power_reading_negative is not UNSET:
            field_dict["l2ActivePowerReadingNegative"] = l_2_active_power_reading_negative
        if l_2_reactive_power is not UNSET:
            field_dict["l2ReactivePower"] = l_2_reactive_power
        if l_2_reactive_power_reading_positive is not UNSET:
            field_dict["l2ReactivePowerReadingPositive"] = l_2_reactive_power_reading_positive
        if l_2_reactive_power_reading_negative is not UNSET:
            field_dict["l2ReactivePowerReadingNegative"] = l_2_reactive_power_reading_negative
        if l_2_apparent_power is not UNSET:
            field_dict["l2ApparentPower"] = l_2_apparent_power
        if l_2_apparent_power_reading_positive is not UNSET:
            field_dict["l2ApparentPowerReadingPositive"] = l_2_apparent_power_reading_positive
        if l_2_apparent_power_reading_negative is not UNSET:
            field_dict["l2ApparentPowerReadingNegative"] = l_2_apparent_power_reading_negative
        if l_2_current is not UNSET:
            field_dict["l2Current"] = l_2_current
        if l_2_voltage is not UNSET:
            field_dict["l2Voltage"] = l_2_voltage
        if l_2_import_power_limit is not UNSET:
            field_dict["l2ImportPowerLimit"] = l_2_import_power_limit
        if l_3_active_power is not UNSET:
            field_dict["l3ActivePower"] = l_3_active_power
        if l_3_active_power_reading_positive is not UNSET:
            field_dict["l3ActivePowerReadingPositive"] = l_3_active_power_reading_positive
        if l_3_active_power_reading_negative is not UNSET:
            field_dict["l3ActivePowerReadingNegative"] = l_3_active_power_reading_negative
        if l_3_reactive_power is not UNSET:
            field_dict["l3ReactivePower"] = l_3_reactive_power
        if l_3_reactive_power_reading_positive is not UNSET:
            field_dict["l3ReactivePowerReadingPositive"] = l_3_reactive_power_reading_positive
        if l_3_reactive_power_reading_negative is not UNSET:
            field_dict["l3ReactivePowerReadingNegative"] = l_3_reactive_power_reading_negative
        if l_3_apparent_power is not UNSET:
            field_dict["l3ApparentPower"] = l_3_apparent_power
        if l_3_apparent_power_reading_positive is not UNSET:
            field_dict["l3ApparentPowerReadingPositive"] = l_3_apparent_power_reading_positive
        if l_3_apparent_power_reading_negative is not UNSET:
            field_dict["l3ApparentPowerReadingNegative"] = l_3_apparent_power_reading_negative
        if l_3_current is not UNSET:
            field_dict["l3Current"] = l_3_current
        if l_3_voltage is not UNSET:
            field_dict["l3Voltage"] = l_3_voltage
        if l_3_import_power_limit is not UNSET:
            field_dict["l3ImportPowerLimit"] = l_3_import_power_limit
        if sum_active_power is not UNSET:
            field_dict["sumActivePower"] = sum_active_power
        if sum_active_power_reading_positive is not UNSET:
            field_dict["sumActivePowerReadingPositive"] = sum_active_power_reading_positive
        if sum_active_power_reading_negative is not UNSET:
            field_dict["sumActivePowerReadingNegative"] = sum_active_power_reading_negative
        if sum_apparent_power is not UNSET:
            field_dict["sumApparentPower"] = sum_apparent_power
        if sum_apparent_power_reading_positive is not UNSET:
            field_dict["sumApparentPowerReadingPositive"] = sum_apparent_power_reading_positive
        if sum_apparent_power_reading_negative is not UNSET:
            field_dict["sumApparentPowerReadingNegative"] = sum_apparent_power_reading_negative
        if sum_reactive_power is not UNSET:
            field_dict["sumReactivePower"] = sum_reactive_power
        if sum_reactive_power_reading_positive is not UNSET:
            field_dict["sumReactivePowerReadingPositive"] = sum_reactive_power_reading_positive
        if sum_reactive_power_reading_negative is not UNSET:
            field_dict["sumReactivePowerReadingNegative"] = sum_reactive_power_reading_negative
        if sum_import_power_limit is not UNSET:
            field_dict["sumImportPowerLimit"] = sum_import_power_limit
        if sum_power_factor is not UNSET:
            field_dict["sumPowerFactor"] = sum_power_factor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _measured_at = d.pop("measuredAt", UNSET)
        measured_at: datetime.datetime | Unset
        if isinstance(_measured_at, Unset):
            measured_at = UNSET
        else:
            measured_at = isoparse(_measured_at)

        l_1_active_power = d.pop("l1ActivePower", UNSET)

        l_1_active_power_reading_positive = d.pop("l1ActivePowerReadingPositive", UNSET)

        l_1_active_power_reading_negative = d.pop("l1ActivePowerReadingNegative", UNSET)

        l_1_reactive_power = d.pop("l1ReactivePower", UNSET)

        l_1_reactive_power_reading_positive = d.pop("l1ReactivePowerReadingPositive", UNSET)

        l_1_reactive_power_reading_negative = d.pop("l1ReactivePowerReadingNegative", UNSET)

        l_1_apparent_power = d.pop("l1ApparentPower", UNSET)

        l_1_apparent_power_reading_positive = d.pop("l1ApparentPowerReadingPositive", UNSET)

        l_1_apparent_power_reading_negative = d.pop("l1ApparentPowerReadingNegative", UNSET)

        l_1_current = d.pop("l1Current", UNSET)

        l_1_voltage = d.pop("l1Voltage", UNSET)

        l_1_import_power_limit = d.pop("l1ImportPowerLimit", UNSET)

        l_2_active_power = d.pop("l2ActivePower", UNSET)

        l_2_active_power_reading_positive = d.pop("l2ActivePowerReadingPositive", UNSET)

        l_2_active_power_reading_negative = d.pop("l2ActivePowerReadingNegative", UNSET)

        l_2_reactive_power = d.pop("l2ReactivePower", UNSET)

        l_2_reactive_power_reading_positive = d.pop("l2ReactivePowerReadingPositive", UNSET)

        l_2_reactive_power_reading_negative = d.pop("l2ReactivePowerReadingNegative", UNSET)

        l_2_apparent_power = d.pop("l2ApparentPower", UNSET)

        l_2_apparent_power_reading_positive = d.pop("l2ApparentPowerReadingPositive", UNSET)

        l_2_apparent_power_reading_negative = d.pop("l2ApparentPowerReadingNegative", UNSET)

        l_2_current = d.pop("l2Current", UNSET)

        l_2_voltage = d.pop("l2Voltage", UNSET)

        l_2_import_power_limit = d.pop("l2ImportPowerLimit", UNSET)

        l_3_active_power = d.pop("l3ActivePower", UNSET)

        l_3_active_power_reading_positive = d.pop("l3ActivePowerReadingPositive", UNSET)

        l_3_active_power_reading_negative = d.pop("l3ActivePowerReadingNegative", UNSET)

        l_3_reactive_power = d.pop("l3ReactivePower", UNSET)

        l_3_reactive_power_reading_positive = d.pop("l3ReactivePowerReadingPositive", UNSET)

        l_3_reactive_power_reading_negative = d.pop("l3ReactivePowerReadingNegative", UNSET)

        l_3_apparent_power = d.pop("l3ApparentPower", UNSET)

        l_3_apparent_power_reading_positive = d.pop("l3ApparentPowerReadingPositive", UNSET)

        l_3_apparent_power_reading_negative = d.pop("l3ApparentPowerReadingNegative", UNSET)

        l_3_current = d.pop("l3Current", UNSET)

        l_3_voltage = d.pop("l3Voltage", UNSET)

        l_3_import_power_limit = d.pop("l3ImportPowerLimit", UNSET)

        sum_active_power = d.pop("sumActivePower", UNSET)

        sum_active_power_reading_positive = d.pop("sumActivePowerReadingPositive", UNSET)

        sum_active_power_reading_negative = d.pop("sumActivePowerReadingNegative", UNSET)

        sum_apparent_power = d.pop("sumApparentPower", UNSET)

        sum_apparent_power_reading_positive = d.pop("sumApparentPowerReadingPositive", UNSET)

        sum_apparent_power_reading_negative = d.pop("sumApparentPowerReadingNegative", UNSET)

        sum_reactive_power = d.pop("sumReactivePower", UNSET)

        sum_reactive_power_reading_positive = d.pop("sumReactivePowerReadingPositive", UNSET)

        sum_reactive_power_reading_negative = d.pop("sumReactivePowerReadingNegative", UNSET)

        sum_import_power_limit = d.pop("sumImportPowerLimit", UNSET)

        sum_power_factor = d.pop("sumPowerFactor", UNSET)

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_meters_measurement = cls(
            measured_at=measured_at,
            l_1_active_power=l_1_active_power,
            l_1_active_power_reading_positive=l_1_active_power_reading_positive,
            l_1_active_power_reading_negative=l_1_active_power_reading_negative,
            l_1_reactive_power=l_1_reactive_power,
            l_1_reactive_power_reading_positive=l_1_reactive_power_reading_positive,
            l_1_reactive_power_reading_negative=l_1_reactive_power_reading_negative,
            l_1_apparent_power=l_1_apparent_power,
            l_1_apparent_power_reading_positive=l_1_apparent_power_reading_positive,
            l_1_apparent_power_reading_negative=l_1_apparent_power_reading_negative,
            l_1_current=l_1_current,
            l_1_voltage=l_1_voltage,
            l_1_import_power_limit=l_1_import_power_limit,
            l_2_active_power=l_2_active_power,
            l_2_active_power_reading_positive=l_2_active_power_reading_positive,
            l_2_active_power_reading_negative=l_2_active_power_reading_negative,
            l_2_reactive_power=l_2_reactive_power,
            l_2_reactive_power_reading_positive=l_2_reactive_power_reading_positive,
            l_2_reactive_power_reading_negative=l_2_reactive_power_reading_negative,
            l_2_apparent_power=l_2_apparent_power,
            l_2_apparent_power_reading_positive=l_2_apparent_power_reading_positive,
            l_2_apparent_power_reading_negative=l_2_apparent_power_reading_negative,
            l_2_current=l_2_current,
            l_2_voltage=l_2_voltage,
            l_2_import_power_limit=l_2_import_power_limit,
            l_3_active_power=l_3_active_power,
            l_3_active_power_reading_positive=l_3_active_power_reading_positive,
            l_3_active_power_reading_negative=l_3_active_power_reading_negative,
            l_3_reactive_power=l_3_reactive_power,
            l_3_reactive_power_reading_positive=l_3_reactive_power_reading_positive,
            l_3_reactive_power_reading_negative=l_3_reactive_power_reading_negative,
            l_3_apparent_power=l_3_apparent_power,
            l_3_apparent_power_reading_positive=l_3_apparent_power_reading_positive,
            l_3_apparent_power_reading_negative=l_3_apparent_power_reading_negative,
            l_3_current=l_3_current,
            l_3_voltage=l_3_voltage,
            l_3_import_power_limit=l_3_import_power_limit,
            sum_active_power=sum_active_power,
            sum_active_power_reading_positive=sum_active_power_reading_positive,
            sum_active_power_reading_negative=sum_active_power_reading_negative,
            sum_apparent_power=sum_apparent_power,
            sum_apparent_power_reading_positive=sum_apparent_power_reading_positive,
            sum_apparent_power_reading_negative=sum_apparent_power_reading_negative,
            sum_reactive_power=sum_reactive_power,
            sum_reactive_power_reading_positive=sum_reactive_power_reading_positive,
            sum_reactive_power_reading_negative=sum_reactive_power_reading_negative,
            sum_import_power_limit=sum_import_power_limit,
            sum_power_factor=sum_power_factor,
        )

        get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_meters_measurement.additional_properties = d
        return get_gateways_gateway_id_appliances_appliance_id_measurements_appliance_meters_measurement

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
