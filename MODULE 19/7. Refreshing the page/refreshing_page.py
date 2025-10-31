# pip install selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(1)
driver.maximize_window()
time.sleep(2)
driver.refresh()
time.sleep(5)

