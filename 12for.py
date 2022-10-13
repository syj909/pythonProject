# 반복문
# 정해진 횟수만큼 특정코드를 실행하도록 만든 문장

# 만일 100번 출력해야 한다면 복붙을 계속할 것인가?
# 또한 반복시 출력하는 문구가 변경된다면? - 다시 수정
# 효율적인 반복실행을 위해서 반복문을 사용함

# for 반복변수 in range(시작값, 종료값 - 1, 증감값) :
# 반복실행할 문장

# range 함수 사용하기
# range(숫자) - 0부터 숫자 - 1 까지의 범위
list(range(10)) # 0 ~ (10 - 1) 범위

# range(시작, 끝 - 1) - 시작값부터 끝값 - 1까지의 범위
list(range(1, 45+1))

# range(시작, 끝 - 1, 증감값)
# -> 시작값부터 증감값을 처리해서 끝값 - 1까지의 범위
list(range(1, 10, 2))
list(range(0, 10, 2))

for i in range(1, 100 + 1) :
    print(i, end=', ')

for i in range(1, 100 + 1, 2):
    print(i, end=', ')

j = 0
for i in range(1, 100 + 1) :
    j += i
print(j)

# 가우스 덧셈 공식을 이용해서
# 1 ~ 100 사이 모든 정수들의 합 계산 후 출력
# x ~ y 까지의 숫자를 더한 합을 구하는 공식
# ((x + y) * (y - x + 1)) / 2



for i in 'Hello, World!!' :
    print(i, end=', ')

# ex) 단을 입력받아 해당 단의 구구단을 출력

j = int(input('숫자입력'))
for i in range(1, 9 + 1) :
    print(f'{j} * {i} = {j * i}')

sum = 0
for i in range (3, 100 + 1, 3) :
    if i%2 :
        print(i, end=', ')
        sum += i
print('\n', sum)