import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# 1. Count num of rows &columns
num_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))

num_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
print("Num of Columns:", num_of_columns)  # 4
print("Num of Rows:", num_of_rows)  # 7

data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# Read all the rows and columnsdata
print("Printing all the rows and columns......")

# for r in range(2, num_of_rows + 1):
#     for c in range(1, num_of_columns + 1):
#         data = driver.find_element(By.XPATH,
#                                    "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
#         print(data, end='  ')
#     print()

#4. Read data based by book names Mukesh

driver.close()