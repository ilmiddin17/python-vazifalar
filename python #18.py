#1-topshiriq
print('Yaqin dostlaringizni royxatini tuzamiz')
dostlar=[]
n=1
while True:
	savol=f'{n}-dostingizni ismini kiriting:'
	ism=input(savol)
	dostlar.append(ism)
	a=input('Yana ism qoshasizmi (ha/yoq)')
	n+=1
	if a!='ha':
		break
for ism in dostlar:
	print(f'{ism.title()}')
#2-topshiriq
print('Yaqin dostlaringiz yoshini saqlaymiz')
friends={}
ishora=True
while ishora:
	dost=input('Dostingizni ismini kiriting:')
	yosh=input(f'{dost.title()}ning yoshini kiriting:')
	friends[dost]=int(yosh)
	b=input('Yana malumot kiritasizmi (ha/yoq):')
	if b!='ha':
		ishora=False
for dost,yosh in friends.items():
	print(f'{dost.title()}ning yoshi:{yosh}')
#3-topshiriq
cars=['matiz','gentra','captiva','malibu','matiz','nexia','cobalt','matiz','tico']
car='matiz'
while car in cars:
	cars.remove(car)
print(cars)
#4-topshiriq
talabalar=['hasan','ali','vali','olim','botir']
b_talabalar={}
while talabalar:
	ism=talabalar.pop()
	baho=input(f'{ism.title()}ning bahosini kiriting:')
	b_talabalar[ism]=int(baho)
	print(f'{ism.title()} baholandi')
for ism,baho in b_talabalar.items():
	print(f'{ism.title()}ning bahosi:{baho}')
print('Hamma oquvchilarga baholar qoyildi')
#5-topshiriq
buyurtmalar=[]
savol='Buyurtma bering\n'
savol+='buyurtma berishni toxtatish uchun stop ni kiriting:'
buyurtma=''
while buyurtma!='stop':
	buyurtma=input(savol)
	if buyurtma!='stop':
		buyurtmalar.append(buyurtma)
		print(f'Siz {buyurtma}ga buyurtma berdingiz')
print(f'Siz bergan buyurtmalar:\n')   
for buyurtma in buyurtmalar:
    print(f'{buyurtma.title()}')
#6-topshiriq
taklif='Mahsulot nomi va narxini kiriting\n'
taklif+='dasturni toxtatish uchun stopni kiriting:'
e_bozor={}
flag=True
while flag:
	mahsulot=input(f'{taklif}')
	if mahsulot=='stop':
		flag=False
	else:
		narx=input('narx:')
		e_bozor[mahsulot]=narx
print('Dastur tugadi')
for mahsulot,narx in e_bozor.items():
	print(f'{mahsulot.title()}ning narxi:{narx}')

#7-topshiriq
for buyurtma in buyurtmalar:
	if buyurtma in e_bozor:
		print(f"{buyurtma.title()} {e_bozor[buyurtma]} so'm")
for buyurtma in buyurtmalar:
		if buyurtma not in e_bozor:
			print(f"Afsuski bizda {buyurtma} yoq")	