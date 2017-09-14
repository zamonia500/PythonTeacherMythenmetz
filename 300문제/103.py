password = '1517'
wrong_count = 0
while True:
    diva = input()
    if password == diva:
        print('맞았습니다. 현관문이 열렸습니다.')
        break
    else:
        print('틀렸습니다. 다시 입력하세요')
        wrong_count += 1

    if wrong_count >= 5:
        print('너무 많이 틀렸습니다. 저리가')
        break

