city = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

max_length = len(city[0])
max_index = 0

for i, one_city in enumerate(city[1:], 1):
    if len(one_city) > max_length:
        max_length = len(one_city)
        max_index = i

print(city[max_index], max_length)

#----------------------------------------

max_index = 0
for i in range(1, len(city[1:])):
    if len(city[max_index]) < len(city[i]):
        max_index = i

print(city[max_index])
