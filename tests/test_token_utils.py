"""Tests for JWT token helpers."""

import base64
import json

import pytest

from gridx_connector.async_connector import AsyncGridboxConnector
from gridx_connector.token_utils import decode_jwt_payload, user_id_from_token


def _make_jwt(payload: object) -> str:
    header = base64.urlsafe_b64encode(b'{"alg":"RS256","typ":"JWT"}').rstrip(b"=").decode()
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=").decode()
    return f"{header}.{body}.signature"


def test_decode_jwt_payload_returns_claims():
    token = _make_jwt({"sub": "auth0|abc123", "email": "user@example.com"})

    payload = decode_jwt_payload(token)

    assert payload == {"sub": "auth0|abc123", "email": "user@example.com"}


@pytest.mark.parametrize(
    "token",
    [
        "not-a-jwt",
        "only.two",
        "a.b.c.d",
        "header.!!!invalid-base64!!!.signature",
        _make_jwt(["not", "an", "object"]),
    ],
    ids=["no-dots", "two-segments", "four-segments", "bad-base64", "non-object-payload"],
)
def test_decode_jwt_payload_rejects_invalid_tokens(token):
    with pytest.raises(ValueError):
        decode_jwt_payload(token)


def test_user_id_from_token_returns_sub():
    token = {"id_token": _make_jwt({"sub": "auth0|abc123"})}

    assert user_id_from_token(token) == "auth0|abc123"


@pytest.mark.parametrize(
    "token",
    [
        {},
        {"access_token": "opaque"},
        {"id_token": "not-a-jwt"},
        {"id_token": _make_jwt({"email": "user@example.com"})},
        {"id_token": _make_jwt({"sub": ""})},
    ],
    ids=["empty", "no-id-token", "malformed-id-token", "no-sub-claim", "empty-sub"],
)
def test_user_id_from_token_returns_none(token):
    assert user_id_from_token(token) is None


def test_async_connector_exposes_user_id(eon_home_config):
    connector = AsyncGridboxConnector(eon_home_config)

    assert connector.user_id is None

    connector.token = {"id_token": _make_jwt({"sub": "auth0|abc123"})}

    assert connector.user_id == "auth0|abc123"
