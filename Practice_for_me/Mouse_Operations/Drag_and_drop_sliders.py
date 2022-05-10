from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

# Minimum and Maximum Sliders:

min_sldr = driver.find_element(By.XPATH, "//body/div[2]/div[2]/span[1]")
max_sldr = driver.find_element(By.XPATH, "//body/div[2]/div[2]/span[2]")

# find location of the element:  Default
print("Location of sliders before moving......") 
print(min_sldr.location)  # {'x': 59, 'y': 250}
print(max_sldr.location)  # {'x': 670, 'y': 250}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_sldr, 100, 0).perform()
time.sleep(3)
act.drag_and_drop_by_offset(max_sldr, -70, 0).perform()
time.sleep(3)
print("Location of sliders after moving......")
print(min_sldr.location)
print(max_sldr.location)

driver.quit()
