from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Captures cookies from web browser
cookies = driver.get_cookies()
print("Size of cookies: ", len(cookies))  # 3

# Print details of all cookies:
for each in cookies:
    # print(each)
    print(each.get('name'), ":", each.get('value'))

# Add new cookie:
driver.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = driver.get_cookies()
print("After adding new one: ", len(cookies))  # 4

# Delete specific cookie from browser:
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("After deleting cookies:", len(cookies))  # 3

# Delete all the cookies:
cookies = driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Deleteted all cookies:", len(cookies))  # 0
driver.quit()
