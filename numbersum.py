numinp = input('Enter a number: ')
if numinp == 'done':
    quit()
try:
    numtype = float(numinp)
except ValueError:
    print ('Invalid input')
    pass

total = 0.0
totalcount = 0
maxlist = []

while True:
    numinp = input('Enter a number: ')
    if str(numinp) == 'done':
        break
    try:
        numtype = float(numinp)
    except ValueError:
        print ('Invalid input')
        total -= numtype
        totalcount -= 1
        pass
    maxlist.append (numtype)
    total += numtype
    totalcount += 1

print ('Total : ' + str(total))
print ('Count : ' + str(totalcount))
print ('Average : ' + str(total/totalcount))
print ('Maximum : ' + str(max(maxlist)))
print ('Minimum : ' + str(min(maxlist)))



