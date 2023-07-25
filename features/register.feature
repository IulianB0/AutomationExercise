Feature: Register User to Website

  Scenario: Successful Verification User Registration with existing email
    Given I am on the signup page
    When I enter my registered name and email address
    And I click the signup button
    Then I should receive the error: 'Email Address already exist!

#  Scenario: Successful Place the Order while Registering the User at Checkout
#    Given
#    When
#    And
#    Then

