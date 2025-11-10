# tests/conftest.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 800},
        "locale": "pl-PL",
        "timezone_id": "Europe/Warsaw",
        # Jeśli Hotable prosi o lokalizację, można dodać:
        # "geolocation": {"longitude": 21.0122, "latitude": 52.2297},
        # "permissions": ["geolocation"],
    }
