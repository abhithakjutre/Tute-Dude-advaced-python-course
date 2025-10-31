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
button = driver.find_element(By.NAME, "btnK")
button.click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.quit()

# query = input("Enter your query: ")
# final_query= query.replace(" ", "+")
# url = f"https://www.google.com/search?q={query}&sca_esv=0c9d9d2c0958ac4e&sxsrf=AE3TifMGs03Q3gmEaUOE5-j8-3FZ3uZsEQ%3A1761795003678&ei=u9sCabKXKfqx4-EPx7T4iAQ&ved=0ahUKEwjy4PHq_cqQAxX62DgGHUcaHkEQ4dUDCBE&uact=5&oq=what+is+python+&gs_lp=Egxnd3Mtd2l6LXNlcnAiD3doYXQgaXMgcHl0aG9uIDIOEAAYgAQYkQIYsQMYigUyCxAAGIAEGJECGIoFMgoQABiABBgUGIcCMgsQABiABBiRAhiKBTILEAAY"

