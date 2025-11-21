def test_incidentes_requiere_jwt(client):
    response = client.get("/api/v1/incidentes")
    assert response.status_code == 401
