import random
import time

t = '0636488522'


class User:
	names = ['John', 'Sten', 'Tim', 'Bill', 'Fill', 'Smit']
	surnames = ['Doe', 'Mustermann', 'Freeman', 'Smith', 'Shark', 'vViber']

	def __init__(self):
		self.nick = random.choice(self.names) + '_' + random.choice(self.surnames) + str(time.time()).replace('.', '')
		self.email = (self.nick).lower() + '@gmail.com'
		self.password = ((random.choice(self.names))[random.randint(0, 2)]).upper() + \
						((random.choice(self.names))[random.randint(0, 2)]).lower() + \
						((random.choice(self.names))[random.randint(0, 2)]).lower() + \
						((random.choice(self.names))[random.randint(0, 2)]).lower() + \
						((random.choice(self.names))[random.randint(0, 2)]).lower() + \
						((random.choice(self.names))[random.randint(0, 2)]).lower() + \
						(random.choice(self.names))[random.randint(0, 2)] + \
						str(random.randint(0, 9)) + \
						str(random.randint(0, 9)) + \
						str(random.randint(0, 9))


if __name__ == '__main__':  # убрать сравнить
	a = User()
	print(a.nick, a.email, a.password)
