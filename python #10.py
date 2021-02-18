#1-topshiriq
cars=['toyota' , 'mazda' , 'gm' , 'hyundai' , 'kia']
for car in cars:
	if car=='gm':
		print(car.upper())
	else:
		print(car.title())
#2-topshiriq
for car in cars:
	if car!='gm':
		print(car.title())
	else:
		print(car.upper())
#3-topshiriq
ism=input('Iltimos login ismingizni kiriting\t')
if ism.lower()=='admin':
	print(f"Hush kelibsiz Admin. Foydalanuvchilar ro'yxatini korasizmi?")
else:
	print('Hush kelibsiz ',ism)
#4-topshiriq
print('2 ta son kiriting')
a=float(input('\t'))
b=float(input('\t'))
if a==b:
 	print('Ikki son bir biriga teng')
a=float(input('Son kiriting'))
if a>=0:
	print(pow(a,0.5))
else:
	print('Musbat son kiriting')
#topshiriq yakunlandi