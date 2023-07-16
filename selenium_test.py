from selenium import webdriver;
from selenium.webdriver.common.by import By;

driver = webdriver.Chrome()

# navigate to login page
driver.get("https://betsy-webshop-remake.ew.r.appspot.com/login")

# print login page title
print(driver.title)

# clear field from previous data
driver.find_element(By.NAME, "username").clear()

# enter text
driver.find_element(By.NAME, "username").send_keys("Marietje")

# click submit button
driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

# get page title - should be profile page
print(driver.title)

# get welcome text on the profile page
message = driver.find_element(By.CSS_SELECTOR, "h2").text

# print the welcome message 
print(message)

