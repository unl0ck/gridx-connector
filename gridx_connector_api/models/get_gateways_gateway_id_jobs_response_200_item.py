from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_gateways_gateway_id_jobs_response_200_item_state import GetGatewaysGatewayIDJobsResponse200ItemState
from ..models.get_gateways_gateway_id_jobs_response_200_item_type import GetGatewaysGatewayIDJobsResponse200ItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_gateways_gateway_id_jobs_response_200_item_job_execution import (
        GetGatewaysGatewayIDJobsResponse200ItemJobExecution,
    )


T = TypeVar("T", bound="GetGatewaysGatewayIDJobsResponse200Item")


@_attrs_define
class GetGatewaysGatewayIDJobsResponse200Item:
    """
    Attributes:
        type_ (GetGatewaysGatewayIDJobsResponse200ItemType): Represents the kind of the job. A job can be of type:
            - `UNKNOWN_TYPE`
            - `RESET`: Indicates that the application has to be reset.
            - `SCAN`: Indicates that the application should start a scan.
            - `RESTART`: Indicates that the application should restart.
             Example: RESET.
        state (GetGatewaysGatewayIDJobsResponse200ItemState): Represents the current state of the job. It can be one of:
            * `UNKNOWN_STATE`
            * `PENDING`: Indicates that the job waits to be fetched.
            * `RECEIVED`: Indicates that the job has reached the gridbox.
            * `STARTED`: Indicates that the job has been started.
            * `DONE`: Indicates that the job is done.
            * `ERROR`: Indicates that the job has failed.
            * `CANCELED`: Indicates that the job was remotely cancelled.It might only have an impact if the state is still
            pending.
             Example: PENDING.
        id (UUID): Unique identifier of a job. Example: d90fc059-b1d0-4277-a347-43609e232f4f.
        executions (list[GetGatewaysGatewayIDJobsResponse200ItemJobExecution]): Represents a set of job executions.
        requested_at (datetime.datetime | Unset): Represents the time at which the job was requested. Example:
            2018-04-15T00:00:00Z.
        received_at (datetime.datetime | Unset): Represents the time at which the job was received by the gateway.
            Example: 2018-04-15T00:00:00Z.
        started_at (datetime.datetime | Unset): Represents the time at which the job was started. Example:
            2018-04-15T00:00:00Z.
        finished_at (datetime.datetime | Unset): Represents the time at which the job was finished. Example:
            2018-04-15T00:00:00Z.
    """

    type_: GetGatewaysGatewayIDJobsResponse200ItemType
    state: GetGatewaysGatewayIDJobsResponse200ItemState
    id: UUID
    executions: list[GetGatewaysGatewayIDJobsResponse200ItemJobExecution]
    requested_at: datetime.datetime | Unset = UNSET
    received_at: datetime.datetime | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        state = self.state.value

        id = str(self.id)

        executions = []
        for executions_item_data in self.executions:
            executions_item = executions_item_data.to_dict()
            executions.append(executions_item)

        requested_at: str | Unset = UNSET
        if not isinstance(self.requested_at, Unset):
            requested_at = self.requested_at.isoformat()

        received_at: str | Unset = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "state": state,
                "id": id,
                "executions": executions,
            }
        )
        if requested_at is not UNSET:
            field_dict["requestedAt"] = requested_at
        if received_at is not UNSET:
            field_dict["receivedAt"] = received_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_gateways_gateway_id_jobs_response_200_item_job_execution import (
            GetGatewaysGatewayIDJobsResponse200ItemJobExecution,
        )

        d = dict(src_dict)
        type_ = GetGatewaysGatewayIDJobsResponse200ItemType(d.pop("type"))

        state = GetGatewaysGatewayIDJobsResponse200ItemState(d.pop("state"))

        id = UUID(d.pop("id"))

        executions = []
        _executions = d.pop("executions")
        for executions_item_data in _executions:
            executions_item = GetGatewaysGatewayIDJobsResponse200ItemJobExecution.from_dict(executions_item_data)

            executions.append(executions_item)

        _requested_at = d.pop("requestedAt", UNSET)
        requested_at: datetime.datetime | Unset
        if isinstance(_requested_at, Unset):
            requested_at = UNSET
        else:
            requested_at = isoparse(_requested_at)

        _received_at = d.pop("receivedAt", UNSET)
        received_at: datetime.datetime | Unset
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _finished_at = d.pop("finishedAt", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)

        get_gateways_gateway_id_jobs_response_200_item = cls(
            type_=type_,
            state=state,
            id=id,
            executions=executions,
            requested_at=requested_at,
            received_at=received_at,
            started_at=started_at,
            finished_at=finished_at,
        )

        get_gateways_gateway_id_jobs_response_200_item.additional_properties = d
        return get_gateways_gateway_id_jobs_response_200_item

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
