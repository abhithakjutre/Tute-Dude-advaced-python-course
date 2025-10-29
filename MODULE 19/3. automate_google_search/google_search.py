# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(4)
driver.maximize_window()
time.sleep(1)
input_box = driver.find_element(By.NAME, "q")
input_box.send_keys('Selenium')
time.sleep(3)
button = driver.find_element(By.NAME, "btnK")
button.click()
time.sleep(5)
