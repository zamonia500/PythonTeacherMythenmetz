a = input("pixle : ")
a = int(a)
a += 20

if a > 255:
    print(255)
elif a <= 255:
    print(a)


a = input("pixle : ")
a = int(a)
a += 20

print(min(a, 255))
