def calc(int1, int2, op):
    if op == '+':
        return int(int1) + int(int2)
    elif op == '-':
        return int(int1) - int(int2)
    elif op == '*':
        return int(int1) * int(int2)
    elif op == '/':
        return int(int1) / int(int2)

with open('exp.txt', 'r') as f:

    for line in f:
        cal_list = line.split()
        while len(cal_list) > 1:
            int1 = cal_list.pop(0)
            op = cal_list.pop(0)
            int2 = cal_list.pop(0)
            result = calc(int1, int2, op)
            cal_list.insert(0, result)
        print(cal_list)


    # 파일의 끝까지 반복한다
    #
    #
    #
    # 앞 int eger
    # 뒤 integer
    # 중간 operator