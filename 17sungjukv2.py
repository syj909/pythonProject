# 성적처리 프로그램 메뉴화면 구현
# while 문과 break 사용

names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

# 프로그램 메뉴 출력을 위한 변수 선언
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
while True :
    menu = input('입력')
    
    if menu == '0' :
        print('성적 프로그램을 종료합니다!')
        break
    elif menu == '1' :
        name = input('이름은')
        kor = int(input('국어점수'))
        eng = int(input('영어점수'))
        mat = int(input('수학점수'))
        tot = kor + eng + mat
        avg = tot / 3
        grd = '가'
        if avg >= 90 : grd = '수'
        elif avg >= 80 : grd = '우'
        elif avg >= 70 : grd = '미'
        elif avg >= 60 : grd = '양'

        names.append(name)
        kors.append(kor)
        engs.append(eng)
        mats.append(mat)
        tots.append(tot)
        avgs.append(avg)
        grds.append(grd)
        
        print('성적데이터추가완료')
    elif menu == '2' : # 이름,국어,영어,수학만 출력
        hdr = '이름 국어 영어 수학\n'
        hdr += '---------------'
        print(hdr)

        for i in range(len(names)) :
            print(f'{names[i]} {kors[i]} {engs[i]} {mats[i]}')
        print('성적 데이터 조회 완료!')