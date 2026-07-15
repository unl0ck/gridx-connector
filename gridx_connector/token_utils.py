"""Helpers for reading claims from OAuth/OIDC tokens."""

from __future__ import annotations

import base64
import json
from typing import Any


def decode_jwt_payload(token: str) -> dict[str, Any]:
    """Decode the payload segment of a JWT without verifying its signature.

    The token is only ever read from a response the identity provider just
    returned over TLS, so signature verification adds nothing here.

    Raises:
        ValueError: If the token is not a structurally valid JWT.
    """
    segments = token.split(".")
    if len(segments) != 3:
        raise ValueError("Token is not a JWT")
    payload_segment = segments[1]
    padding = "=" * (-len(payload_segment) % 4)
    try:
        payload = json.loads(base64.urlsafe_b64decode(payload_segment + padding))
    except ValueError as err:
        raise ValueError("Token payload is not base64url-encoded JSON") from err
    if not isinstance(payload, dict):
        raise ValueError("Token payload is not a JSON object")
    return payload


def user_id_from_token(token: dict[str, Any]) -> str | None:
    """Return the stable OIDC subject (``sub``) from a token response.

    Returns None when the response has no id_token, the id_token cannot be
    decoded, or it carries no ``sub`` claim.
    """
    id_token = token.get("id_token")
    if not id_token:
        return None
    try:
        payload = decode_jwt_payload(id_token)
    except ValueError:
        return None
    sub = payload.get("sub")
    return str(sub) if sub else None
