import time

print ('COUNTDOWN SIMULATOR')
print ('-------------------')

duration = int(input ('Insert time (in second) : '))
start = input ('Type "yes" to start : ')

if start.lower().strip() == 'yes':
	a = duration + 1
	while a > 1:
		a = a - 1
		print (a)
		time.sleep (1)
	print ('DONE!')

print ('Thank you!')