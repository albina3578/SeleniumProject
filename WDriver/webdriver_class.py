# WDriver package webdriver_class.py module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initializing the chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)  # max wait time for all find windows
driver.get("https://demoqa.com/browser-windows")
time.sleep(3)

print("Driver.current_url; ", driver.current_url)
print("Driver.window_handle: ", driver.current_window_handle)
#
# # refresh, back,forward
driver.back()
driver.refresh()
print("Driver.current_url; ", driver.current_url)
driver.forward()
print("Driver.current_url; ", driver.current_url)
time.sleep(2)
print("Window handles and multiple windows/tabs")
# driver.find_element(By.XPATH, "//button[@id='tabButton']")
# driver.find_element(By.CSS_SELECTOR, "tabButton")
driver.find_element(By.ID, "tabButton").click()
time.sleep(2)
print("Driver.window_handles: ", driver.window_handles)
print("Driver.current_url; ", driver.current_url)
print("##switching to a new tab...")
# new_tab_name=driver.window_handles[1]
# driver.switch_to.window(new_tab_name)
driver.switch_to.window(driver.window_handles[-1])  # switching to last tab
time.sleep(2)

print("##switching to alert")
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "promtButton").click()
alert = driver.switch_to.alert
time.sleep(2)
print("Clicking the OK Button...")
alert.accept()  # clicking ok button
time.sleep(2)

print("##Clicking the cancel to alert")
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "promtButton").click()
alert = driver.switch_to.alert
time.sleep(2)
alert.dismiss()  # clicking cancel button
time.sleep(2)

print("##Entering the Alert text")
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, "promtButton").click()
alert = driver.switch_to.alert
alert.send_keys("John Doe")
alert.accept()
time.sleep(2)
print("Other attributes:    .......")
print("driver name:  ", driver.name)
print("driver title: ", driver.title)
print("Closing the browser completely")
time.sleep(2)
driver.quit()
# What is property???
# class Abc():
#     name = ' '
#
#     @property
#     def title(self):
#         return "this is the title"
#
#
#     @property
#     def title_xpath(self):
#         return f"//div[@id='title]"
# abc = Abc()
# print(abc.title)
