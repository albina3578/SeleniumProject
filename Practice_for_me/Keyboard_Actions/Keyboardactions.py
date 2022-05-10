# Ctrl+A select text
# Ctrl+C copy text
# Tab go to next text box
# Ctrl+V paste text

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("Welcome to Selenium")
time.sleep(3)
act = ActionChains(driver)
# input1-->ctrl+A -->select the text
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input1 -->Ctrl+C Copy text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press TAB Key to navigate to input2 box
act.send_keys(Keys.TAB).perform()

# input2 -->press CtrlV Past the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)
driver.quit()
