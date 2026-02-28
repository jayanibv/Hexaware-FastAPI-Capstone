import pytest

def test_create_hub_admin(client, admin_token):
    response = client.post(
        "/hubs",
        json={
            "hub_name": "Central Hub",
            "city": "Metropolis"
        },
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert response.json()["hub_name"] == "Central Hub"

def test_get_all_hubs_admin(client, admin_token):
    response = client.get(
        "/hubs",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

