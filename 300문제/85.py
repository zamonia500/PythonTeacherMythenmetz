# 1. 사용자로부터점수를 입력받는다.
score = int(input('점수를 입력해 주세요.'))
print(score)

# 2. 등급을 출력하다.

if score >= 81:
    print('A')
elif 61 <= score < 81:
    print('B')
elif 41 <= score < 61:
    print('C')
elif 21 <= score < 41:
    print('D')
elif 0 <= score < 21:
    print('E')

#
#
#
#
#
#
