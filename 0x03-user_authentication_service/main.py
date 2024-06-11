#!/usr/bin/env python3
"""A simple end-to-end (E2E) integration test for `app.py`.
"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """Tests registering a user."""
    url = f"{BASE_URL}/users"
    body = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, json=body)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}
    res = requests.post(url, json=body)
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests logging in with a wrong password."""
    url = f"{BASE_URL}/sessions"
    body = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, json=body)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """Tests logging in."""
    url = f"{BASE_URL}/sessions"
    body = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, json=body)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "logged in"}
    return res.cookies.get('session_id')


def profile_unlogged() -> None:
    """Tests retrieving profile information whilst logged out."""
    url = f"{BASE_URL}/profile"
    res = requests.get(url)
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """Tests retrieving profile information whilst logged in."""
    url = f"{BASE_URL}/profile"
    req_cookies = {
        'session_id': session_id,
    }
    res = requests.get(url, cookies=req_cookies)
    assert res.status_code == 200
    assert "email" in res.json()


def log_out(session_id: str) -> None:
    """Tests logging out of a session."""
    url = f"{BASE_URL}/sessions"
    req_cookies = {
        'session_id': session_id,
    }
    res = requests.delete(url, cookies=req_cookies)
    assert res.status_code == 200
    assert res.json() == {"message": "session deleted"}


def reset_password_token(email: str) -> str:
    """Tests requesting a password reset."""
    url = f"{BASE_URL}/reset_password"
    body = {'email': email}
    res = requests.post(url, json=body)
    assert res.status_code == 200
    assert res.json().get("email") == email
    assert "reset_token" in res.json()
    return res.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests updating a user's password."""
    url = f"{BASE_URL}/reset_password"
    body = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password,
    }
    res = requests.put(url, json=body)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
