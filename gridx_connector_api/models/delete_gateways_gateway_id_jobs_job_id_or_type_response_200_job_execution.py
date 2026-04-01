from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteGatewaysGatewayIDJobsJobIDOrTypeResponse200JobExecution")


@_attrs_define
class DeleteGatewaysGatewayIDJobsJobIDOrTypeResponse200JobExecution:
    """Represents an execution of a job.

    Attributes:
        id (UUID): Unique identifier of a job execution. Example: 5830cd32-a194-4b9d-bea3-c2332f27167f.
        job_id (UUID | Unset): Unique identifier of a job.
        succeeded (bool | Unset): Indicates that the execution was successful.
        error (str | Unset): A possible error message.
        started_at (datetime.datetime | Unset): Represents the time at which the execution was started at the gridbox.
            Example: 2018-04-15T00:00:00Z.
        finished_at (datetime.datetime | Unset): Represents the time at which the execution was finished. Example:
            2018-04-15T00:00:00Z.
    """

    id: UUID
    job_id: UUID | Unset = UNSET
    succeeded: bool | Unset = UNSET
    error: str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        succeeded = self.succeeded

        error = self.error

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
                "id": id,
            }
        )
        if job_id is not UNSET:
            field_dict["jobID"] = job_id
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded
        if error is not UNSET:
            field_dict["error"] = error
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        _job_id = d.pop("jobID", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        succeeded = d.pop("succeeded", UNSET)

        error = d.pop("error", UNSET)

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

        delete_gateways_gateway_id_jobs_job_id_or_type_response_200_job_execution = cls(
            id=id,
            job_id=job_id,
            succeeded=succeeded,
            error=error,
            started_at=started_at,
            finished_at=finished_at,
        )

        delete_gateways_gateway_id_jobs_job_id_or_type_response_200_job_execution.additional_properties = d
        return delete_gateways_gateway_id_jobs_job_id_or_type_response_200_job_execution

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
