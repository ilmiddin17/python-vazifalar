#1-topshiriq
davlatlar=['Uzbekistan' , 'Italy' , 'Russia' , 'Germany' , 'USA' , 'UK']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
#2-topshiriq
juft_sonlar=list(range(0,120,2))
print(juft_sonlar)
yigindi=sum(juft_sonlar)
print(yigindi)
maks=int(max(juft_sonlar))
minimum=int(min(juft_sonlar))
print(maks-minimum)
print(len(juft_sonlar))
print(juft_sonlar[:20])
print(juft_sonlar[20:])
#3-topshiriq
foods=['palov' , 'manti' , 'mastava' , 'noxotshorva' , 'dimlama']
breakfast=foods[:]#nusxa ko'chirish
del breakfast[0]
del breakfast[1]
breakfast.append('qaymoq va non')
breakfast=tuple(breakfast)
print(breakfast)