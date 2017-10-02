import random
# 반복한다
    # 랜덤 숫자를 받는다
    # 숫자가 리스트에 없다면
        # 이 숫자를 리스트에 넣는다

lotto = []

while len(lotto) < 6:
    number = random.randint(1, 45)
    if number not in lotto:
        lotto.append(number)

print(lotto)


