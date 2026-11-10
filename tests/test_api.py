def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_create_booking(client):
    response = client.post("/api/bookings", json={
        "guest_name": "Asha Rao",
        "email": "asha@example.com",
        "check_in": "2027-01-10",
        "check_out": "2027-01-12",
        "guests": 2
    })
    assert response.status_code == 201
    assert response.get_json()["booking"]["guests"] == 2

def test_reject_checkout_before_checkin(client):
    response = client.post("/api/bookings", json={
        "guest_name": "Asha Rao",
        "email": "asha@example.com",
        "check_in": "2027-01-12",
        "check_out": "2027-01-10"
    })
    assert response.status_code == 400

def test_reject_missing_fields(client):
    response = client.post("/api/bookings", json={"guest_name": "Asha"})
    assert response.status_code == 400
