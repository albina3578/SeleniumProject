from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@id='HTML10']")

field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear()
time.sleep(3)
field1.send_keys("Hello Master!")
time.sleep(3)
button = driver.find_element(By.XPATH, "//button[contains(text(),'Copy Text')]")
act = ActionChains(driver)
act.double_click(button).perform()
time.sleep(3)
driver.quit()
