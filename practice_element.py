# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://itera-qa.azurewebsites.net/home/automation")
# driver.maximize_window()
# time.sleep(3)
#
# # driver.find_element(By.XPATH, "//input[@id='monday']").click()
#
# checkboxes = driver.find_elements(By.XPATH, "//input[@type ='checkbox' and contains(@id,'day')]")
# print(len(checkboxes))
# # Approach 1:
# # for i in range(len(checkboxes)):
# #     checkboxes[i].click()
#
# # Approaxh2:
# for checkbox in checkboxes:
#     checkbox.click()
# time.sleep(3)
# # Approach3: multiple checkboxes
# # for checkbox in checkboxes:
# #     weekname = checkbox.get_attribute('id')
# #     if weekname == 'monday' or weekname == 'sunday':
# #         checkbox.click()
# # Approach4:select last 2 checkboxes
# # range(5,7)--->6,7
# # for i in range(len(checkboxes) - 2, len(checkboxes)):
# #     checkboxes[i].click()
#
# # Approach5:select first 2 checkboxes
# # range(5,7)--->6,7
# # for i in range(len(checkboxes)):
# #     if i < 2:
# #         checkboxes[i].click()
#
# # Approach 6: clear all the checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()
#
# time.sleep(3)
# driver.close()

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/ ")
driver.maximize_window()
time.sleep(3)

# Click on link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click() #do not try use

# Find total number of links in a page
# links = driver.find_elements(By.XPATH, '//a')
# print('Total number of links:', len(links))
#
# #print all 90 link names
# for link in links:
#     print(link.text)

# allLinks = driver.find_elements(By.TAG_NAME, 'a')
# count = 0
#
# for link in allLinks:
#     url = link.get_attribute('href')
#     try:
#         res = requests.head(url)
#     except:
#         None
#
#     if res.status_code >= 400:
#         print(url, 'is broken')
#         count += 1
#     else:
#         print(url, ' is valid link')
# print("Total number of broken link:", count)

# drpcountry_ele = driver.find_element(By.XPATH, "//select[@id='input-country']")
# drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("10")  # Argentina
# drpcountry.select_by_index(13) #index it`s a number

# all_options = drpcountry.options
# print("Total number of options:", len(all_options))

# for opt in all_options:
#     print(opt.text)

# select option from dropdown without using bild in functions: Need to write a logic
# for opt in all_options:
#     if opt.text == 'India':
#         opt.click()
#         break

windowIDs = driver.current_window_handle  # CDwindow-E81390E4B60810F7355164B6C35CD5C8
# CDwindow-CBFAE0D15EE7AB534B27576499CB0D85
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowsIDs = driver.window_handles
# parent_window_ID = windowsIDs[0] #CDwindow-74729343584FD45687AADACD061F6CF3
# child_window_ID = windowsIDs[1]  #CDwindow-98B1C0F129384E8DF35BB7AC56DC6351
#
# # print(parent_window_ID,child_window_ID)
# driver.switch_to.window(child_window_ID)
# print("child window:",driver.title)
#
# driver.switch_to.window(parent_window_ID)
# print("Parent window:",driver.title)
# # driver.close()

# for winid in windowsIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)
time.sleep(3)

for winid in windowsIDs:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM" and driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS":
        driver.close()
