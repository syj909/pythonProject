# 컨프리헨션 - 축약표기
# 다양한 데이터 객체에 사용하는 복잡한 구문을 
# 단순하게 작성할 수 있도록 지원

# 파이썬에는 4가지 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약
# 1 ~ 10 까지의 정수를 생성해서 리스트에 저장
a = list(range(1, 10 + 1))
print(a)

b = []
for i in range(1, 10 + 1) :
    b.append(i)
print(b)

# 리스트 for 축약문
# [ 표현식 for 항목 in 반복가능개체 ]
c = [ i for i in range(1, 10 + 1) ]
print(c)


# ex) 1 ~ 20 사이 정수 중 짝수를 리스트로 생성
d = [ i for i in range(2, 20 + 1, 2) ]
print(d)

# ex) 1 ~ 10 사이 정수를 제곱한 값을 리스트로 생성
e = [ i**2 for i in range(1, 10 + 1)]
print(e)

# ex) 아래 각각의 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성하세요
val1 = [1, 2, 3, 4, 5]
f = [ i**2 for i in val1]
print(f)

# for if 축약문
val2 = [1, 2, 'A', False, 9, 100]
g = [ i ** 2 for i in val2 if type(i) == int ]
print(g)

# 1 ~ 60 사이 정수 중 홀수만 골라 리스트에 저장
h = [ i for i in range(1, 60 + 1, 2)]
print(h)
# 1 ~ 60 사이 정수 중 5의 배수만 골라 리스트에 저장
i = [ i for i in range(1, 60 + 1) if i % 5 ==0]
print(i)

# ex) 1 ~ 100 사이 정수 중 임의의 정수가 짝수면 'even'
# 홀수면 'odd'라고 구분해서 리스트에 저장
j = ['even' if i % 2 == 0 else 'odd' for i in range(1, 100 + 1)]
print(j)

# 중첩 for 축약
# [ 표현식 for 항목  in 반복가능개체]
# ex) 구구단 중 7,8단의 결과값을 리스트에 저장
k = [i * j for i in range(7, 8 + 1) for j in range(1, 9 + 1)]
print(k)

# ex) name, grd 리스트의 값들을
# 각각의 키의 값으로 딕셔너리에 저장
name = ['혜교', '지현', '수지']
grd= ['수', '우', '미']

# 단순하게 작성
# 새로운 dict요소 생성 : 객체명[키이름] = 값
s = {}
s[name[0]] = grd[0]
s[name[1]] = grd[1]
s[name[2]] = grd[2]
print(s)

# 반복문으로 재작성
for i in range(len(name)):
    s[name[i]] = grd[i]
print(s)

# 딕셔너리 for 축약문
# { for k, v in zip (반복가능객체1, 반복가능개체2)}
l = { k:v for k, v in zip(name, grd)}
print(l)

# ex) 학생과 국어점수에 대한 리스트가 있을 때
# 학생은 키로, 합격여부를 값으로하는 딕셔너리 객체를 생성
# 단, 합격여부에는 국어점수가 85점 이상인 경우 '합격'
# 그 외는 '불합격'이라고 출력함
name = ['철수', '영희', '길동', '꺽정']
kor = [50, 80, 90, 60]
final = {k: '합격' if v>=85 else '불합격' for k, v in zip(name, kor)}
print(final)

# p111 ex3)
message = ['spam', 'ham', 'spam', 'ham', 'spam']
# A) spam은 1로 ham은 0으로 생성하는 dummy 변수 생성
dummy = [1 if str == 'spam' else 0 for str in message]
print(dummy)

def makeDummy(x):
    val = 0
    if x == 'spam': val = 1
    return val
dummy = list(map(makeDummy, message))
print(dummy)
# B) spam 원소만 추출
spam = [str for str in message if str=='spam']
print(spam)

def makeSpams(x):
    isSpam = False
    if x== 'spam' : isSpam == True
    return isSpam

list(filter(makeSpams, message))
list(filter(lambda x:x=='spam', message))