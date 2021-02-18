#python #11-dars 18/02/2021
son=float(input('Ixtiyoriy juft son kiriting:\t '))
#1-topshiriq
if son%2==0:
	print('Raxmat')
else:
	print('Bu juft son emas!')
#2-topshiriq
yosh=int(input('Yoshingiz nechada?>>>'))
if yosh<4 or yosh>60:
	print('Muzeyga kirish siz uchun bepul')
elif yosh<18:
	print('Chipta narxi 10 ming som')
elif yosh<=60:
	print('Chipta narxi 20 ming som')
#3-topshiriq
telefonlar=['a10' , 'a21' , 'a20' , 's9' , 's10' , 's20' , 'a50' , 'a51' , 'a70' , 's8']
model=input('Bizda Samsung Galaxyning A va S seriyadagi telefonlar bor.Ixtiyoriy model nomini kiriting\t')
if model.lower() in telefonlar:
	print('Bu model dokonimizda bor')
else:
	print('Afsuski bu model bizda yoq')
#5-topshiriq
price=10000
choy=True
kabob=False
non=True
salat=1
if choy:
	print('Mijoz choy oldi')
	price=price+2000
if kabob:
	print('Mijoz kabob oldi')
	price=price+15000
if non:
	print ('Mijoz non oldi')
	price=price+4000
if salat:
	print('Mijoz salat oldi')
	price=price+3000
print(f"Jami summa {price} boldi")
#6-topshiriq
telefonlar=['a10' , 'a21' , 'a20' , 's9' , 's10' , 's20' , 'a50' , 'a51' , 'a70' , 's8']
mavjud_emas=[]
mavjud_modellar=[]
istaklar=[]
for n in range(5):
	istaklar.append(input(f"Istalgan 5 ta model turini kiriting {n+1}."))
if istaklar:
	for model in istaklar:
		if model.lower() in telefonlar:
			print(f"Bizning dokinimizda {model} mavjud")
			mavjud_modellar.append(model)
			
		else:
				print(f"Bu {model} model dokonimizda yoq")
				mavjud_emas.append(model)
#7-topshiriq
foydalanuvchilar=['admin' , 'ali' , 'vali' , 'ilmiddin' , 'spider']
login=input('Login kiriting>>>')
if login.lower() in foydalanuvchilar:
	print('Bu login band')
else:
	print('Xush kelibsiz')
#8-topshiriq
son=int(input('Ixtiyoriy butun son kiriting>>>'))
for n in range(10):
	if son%(n+1)==0:
		print(f"Siz kiritgan son {n+1} ga bolinadi")
	
	



	