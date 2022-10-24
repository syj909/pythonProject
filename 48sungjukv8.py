# OOP을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은
# sungjukv8lib, sungjukv8dao에 작성함
# 모듈명은 sjv5로 줄여서 사용함
from SungJukv8Lib import SungJukv8Lib as sjv8
# 성적 데이터 저장할 변수 선언

# 프로그램 주 실행부
while True :
    menu = sjv8.display_menu()
    if menu == '0' :
        print('성적 프로그램을 종료합니다!')
        break
    elif menu == '1' : sjv8.add_sungjuk()
    elif menu == '2' : sjv8.read_sungjuk()
    elif menu == '3' : sjv8.readone_sungjuk()
    elif menu == '4' : sjv8.modify_sungjuk()
    elif menu == '5' : sjv8.remove_sungjuk()
    elif menu == '0' : break
    else: print('잘못된 번호입력')