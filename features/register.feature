Feature: Register User to Website

  Scenario: Successful User Registration
    Given I am on the home page
    When I click on the 'signup/login' button
    Then It should be visible the message: 'New User Signup'
    When I enter my name and email address
    And I click the 'signup' button
    Then It should be visible the message: 'ENTER ACCOUNT INFORMATION'
    When I fill the title, password and date of birth
    And I select the checkbox 'Sign up for our newsletter!'
    And I select the checkbox 'Receive special offers from our partners!'
    And I fill the first name, last name, company, address, country, state, city, zipcode and mobile number
    And I click 'create account' button
    Then I should receive the message: 'ACCOUNT CREATED!'
    When I click 'continue' button

  Scenario: Delete User
    Given I am logged in the home page
    Then It should be visible the message: 'Logged in as'
    When I click 'delete account' button
    Then I should receive the message: 'ACCOUNT DELETED!'

  Scenario: Successful Verification User Registration with existing email
    Given I am on the main page
    When I click on the login button
    Then It should be visible the message: New User Signup
    When I fill with registered name and registered email address
    And I click the signup button
    Then I should receive the error: 'Email Address already exist!

#  Scenario: Successful Place the Order while Registering the User at Checkout
#    Given I am on the home page
#    When I add products to cart
#    And I click on the 'view cart' button
#    Then I should be redirected to the cart page
#    When I click 'proceed to checkout' button
#    And I click 'register / login' button
#    Then It should be visible the message: 'ENTER ACCOUNT INFORMATION'
#    When I fill the title, name, email, password and date of birth
#    And I select the checkbox 'Sign up for our newsletter!'
#    And I select the checkbox 'Receive special offers from our partners!'
#    And I fill the first name, last name, company, address, country, state, city, zipcode and mobile number
#    And I click 'create account' button
#    Then I should receive the message: 'ACCOUNT CREATED!'
#    When I click 'continue' button
#    Then It should be visible the message: 'Logged in as Ionut'
#    When I 'proceed to checkout' button
#    Then It should be visible the message 'Address Details'
#    When I enter description in comment text area
#    And I enter name on card, card cumber, cvc, expiration date
#    And I click 'pay and confirm order' button
#    Then I should receive the message: 'Your order has been placed successfully!'
#    When I click 'delete account' button
#    Then I should receive the message: 'ACCOUNT DELETED!'
