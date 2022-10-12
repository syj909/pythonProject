# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
name = 'hong'
kor = 99
eng = 98
mat = 99
total = kor + eng + mat
avg = total / 3

# 출력3 - 출력서식 사용 : % 문자 사용
# print(출력서식 % 변수들..)
# 출력서식 문자 : %d %f %s
print('이름 : %s' % name)
print('국어 : %d 영어 : %d 수학 : %d ' % (kor, eng, mat))
print('총점 : %d 평균 : %d' % (total, avg))

# 출력4 - 인덱스, 출력서식 사용 : .format함수 사용
# print({인덱스:출력서식}.format(변수들...))
print('이름 : {0:s}'.format(name))
print('국어 : {0:03d}, 영어 : {1:03d}, 수학 : {2:03d}'.format(kor, eng, mat))
print('총점 : {0:d}, 평균 : {1:.1f}'.format(total, avg))

# 출력5 - 문자열 템플릿(f-string) : py 3.6이후 지원
# print({변수명:출력서식})
print(f'이름 : {name:s}')
print(f'국어 : {kor:03d}, 영어 : {eng:03d}, 수학 : {mat:03d}')
print(f'총점 : {total:d}, 평균 : {avg:.1f}')