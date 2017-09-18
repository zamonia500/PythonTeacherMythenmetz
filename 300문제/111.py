mylist = [1,2,5,6,74,2]

for i in mylist:
    print(i)

a = 0
for item in mylist:
    print(a, item)
    a += 1

for i in range(len(mylist)):
    print(i, mylist[i])

for i, item in enumerate(mylist):
    print(i, item)