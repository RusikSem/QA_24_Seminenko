import time
import os
from newuser.new_user import User
from test_1_1 import *
from xpath_mainpage.mainpage import *


def register_user():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    options = ChromeOptions()

    options.headless = False  # True Запуск теста без включения браузера
    path = f'{os.getcwd()}/driver/chromedriver'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://www.atomic-shop.ua/'

    driver.maximize_window()
    driver.get(url)

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    user = User()

    test_2 = Reg_page()

    enter_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', button_enter)))
    enter_button.click()

    test_2.nick_field(driver, user.nick)
    test_2.lastname_field(driver, user.nick)
    time.sleep(3)
    test_2.phone_field(driver)

    placeholder_field_click = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', placeholder_field)))
    placeholder_field_click.click()

    test_2.email_field(driver, user.email)
    test_2.address_field(driver, user.password)
    time.sleep(2)
    test_2.password_field(driver, user.password)
    time.sleep(1)

    f_reg_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', finish_button_reg)))
    f_reg_button.click()
    time.sleep(1)

    f_reg_button1 = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', finish_button_reg1)))
    f_reg_button1.click()
    time.sleep(2)

    nick_textarea = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', nick_text)))
    time.sleep(2)
    login1 = nick_textarea.text

    if user.nick in login1:
        print('1')
        login1 = user.nick

    return user.nick, login1


if __name__ == '__main__':
    print(register_user())

