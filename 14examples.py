# ex2 숫자 맞추기 (1 ~ 10)
import random
print('>>숫자 맞추기 게임<<')
com = random.randint(1, 10)
while True :
    my = int(input('예상 숫자를 입력하시오 : '))
    if com == my :
        print('성공')
        break
    elif com > my :
        print('더 큽니다.')
        continue
    elif com < my :
        print('더 작습니다.')
        continue
print(com)

# ex30) 숫자 맞추기 (1 ~ 100)
import random
print('>>숫자 맞추기 게임<<')
com = random.randint(1, 100)
while True :
    my = int(input('예상 숫자를 입력하시오 : '))
    if com == my :
        print('성공')
        break
    elif com > my :
        print('더 큽니다.')
        continue
    elif com < my :
        print('더 작습니다.')
        continue
print(com)

# ex25) 복권 프로그램 - 3자리수 난수 생성/사용자 입력
# 난수범위 - 100 ~ 999, 위치는 상관없이 숫자만 일치여부 판단
# ex) 123 -> 345 (1개일치)
# 문자열 슬라이싱을 위한 무자열 변환 str함수사용
import random

c = 0
com = str(random.randint(100, 999))
my = input('번호 3자리를 입력해주세요')
yourkey = list(my)
lottokey = list(com)

for i in range(0, len(yourkey)) :
    for j in range(0, len(lottokey)) :
        if yourkey[i] == lottokey[j] :
            c += 1

print(com)
print(my)
if c == 0 :
    print('다음 기회에')
elif c == 1 :
    print('상금 1천원')
elif c == 2 :
    print('상금 5만원')
elif c == 3 :
    print('상금 100만원')


# ex48
count = 25000
y = 0
while True :
    count = count * 1.06
    y = y + 1
    if count > 50000 :
        break;

print(y)

# ex51
for j in range(1, 9 + 1) :
    for i in range(1, 9 + 1) :
        print(f'{j} * {i} = {j * i}')

# ex53
year = 2022
exyear31 = ((year - 1) * 365 + (year - 1) / 4 - (year - 1) / 100 + (year - 1) / 400) % 7
print(input(exyear31))