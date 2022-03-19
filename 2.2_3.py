from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

def sum(x,y):
    return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "h2 #num1")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "h2 #num2")
    y = y_element.text
    z = sum(x,y)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z) # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()