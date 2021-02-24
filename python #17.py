#1-topshiriq
print('Istalgan sonning kvadratini hisoblaydigan dastur')
savol='Istalgan son kiriting\n'
savol+="(dasturni toxtatish uchun 'exit' ni kiriting. )"
qiymat=' '
while qiymat!='exit':
	qiymat=input(savol)
	if qiymat!='exit':
		print(float(qiymat)**2)
print('Dastur tugadi')
#2-topshiriq
savol='Yaxshi korgan kitobingiz nomini kiriting\n'
savol+='dasturni toxtatish uchun stop ni kiriting:'
kitoblar=[]
kitob=''
while qiymat!='stop':
	qiymat=input(savol)
	if qiymat!='stop':
	         kitoblar.append(qiymat)
	         print(kitoblar) 
print('Dastur tugadi')
#3-topshiriq
kirish='Yoshingiz nechada?\n'
kirish+='(dasturni toxtatish uchun exit yoki quit ni kiriting):'
yosh=''
while yosh!=('exit' and 'quit'):
	yosh=input(kirish)
	if yosh!=('exit' and 'quit'):
		yosh=int(yosh)
		if yosh<7:
			narx=2000
		if yosh>=7 and yosh<18:
			narx=3000
		if yosh>=18 and yosh<65:
			narx=10000
		if yosh>=65:
			narx=0
		print(f'Siz uchun muzeyga kirish {narx} som')
print('Dastur tugadi')
#4-topshiriq

		