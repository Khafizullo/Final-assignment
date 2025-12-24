Feature: Product management

Scenario: List all products
    Given I have some products
    When I request the list of products
    Then I should see all products
