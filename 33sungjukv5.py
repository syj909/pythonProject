# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv5lib.py에 작성함
# 모듈명은 sjv5로 줄여서 사용함
import sungjukv5lib as sjv5
# 성적 데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부
while True :
    menu = sjv5.displayMenu()
    if menu == '0' :
        print('성적 프로그램을 종료합니다!')
        break
    elif menu == '1' : sjv5.addSungJuk(sjs)
    elif menu == '2' : sjv5.readSungJuk(sjs)
    elif menu == '3' : sjv5.readOneSungJuk(sjs)
    elif menu == '4' : sjv5.modifySungJuk(sjs)
    elif menu == '5' : sjv5.removeSungJuk(sjs)