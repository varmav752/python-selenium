import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the inventory page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(context.driver, 10).until(EC.url_contains("inventory.html"))

@when('user sorts products from high price to low price')
def step_impl(context):
    time.sleep(2)
    sort_dropdown = context.driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_dropdown.click()
    # Select "Price (high to low)"
    sort_dropdown.find_element(By.XPATH, "//option[@value='hilo']").click()

@when('user adds highest priced product')
def step_impl(context):
    time.sleep(2)
    # Find the first add-to-cart button after sorting
    add_to_cart_button = context.driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]//button")
    add_to_cart_button.click()

@when('user clicks on cart')
def step_impl(context):
    time.sleep(20)
    cart_button = context.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    WebDriverWait(context.driver, 10).until(EC.url_contains("cart.html"))

@when('user clicks on checkout')
def step_impl(context):
    time.sleep(20)
    checkout_button = context.driver.find_element(By.ID, "checkout")
    checkout_button.click()
    WebDriverWait(context.driver, 10).until(EC.url_contains("checkout-step-one.html"))

@when('user enters first name Alice')
def step_impl(context):
    time.sleep(2)
    first_name_field = context.driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Alice")

@when('user enters last name Doe')
def step_impl(context):
    time.sleep(2)
    last_name_field = context.driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Doe")

@when('user enters zip code 592')
def step_impl(context):
    time.sleep(2)
    zip_code_field = context.driver.find_element(By.ID, "postal-code")
    zip_code_field.send_keys("592")

@when('user clicks Continue button')
def step_impl(context):
    time.sleep(2)
    continue_button = context.driver.find_element(By.ID, "continue")
    continue_button.click()
    WebDriverWait(context.driver, 10).until(EC.url_contains("checkout-step-two.html"))

@then('I verify in Checkout overview page if the total amount for the added item is $49.99')
def step_impl(context):
    time.sleep(20)
    total_amount = context.driver.find_element(By.CLASS_NAME, "summary_total_label")
    assert "$49.99" in total_amount.text

@when('user clicks Finish button')
def step_impl(context):
    time.sleep(20)
    finish_button = context.driver.find_element(By.ID, "finish")
    finish_button.click()
    WebDriverWait(context.driver, 10).until(EC.url_contains("checkout-complete.html"))

@then('Thank You header is shown in Checkout Complete page')
def step_impl(context):
    time.sleep(20)
    thank_you_header = context.driver.find_element(By.CLASS_NAME, "complete-header")
    assert "THANK YOU FOR YOUR ORDER" in thank_you_header.text
