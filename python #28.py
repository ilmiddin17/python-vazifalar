class User:
	def __init__(self,name,surname,email,gender,birthdate):
		self.ism=name
		self.familya=surname
		self.pochta=email
		self.jins=gender
		self.tyil=birthdate
foydalanuvchi=User('ali','valiyev','ali@gmail.com','erkak',1997)
def tanishtir(self):
	get=f'Foydalanuvchi ismi-{(self.ism).title()} {(self.familya).title()}. Elektron manzili {self.pochta}. {self.tyil}-yilda tugilgan. Jinsi {self.jins}'
	return get
print(tanishtir(foydalanuvchi))
def get_name(self):
	return self.ism.title()
print(get_name(foydalanuvchi))
def full_name(self):
	full=f'{self.ism.title()} {self.familya.title()}'
	return full
print(full_name(foydalanuvchi))
def age(self, yil):
	return yil-self.tyil
print(age(foydalanuvchi,2021))


