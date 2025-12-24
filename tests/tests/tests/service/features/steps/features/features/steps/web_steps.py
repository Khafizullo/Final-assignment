from behave import when, then

@when("I request the list of products")
def step_impl(context):
    context.response = context.client.get("/products")

@then("I should see all products")
def step_impl(context):
    assert len(context.response.json) == len(context.products)
