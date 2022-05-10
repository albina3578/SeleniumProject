import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
# 1. Count num of rows &columns
# num_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
#
# num_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
# print("Num of Columns:", num_of_columns)  # 4
# print("Num of Rows:", num_of_rows)  # 7
#
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# # print(data)
#
# # Read all the rows and columnsdata
# print("Printing all the rows and columns......")
#
# # for r in range(2, num_of_rows + 1):
# #     for c in range(1, num_of_columns + 1):
# #         data = driver.find_element(By.XPATH,
# #                                    "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
# #         print(data, end='  ')
# #     print()
#
# # 4. Read data based by book names Mukesh
# for r in range(2, num_of_rows + 1):
#     authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
#     if authorName == "Mukesh":
#         bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
#         price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
#         print(bookName, "   ", authorName, "  ", price)
#
#     # driver.close()
# LOGIN:
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)
# Admin-->usermangmentt-->users
driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']").click()
# total#ofrows
rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody/tr"))
print("Total number of rows in a table: ", rows)
count = 0
for r in range(1, rows + 1):
    status = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[5]").text
    if status == "Enabled":
        count = count + 1

print("Total number of users: ", rows)
print("Number of enabled users: ", count)
print("Number of disabled users: ", (rows-count))