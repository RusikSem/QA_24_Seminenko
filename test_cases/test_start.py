from test_cases.test_1 import register_user as positive_register
from test_cases.test_2 import register_user as empty_nick
from test_cases.test_3 import register_user as empty_lastname
from test_cases.test_4 import register_user as register_user_without_email


def test_user_registration_positive():
	a = positive_register()
	assert a[0] == a[1]


def test_user_registration_nick_empty():
	a = empty_nick()
	assert a[0] == a[1]


def test_user_registration_lastname_empty():
	a = empty_lastname()
	assert a[0] == a[1]


def test_email_empty():
	a = register_user_without_email()
	assert a[0] == a[1]
