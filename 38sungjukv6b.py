# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv5lib.py에 작성함
# 모듈명은 sjv5로 줄여서 사용함
import sungjukv6blib as sjv6b
# 성적 데이터 저장할 변수 선언
sjs = []
sjv6b.loadSungJuk()

# 프로그램 주 실행부
while True :

    menu = sjv6b.displayMenu()
    if menu == '0' :
        print('성적 프로그램을 종료합니다!')
        break
    elif menu == '1' : sjv6b.addSungJuk(sjs)
    elif menu == '2' : sjv6b.readSungJuk()
    elif menu == '3' : sjv6b.readOneSungJuk(sjs)
    elif menu == '4' : sjv6b.modifySungJuk()
    elif menu == '5' : sjv6b.removeSungJuk()
    elif menu == '0' : break
    else: print('잘못된 번호입력')