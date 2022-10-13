# 33

cardNumber = input('카드번호를 입력하세요.')

if cardNumber[0:2] == '35':
    if cardNumber[2:6] == '6317' :
        print('NH농협 JCB카드')
    elif cardNumber[2:6] == '6901' :
        print('신한 JCB카드')
    elif cardNumber[2:6] == '6912' :
        print('KB국민 JCB카드')
elif cardNumber[0] == '4' :
    if cardNumber[2:6] == '4825' :
        print('비씨 VISA카드')
    if cardNumber[2:6] == '8676' :
        print('신한 VISA카드')
    if cardNumber[2:6] == '7973' :
        print('KB국민 VISA카드')
elif cardNumber[0] == '5' :
    if cardNumber[2:6] == '5594' :
        print('신한카드 Master카드')
    if cardNumber[2:6] == '4353' :
        print('외환카드 Master카드')
    if cardNumber[2:6] == '0926' :
        print('KB국민카드 Master카드')

# 35
daytime = input('영단어를 입력바람')

if daytime == 'morning hours' :
    print('아침시간 (7-12)')
elif daytime == 'midday ' or 'noon' :
    print('점심시간 (12-1)')
elif daytime == 'afternoon hours' :
    print('오후 (1-6)')
elif daytime == 'evening hours' :
    print('저녁시간 (6-9)')
elif daytime == 'night hours' :
    print('밤시간 (9-12)')
elif daytime == 'midnight' :
    print('자정시간 (12)')
elif daytime == 'early morning hours' :
    print('새벽시간 (12-5)')
elif daytime == 'small hours' :
    print('새벽 (1-3)')
elif daytime == 'dawn' or 'daybreak' :
    print('해뜰력 (5-7)')
else :
    print('잘못입력함')

# switch ~ case 와 비슷하게 작성해보기
# 파이썬은 지금까지 (~v3.9) switch ~ case 구문을 지원하지 않음
# 만일, switch ~case 구문을 구현하려면 dict을 이용해야함
# 한편, v3.10 이상부터는 match case라는 구문으로 구현가능

# dict 자료구조
# 키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류임
# 객체명 = {키 : 값} => 객체명.get(키), 객체명[키]

cards = {'356317' : 'NH농협JCB카드', '404825' : '비씨Visa카드', '515594' : '신한Master카드'}

cards.get('404825')

# 성적처리 프로그램 v3b
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 계산하고 출력함
# 학점처리 조건은 수우미양가로 함
# 단, 학점은 dict을 이용해서 처리함

name = input('이름입력')
kor = int(input('국어'))
eng = int(input('영어'))
mat = int(input('수학'))
grade = ''

total = kor + eng + mat
avg = total / 3

grade = { 100 >= avg >= 81 : '수', 80 >= avg >= 61 : '우', 60 >= avg >= 41 : '미', 40 >= avg >= 21 : '양', 20 >= avg : '가' }

print(f'이름 : {name}, 평균 : {avg:.1f}, 학점 : {grade.get(True)}')