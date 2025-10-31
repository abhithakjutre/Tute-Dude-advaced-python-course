# pip install selenium
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
time.sleep(3)
driver.maximize_window()
time.sleep(4)
select = driver.find_element(By.LINK_TEXT, "Electronics")
time.sleep(2)
select.click()
time.sleep(5)
select1 = driver.find_element(By.LINK_TEXT, "Audio")
time.sleep(1)
select1.click()
time.sleep(10)