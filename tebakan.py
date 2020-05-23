import random

jawaban = random.randint (1,10)
pertanyaan = int(input ('Berapa umur adik saya? '))

while pertanyaan != jawaban:
	if pertanyaan > jawaban:
		print ('Kebesaran bor')
	elif pertanyaan < jawaban:
		print ('Kekecilan cuy')
	pertanyaan = int(input ('Coba lagi dong '))

print ('Kok jago')
