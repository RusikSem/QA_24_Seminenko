import random
import string


def generate_alphanum_random_string(length):  # Рандомный текст
	letters_and_digits = string.ascii_letters + string.digits
	rand_string = ''.join(random.sample(letters_and_digits, length))
	return rand_string


ran = generate_alphanum_random_string(10)

p = ran.split(',')
print(type(p))


# 20 случайных чисел в интервале [0:100]
random_list = [random.randint(0, 30) for i in range(10)]

print(random_list)

print(type(['Zxi0lP3AsR', 'DASFjhm3Bo']))