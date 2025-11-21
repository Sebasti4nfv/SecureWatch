def test_alertas_se_envia_incidente_critico(client, mocker):
    mock_notifier = mocker.patch("app.alertas.enviar_telegram")
    
    incidente = {"severidad": "critical"}
    client.post("/api/v1/internos/alertas", json=incidente)
    
    mock_notifier.assert_called_once()
