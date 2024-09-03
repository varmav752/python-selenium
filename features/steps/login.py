import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the Demo Login Page')
def step_impl(context):
    print("I a execruting ")
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account {user} into the Username field and the Password field')
def step_impl(context, user):
    credentials = {
        "StandardUser": ("standard_user", "secret_sauce"),
        "LockedOutUser": ("locked_out_user", "secret_sauce")
    }
    username, password = credentials[user]
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)

@when('I click the Login Button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('I am redirected to the Demo Main Page')
def step_impl(context):

    WebDriverWait(context.driver, 10).until(EC.url_contains("inventory.html"))

@then('I verify the App Logo exists')
def step_impl(context):
    logo = context.driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed()


@then('I verify the Error Message contains the text "{error_message}"')
def step_impl(context, error_message):
    time.sleep(1)
    error_banner = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )
    assert error_message in error_banner.text