#1-topshiriq
import json
data={"model":'malibu','rang':'qora',
             'yil':2020,'narx':30000}
data_json=json.dumps(data, indent=4)
print(data_json)
#2-topshiriq
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba=json.loads(talaba_json)
print(talaba['ism'])
print(talaba['familiya'])
ism_json=json.dumps(talaba['ism'])
surname=json.dumps(talaba['familiya'])
#3-topshiriq
filename="students.json"
with open(filename) as file:
	students=json.load(file)
for info in students.values():
	for n in range(len(info)):
		print(f"{info[n]['name']} {info[n]['lastname']}. "
		f"{info[n]['faculty']} fakulteti "
		f"{info[n]['year']}-kurs talabasi")
#4-topshiriq
result={"batchcomplete":"","query":{"pages":{"13801":{"pageid":13801,"ns":0,"title":"Python","extract":"Python (talaffuzi: Piton) \u2014 umumiy-maqsadli dasturlash uchun keng tarzda foydalaniladigan yuqori darajali dasturlash tili. Ushbu dasturlash tili Guido van Rossum tomonidan yaratilgan va birinchi marta 1991-yilda foydalanib ko\u02bbrilgan.\nPython har xil platformalar uchun yozilgan, masalan\nWindows, Linux, Mac OS X, Palm OS, Mac OS va boshqalar. Python Microsoft.NET platformasi uchun yozilgan realizatsiyasi ham mavjud bo\u02bblib, uning nomi \u2014 IronPython."}}}}
print(result['query']['pages']['13801']['title'])
print(result['query']['pages']['13801']['extract'])
