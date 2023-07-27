from behave import *

from pages.register_user_page import RegisterUser


@given ("I am on the main page")
def step_impl(context):
    context.page = RegisterUser()
    context.page.load_url(str(context.config.userdata['home_url']))

@when ("I click on the login button")
def step_imp(context):
    context.page.click(str(context.config.userdata["signup_login_xpath_button"]))

@then ("It should be visible the message: New User Signup")
def step_imp(context):
    assert str(context.page.get_text(str(context.config.userdata['user_signup_text'])) == f"{str(context.config.userdata['user_signup_text'])}")

@when ("I fill with registered name and registered email address")
def step_imp(context):
    context.page.fill_text(str(context.config.userdata["registered_name"]), str(context.config.userdata["name_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["registered_email"]), str(context.config.userdata["email_xpath_form"]))

@when ("I click the signup button")
def step_imp(context):
    context.page.click(str(context.config.userdata["signup_xpath_button"]))

@then ("I should receive the error: 'Email Address already exist!")
def step_imp(context):
    assert str(context.page.get_text(str(context.config.userdata['email_exist_text'])) == f"{str(context.config.userdata['email_exist_text'])}")
