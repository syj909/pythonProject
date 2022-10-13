# 다중 if문
# if~else 만으로 다양한 조건을 판단하기 어려움
# 다양한 조건에 따라 판단하기 위해서는
# if ~ elif ~ else 구문을 사용해야 함


jumsu = 55
if jumsu <= 50 : print('노력하세요')
else :
    if jumsu <= 80 : print('잘했어요')
    else:
        if jumsu <=100 : print('최고에요')


if jumsu <= 50 :
    print('노력하세요')
elif jumsu <= 80 :
    print('잘했어요')
elif jumsu <=100 :
    print('최고에요')

# 성적처리 프로그램 v3
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 계산하고 출력함
# 학점처리 조건은 수우미양가로 함
name = input('이름입력') 
kor = int(input('국어'))
eng = int(input('영어'))
mat = int(input('수학'))
grade = ''

total = kor + eng + mat
avg = total / 3
if avg >= 81 :
    grade = '수'
elif avg >= 61 :
    grade = '우'
elif avg >= 41 :
    grade = '미'
elif avg >= 21 :
    grade = '양'
else :
    grade = '가'

print(f'이름 : {name}, 평균 : {avg:.1f}, 학점 : {grade}')


# ex) p77. 항공사 짐 무게에 따른 수수료 계산

weight = int(input('짐의 무게는 얼마입니까?'))
fare = 0

if weight >= 10 :
    print('수수료는 10000원입니다.')
else :
    print('수수료는 없습니다.')


weight = int(input('짐의 무게는 얼마입니까?'))
fare = 0

if weight >= 10 :
    fare = weight // 10
    print(f'수수료는 {fare * 10000}원입니다.')
else :
    print('수수료는 없습니다.')
    
# 출생연도를 입력받아 나이 계산한 후
# 나이에 따른 학생 분류 후 결과 출력
from datetime import datetime

now = datetime.now()

year = int(input('출력연도를 입력하세요'))
age = now.year - year

if age < 8 or 25 < age  :
    print('학생이 아닙니다.')
elif age >= 20 :
    print('대학생입니다.')
elif age >= 17 :
    print('고등학생입니다.')
elif age >= 14 :
    print('중학생입니다.')
elif age >= 8 :
    print('초등학생입니다.')

