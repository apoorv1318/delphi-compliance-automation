import requests
import pytest

BASE_URL = "https://compliance.whyqtech.com"  # Verify if this is correct


@pytest.fixture
def get_headers():
    return {"Content-Type": "application/json"}


def test_login_valid_credentials(get_headers):
    """Test login with valid email and password"""
    payload = {"email": "test@gmail.com", "password": "Kishan@1"}

    response = requests.post(f"{BASE_URL}/auth/login", data=payload, headers=get_headers)

    # 🔍 Debugging Info
    print("Request URL:", f"{BASE_URL}/auth/login")
    print("Response Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Text:", response.text)

    assert response.status_code == 200, "Login failed with valid credentials"
    assert "token" in response.json(), "Token not received"
