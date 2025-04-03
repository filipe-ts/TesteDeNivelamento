def test_health_check(test_client):
    response = test_client.get('/health/')
    assert response.status_code == 200
    assert b'Healthy!' in response.data

def test_search_by_cnpj(test_client):
    # erro ao enviar apenas o dado
    valid_cnpj = {'CNPJ':'195'}

    response = test_client.post('operadoras/search/', json=valid_cnpj)
    assert response.status_code == 400

    # acerto ao procurar por cnpj parcial
    valid_msg = {'search': 'CNPJ', 'value':'195'}

    response = test_client.post('operadoras/search/', json=valid_msg)
    assert response.status_code == 200
    assert response.json['pagination']['total_items'] == 15

    # acerto ao procurar por cnpj completo
    valid_msg = {'search': 'CNPJ', 'value': '41788751000100'}

    response = test_client.post('operadoras/search/', json=valid_msg)
    assert response.status_code == 200
    assert response.json['pagination']['total_items'] == 1

    # acerto ao procurar por nome fantasia parcial
    valid_msg = {'search': 'Nome_Fantasia', 'value': 'AIRES'}

    response = test_client.post('operadoras/search/', json=valid_msg)
    assert response.status_code == 200
    assert response.json['pagination']['total_items'] == 1

    # errr ao procurar por nome fantasia parcial com parametro search incorreto
    invalid_msg = {'search': 'NomeFantasia', 'value': 'AIRES'}

    response = test_client.post('operadoras/search/', json=invalid_msg)
    assert response.status_code == 400
