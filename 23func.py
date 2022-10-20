# 함수function
# 주어진 입력값으로 무언가를 수행하고 결과물을 내놓는 객체
# 한번 작성해두면 언제든 재사용 가능
# 논리적인 단위 분할 가능 -> 개발의 분업화
# 코드의 구현을 외부로 부터 숨길수 있음 -> 캡슐화

# 함수 정의
# def 함수이름(매개변수):
#     함수몸체

# 함수 호출
# 함수이름(인수)

# 인사말 출력하는 코드 1
print('Hello, World!!')

# 인사말 출력하는 코드 2 - 3번 반복
# print('Hello, World!!')
# print('Hello, World!!')
# print('Hello, World!!')

for _ in range(3) :
    print('Hello, World!!')

# 인사말 출력하는 코드 3
# -> 3번 반복하는 코드를 3번 반복한다면?
# 복붙으로 해결할 수 있지만, 수정사항이 생기면 유지보수가 어려움
for _ in range(3) :
    print('Hello, World!!')
for _ in range(3) :
    print('Hello, World!!')
for _ in range(3) :
    print('Hello, World!!')

for _ in range(3):
    for _ in range(3):
        print('Hello, World!!')

# 인사말 출력하는 코드 4 - 함수
def sayHello():
    for _ in range(3):
        print('Hello, World!!')
sayHello()
sayHello()
sayHello()

# 매개변수 parameter vs 인수 argument
# 매개변수 : 함수 정의시 입력으로 전달된 값을 받는 변수
# 인수 : 인수 호출시 실제 입력으로 전달하는 값

def sayHello(msg):
    for _ in range(3):
        print(f'Hello, {msg}!!')

sayHello('python')
sayHello('Java')

# ex) 두 수를 입력받아 add라는 함수로 호출해서 결과 출력
# 단, add라는 함수는 두 입력값을 더한 후 결과 출력함
def add():
    num1 = int(input('첫번째 숫자'))
    num2 = int(input('두번째 숫자'))
    print(num1 + num2)

add()

# 함수 다중정의 - overloading
# 동일한 이름의 함수를 매개변수에 따라 다른 기능으로
# 동작하도록 작성하는 것을 의미
# 파이썬에서는 공식적으로 지원하는 기능은 아님 - 구현가능
# 다중정의를 너무 남발하면 코드가 복잡해짐

# ex) 잔돈계산하는 프로그램을 함수로 작성
# 함수명 : computeCharge(비용, 지불)
def computeCharge(payMoney, receiveMoney) :
    changeMoney = receiveMoney - payMoney
    print(f'지불금액은 {payMoney}원이고 받은금액은 {receiveMoney}원 입니다. \n 잔액은 {changeMoney} 원입니다.')
    #50000
    money50000 = changeMoney // 50000
    changeMoney = changeMoney - (money50000 * 50000)
    #10000
    money10000 = changeMoney // 10000
    changeMoney = changeMoney - (money10000 * 10000)
    #5000
    money5000 = changeMoney // 5000
    changeMoney = changeMoney - (money5000 * 5000)
    #1000
    money1000 = changeMoney // 1000
    changeMoney = changeMoney - (money1000 * 1000)
    #500
    money500 = changeMoney // 500
    changeMoney = changeMoney - (money500 * 500)
    #100
    money100 = changeMoney // 100
    changeMoney = changeMoney - (money100 * 100)
    #50
    money50 = changeMoney // 50
    changeMoney = changeMoney - (money50 * 50)
    #10
    money10 = changeMoney // 10
    changeMoney = changeMoney - (money10 * 10)

    print(f'50000원권은 {money50000}장, 10000원권은 {money10000}장 \n'
          f'5000원권은 {money5000}장, 1000원권은 {money1000}장 \n'
          f'500원권은 {money500}개, 100원권은 {money100}개 \n'
          f'50원권은 {money50}개, 10원권은 {money10}개 \n')

payMoney = int(input('지불금액을 입력하세요.'))
receiveMoney = int(input('받은금액을 입력하세요.'))

computeCharge(payMoney, receiveMoney)

# 33 - 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 : checkCredit(코드)
# dict 자료구조를 이용해서 작성
def checkCrredit(cardNumber):
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

cardNumber = input('카드번호를 입력하세요.')

checkCrredit(cardNumber)

# ex) 60갑자를 출력해주는 프로그램을 함수로 작성
# checkChinaZodiac(변수)

def checkChinaZodiac(year) :
    BASE = 1444
    ten = ('갑', '을', '병', '정', '무', '기', '경', '신', '임', '계')
    twelve = ('자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해')
    animal = ('쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지')
    i1 = (year - BASE) % 10
    i2 = (year - BASE) % 12
    print("%d년은 %s년(%s의 해) 입니다." % (year, ten[i1] + twelve[i2], animal[i2]))

year = int(input('연도입력:'))
checkChinaZodiac(year)