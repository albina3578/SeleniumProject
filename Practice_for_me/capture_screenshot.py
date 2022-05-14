from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
import os

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # max wait time for all find element steps
print("Browser initialized.Opening the website...")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.save_screenshot("C:\\dev\\SeleniumProject\\Practice_for_me\\homepage.png") #1st way
# driver.save_screenshot(os.getcwd() + "\\homepage.png") #2nd way
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.quit()
