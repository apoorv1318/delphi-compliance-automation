from utils.api_client import APIClient

def test_get_post():
    client = APIClient()
    response = client.get("/posts/1")

    assert response.status == 200
    assert response.json()["id"] == 1

    client.close()
