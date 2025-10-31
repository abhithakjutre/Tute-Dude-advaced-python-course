# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

time.sleep(4)
driver.maximize_window()
time.sleep(1)
input_box = driver.find_element(By.NAME, "q")
input_box.send_keys('Selenium')
time.sleep(3)
button = driver.find_element(By.CLASS_NAME, "gNO89b")
button.click()
time.sleep(10)
