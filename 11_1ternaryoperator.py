print('참' if True else '거짓')
print('참' if False else '거짓')

# ex) 윤년여부를 출력하는 프로그램을 작성하세요
# 단, 3항 연산자를 이용해서 구현함

year = int(input('년도는?'))
result = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(year ,'윤년입니다' if result else '윤년이 아닙니다.')

# ex) 년도와 월을 입력받아 윤년여부와
# 입력한 달의 마지막 날을 출력하는 프로그램을 작성하세요
# 30 : 4, 6, 9, 11
# 31 : 1, 3, 5, 8, 10, 12
# 28 : 2
# 29 : 2 (윤년)

year = int(input('년도는?'))
month = int(input('월은?'))

leapyear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
result = '윤년이며' if leapyear else '윤년이 아니며'

dayGroup = {1 : 31, 2 : 29 if leapyear else 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }
day = dayGroup.get(month)
print(f'{year}년은 {result}, {month}는 {day}일까지 있습니다')