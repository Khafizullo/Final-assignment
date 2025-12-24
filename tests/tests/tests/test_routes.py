def test_list_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200
