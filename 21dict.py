member = {'userid': 'abc123', 'passwd': '987xyz'}

#dict 값 조회
print(member['userid'], member['passwd'])

# dict 모든 키 조회: 객체명.keys()
# for ~ in 반복문으로 조회 가능
print(member.keys())

for key in member.keys() :
    print(key, end=' ')

# dict 모든 값 조회: 객체명.values()
# for ~ in 반복문으로 조회 가능
print(member.values())

for val in member.values() :
    print(val, end=' ')

# dict 모든 키, 값 조회 : 객체명.items()
print(member.items())

for k, v in member.items() :
    print(f'({k}, {v})', end=' ')

# dict 모든 키, 값 조회 2 : 키 이용
for k in member.keys() :
    print(member[k], end=' ')

# dict 모든 키, 값 조회2 : 객체명.get(키) 이용 (추천)
for k in member.keys() :
    print(member.get(k), end=' ')

# dict 동적 생성 1
user = {}   # 사용자 - 이름, 나이, 이메일로 구성

# 객체명[새로운키] = 새로운 값
user['name'] = '홍길동'
user['age'] = 20
user['email'] = 'asd322@naver.com'

print(user)

# dict 동적 생성 2 : dict(키=값, ..)

user2 = dict(name='홍길동', age=35, email='asd322@naver.com')
print(user2)

# dict 동적 생성 3 : list 이용 - [ [키, 값], ... ]
user3 = [['name', '홍길동'], ['age', 35], ['email', 'asd322@naver.com']]

print(dict(user3))

# dict 수정하기 : 객체명[기존키] = 새로운 값
user['age'] = 30
user['email'] = 'asd322@naver.com'

# dict 삭제하기 : del 객체명[기존키] - 키와 값 모두 삭제
del user['age']

# 객체명.get(키) vs 객체명[키]
user[''] # 존재하지 않는 키 호출시 - 오류표시
user.get('regdate') # 존재하지 않는 키 호출시 - 오류표시 x
# 반환값이 None인지 여부에 따라 오류처리 대처

# ex1 ) dict 자료구조를 이용해서 학생 1명분의 데이터를 입력받아 처리
# 저장형식 : { 'name':??, 'kor':??, 'eng':??, 'mat':??,
#             'tot':??, 'avg':??, 'grd':??  }

user['name'] = input('이름을 입력하세요')
user['kor'] = int(input('국어성적을 입력하세요'))
user['eng'] = int(input('영어성적을 입력하세요'))
user['mat'] = int(input('수학성적을 입력하세요'))
user['tot'] = user.get('kor') + user.get('eng') + user.get('mat')
user['avg'] = user.get('tot') / 3
grd = '가'
if user['avg'] >= 90:
    grd = '수'
elif user['avg'] >= 80:
    grd = '우'
elif user['avg'] >= 70:
    grd = '미'
elif user['avg'] >= 60:
    grd = '양'
user['grd'] = grd

print(user)

# dict 자료구조를 이용해서 학생 3명분의 데이터를 처리
# dict 자료구조를 이용해서 처리
# 저장형식 : { 'name':??, 'kor':??, 'eng':??, 'mat':??,
#             'tot':??, 'avg':??, 'grd':??  }
userGroup = []

for i in range(3) :
    user['name'] = input('이름을 입력하세요')
    user['kor'] = int(input('국어성적을 입력하세요'))
    user['eng'] = int(input('영어성적을 입력하세요'))
    user['mat'] = int(input('수학성적을 입력하세요'))
    user['tot'] = user.get('kor') + user.get('eng') + user.get('mat')
    user['avg'] = user.get('tot') / 3
    grd = '가'
    if user['avg'] >= 90:
        grd = '수'
    elif user['avg'] >= 80:
        grd = '우'
    elif user['avg'] >= 70:
        grd = '미'
    elif user['avg'] >= 60:
        grd = '양'
    user['grd'] = grd
    userGroup.append(user)
print(userGroup)


# dict 형식 데이터 출력시 예쁘게 표시 : pretty print
from pprint import pprint as pp

for user in userGroup:
    pp(user)