# 조건문
# 조건에 따라 프로그램의 실행 순서를 조정하는 문장
# 만약에 ~한다면 ~하고 아니면 ~하라 라는 문제 해결시 주로 사용
# 조건무 ㄴ

# if
#   참일 때 실행할 문장
# else :
#   거짓일 때 실행할 문장

# ex1) 입력한 어떤 수가 짝수인지 판단하는 조건문
num = int(input('정수 하나를 입력하세요'))

if num % 2 == 0 :
    print('입력한 순느 짝수입니다.')

# ex2) 점수 3개를 입력받아 평균이 60이상이고
# 각 점수가 40점 이상이면 합격이라 출력하는 조건문 작성
# 50 60 65
# 40 90 65

kor = int(input('국어 점수를 입력하세요.'))
eng = int(input('영어 점수를 입력하세요.'))
mat = int(input('수학 점수를 입력하세요.'))
isPassed = True

score = [kor, eng, mat]
avg = (kor + eng + mat) / 3

if avg >= 60 :
    for j in range(0, len(score)):
        if isPassed and score[j] >= 40 :
            print(score[j])
            isPassed = True
        else :
            isPassed = False
else :
    isPassed = False

print('합격입니다' if (isPassed) else '불합격입니다.')

# ex4) 아이디, 비밀번호를 입력받아
# 미리 설정해둔 아이디, 비밀번호와 일치하면 '로그인  성공!'
# 일치하지 않으면 '로그인 실패!'라고 출력하는 조건문 작성
# 아이디 : abc123, 비밀번호: 987xyz

uid = 'abc123'
pwd = '987xyz'

inputUid = input('아이디를 입력하세요.')
inputPwd = input('비밀번호를 입력하세요.')

if((uid==inputUid) and (pwd==inputPwd)) :
    print('로그인 성공!')
else :
    print('로그인 실패!')