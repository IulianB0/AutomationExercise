from behave import *

from pages.register_user_page import RegisterUser


@given ("I am logged in the home page")
def step_impl(context):
    context.page = RegisterUser()
    context.page.load_url(str(context.config.userdata['home_url']))

@then("It should be visible the message: 'Logged in as'")
def step_imp(context):
    assert str(context.page.get_text(str(context.config.userdata['user_logged_text'])) == f"{str(context.config.userdata['user_logged_text'])}")
@when ("I click 'delete account' button")
def step_imp(context):
    context.page.click(str(context.config.userdata["delete_button"]))

@then ("I should receive the message: 'ACCOUNT DELETED!'")
def step_imp(context):
    assert str(context.page.get_text(str(context.config.userdata['account_deleted_text'])) == f"{str(context.config.userdata['account_deleted_text'])}")