from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.abstract_job_state import AbstractJobState
from ..models.abstract_job_type import AbstractJobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AbstractJob")


@_attrs_define
class AbstractJob:
    """Represents an application-based job on the gridBox.

    Attributes:
        type_ (AbstractJobType | Unset): Represents the kind of the job. A job can be of type:
            - `UNKNOWN_TYPE`
            - `RESET`: Indicates that the application has to be reset.
            - `SCAN`: Indicates that the application should start a scan.
            - `RESTART`: Indicates that the application should restart.
             Example: RESET.
        requested_at (datetime.datetime | Unset): Represents the time at which the job was requested. Example:
            2018-04-15T00:00:00Z.
        state (AbstractJobState | Unset): Represents the current state of the job. It can be one of:
            * `UNKNOWN_STATE`
            * `PENDING`: Indicates that the job waits to be fetched.
            * `RECEIVED`: Indicates that the job has reached the gridbox.
            * `STARTED`: Indicates that the job has been started.
            * `DONE`: Indicates that the job is done.
            * `ERROR`: Indicates that the job has failed.
            * `CANCELED`: Indicates that the job was remotely cancelled.It might only have an impact if the state is still
            pending.
             Example: PENDING.
    """

    type_: AbstractJobType | Unset = UNSET
    requested_at: datetime.datetime | Unset = UNSET
    state: AbstractJobState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        requested_at: str | Unset = UNSET
        if not isinstance(self.requested_at, Unset):
            requested_at = self.requested_at.isoformat()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if requested_at is not UNSET:
            field_dict["requestedAt"] = requested_at
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AbstractJobType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AbstractJobType(_type_)

        _requested_at = d.pop("requestedAt", UNSET)
        requested_at: datetime.datetime | Unset
        if isinstance(_requested_at, Unset):
            requested_at = UNSET
        else:
            requested_at = isoparse(_requested_at)

        _state = d.pop("state", UNSET)
        state: AbstractJobState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = AbstractJobState(_state)

        abstract_job = cls(
            type_=type_,
            requested_at=requested_at,
            state=state,
        )

        abstract_job.additional_properties = d
        return abstract_job

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
