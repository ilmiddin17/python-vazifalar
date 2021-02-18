#1-topshiriq
ismlar=['Mohirbek ','Abror' ,'Omadbek ','Abdushukur']
yaqin=ismlar[0]
pishshiq=ismlar[1]
mashinnik=ismlar[2]
qoshni=ismlar[3]
print(yaqin+' '+qoshni)
ismlar.append('Abbos')
print(ismlar)
ismlar.insert(2,'Elmurod')
print(ismlar)
del ismlar[-1]
print(ismlar)
ismlar.remove('Elmurod');print(ismlar)
print(ismlar[1].upper())
#2-topshiriq
sonlar=['-2', '5.7', '20', '278', '45', '34.9']
print(sonlar)
sonlar[2]=95
print(sonlar)
print(int(sonlar[3])+int(sonlar[2]))
#3-topshiriq
raqamlar=[5, 6477, 73, 62, 92, 61]
print(raqamlar[1]//raqamlar[3]);
raqamlar.insert(2,56)
print(raqamlar)
#4-topshiriq
friends=[]
friends.append('ali.')
friends.append('vali')
friends.append('anvar')
friends.append('AHROR')
print(friends[0].capitalize())
yolgonchi=friends.pop(1)
print("Gapga" ,yolgonchi.capitalize()," kela olmaydi")
print("Mening eng yaqin do'stlarim ",friends)

