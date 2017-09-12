money = {'달러':1167, '엔':1.096, '유로':1268, '위안':171}

won, currency = input('').split()
print(currency,':', int(won) * money[currency])


