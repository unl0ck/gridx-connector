from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_creation_state import JobCreationState
from ..models.job_creation_type import JobCreationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobCreation")


@_attrs_define
class JobCreation:
    """
    Attributes:
        type_ (JobCreationType): Represents the kind of the job. A job can be of type:
            - `UNKNOWN_TYPE`
            - `RESET`: Indicates that the application has to be reset.
            - `SCAN`: Indicates that the application should start a scan.
            - `RESTART`: Indicates that the application should restart.
             Example: RESET.
        state (JobCreationState): Represents the current state of the job. It can be one of:
            * `UNKNOWN_STATE`
            * `PENDING`: Indicates that the job waits to be fetched.
            * `RECEIVED`: Indicates that the job has reached the gridbox.
            * `STARTED`: Indicates that the job has been started.
            * `DONE`: Indicates that the job is done.
            * `ERROR`: Indicates that the job has failed.
            * `CANCELED`: Indicates that the job was remotely cancelled.It might only have an impact if the state is still
            pending.
             Example: PENDING.
        requested_at (datetime.datetime | Unset): Represents the time at which the job was requested. Example:
            2018-04-15T00:00:00Z.
        id (UUID | Unset): Unique identifier of a job. Example: d90fc059-b1d0-4277-a347-43609e232f4f.
    """

    type_: JobCreationType
    state: JobCreationState
    requested_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        state = self.state.value

        requested_at: str | Unset = UNSET
        if not isinstance(self.requested_at, Unset):
            requested_at = self.requested_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "state": state,
            }
        )
        if requested_at is not UNSET:
            field_dict["requestedAt"] = requested_at
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = JobCreationType(d.pop("type"))

        state = JobCreationState(d.pop("state"))

        _requested_at = d.pop("requestedAt", UNSET)
        requested_at: datetime.datetime | Unset
        if isinstance(_requested_at, Unset):
            requested_at = UNSET
        else:
            requested_at = isoparse(_requested_at)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        job_creation = cls(
            type_=type_,
            state=state,
            requested_at=requested_at,
            id=id,
        )

        job_creation.additional_properties = d
        return job_creation

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
