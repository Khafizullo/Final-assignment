def test_create_product(db_session):
    product = ProductFactory()
    db_session.add(product)
    db_session.commit()
    assert product.id is not None

def test_find_by_name(db_session):
    product = ProductFactory(name="TestProduct")
    db_session.add(product)
    db_session.commit()
    found = Product.query.filter_by(name="TestProduct").first()
    assert found.name == "TestProduct"
