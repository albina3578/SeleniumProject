from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # max wait time for all find element steps
print("Browser initialized.Opening the website...")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
countrieslist = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countrieslist))

for country in countrieslist:
    if country.text == "Uzbekistan":
        country.click()
        break

time.sleep(3)
driver.quit()
