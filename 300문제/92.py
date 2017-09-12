warn_investment_list = ['Nicrosoft', 'Doogle', 'Never', 'KiKio', 'SEMSUNG', 'HELG']

while True:
    isIn = input('input some company: ')
    if isIn in warn_investment_list:
        print('It\'s in')
    else:
        print('Nope')
    if isIn == "Q":
        break
