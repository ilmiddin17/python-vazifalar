#1-topshiriq
print('Hush kelibsiz')
print('Bizning dastur yordamida a dan b gacha sonlarni kubini hisoblashingiz mumkin')
a=int(input('a ni kiriting\t'))
b=int(input('b ni kiriting\t'))
sonlar=list(range(a,b+1))
for son in sonlar:
	kub=pow(son,3)
	print(f"{son} ning kubi {kub} ga teng\n")
#2-topshiriq
print('5ta eng sevimli kinolaringizni kiriting')
kinolar=[]
for n in range(5):
	 kinolar.append(input(f"kinoni nomini kiriting\t"))
print(kinolar)