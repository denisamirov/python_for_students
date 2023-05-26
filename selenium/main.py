from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe')

url='https://selenium-python.readthedocs.io/locating-elements.html'

try:
    driver.get(url=url)
    time.sleep(4)
    driver.find_element(By.NAME,"q").send_keys("some text")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()