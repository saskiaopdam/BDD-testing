from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://betsy-webshop-remake.ew.r.appspot.com")

print(driver.title)