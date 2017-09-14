id_number = input()
sex_verify = int(id_number[7])
if sex_verify == 1 or sex_verify == 3:
    print('남자')
elif sex_verity == 2 or sex_verify == 4:
    print('여자')
