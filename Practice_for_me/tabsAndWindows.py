from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()

# reglink = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(reglink)

#Opens new tab or window:
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)
driver.switch_to.new_window('window')
# driver.switch_to.new_window('tab')
driver.get("https://orangehrm.com/")