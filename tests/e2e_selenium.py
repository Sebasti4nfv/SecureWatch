from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://securewatch-demo.com/login")

driver.find_element(By.NAME, "email").send_keys("demo@cliente.com")
driver.find_element(By.NAME, "password").send_keys("Demo1234")
driver.find_element(By.TAG_NAME, "button").click()

assert "Dashboard" in driver.title
driver.quit()
