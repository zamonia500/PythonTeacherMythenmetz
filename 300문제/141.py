def print5xn(string):
    for i in range(len(string)):
        print(string[i], end='')
        if (i+1) % 5 == 0:
            print('')


a = '아이엠어보이유알어걸'
print5xn(a)