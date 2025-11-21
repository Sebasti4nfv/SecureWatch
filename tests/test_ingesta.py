def test_ingesta_publica_en_kafka(client, mocker):
    mock_kafka = mocker.patch("app.main.producer.send")
    
    payload = {"source": "firewall", "log": "Blocked IP 1.2.3.4"}
    response = client.post("/api/v1/logs", json=payload, headers={"x-client-id": "demo"})
    
    assert response.status_code == 200
    mock_kafka.assert_called_once()