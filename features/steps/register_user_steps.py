from behave import *

from pages.register_user_page import RegisterUser


@given("I am on the home page")
def step_impl(context):
    context.page = RegisterUser()
    context.page.load_url(str(context.config.userdata['home_url']))

@when("I click on the 'signup/login' button")
def step_imp(context):
    context.page.click(str(context.config.userdata["signup_login_xpath_button"]))

@then("It should be visible the message: 'New User Signup'")
def step_imp(context):
    assert str(context.page.get_text(str(context.config.userdata['user_signup_text'])) == f"{str(context.config.userdata['user_signup_text'])}")

@when ("I enter my name and email address")
def step_imp(context):
    context.page.fill_text(str(context.config.userdata["first_name"]), str(context.config.userdata["name_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["email"]), str(context.config.userdata["email_xpath_form"]))

@when ("I click the 'signup' button")
def step_imp(context):
    context.page.click(str(context.config.userdata["signup_xpath_button"]))

@then ("It should be visible the message: 'ENTER ACCOUNT INFORMATION'")
def step_imp(context):
    assert str(context.page.get_text(str(context.config.userdata['account_info_text'])) == f"{str(context.config.userdata['account_info_text'])}")

@when ("I fill the title, password and date of birth")
def step_imp(context):
    context.page.click(str(context.config.userdata["title_xpath_button"]))
    context.page.fill_text(str(context.config.userdata["password"]), str(context.config.userdata["password_xpath_form"]))
    context.page.click(str(context.config.userdata["birth_day_xpath_button"]))
    context.page.click(str(context.config.userdata["birth_month_xpath_button"]))
    context.page.click(str(context.config.userdata["birth_year_xpath_button"]))

@when ("I select the checkbox 'Sign up for our newsletter!'")
def step_imp(context):
    context.page.click(str(context.config.userdata["newsletter_xpath_button"]))

@when ("I select the checkbox 'Receive special offers from our partners!'")
def step_imp(context):
    context.page.click(str(context.config.userdata["offers_xpath_button"]))

@when ("I fill the first name, last name, company, address, country, state, city, zipcode and mobile number")
def step_imp(context):
    context.page.fill_text(str(context.config.userdata["first_name"]), str(context.config.userdata["first_name_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["last_name"]), str(context.config.userdata["last_name_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["company"]), str(context.config.userdata["company_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["address"]), str(context.config.userdata["address_xpath_form"]))
    context.page.click(str(context.config.userdata["country_xpath_button"]))
    context.page.fill_text(str(context.config.userdata["state"]), str(context.config.userdata["state_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["city"]), str(context.config.userdata["city_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["zipcode"]), str(context.config.userdata["zipcode_xpath_form"]))
    context.page.fill_text(str(context.config.userdata["mobile_nr"]), str(context.config.userdata["mobile_nr_xpath_form"]))

@when ("I click 'create account' button")
def step_imp(context):
    context.page.click(str(context.config.userdata["create_account_button"]))

@then ("I should receive the message: 'ACCOUNT CREATED!'")
def step_imp(context):
    assert str(context.page.get_text(str(context.config.userdata['account_created_text'])) == f"{str(context.config.userdata['account_created_text'])}")

@when ("I click 'continue' button")
def step_imp(context):
    context.page.click(str(context.config.userdata["continue_button"]))