#1-topshiriq
#Quyida keltirilgam malumotlar toqima
mashhurlar={'tim cook':{'tyil':1970,
                          'shahar':'nyu york',
                          'kasb':'apple co'},
                          'jeff bozes':{'tyil':1968,
                          'shahar':'mayami',
                          'kasb':'amazon co'},
                          'jack maa':{'tyil':1976,
                          'shahar':'tokio',
                          'kasb':'alibaba co'},
                          'sotaqozi':{'tyil':1900,
                          'shahar':'tashkent',
                          'kasb':'bekorchilik co'}
                        }
for ism,info in mashhurlar.items():
	print(f"\n{ism.title()} {info['tyil']}-yilda "
	f"{info['shahar'].title()} shahrida tugilgan."
	f"{info['kasb'].title()} da ishlaydi"
	)
#2-topshiriq
mashhurlar['jeff bozes']['asar']='success'
mashhurlar['jack maa']['asar']='never give up'
mashhurlar['sotaqozi']['asar']='dangasalik sanati'
mashhurlar['tim cook']['asar']='work smartly'
for ism,info in mashhurlar.items():
	print(f"{ism.title()} {info['asar'].title()} asarini oqishni yaxshi koradi")
#3-topshiriq
dost_kino={'ali':{'kino':None},
'vali':{'kino':None},
'hasan':{'kino':None},
'olim':{'kino':None}}
for ism,info in dost_kino.items():
	film=input(f'{ism.title()}, sevimli kinofilmingiz qaysi?>>>')
	info['kino']=film
for ism,info in dost_kino.items():
	print(f'{ism.title()}ning sevimli kinofilmi-{info["kino"].title()}')
#4-topshiriq
davlatlar={'uzbekistan':{'capital':'tashkent', 'maydoni':448_978,
 'aholisi':34_000_000,
 'pul_birligi':'som'},
 'russia':{'capital':'moscow',
 'maydoni':17_098_246,
 'aholisi':144_000_000,
 'pul_birligi':'rubl'},
 'usa':{'capital':'washington',
 'maydoni':9_631_418,
 'aholisi':327_000_000,
 'pul_birligi':'dollar'},
 'spain':{'capital':'madrid',
 'maydoni':267_087,
 'aholisi':67_457_247,
 'pul_birligi':'euro'}
 }
for davlat,info in davlatlar.items():
  if davlat=='usa':
 	 davlat=davlat.upper()
  else:
      davlat=davlat.title()
  print(f'{davlat}ning poytaxti '
  f"{info['capital'].title()}. Maydoni-{info['maydoni']} "
  f"km. kvadrat. Aholisi-{info['aholisi']} "
  f"pul birligi-{info['pul_birligi'].title()}"
  )
#5-topshiriq
state=input('Istalgan davlat nomini kiriting')
dav=davlatlar.get(state)
if dav!=None:
#	if state=='usa':
#		 state=state.upper()
#	else:
#	     state=state.title()
    print(f"{state.title()}ning poytaxti "        f"{dav['capital'].title()}. Maydoni-{dav['maydoni']} "
f"km. kvadrat. Aholisi-{dav['aholisi']} "
f"pul birligi-{dav['pul_birligi'].title()}")
else:
	print(f'{state.title()} haqida malumot topilmadi')
#6-topshiriq
#Quyida keltirilgam malumotlar toqima
shaxs1={'ism':'tim cook','tyil':1970,
                          'shahar':'nyu york',
                          'kasb':'apple co'}
shaxs2={'ism':'jeff bozes','tyil':1968,
                          'shahar':'mayami',
                          'kasb':'amazon co'}
shaxs3={'ism':'jack maa','tyil':1976,
                          'shahar':'tokio',
                          'kasb':'alibaba co'}
shaxs4={'ism':'sotaqozi','tyil':1900,
                          'shahar':'tashkent',
                          'kasb':'bekorchilik co'}
shaxslar=[shaxs1,shaxs2,shaxs3,shaxs4]
for shaxs in shaxslar:
	print(f"\n{shaxs['ism']} {shaxs['tyil']}-yilda "
	f"{shaxs['shahar'].title()} shahrida tugilgan."
	f"{shaxs['kasb'].title()} da ishlaydi"

                             