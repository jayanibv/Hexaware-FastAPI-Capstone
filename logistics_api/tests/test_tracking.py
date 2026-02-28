import pytest
def test_get_tracking_history(client, customer_token, agent_token):
    # Create
    resp = client.post(
        "/shipments",
        json={"source_address": "A", "destination_address": "B"},
        headers={"Authorization": f"Bearer {customer_token}"}
    )
    tracking = resp.json()["tracking_number"]
    
    # Update
    client.post(
        f"/tracking/{tracking}",
        json={"location": "W1", "status": "SHIPPED"},
        headers={"Authorization": f"Bearer {agent_token}"}
    )
    
    # History
    response = client.get(
        f"/tracking/{tracking}",
        headers={"Authorization": f"Bearer {customer_token}"}
    )
    assert response.status_code == 200
    assert len(response.json()) >= 2  # Created + Shipped
