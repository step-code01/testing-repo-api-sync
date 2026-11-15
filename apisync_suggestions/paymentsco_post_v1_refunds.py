"""Suggested integration helper for PaymentsCo POST /v1/refunds."""

from __future__ import annotations

from typing import Any

import requests


def call_post_v1_refunds(base_url: str, headers: dict[str, str] | None = None, json: dict[str, Any] | None = None) -> requests.Response:
    """Call POST /v1/refunds introduced in PaymentsCo."""
    url = f"{base_url.rstrip('/')}/v1/refunds"
    return requests.request('POST', url, headers=headers, json=json, timeout=15.0)
