#1-topshiriq
def katta_harf(ismlar):
	names=[]
	for ism in ismlar:
		ism=ism.title()
		names.append(ism)
	return names
talabalar=['ali','vali','hasan','olim','anvar']
print(katta_harf(talabalar))
print(talabalar)
#2-topshiriq
def bahola(names):
	baholar={}
	for name in names:
		baho=int(input(f'{name.title()}ning bahosini kiriting:'))
		baholar[name]=baho
	return baholar
oquvchilar=['ali','hasan','husan','olim','abror','ravshan']
marks=bahola(oquvchilar)
print(marks)
#3-topshiriq
def mark(names):
	marks={}
	while names:
		name=names.pop()
		baho=int(input(f'{name.title()}ning bahosini kiriting:'))
		marks[name]=baho
	return marks
studentlar=['ali','vali','bek','shox']
baholar=mark(studentlar)
print(baholar)
print(studentlar)
#4-topshiriq
def kattasini_aniqla(a,b,c):
	max=a
	if b>=max:
		max=b
	if c>=max:
		max=c
	return max
print(kattasini_aniqla(2,5,7))
#5-topshiriq
def fibonachchi(n):
	fibona=[]
	for x in range(n):
		if x==1 or x==0:
			fibona.append(1)
		else:
			fibona.append(fibona[x-1]+fibona[x-2])
	return fibona
print(fibonachchi(10))