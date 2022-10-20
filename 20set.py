# 집합(set)
# 비순차 열거형 자료구조
# 데이터가 저장된 순서를 기억하지 않음 (인덱스 사용x)
# 단, 집합을 리스트나 튜플로 변환하면 사용가능
# 입력된 데이터의 중복을 허용하지 않음
# 선언방법은 () 안에값들을 정의하고 사용

# 집합선언
nums = {1, 2, 3, 4, 5}

# 집합 출력 1
nums[0] # 인덱스를 이용한 조회불가

# 집합 출력2
for i in range(len(nums)) :
    print(nums[i])

# 집합 출력 3
for num in nums :
    print(num, end=' ')

# 집합 동적 생성
nums = set()    # {} 는 dict 자료형으로 인식

nums.add(10)
nums.add(20)
nums.add(30)
nums.add(40)    # 중복 저장 불가

print(nums)

# 집합 값 제거 : remove(값)
nums.remove(20)
print(nums)

# 집합 값 수정 : 기본적으로는 불가, 단 리스트 변환시 가능
nums = list(nums)
nums[0] = 999
nums = set(nums)

print(nums)


# ex) 로또 645 : 1 ~ 45 사이 임의의 숫자 6개 생성
# 단, set을 이용해서 같은 숫자가 출현하지 않도록 작성
import random as rnd

lottos = set()

for _ in range(6) :
    lotto = rnd.randint(1, 45)
    lottos.add(lotto)

while True :
    if len(lottos) > 6 : break
    lotto = rnd.randint(1, 45)
    lottos.add(lotto)

print(lottos)
# ex) 로또 645 : 1 ~ 45 사이 임의의 숫자 6개 생성
# 단, list을 이용해서 같은 숫자가 출현하지 않도록 작성
import random
lottokey = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

key = []
count = 45
for i in range(6) :
    x = random.randint(1, count)
    key.append(lottokey[x])
    lottokey.remove(lottokey[x])
    count = count - 1
    x = random.randint(1, count)
print(key)

lottos = []

while True :
    if len(lottos) > 5 : break
    lotto = rnd.randint(1, 45)
    if lotto not in lottos:
        lottos.add(lotto)
print(lottos)