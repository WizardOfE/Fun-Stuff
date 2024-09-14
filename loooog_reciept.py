
# how many items on the list and what's the tax
listLen = int(input('how many items on the list: '))
taxPerc = float(input('tax as decimal: '))


# incrementer var and list vars
i = 0
namelist = ['']
pricelist = [0.00]

# there should be a loop as long as listLen to get inputs as a list type
while i < listLen:
    namelist.append(input('name...  '))
    pricelist.append(input('price... '))
    i += 1



# now we have inputs, pop placeholder value
namelist.pop(0)
pricelist.pop(0)

# reset i
i = 0

# calc whitespaces
wslist = [0]



while i < listLen:
    wslist.append(40 - len(namelist[i]) - len('%.2f' % float(pricelist[i])) - 2)
    i += 1

# pop ws placeholder
wslist.pop(0)


''' now the printing '''

# top formating
print('\n' * 2)
print('-' * 40)
print('PURCHASES:\n')

# reset i again
i = 0


# print item list
while i < listLen:
    print(namelist[i] + (' ' * wslist[i]) + '$' + '%.2f' % float(pricelist[i]))
    i += 1

print('')

# need to get a total price
total = 0

# reset i 
i = 0

while i < listLen:
    total += float(pricelist[i])
    i += 1

# var for strings
taxline = 'Amount added for tax ---'
totalline = 'Total ---'

# var for tax added and final total
taxAdded = taxPerc * total
total += taxAdded

# printing out the tax line
print(taxline + ' ' * (40 - len(taxline) - len('%.2f' % taxAdded)) + '$%.2f' % taxAdded)

# ending formating
print('\n', '-' * 40)

print(totalline + ' ' * (40 - len(totalline) - len('%.2f' % total)) + '$%.2f' % total)


