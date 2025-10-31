from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
from private_data import username, password

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
email_element = driver.find_element(By.XPATH, './/*[@id="email"]')
email_element.send_keys(f'{username}')
password_element = driver.find_element(By.XPATH, './/*[@id="pass"]')
password_element.send_keys(f'{password}')
sleep(5)
button = driver.find_element(By.CLASS_NAME, "_6ltg")
button.click()
sleep(30)

# after loggin  click step 2
post_button = driver.find_element(By.XPATH, './/*[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"]')
post_button.click()
 
# I’m facing some issues like a captcha; otherwise, it was created allmost done successfully. I’ll try again after some time.
