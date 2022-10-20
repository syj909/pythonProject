# 내장함수
# dont't reinvent the wheel
# 파이썬에서 활용빈도 높은 기능을 함수로 미리 작성해두었음
# 이러한 함수를 사용할 때는 특별한 지시문 필요 x

# 숫자관련
abs(-10)    #절대값
abs(10)

sum([10, 20, 30])       # 요소의 총합 계산

max([10, 20, 30])       # 최대값 출력
min([10, 20, 30])       # 최소값 출력

round(34.56)            # 반올림
round(34.46)

# 자료형 관련
type(10)
type(10.5)
type(True)

# 변환 함수
ord('A')                # 유니코드 문자를 입력하면 코드값 출력
chr(65)                 # 코드값을 입력하면 유니코드 문자 출력

# 정렬 함수
nums = [10, 7, 15, 4]
sorted(nums)                # 오름차순 정렬
sorted(nums, reverse=True)  # 내림차순 정렬
list(reversed(nums))        # 순서 반전

# 묶음 함수 : zip
names = ['혜교','지현','수지']
ages = [33, 65, 77]
actor = list(zip(names, ages))

# 함수를 조건식에 적용 - filter, map
# ex) 1 ~ 100 사이 정수 중 짝수만 골라서 리스트에 저장
evens = []
for num in range(1, 100 + 1) :
    if num % 2 == 0:
        evens.append(num)
print(evens)

# 짝수를 판별하는 코드를 함수로 캡슐화
def chkEven(num):
    isEven = False
    if num % 2 == 0 : isEven = True
    return isEven

evens = []
for num in range(1, 100 + 1) :
    if chkEven(num):
        evens.append(num)

# 짝수를 판별하는 함수를 filter 함수로 재적용
# filter(적용할 함수, 함수에 사용할 값객체)
# 리턴값 : 조건을 만족하는 값
evens = list(filter(chkEven, range(1, 100 + 1)))
print(evens)

# 짝수 판별하는 함수를 람다식으로 재적용
evens2 = list(filter(lambda x:x % 2 == 0, range(1, 100 + 1)))
print(evens2)

# ex) 1 ~ 10 사이 정수를 제곱해서 리스트에 저장
squares = []
for num in range(1, 10+1):
    val = num ** 2
    squares.append(val)
print(squares)

# 정수를 제곱하는 함수를 만들어 재적용
def squrNum(num):
    return num ** 2

squares = []
for num in range(1, 10+1):
    squares.append(squrNum())

# 정수를 제곱하는 함수를 map 함수로 재적용
# map (적용할 함수, 함수를 적용할 대상)
# 리턴값 : 함수를 적용한 값
sqr1 = list(map(squrNum, range(1, 10 + 1)))
print(sqr1)

# 정수를 제곱하는 함수를 람다식으로 재적용
sqr1 = list(map(lambda x:x**2, range(1, 10 + 1)))
print(sqr1)

# 열거형 데이터 다루기 : enumberate
# 순서있는 객체들을 다룰 때 인덱스를 포함시켜 객체를 리턴해 줌
print(names)    # 값만 출력

# ex29) 사용자로부터 소문자를 입력받아 대문자로 변환
# 단, 숫자나 대문자 입력시 경고 출력

def upperAlpha(str):
    if str.isalpha() or str.islower() :
        str = str.upper()
    return  str

print(upperAlpha('asda'))