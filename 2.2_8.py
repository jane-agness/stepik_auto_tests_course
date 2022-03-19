from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group [name='firstname']")
    input1.send_keys("Jane")
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-group [name='lastname']")
    input2.send_keys("Weiss")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group [name='email']")
    input3.send_keys("jw@ya.ru")

    file = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)

    option = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    option.click()

finally:
    time.sleep(10)
    browser.quit()