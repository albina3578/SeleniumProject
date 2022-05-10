from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(3)

driver.switch_to.frame(0)  # switch to frame
# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("05/30/2023")# mm/dd/yyyy

# 2 Logic
year = "2021"
month = "May"
date = "30"
driver.find_element(By.XPATH, "//*[@id='datepicker']").click()  # will open datepicker element

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # next arrow
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  # Previos arrow-old date


# 3 select date
dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break


time.sleep(3)
driver.quit()