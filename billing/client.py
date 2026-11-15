import requests

BASE_URL = "https://api.paymentsco.com"


def cancel_charge(charge_id: str) -> requests.Response:
    # Breaking in v2: DELETE /v1/charges is replaced by DELETE /v2/charges (auto-patched via PR)
    return requests.delete(f"{BASE_URL}/v1/charges")


def list_payments() -> requests.Response:
    # Breaking in v2: 'currency' query param is removed (auto-patched via PR)
    return requests.get(f"{BASE_URL}/v1/payments", params={"currency": "usd", "limit": 10})


def create_payment(amount: int) -> requests.Response:
    # Breaking in v2: required 'currency' body field added (flagged as Manual Fix Needed)
    return requests.post(f"{BASE_URL}/v1/payments", json={"amount": amount})