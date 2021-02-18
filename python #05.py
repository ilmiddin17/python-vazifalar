#1-topshiriq
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha} ko'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati ")
#2-topshiriq
print("Iltimos quyidagi ma'lumotlarni kiriting")
mahalla=input("Mahallangiz nomi\t")
kocha=input("Ko'changiz nomi\t")
tuman=input("Qaysi tumandansiz\t")
viloyat=input("Qaysi viloyatdansiz\t")
manzil=f"{viloyat.upper()} viloyati, {tuman.lower()}, tumani, {mahalla.capitalize()}, mahallasi, {kocha.capitalize()}, ko'chasi"
print(manzil)