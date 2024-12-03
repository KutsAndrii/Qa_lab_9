from behave import given, when, then

# Scenario: Successful registration
@given('I am on the registration page')
def step_on_registration_page(context):
    # Code to navigate to the registration page
    context.page = "registration"
    print("Navigated to the registration page.")

@when('I submit the registration form with valid data')
def step_submit_valid_registration_form(context):
    # Code to fill in and submit a valid registration form
    context.form_submission = "valid"
    print("Submitted registration form with valid data.")

@then('I should be redirected to the inventory page')
def step_redirect_to_inventory_page(context):
    # Code to verify redirection to the inventory page
    if context.form_submission == "valid":
        context.page = "inventory"
        print("Redirected to the inventory page.")
    else:
        raise AssertionError("Not redirected to the inventory page.")

# Scenario: Password mismatch
@when('I submit the registration form with mismatched passwords')
def step_submit_mismatched_passwords(context):
    # Code to simulate submitting the form with mismatched passwords
    context.form_submission = "password_mismatch"
    print("Submitted registration form with mismatched passwords.")

@then('I should see an error message "Passwords do not match"')
def step_see_password_mismatch_error(context):
    # Code to verify the error message is displayed
    if context.form_submission == "password_mismatch":
        context.error_message = "Passwords do not match"
        print("Error: Passwords do not match.")
    else:
        raise AssertionError("Expected error message not found.")

# Scenario: Existing email
@when('I submit the registration form with an already registered email')
def step_submit_existing_email(context):
    # Code to simulate submitting the form with an existing email
    context.form_submission = "email_exists"
    print("Submitted registration form with an already registered email.")

@then('I should see an error message "This email is already registered"')
def step_see_existing_email_error(context):
    # Code to verify the error message for existing email
    if context.form_submission == "email_exists":
        context.error_message = "This email is already registered"
        print("Error: This email is already registered.")
    else:
        raise AssertionError("Expected error message not found.")
