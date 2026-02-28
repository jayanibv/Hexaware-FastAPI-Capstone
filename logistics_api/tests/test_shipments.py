import pytest

def test_create_shipment(client, customer_token):
    response = client.post(
        "/shipments",
        json={
            "source_address": "Hub A",
            "destination_address": "Hub B"
        },
        headers={"Authorization": f"Bearer {customer_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "tracking_number" in data
    assert "id" in data
    assert isinstance(data["id"], int)

def test_get_shipment_details(client, customer_token):
    # Create first
    resp = client.post(
        "/shipments",
        json={"source_address": "A", "destination_address": "B"},
        headers={"Authorization": f"Bearer {customer_token}"}
    )
    tracking = resp.json()["tracking_number"]
    
    # Get details
    response = client.get(
        f"/shipments/{tracking}",
        headers={"Authorization": f"Bearer {customer_token}"}
    )
    assert response.status_code == 200
    assert response.json()["tracking_number"] == tracking

def test_cancel_shipment(client, customer_token):
    # Create
    resp = client.post(
        "/shipments",
        json={"source_address": "A", "destination_address": "B"},
        headers={"Authorization": f"Bearer {customer_token}"}
    )
    tracking = resp.json()["tracking_number"]
    
    # Cancel
    response = client.put(
        f"/shipments/{tracking}/cancel",
        headers={"Authorization": f"Bearer {customer_token}"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "CANCELLED"
