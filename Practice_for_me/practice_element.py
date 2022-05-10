from selenium import webdriver
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

# Admin-->--UserManagment-->Users
driver.find_element(By.XPATH, "//a[@id='menu_admin_viewAdminModule']").click()
driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH, "//a[@id='menu_admin_viewSystemUsers']").click()
time.sleep(2)
# Get Username &UserRole and print ESS
rows = (len(driver.find_elements(By.XPATH, "//table[@id='resultTable']//tbody/tr")))
print("Total Rows: ", rows)
count = 0
for r in range(1, rows + 1):
    status = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[3]").text
    if status == "ESS":
        count = count + 1

print("Total number of users: ", rows)
print("Number of ESS users: ", count)
print("Number of Admin: ", (rows-count))