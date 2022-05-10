from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(3)

# # 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved ", value)  # 3000

# # 2. Scroll down page till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved ", value) #5092

#3A. Scroll down page till end:
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved ", value)#0
# time.sleep(3)


#3B.Scroll up to statrting position:
driver.execute_script("window.scrollBy(0, - document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved ", value)
time.sleep(3)
driver.quit()
