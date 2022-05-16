from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

# VARIABLE:
email = f"jdoe{time.strftime('%Y%m%d%H%M%S')}@mail.com"
url = "http://automationpractice.com"
first_name = 'John'
last_name = 'Doe'
password = "123456"

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # max wait time for all find element steps
print("Browser initialized.Opening the website...")
driver.get("http://automationpractice.com")
driver.maximize_window()
time.sleep(2)

print("----Test case Steps here----")
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
time.sleep(2)
print(" ----Verify 'authentication is in the url----")
assert 'authentication' in driver.current_url, print("Authentication page verified")

print("----Enter email in the Create and Account box----")
# email to register: 'jdoe20220510201805@mail.com'
print("----click 'create an account' button----")
print(f"email to register: '{email}'")
driver.find_element(By.ID, 'email_create').send_keys(email)
time.sleep(1)

print("click 'create an account' button")
driver.find_element(By.ID, 'SubmitCreate').click()

# print(" verify account creation url")

print("Filling Form: ")
print("select radio button 'Mr.'")
mr_title = driver.find_element(By.ID, "id_gender1")
mr_title.click()
time.sleep(1)
print(("MR is selected or not?", mr_title.is_selected()))
assert mr_title.is_selected(), "Title MR was not selected"

print("Enter First name: John")
driver.find_element(By.ID, 'customer_firstname').send_keys(first_name)

print("Enter Last name: Doe")
driver.find_element(By.ID, 'customer_lastname').send_keys(last_name)

print("Enter the email or click confirm")
driver.find_element(By.ID, "email").click()

print("Enter password '123456'")
driver.find_element(By.ID, "passwd").send_keys(password)
time.sleep(2)
print("Select Day '10'")
# # dropdown
drop_down = driver.find_element(By.ID, 'days')  # find element with Select tagname
selection = Select(drop_down)
selection.select_by_value('10')
time.sleep(2)

print("Select Months 'December'")
selection = Select(driver.find_element(By.ID, 'months'))
selection.select_by_value('12')
time.sleep(2)

print("Select Year '2000'")
selection = Select(driver.find_element(By.ID, 'years'))
selection.select_by_value('2000')
time.sleep(2)

print("Check 'Sign up for our newsletter' checkbox")
signup_checkbox = driver.find_element(By.ID, "newsletter")
signup_checkbox.click()
time.sleep(2)
assert signup_checkbox.is_selected(), "signup_checkbox verification failed"
time.sleep(2)
#
# print("verify First name under address")
# address_firstname = driver.find_element(By.ID, "firstname").text
# assert address_firstname.strip() == first_name
# # time.sleep(2)

print("Enter address: 123 Address st")
driver.find_element(By.ID, "address1").send_keys("123 Address st")
time.sleep(2)

print("Enter City: New York")
driver.find_element(By.ID, "city").send_keys("New York")
time.sleep(2)

print("Select state: New York")
selection = Select(driver.find_element(By.ID, "id_state"))
selection.select_by_visible_text('New York')
print("Selected first option", selection.first_selected_option)
time.sleep(2)

print("Enter zip code:11224")
driver.find_element(By.XPATH, "//input[@id='postcode']").send_keys("11224")
time.sleep(2)

print("Enter country: first country")
driver.find_element(By.ID, "id_country")
selection = Select(driver.find_element(By.ID, 'id_country'))
selection.select_by_index(1)
time.sleep(2)

print("Enter Home phone: ")
driver.find_element(By.ID, "phone").send_keys("917-897-5899")
time.sleep(2)

print("Enter Mobile phone: ")
driver.find_element(By.ID, "phone_mobile").send_keys("917-998-7775")
time.sleep(2)

print("REGISTER Button click now:")
driver.find_element(By.ID, "submitAccount").click()
time.sleep(3)
assert 'controller=my-account' in driver.current_url

print("closing the whole browser")
time.sleep(10)
driver.quit()

