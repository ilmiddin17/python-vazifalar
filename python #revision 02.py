#revision
#1-topshiriq
friends=['ali','vali','olim','anvar','abror','hasan','husan']
mehmonlar=[]
for n in range(4):
	mehmon=friends.pop(2)
	mehmonlar.append(mehmon)
print(mehmonlar)
#2-topshiriq
sonlar=[]
for n in range(12,40,2):
		sonlar.append(n)
print(sonlar)
#3-topshiriq
numbers=list(range(1,20,2))
print(f'{numbers} lar yigindisi {sum(numbers)} ga teng')
#4-topshoriq
print(len(sonlar))
print(sonlar[:5])
taomlar=["osh",'mastava','dimlama','sho\'rva','grechka']
nonushta=taomlar[:]
nonushta.remove('osh')
del nonushta[2]
nonushta.append('non va qaymoq')
print(nonushta)
#5-topshiriq
#dostlar=[]
#print('5 ta eng yaqin dostingizni ismini kiriting')
#for n in range(5):
#	dost=input(f'{n+1}.')
#	dost=dost.title()
#	dostlar.append(dost)
#print(dostlar)
#for friend in dostlar:
#	print(f'Assalomu aleykum, {friend}\n'
#	f'sizni tugilgan kunim munosabati bilan '
#	f'otkazilayotgan bayramga taklif qilaman'
#	)
#6-topshiriq
toq_sonlar=tuple(range(11,50,2))
for toq in toq_sonlar:
	kub=toq**3
	print(f'{toq} soning kubi:{kub}')
print(type(toq_sonlar))
#7-topshiriq
#a foydalanuvchidan soralgan son
a=float(input('Son kiriting>>>'))
if a>=0:
	print(f'{a} ning ildizi {a**0.5} ga teng')
else:
	print('Musbat son kiriting')
print('istalgan butun soning boluvchilarini chiqaruvchi dastur')
#b foydalanuvchidan soralgan son
b=int(input('Ixtiyoriy son kiriting:'))
for n in range(99999):
		if b%(n+1)==0:
			print(f'{b} soni {n+1} ga bolinadi')
#8-topshiriq
yosh=int(input('Yoshingiz nechada>>>'))
if yosh<4 or yosh>60:
	narx=0
if yosh>=4 and yosh<18:
	narx=10000
if yosh>=18 and yosh<=60:
	narx=20000
print(f'Chipta narxi siz uchun {narx} som ')
#9-topshiriq
mahsulotlar=['olma','anor','behi','kartoshka','piyoz','sabzi','guruch','shakar']
savat=[]
print('5 ta mahsulot nomini kiriting')
for n in range(5):
	savat.append(input(f'{n+1}.'))
for mahsulot in savat:
	if mahsulot in mahsulotlar:
			print(f'{mahsulot} dokonimizda bor')
	else:
		print(f'Dokonimizda {mahsulot} yoq')
#10-topshiriq
en_uz={'apple':'olma',
'banana':'banan',
'juice':'sharbat',
'grape':'uzum',
'melon':'qovun',
'watermelon':'tarvuz'
}
soz=input('Ingizcha soz kiriting>>>')
meva=en_uz.get(soz)
if meva!=None:
	print(f'{soz} ning tarjimasi: {meva}')
else:
	print('Soz topilmadi')
#11-topshiriq
menu={'palov':18000,
'dimlama':15000,
'shorva':12000,
'mastava':10000,
'gumma':2000,
'perashki':1500,
'somsa':3000,
'napaleon':5000,
'coca cola':6000,
'pepsi':7000,
'choy':500,
'kofe':1500
}
buyurtmalar=[]
print('Buyurtma bering')
for n in range(3):
	buyurtmalar.append(input(f"Buyurtma bering. {n+1}-"))
for buyurtma in buyurtmalar:
	if buyurtma in menu:
		print(f"{buyurtma.title()} oshxonamizda {menu[buyurtma]} so'm")
for buyurtma in buyurtmalar:
		if buyurtma not in menu:
			print(f"Afsuski bizda {buyurtma} taomi yoq")