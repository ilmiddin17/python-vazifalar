#1-topshiriq
class Shaxs:
	def __init__(self,ism,familya,tyil):
		self.name=ism
		self.surname=familya
		self.birth_year=tyil
	def get_info(self):
		return f'{self.surname.title()} {self.name.title()} {self.birth_year}-yilda tugilgan'
	def get_name(self):
		return self.name
	def get_surname(self):
		return self.surname
	def get_tyil(self):
		return self.birth_year
inson=Shaxs('alijon','olimov',1987)
print(inson.get_info())
#2-topshiriq
class Talaba(Shaxs):
	def __init__(self,ism,familya,tyil,bosqich,idraqam):
		super().__init__(ism,familya,tyil)
		self.idraqam=idraqam
		self.bosqich=bosqich
		self.fanlar=[]
	def set_bosqich(self,kurs):
		self.bosqich= kurs
	def get_sub(self):
		return 'Siz yozilgan fanlar:'
		for sub in self.fanlar:
			return f'{sub}'
	def fanga_yozil(self,*fan):
		self.fanlar.append(fan)
	def remove_fan(self,fan):
		if fan in self.fanlar:
			self.fanlar.remove(fan)
		else:
			print('Siz bu fanga yozilmagansiz')
talaba1=Talaba('olim','arsonov',1999,1,'FB1235438109')
print(talaba1.get_info())
print(talaba1.get_name())
#3-topshiriq
class Fan:
	def matematika():
		return print('Dysu')
#4-topshiriq
class Professor(Shaxs):
	def __init__(self,ism,familya,tyil,fan,ilmiy_darajasi,univer):
		super().__init__(ism,familya,tyil)
		self.subject=fan
		self.ilmiy_daraja=ilmiy_darajasi
		self.univer=univer
	def get_info(self):
		return f'{self.surname.title()} {self.name.title()}. {self.birth_year}-yilda tugilgan. Hozirda {self.univer.upper()} da {self.subject.capitalize()}dan dars berib kelmoqda. Ilmiy darajasi - {self.ilmiy_daraja}.'
p1=Professor('iqbol','olimov',1978,'temir yoldan foydalanish ishlarini boshqarish','dotsent','tdtu')
#5-topshiriq
class Foydalanuvchi(Shaxs):
	def __init__(self,ism,familya,tyil,jinsi,pochta):
		super().__init__(ism,familya,tyil)
		self.jins=jinsi
		self.email=pochta
	def registration(self):
		print(f'Assalomu alaykum, {self.name.title()}. Iltimos parol kiriting, kamida 8 belgidan iborat')
		parol=input('>>>')
		while len(parol)<8:
			print('Parol kamida 8 belgidan iborat bolishi kerak')
			parol=input('>>>')
			continue
		print('Royxatdan otish muvaffaqiyatli.')
f1=Foydalanuvchi('anvar','valiyev',1986,'erkak','anvar@gamil.com')
f1.registration()
#6-topshiriq
class Admin(Shaxs):
	def __init__(self,ism,familya,tyil,nick_name):
		super().__init__(ism,familya,tyil)
		self.nick_name=nick_name
	def ban_user(self,name):
		return print(f'{name.title()} ismli foydalanuvchi bloklandi.')
a1=Admin('abror','aliyev',2001,'abror_ali')
a1.ban_user('asal')


		
		
		
