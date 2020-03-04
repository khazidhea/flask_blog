def test_index(client):
    resp = client.get('/')
    assert resp.data
