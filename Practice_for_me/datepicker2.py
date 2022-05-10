from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='dob']").click()  # opens date picker

datepicker_month = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec")
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("1990")

all_dates = driver.find_elements(By.XPATH, "//div[@id='ui/datepicker-div']//tabletbody/tr/td/a")

for date in all_dates:
    if date.text == "25":
        date.click()
    break
time.sleep(20)
driver.quit()