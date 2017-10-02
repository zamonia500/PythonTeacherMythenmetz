def check_telecom(phone_number):
    if phone_number[0:3] == '011':
        return 'SKT'
    elif phone_number[0:3] == '016':
        return 'KT'
    elif phone_number[0:3] == '019':
        return 'LGT'
    elif phone_number[0:3] == '010':
        return '알수없음'


phone_number = input('전화번호: ')
telecom = check_telecom(phone_number)
print(telecom)

