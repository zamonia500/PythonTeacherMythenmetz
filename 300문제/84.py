num1 = int(input('input number1:'))
num2 = int(input('input number2:'))
num3 = int(input('input number3:'))

biggest = num1

# num2가 biggist 보다 크면
#   num2를 biggest에 넣는다.
# num2가 biggist 보다 크지 않으면
# 넣지 않는다.
#
# biggist = num1
# biggist = num2
# 하지만 그 중 더 큰 수가 들어가 있습니다.
#
# num3가 bingist 보다 크면
#   num3을 biggest에 넣는다.
# num3가 biggist 보다 크지 않으면
#   넣지 않는다.
#
#

if num2 > biggest:
    biggest = num2
if num3 > biggest:
    biggest = num3

print(biggest)


