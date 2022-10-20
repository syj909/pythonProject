# 파이썬 자료구조
# 자료구조는 대량의 데이터를 효율적으로 저장, 조회, 수정, 삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

# 성적프로그램 v2
# 이름, 국어, 영어, 수학을 입력하면
# 총점, 평균, 학점을 처리해서 결과출력
# 단, 3명의 학새엥 대해 성적처리를 진행함
# 변수 초기화
name1, name2, name3 = '혜교', '지현', '수지'
kor1, kor2, kor3 = 99, 65, 75
# ...
# 처리할 데이터 갯수에 따라 변수를 일일이 선언해야함 - 불편

# tot1 =kor1 + eng1 + mat1
# tot2 =kor2 + eng2 + mat2
# tot3 =kor3 + eng3 + mat
# ...
# 성적처리시에도 동일한 코드를 여러번 반복해 작성함 - 번거로움


# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근하려면 변수[인덱스] 형식을 사용

# 점심메뉴를 리스트로 정의
menus = ['라면', '돈까스', '짜장면', '냉면', '정식']

print(menus)
print(menus[0], menus[1], menus[2], menus[3], menus[4])

i = 0
for i in range(len(menus)) :
    print(menus[i], end=' ')

for menu in menus: # 리스트의 요소를 하나씩 훑어가며 출력
    print(menu, end=' ')


names = ['혜교', '지현', '수지']
kors = [99, 54, 65]
engs = [76, 77, 87]
mats = [87, 77, 90]
tots = [0, 0, 0]
avgs = [0, 0, 0]
grds = ['', '', '']

tots[0] = kors[0] + engs[0] + mats[0]
tots[1] = kors[1] + engs[1] + mats[1]
tots[2] = kors[2] + engs[2] + mats[2]

avgs[0] = tots[0] / 3
avgs[1] = tots[1] / 3
avgs[2] = tots[2] / 3

if avgs[0] >=90: grds[0] = '수'
elif avgs[0] >=80: grds[0] = '우'
elif avgs[0] >=70: grds[0] = '미'
elif avgs[0] >=60: grds[0] = '양'

if avgs[1] >=90: grds[1] = '수'
elif avgs[1] >=80: grds[1] = '우'
elif avgs[1] >=70: grds[1] = '미'
elif avgs[1] >=60: grds[1] = '양'

if avgs[2] >=90: grds[2] = '수'
elif avgs[2] >=80: grds[2] = '우'
elif avgs[2] >=70: grds[2] = '미'
elif avgs[2] >=60: grds[2] = '양'

# 결과출력
print(names[0], kors[0], engs[0], mats[0], tots[0], avgs[0], grds[0])
print(names[1], kors[1], engs[1], mats[1], tots[1], avgs[1], grds[1])
print(names[2], kors[2], engs[2], mats[2], tots[2], avgs[2], grds[2])

for i in range(len(names)) :
    tots[i] = kors[i] + engs[i] + mats[i]
    avgs[i] = tots[i] / 3
    if avgs[i] >= 90:
        grds[i] = '수'
    elif avgs[i] >= 80:
        grds[i] = '우'
    elif avgs[i] >= 70:
        grds[i] = '미'
    elif avgs[i] >= 60:
        grds[i] = '양'
for i in range(len(names)) :
    print(names[i], kors[i], engs[i], mats[i], tots[i], avgs[i], grds[i])

# p110 ex1), ex2)

lst = [10, 1, 5, 2]
result = lst * 2
print('1단계:', result)

result.append(lst[0] * 2)
print('2단계', result)

result2 = []
for i in range(len(result)) :
    if i % 2 != 0 :
        result2.append(result[i])
print('3단계', result2)

# ex2 - A
time = 0
count = int(input('리스트의 크기를 입력하세요.'))
list = []

for time in range(count) :
    list.append(int(input(f'{time + 1}번째 숫자를 입력하세요')))

print('list의 크기:', len(list))
print('list:', list)

# ex2 - B
time = 0
count = int(input('리스트의 크기를 입력하세요.'))
list = []

for time in range(count) :
    list.append(int(input(f'{time + 1}번째 숫자를 입력하세요')))

search = int(input('찾을 숫자를 입력하세요'))

# for i in list :
#     if i == search :
#         print('YES')
#         break
#     else :
#         print('NO')
#         break
if search in list :
    print('YES')
else :
    print('NO')

# employees.csv를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid
empnoList = []
fnameList = []
lnameList = []
emailList = []
hdateList = []
jobidList = []
salList = []
deptidList = []
add = ''

while True :
    empnoList.append(input('사번을 입력하세요'))
    fnameList.append(input('이름을 입력하세요'))
    lnameList.append(input('성을 입력하세요'))
    emailList.append(input('이메일을 입력하세요'))
    hdateList.append(input('입사일을 입력하세요'))
    jobidList.append(input('직책을 입력하세요'))
    salList.append(input('급여를 입력하세요'))
    deptidList.append(input('부서번호를 입력하세요'))
    add = input('더 추가하시겠습니까? (y/n)')
    if add == 'n' :
        break
    elif add == 'y' :
        continue

for i in range(len(empnoList)) :
    print(empnoList[i], fnameList[i], lnameList[i], emailList[i]
          , hdateList[i], jobidList[i], salList[i], deptidList[i])

# 2차원 리스트
# 리스트 선언시 요소의 자료형에는 제약이 없음
# 따라서, 리스트의 요소로 리스트 자체를 값으로 구성할 수 있음.

# A,B,C 반 학생의 성적 데이터를 리스트로 구현
# 리스트의 요소로 사용하는 리스트
score = [
    [98, 56, 54, 65, 87],
    [55, 66, 77, 88, 99],
    [11, 22, 33]
]
print(score)

# 2차원 리스트 출력하기 1 :for ~ range
for i in range(len(score)) :
    print(score[i])

# 2차원 리스트 출력하기 2 :
for sc in score :
    print(sc)
# 2차원 리스트 출력하기 3 : 중첩 for ~ in
for sc in score :
    for s in sc :
        print(s, end=' ')
    print()     # 요소 리스트의 모든 값 출력 후 줄바꿈
    
# 2차원 리스트 동적 생성
# 리스트 크기를 사용자로부터 입력받음
# 요소로 사용하는 리스트의 크기는 난수로 생성하고
# 요소 리스트를 구성하는 값 역시 난수로 생성

import random
lsts = []
size1 = int(input('리스트이 크기는?'))

for i in range(size1) :
    lst = []
    size2 = random.randint(1, 10)
    for j in range(size2) :
        val = random.randint(50, 100)
        lst.append(val)
    lsts.append(lst)
print(lsts)