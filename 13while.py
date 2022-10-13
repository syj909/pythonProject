# 변수초기화
# while 조건식
#   실행할 문구
#   증감식


i = 1
while i <= 100 :
    print(i, end=' ')
    i += 1

# ex) 1 ~ 100 사이 정수 중 홀수만 출력
i = 1
while i <= 100 :
    print(i, end=', ')
    i += 2

# ex) 1~10 사이 정수들의 모든 합 계산 후 출력
sum = 0
i = 0
while i <= 100 :
    sum += i
    i = i + 1
print(sum)
# ex) 단을 입력받아 해당 단의 구구단을 출력
dan = int(input('숫자입력'))
i = 1
while i <= 9:
    print(f'{dan} * {i} = {dan * i}')
    i = i + 1
# ex)
i = 3
sum = 0
while i <= 100 :
    if i % 2 :
        print(i, end=', ')
        sum += i
    i = i +3
print('\n', sum)

i = 1
sum = 0
while i<=1000 :
    if sum>15000 :
        break
    sum += i
    i = i + 1
print(sum, i)