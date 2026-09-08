import pytest
from app.api_request import fetch_my_ip, fetch_target_ip


@pytest.mark.asyncio
async def test_real_my_ip_api():
    """Verify that the application can fetch IP information from the API."""

    result = await fetch_my_ip()

    assert result is not None
    assert "ip" in result

    print(f"\nDetected IP: {result['ip']}")


@pytest.mark.asyncio
async def test_real_target_ip_api():
    """Verify that the application can fetch information for a target IP."""

    result = await fetch_target_ip("8.8.8.8")

    assert result is not None
    assert "ip" in result
    assert result["ip"] == "8.8.8.8"

    print(f"\nTarget IP: {result['ip']}")