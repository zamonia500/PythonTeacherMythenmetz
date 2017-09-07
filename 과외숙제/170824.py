l = [1,2,3,4,5]
l2 = []
for item in l:
    l2.append(item * item)
print(l2)

e = lambda x: x ** 2
l3 = list(map(e, l))
print(l3)
