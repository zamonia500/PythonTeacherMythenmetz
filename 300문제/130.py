def check_gender(id_number):
    num = int(id_number[7])
    if num == 1 or num == 3:
        print('남자')
    elif num == 2 or num == 4:
        print('여자')

number = input('주민등록번호 입력:')
check_gender(number)
