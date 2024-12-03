Feature: User Registration
  As a new user, I want to register on the platform to gain access to the inventory.

  Scenario: Successful registration
    Given I am on the registration page
    When I submit the registration form with valid data
    Then I should be redirected to the inventory page

  Scenario: Password mismatch
    Given I am on the registration page
    When I submit the registration form with mismatched passwords
    Then I should see an error message "Passwords do not match"

  Scenario: Existing email
    Given I am on the registration page
    When I submit the registration form with an already registered email
    Then I should see an error message "This email is already registered"
