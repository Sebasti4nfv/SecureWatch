def test_consulta_elasticsearch_rapida(mocker, client):
    fake_es = mocker.patch("app.search.es.search")
    fake_es.return_value = {"hits": {"hits": []}}
    
    response = client.get("/api/v1/search?source=firewall")
    
    assert response.status_code == 200
    fake_es.assert_called_once()
