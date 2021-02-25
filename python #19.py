#1-topshiriq
#ot=input('Ismingiz nima?>>>')
#yil=int(input('Nechanchi yilda tugilgansiz?>>>'))
def yosh_hisobla(ism,t_yil):
	"""Foydalanuvchidan ismini va t_yilini
	sorab yoshini aniqlaydi"""
	print(f'{ism.title()} {2021-t_yil} yoshda')
yosh_hisobla(ism='ali', t_yil=1899)
#2-topshiriq
print('Ixtiyoriy sonning istalgan darajasini hisoblovchi dastur')
#a=float(input('Son kiriting:'))
#b=float(input('Uning darajasini kiriting:'))
def hisobla(son,daraja):
	"""Foydalanuvchidan son olib, uning ixtiyoriy darajasini hisoblab konsolga chiqaruvchi funksiya"""
	print(f'{son} ning {daraja}-darajasi {son**daraja} ga teng')
hisobla(son=4,daraja=5)
print(hisobla.__doc__)
#3-topshiriq
print('Sonni juft yoki toqligini aniqlovchi dastur')
#qiymat=float(input('Son kiriting:'))
def juft_toq_aniqla(c):
	"""Sonni juft yoki toqligini aniqlovchi funksiya"""
	if c%2==0:
		print(f'{c} juft son')
	else:
		print(f'{c} toq son')
juft_toq_aniqla(c=8)
#4-topshiriq
def katta_kichik(son1,son2):
	"""Ikki sonni katta kichikligini aniqlovchi funksiya """
	if son1>son2:
		print(f'{son1} soni katta')
	if son1<son2:
		print(f'{son2} soni katta')
	if son1==son2:
		print('Ikki son bor biriga teng')
katta_kichik(7,2737)
#5-topshiriq
def kvadratini_hisobla(x,y=2):
	"""Sonni kvadratini hisoblovchi dastur y=2 deb standart qiymat berdik"""
	print(f'{x} ning kvadrati {float(x)**float(y)} ga teng')
kvadratini_hisobla(4)
#6-topshiriq
def bolinish(d):
	for n in range(2,11):
		if d%n==0:
			print(f'{d} {n} ga qoldiqsiz bolinadi')
bolinish(70)