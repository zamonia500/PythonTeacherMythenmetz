date = ['09/05', '09/06', '09/07', '09/08', '09/09', '09/10']
end_price = [10500, 10300, 10100, 10800, 11000]

for i in zip(date, end_price):
    print(i)

for i, j in zip(date, end_price):
    print(i, j)

print(dict(zip(date, end_price)))
