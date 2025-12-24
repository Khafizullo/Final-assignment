import factory
from service.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker('word')
    category = factory.Faker('word')
    price = factory.Faker('random_number', digits=5)
    available = factory.Faker('boolean')
