# WebElement properties and functions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)  # max wait time for all find windows
    # driver.get("http://automationpractice.com")
    # driver.find_element(By.ID, 'search_query_top')
    return driver


def webelement_properties(driver):
    driver.get("http://automationpractice.com")
    print("finding the multiple elements")
    product_names = driver.find_elements(By.XPATH, "//a[@class='product-name']")
    time.sleep(1)

    print("Using the webelement properties for each element")
    for prod_name in product_names:
        print("prod_name text:", prod_name.text)
        print("prod_name size:", prod_name.size)
        print("prod_name tag name:", prod_name.tag_name)
    print("---------------------------------------")
    print('Number of elements found:', len(product_names))


def close_browser(driver):
    print("closing the whole browser")
    time.sleep(3)
    driver.quit()


def webelement_methods(driver):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(20)  # max wait time for all find windows
    driver.get("http://automationpractice.com")
    search_box = driver.find_element(By.ID, 'search_query_top')
    search_box.send_keys('slenium')
    time.sleep(5)
    # clear the search box and enter dress
    search_box.click()
    search_box.send_keys('dress')
    # click search button
    search_button = driver.find_element(By.NAME, 'submit_search')
    search_button.click()
    # verify compare button is displayed
    compaire_bth = driver.find_element(By.XPATH, "//form[@class='compare-form']")
    print("compaire_bth.is_dispayed: ", compaire_bth.is_displayed())
    # assert compaire_bth.is_displayed()

    # verify compare button is enabled
    print("compaire_bth.is_dispayed: ", compaire_bth.is_enabled())

    # get attribute 'action' of compare
    print("Action attribute of compare form: ", compaire_bth.get_attribute("action"))


def working_with_alert(driver):
    print("Switching to alert"----)
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID,"promtButton").click()
    alrt=driver.switch_to.alert
    time.sleep(2)
    print("Cliking th OK")
    alrt.accept()
