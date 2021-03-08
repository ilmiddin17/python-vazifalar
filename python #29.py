class Avto():
	"""Avtomobil nomli class"""
	def __init__(self,model,rang,narx,karobka):
		self.model=model
		self.color=rang
		self.price=narx
		self.carobka=karobka
		self.kilometr=0
	def get_info(self):
		return f'{self.color.title()} rangli {self.model.title()}. Karobkasi {self.carobka}  narxi - ${self.price}. Bosib otgan yoli - {self.kilometr} km'
	def get_model(self):
		return self.model
	def get_price(self):
		return self.price
	def update_km(self,masofa):
		self.kilometr=masofa
car1=Avto('malibu','qora',35000,'avtomat')
print(car1.get_info())
car1.update_km(100)
print(car1.get_info())
def see_methods(Class):
	return [method for method in dir(Class) if method.startswith('__') is False]
print(see_methods(Avto))
class Avtosalon():
	def __init__(self,nomi,joyi):
		self.name=nomi
		self.location=joyi
		self.cars=[]
		self.number_cars=0
	def add_car(self,car):
		self.cars.append(car)
		self.number_cars+=1
	def get_car(self):
		return[car.get_info() for car in self.cars]
salon=Avtosalon('Hyundai','Kokand')
salon.add_car(car1)
print(salon.get_car())
car2=Avto('gentra','oq',11000,'mexanika')
salon.add_car(car2)
print(salon.get_car())	
		
		