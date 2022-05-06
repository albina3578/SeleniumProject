from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initializing the chrome driver
driver = webdriver.Chrome()
#
# # test scenario starts here
driver.get("https://www.google.com/")
driver.maximize_window()
searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('Selenium')
searchbox.submit()

time.sleep(3)
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
time.sleep(3)
driver.quit()
