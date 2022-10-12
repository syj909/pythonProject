#input 함수
# 변수명 = input(입력메세지)

# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균을 계산하고 출력함
name = input('이름은?')

kor = int(input('국어'))
eng = int(input('영어'))
mat = int(input('수학'))

total = kor + eng + mat
avg = total / 3
print(f'{name}의 국어: {kor:03d}, 영어: {eng:03d} , 수학 : {mat:03d}')
print(f'총합은 {total:d}')
print(f'평균은 {avg:.1f}')


fat = int(input('지방의 그램을 입력하세요'))
carbohydrate = int(input('탄수화물의 그램을 입력하세요'))
protein = int(input('단백질의 그램을 입력하세요'))

total = (fat * 9) + (carbohydrate * 4) + (protein * 4)
print(f'총칼로리 : {total} cal')

print('    성적 처리 프로그램')
print('-----------------------')
print('  1. 성적 데이터 추가')
print('  2. 성적 데이터 조회')
print('  3. 성적 데이터 상세조회')
print('  4. 성적 데이터 수정')
print('  5. 성적 데이터 삭제')
print('  0. 프로그램 종료')
print('-----------------------')
work = input('=> 작업을 선택하세요 :')

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
print(main_menu)
work = input('=> 작업을 선택하세요 :')