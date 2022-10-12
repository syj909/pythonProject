# ex) 주민번호에서 생년과 월, 일, 성별을 추출해서
# 각 변수에 적절히 저장하세요.
jumin = '2205092123456'

year = jumin[0 : 2]
month = jumin[2 : 4]
day = jumin[4 : 6]
gender = '여' if (int(jumin[6]) == 2) else '남'

print(f'생년월일은 {year}년 {month}월 {day}일이며 성별은 {gender}입니다.')

# 16 - 잔돈계산
payMoney = int(input('지불금액을 입력하세요.'))
receiveMoney = int(input('받은금액을 입력하세요.'))

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
      f'500원권은 {money500}장, 100원권은 {money100}장 \n'
      f'50원권은 {money50}장, 10원권은 {money10}장 \n')