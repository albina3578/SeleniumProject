from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(3)

# 1st LOGIN:
driver.find_element(By.XPATH, "//*[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()
time.sleep(2)

# Admin-->--User management-->Users
admin = driver.find_element(By.XPATH, "//a[@id='menu_admin_viewAdminModule']")
usermgmt = driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")

#MouseHover
#we need to create class, object of the class
act = ActionChains(driver)
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()