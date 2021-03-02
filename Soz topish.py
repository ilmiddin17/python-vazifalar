#Ustoz Anvar Anvar Narzullayevni kodlari asosida
from uzwords import words
import random
def get_word():
	word=random.choice(words)
	while "-" in word or ' ' in word:
		word=random.choice()
	return word.upper()
def display(user_letters, word):
	display_letter=' '
	for letter in word:
		if letter in user_letters.upper():
			display_letter+=letter
		else:
			display_letter+='-'
	return display_letter
def play():
	word=get_word()
	word_letters=set(word)
	user_letters=' '
	print(f'Men {len(word)} harfdan iborat soz oyladim. Topa olasizmi?')
	while len(word_letters)>0:
		print(display(user_letters,word))
		if len(word_letters)>0:
			print(f'Shu paytgacha siz kiritgan harflar:{user_letters}')
		letter=input('Harf kiriting: ').upper()
		if letter in user_letters:
			print(f'{letter} harfini oldin kiritgansiz. Boshqa harf kiriting')
			continue
		elif letter in word:
			word_letters.remove(letter)
			print(f'Barakalla {letter} harfi men oylagan soz ichid bor')
		else:
			print('Bunday harf yoq')
		user_letters+=letter
	print(f'Tabriklayman. {word} sozini {len(user_letters)} ta harf kiritish orqali topdingiz')
play()
		
