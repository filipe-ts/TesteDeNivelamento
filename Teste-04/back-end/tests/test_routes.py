def test_health_check(test_client):
    response = test_client.get('/health/')
    assert response.status_code == 200
    assert b'Healthy!' in response.data

def test_search_by_cnpj(test_client):
    valid_cnpj = {'CNPJ':'195'}

    response = test_client.post('operadoras/searchByCNPJ/', json=valid_cnpj)
    assert response.status_code == 200
    assert response.json['operadoras'] == '41788751000100'