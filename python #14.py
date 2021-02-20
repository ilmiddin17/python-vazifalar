#python #14 dars
#1-topshiriq
dost={'ism':'tim cook','ish':'direktor','shahar':'los angeles'}
print(f"Mening do'stim {dost['ism'].title()} {dost['ish']} bo'lib ishlaydi.U {dost['shahar'].title()}lik")
#2-topshiriq
sevimli={'Mohirbek':'palov','Akbarjon':'kabob','Dilmirod':'dimlama','Rustam':'mastava','Baxtiyor':'lavash','Azamjon':'kfc'}
ism=sevimli.get('ot', 'Bunday ism yoq')
print(f"Mohirbek {sevimli['Mohirbek']}ni yaxshi koradi")
#3-topshiriq
sevimli={'Mohirbek':'palov','Akbarjon':'kabob','Dilmurod':'dimlama','Rustam':'mastava','Baxtiyor':'lavash','Azamjon':'kfc'}
ot=input('Dostingizni ismini kiriting\t')
ot=ot.title()
ism=sevimli.get(ot)
if ism==None:
	print('Bunday ism yoq')
else:
	print(f"{ot} {ism}ni yaxshi koradi")
#4-topshiriq
en_uz={'apple':'olma','apricot':"o'rik",'banana':'banan','melon':'qovun','watermelon':'tarvuz',}
soz=input('Inglizcha meva nomini kiriting>>>')
meva=en_uz.get(soz)
if meva!=None:
	print(meva)
else:
	print('Soz topilmadi')