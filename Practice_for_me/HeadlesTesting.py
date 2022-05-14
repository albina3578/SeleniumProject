from selenium import webdriver


def headles_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Program Files\Python310\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj, options=ops) #will make it headless
    return driver


driver = headles_chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.quit()
