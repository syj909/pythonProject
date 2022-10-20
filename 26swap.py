# 변수의 유효범위scope
# 변수가 코드내에서 사용되는 범위를 의미
# 지역local변수 : 변수의 유효범위가 함수내 또는 블럭내로 한정
# 전역global변수 : 변수의 유효범위가 프로그램 전체에 미침

# 함수의 호출방식
# call by value : 함수에 인수전달시 값의 복사가 일어남
#              따라서, 함수내의 변수와 함수밖의 변수는 다름
#              함수내에서 값을 수정하더라도
#              함수밖에서는 아무런 영향이 없음

# call by reference : 함수에 인수전달시 값의 주소를 전달
#              따라서, 함수내의 변수와 함수밖의 변수는 같음
#              함수내에서 값을 수정하면
#              함수밖에서도 그 영향을 받음

# 파이썬에서는 call by object-reference 또는
# pass by assignment 방식으로 처리함

# ex) 숫자 바꾸기
# 입력받은 매개변수의 값을 서로 바꿔 출력하는 함수 - swap
# x = 3, y = 5 -> swap(x, y) -> x = 5, y = 5

def swap(a, b) :
    c = a
    a = b
    b = c
    print('swap 내부', a, b, id(a), id(b))

x = 3
y = 5
print('swap 호출 전', x, y, id(x), id(y))
swap(x, y)
print('swap 호출 후', x, y)

# ex) 숫자 바꾸기 2
# 입력받은 매개변수의 값을 서로 바꿔 출력하는 함수 - swap2
# 매개변수를 가변객체로 정의

def swap2(nums):
    c = nums[0]
    nums[0] = nums[1]
    nums[1] = c
    print('swap2 내부', nums[0], nums[1], id(nums[0]), id(nums[1]))
nums = [3, 5]
print('swap2 호출전', nums[0], nums[1], id(nums[0]), id(nums[1]))

swap2(nums)
print('swap2 호출후', nums[0], nums[1], id(nums[0]), id(nums[1]))

# 불변 객체를 함수 내에서 조작하기
# 함수밖에서 선언한 변수는 global이라는 키워드를 선언하면 함수내에서도 조작할 수 있음

# ex) 숫자 바꾸기 3
# 입력받은 매개변수의 값을 서로 바꿔 출력하는 함수 - swap3
# 매개변수를 가변객체로 정의하고 global이라는 키워드 사용
def swap3() :
    global x
    global y
    c = x
    x = y
    y = c
    print('swap 내부', x, y, id(x), id(y))

x = 3
y = 5
print('swap3 호출전', nums[0], nums[1], id(nums[0]), id(nums[1]))
swap3()
print('swap3 호출후', nums[0], nums[1], id(nums[0]), id(nums[1]))