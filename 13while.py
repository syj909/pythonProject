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


# 성적처리 프로그램 메뉴화면 구현
# while 문과 break 사용
main_menu = f'''
    성적 처리 프로그램
-----------------------
  1. 성적 데이터 추가
  2. 성적 데이터 조회
  3. 성적 데이터 상세조회
  4. 성적 데이터 수정
  5. 성적 데이터 삭제
  0. 프로그램 종료
-----------------------
'''
while True :
    print(main_menu)
    menu = input('=> 작업을 선택하세요 :')
    
    if menu == '0' :
        print('성적 프로그램을 종료합니다!')
        break
    elif menu == '1' : print('성적 데이터 추가 완료!')
    elif menu == '2' : print('성적 데이터 조회 완료!')
    elif menu == '3' : print('성적 데이터 상세조회 완료!')
    elif menu == '4' : print('성적 데이터 수정 완료!')
    elif menu == '5' : print('성적 데이터 삭제 완료!')
    else : print('잘못된 번호를 입력했습니다.')

# 반복실행시 특정 코드 회피 : continue
# 특정 코드블럭의 실행을 생략하고 싶을 때 사용

# ex) 1~1000사이의 모든 정수의 합을 출력하세요
# 단, 7의 배수나 9의 배수는 젱히하고 누적합을 구함
i = 0
sum = 0

while i <= 1000 :
    i += 1
    if i & 7 == 0 or i % 9 == 0: continue
    sum += i

print(sum)

# ex4) 아이디, 비밀번호를 입력받아
# 미리 설정해둔 아이디, 비밀번호와 일치하면 '로그인  성공!'
# 일치하지 않으면 '로그인 실패!'라고 출력하는 조건문 작성
# 아이디 : abc123, 비밀번호: 987xyz
uid = 'abc123'
pwd = '987xyz'
while True:
    inputUid = input('아이디를 입력하세요.')
    inputPwd = input('비밀번호를 입력하세요.')
    if ((uid == inputUid) and (pwd == inputPwd)):
        print('로그인 성공!')
        break
    else:
        print('로그인 실패!')
        continue

import random as rnd

rnd.seed(2210171044)

# 1 ~ 10 사이 임의의 정수 생성
print(rnd.randint(1, 10))

# 1 ~ 45 사이 임의의 정수 6개 생성

for _ in range(6) : # 반복실행시 인덱스가 필요없으면 _ 사용
    print(rnd.randint(1, 45), end=' ')