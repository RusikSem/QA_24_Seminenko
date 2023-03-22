from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpath_mainpage.mainpage import *


class Reg_page():

	def nick_field(self, driver, nick):

		register_nick = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located(('xpath', nick_1)))
		register_nick.send_keys(nick)

	def lastname_field(self, driver, nick):

		register_lastname = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located(('xpath', lastname_1)))
		register_lastname.send_keys(nick)

	def phone_field(self, driver):
		t = '0636488543'

		register_phone_1 = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located(('xpath', phone_1)))
		register_phone_1.send_keys(t)

	def email_field(self, driver, email):

		register_email_field = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located(('xpath', email_1)))
		register_email_field.send_keys(email)

	def address_field(self, driver, password):

		register_address_1 = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located(('xpath', address_1)))
		register_address_1.send_keys(password)

	def password_field(self, driver, password):

		register_password1 = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located(('xpath', password_1)))
		register_password1.send_keys(password)
