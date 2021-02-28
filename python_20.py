#1-topshiriq
def oraliq(min,max,qadam=' '):
	sonlar=[]
	if qadam==None:
		while min<max:
			sonlar.append(min)
			min+=1
	else:
		while min<max:
			sonlar.append(min)
			min=min+qadam
	return sonlar
#2-topshiriq
def toliq_ism_yasa(ism,familya,otasining_ismi=' '):
	if not otasining_ismi:
		toliq_ism=f'{ism.title()} {familya.title()}'
	else:
		toliq_ism=f'{ism.title()} {otasining_ismi.title()} {familya.title()}'
	return toliq_ism
talaba=toliq_ism_yasa('olim','anvarov')
print(talaba)
talaba2=toliq_ism_yasa('olim','anvarov','nikolayevich')
print(talaba2)
#3-topshiriq
def avto_info(kampaniya,model,rangi,karobka,yili,narxi=None):
	avto={'kampaniya':kampaniya,
	'model':model,
	'rang':rangi,
	'karobka':karobka,
	'yil':yili,
	'narx':narxi
	}
	return avto
avto1=avto_info('GM','Gentra','Qora','mexanika',2019,9500)
avto2=avto_info('Audi','A8','Qizil','avto',2021)
avtolar=[avto1,avto2]
for avto in avtolar:
	if avto['narx']:
		narx=avto['narx']
	else:
		narx='Nomalum'
	print(f"{avto['rang']} {avto['model']} narxi:{narx}")
#4-topshiriq
#def info(ismi,familyasi,t_yili,t_joyi,t_nomeri=None,emaili=None):
#	malumot={'ism':ismi,
#	'familya':familyasi,
#	't_yil':t_yili,
#	't_joy':t_joyi,
#	't_nomer':t_nomeri,
#	'email':emaili}
#	return malumot
#mijoz=info('ali','olimov',1998,'kokand',emaili='ali@gmail.com')
#print(mijoz)
#flag=True
#while flag:
#	for key,value in malumot.items()
#5-topshiriq
def sonlar():
	"""3ta son qabul qilib eng kattasini qaytaruvchi funksiya"""
	a=float(input('1-sonni kiriting:'))
	b=float(input('2-sonni kiriting:'))
	c=float(input('3-sonni kiriting:'))
	if a>b:
		if a>c:
			return a
		if a<c:
			return c
		if a==c:
			return a
	if a<b:
		if b>c:
			return b
		if b<c:
			return c
		if b==c:
			return b
	if a==b:
		if a>c:
			return a
		if a<c:
			return c
		if a==c:
			return a
print(sonlar())
#6-topshiriq
def geometry():
	"""Foudalanuvchidan doirani radiusini qabul qilib uning diametri, yuzi,uzunligini lugat korinishida qaytaruvchi funksiya"""
	r=float(input('Doirani radiusini kiriting:'))
	d=2*r
	PI=3.1415
	S=round(PI*(r**2),2)
	C=round(PI*d,2)
	inform={'diametr':d,
	'yuza':S,
	'uzunlik':C}
	form=f"{r} radiusli doiraning yuzi S={inform['yuza']}, uninv diametri d={inform['diametr']}, uzunligi C={inform['uzunlik']} ga teng"
	print(form)
	return inform
#7-topshiriq
	"""Berilgan oraliqdagi tub sonlarni chiqaruvchi funksiya"""
def tub_son(min,max):
		"""Berilgan oraliqdagi tub sonlarni chiqaruvchi funksiya"""
	tub_sonlar=[]
	for n in range(min,max+1):
		tub=True
		if n==1:
			tub=False
		elif n==2:
			tub=True
		else:
			for x in range(2,n):
				if n%x==0:
					tub=False
		if tub:
			tub_sonlar.append(n)
	return tub_sonlar
print(tub_son(2,20))
	

				
