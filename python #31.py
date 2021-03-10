#1-topshiriq
from uuid import uuid4
class Avto:
	__num_avto=0
	def __init__(self,company,model,color,year,km=0):
		self.company=company
		self.model=model
		self.color=color
		self.year=year
		self.__km=km
		self.__id=uuid4()
		Avto.__num_avto+=1
	def get_km(self):
		return self.__km
	def get_id(self):
		return self.__id
	def add_km(self,km):
		if km>=0:
			self.__km+=km
		else:
			print('Mashinaning bosib o\'tgan yol ko\'rsatkichini kamaytirib bo\'lmaydi')
		
	@classmethod
	def get_num_avto(cls):
		return cls.__num_avto

#avto1=Avto('gm','gentra','white',2021,500)
#avto1.add_km(-1260)
#print(avto1.get_km())
#2-topshiriq
class Person:
	def __init__(self,name,surname,year):
		self.name=name
		self.surname=surname
		self.year=year
	def get_name(self):
		return self.name
	def get_info(self):
		return f'{self.surname.title()} {self.name.title()} {self.year}-yilda tug\'ilgan.'
class Student(Person):
	__total_students=0
	def __init__(self,name,surname,year,facultet,course):
		super().__init__(name,surname,year)
		self.facultet=facultet
		self.course=course
		self.__id=uuid4()
		Student.__total_students+=1
	def get_id(self):
		return self.__id
	@classmethod
	def get_total(cls):
		return cls.__total_students
	def get_id(self):
		return self.__id
	def get_info(self):
		return f"Hozirda {self.name.title()} {self.surname.title()} {self.facultet.title()} fakultetida o'qiydi. {self.course}-kurs."
t1=Student('olim','nosirov',1998,'science',2)
#print(t1.get_total())
print(t1.get_info())