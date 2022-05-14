from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # max wait time for all find element steps

print("Browser initialized.Opening the website...")
driver.get("https://www.google.com")
driver.switch_to.new_window('window')
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# driver.close()
