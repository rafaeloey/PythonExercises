while True:
	choice = input('Apakah ingin menggunakan kalkulator? (y/n) ')

	if choice.lower().strip() == 'y':
		print ('')
		print ('----------------')
		print ('CALCULATOR')
		print ('----------------')
		print ('')

		angkapertama = int(input ('Masukkan angka pertama : '))
		print ('Angka pertama adalah ' + str(angkapertama))

		angkakedua = int(input ('Masukkan angka kedua : '))
		print ('Angka kedua adalah ' + str(angkakedua))

		print ('1 = tambah')
		print ('2 = kurang')
		print ('3 = kali')
		print ('4 = bagi')
		operasi = int(input('Masukkan operasi hitung : '))

		if operasi == 1:
			hasil = angkapertama + angkakedua
			
		elif operasi == 2:
			hasil = angkapertama - angkakedua
			
		elif operasi == 3:
			hasil = angkapertama * angkakedua
			
		else:
			hasil = float(angkapertama) / float(angkakedua)

		print ('Hasil : ' + str(hasil))

		print ('----------------')
		
		break
		
	elif choice.lower().strip() == 'n':
		break

	else:
		continue


	

