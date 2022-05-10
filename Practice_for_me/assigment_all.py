from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

# initializing the chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)  # max wait time for all find windows
driver.get("https://www.dummyticket.com")
time.sleep(3)

# buy_ticket = driver.find_element(By.XPATH, "//a[contains(text(),'Buy Ticket')]").click()  # 1 option open buyticket
driver.find_element(By.PARTIAL_LINK_TEXT, "Buy Ticket").click()  ## 2nd option or open buyticket by LINK
# dummy_ticket = driver.find_element(By.XPATH, "//*[@id='checkout-products']/li[1]").click()

# choose the 1st checkbox $1200
dummy_ticket_btn = driver.find_element(By.XPATH, "//*[@id='product_549']").click()

# add passenger details:
fname = driver.find_element(By.XPATH, "//*[@id='travname']").send_keys("John")  # add first name
lname = driver.find_element(By.XPATH, "//*[@id='travlastname']").send_keys("Dow")  # add last name

# pick Date of birt dropdown:
driver.find_element(By.XPATH, "//*[@id='dob']").click()  # opens datepicker
datepicker_month = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text('Dec')
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("1990")
alldates = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in alldates:
    if date.text == "25":
        date.click()
        break
# driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/button[2]").click()
time.sleep(5)

# pick sex male:
driver.find_element(By.XPATH, "//*[@id='sex_1']").click()
time.sleep(5)
# Travel Details:
driver.find_elements(By.XPATH, "//*[@id='traveltype_field']")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='traveltype_2']").click()
time.sleep(3)
# From City:
driver.find_element(By.XPATH, "//*[@id='fromcity']").send_keys("Dallas")
time.sleep(5)
# To City:
driver.find_element(By.XPATH, "//*[@id='tocity']").send_keys("New York")
# Date Departure:
driver.find_element(By.XPATH, "//*[@id='departon']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']").click()  # opens datepicker
date_dep_month = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
date_dep_month.select_by_visible_text('Jun')
date_dep_year = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
date_dep_year.select_by_visible_text("2022")
alldates_deps = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in alldates_deps:
    if date.text == "15":
        date.click()
        break
# driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[2]/button[2]").click()
# time.sleep(10)
# # Delivery Options:
# del_opt = Select(driver.find_element(By.XPATH, "//select[@id='reasondummy']"))
# del_opt.select_by_value("4")

time.sleep(15)
driver.quit()
