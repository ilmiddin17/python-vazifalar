import random as r
def son_top(n=10):
	a=r.randint(1,n)
	sonlar=[]
	print(f'Men 1 dan {n} gacha son oyladim. Topa olasizmi?')
	x=int(input('>>>'))
	while a!=x:
		#sonlar.append(x)
		if a>x:
			print('Men oylagan son bundan kattaroq. Yana harakat qilib koring')
			x=int(input('>>>'))
			sonlar.append(x)
		if a<x:
			print('Men oylagan son bundan kichikroq. Yana harakat qilib koring')
			x=int(input('>>>'))
			sonlar.append(x)
	print(f'Barakalla topdingiz, men {x} ni oylagan edim')
	print(f'{len(sonlar)+1} ta urinishda topdingiz')
	return len(sonlar)+1
son_top(15)			