#1-topshiriq
izohli={'sort':'saralash',
               'remove':'olib tashlash',
               'append':'element qoshish',
               'items':'barchasini chiqarish',
               'keys':'faqat kalitlarni',
               'values':'faqat qiymatlarni',
               'insert':'element qoshish',
               'upper':'faqat katta harflar',
               'lower':'faqat kichik harflar',
               'title':'1-harflar katta'
                }
for key,value in izohli.items():
	print(f"Kalit:{key}") 
	print(f"Qiymat:{value}\n")       
#2-topshiriq
dav_poytaxt={'uzbekistan':'tashkent',
                             'russia':'moscow',
                             'italy':'rim',
                             'germany':'berlin',
                             'francy':'paris',
                             'usa':'washington',
                             'spain':'madrid'
                             }
for davlat in sorted(dav_poytaxt.keys()):
	print(f"Davlatlar:{davlat.title()}")
print('  '*10)
for poytaxt in sorted(dav_poytaxt.values()):
	print(f"Poytaxtlar:{poytaxt.title()}")
#3-topshiriq
state=input('Istalgan davlat nomini kiriting\t')
capital=dav_poytaxt.get(state)
#get ni ichiga state '' siz yoziladi ekan
if capital==None:
	print('Bunday davlat topilmadi')
else:
	print(f"{state.title()}ning poytaxti {capital.title()}")
#4-topshiriq
capita=dav_poytaxt.get('frany','Topilmadi')
print(capita)
menu={'palov':15000,
               'mastava':12000,
               'shorva':13000,
               'dimlama':14000,
               'baliq':18000,
               'kabob':9000,
               'tuxum':1100,
               'gumma':2000,
               'perashka':1500,
               'lavash':16000,
               'burger':15500
}
buyurtmalar=[]
for n in range(3):
	buyurtmalar.append(input(f"Buyurtma bering. {n+1}-"))
for buyurtma in buyurtmalar:
	if buyurtma in menu:
		print(f"{buyurtma.title()} oshxonada {menu[buyurtma]} so'm")
for buyurtma in buyurtmalar:
		if buyurtma not in menu:
			print(f"Afsuski bizda {buyurtma} taomi yoq")