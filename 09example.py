import random
# 25 - 복권 발행 프로그램
c = 0
yourkey = [int(input('1번째 번호')), int(input('2번째 번호')), int(input('3번째 번호'))]
lottokey = [random.randint(1, 45), random.randint(1, 45), random.randint(1, 45)]

for i in range(0, len(yourkey)) :
    for j in range(0, len(lottokey)) :
        if yourkey[i] == lottokey[j] :
            c += 1

print(yourkey)
print(lottokey)
print('당첨입니다' if c == 3 else '미당첨입니다.')


# 26 - 연봉/결혼 여부 세금 계산

salary = int(input('연봉을 입력하세요'))
isMarried = input('결혼여부를 입력하세요. 결혼/미혼')
tax = 0

if isMarried=='결혼' :
    if salary > 3000 :
        tax = salary * 0.25
    if salary < 3000 :
        tax = salary * 0.1
if isMarried=='미혼' :
    if salary > 6000 :
        tax = salary * 0.35
    if salary < 6000 :
        tax = salary * 0.15


print(f'내야할 세금은 {tax}원 입니다.')

# 27 - 윤년 여부
year = int(input('년도는?'))

if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print(year, '년은 윤년입니다')
else:
    print(year, '년은 윤년이 아닙니다.')