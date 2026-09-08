from streamlit.testing.v1 import AppTest
from unittest.mock import patch
import pytest


@pytest.fixture
def app():
    return AppTest.from_file("../app/streamlit_app.py", default_timeout=10)


def test_app_loads(app):
    """UI-01: Verify that the application loads successfully."""

    with patch("app.api_request.fetch_my_ip") as mock_fetch:

        mock_fetch.return_value = {
            "ip": "203.0.113.10",
            "currency": "PHP",
            "country": "PH",
            "country_name": "Philippines",
            "asn": "AS12345",
            "region": "Metro Manila",
            "city": "Manila",
            "latitude": 14.5995,
            "longitude": 120.9842,
            "timezone": "Asia/Manila",
            "postal": "1000"
        }

        app.run()

        assert not app.exception


def test_my_ip_page(app):
    """UI-02: Verify that the My IP page displays correctly."""

    with patch("app.api_request.fetch_my_ip") as mock_fetch:

        mock_fetch.return_value = {
            "ip": "203.0.113.10",
            "currency": "PHP",
            "country": "PH",
            "country_name": "Philippines",
            "asn": "AS12345",
            "region": "Metro Manila",
            "city": "Manila",
            "latitude": 14.5995,
            "longitude": 120.9842,
            "timezone": "Asia/Manila",
            "postal": "1000"
        }

        app.run()

        assert not app.exception
        assert "My IP" in app.sidebar.radio[0].options


def test_search_ip_page(app):
    """UI-05: Verify that the Search IP page appears."""

    with patch("app.api_request.fetch_my_ip") as mock_fetch:

        mock_fetch.return_value = {
            "ip": "203.0.113.10"
        }

        app.run()

        app.sidebar.radio[0].set_value("Search IP").run()

        assert not app.exception
        assert len(app.text_input) == 1
        assert len(app.button) >= 1


def test_empty_ip_search(app):
    """UI-06: Verify warning when search is submitted without an IP."""

    with patch("app.api_request.fetch_my_ip") as mock_my_ip:

        mock_my_ip.return_value = {
            "ip": "203.0.113.10"
        }

        app.run()

        app.sidebar.radio[0].set_value("Search IP").run()

        app.button[0].click().run()

        assert not app.exception
        assert any(
            "Please enter an IP address." in warning.value
            for warning in app.warning
        )