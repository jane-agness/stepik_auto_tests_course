from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, ".form-group #answer")
    input.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, ".form-group #solve")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()
