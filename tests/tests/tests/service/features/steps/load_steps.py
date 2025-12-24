from behave import given
from tests.factories import ProductFactory

@given("I have some products")
def step_impl(context):
    context.products = [ProductFactory() for _ in range(5)]
