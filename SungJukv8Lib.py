import pymysql

from SungJukVO import SungJukVO
from SungJukv8DAO import SungJukv8DAO as sjdao


class SungJukv8Lib:
    @staticmethod
    def display_menu():
        main_menu = f'''
            성적 처리 프로그램v8
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
        return input('실행할 구문?')
    
    # priavte function으로 선언
    @staticmethod
    def __input_sungjuk():
        name = input('이름은')
        kor = int(input('국어점수'))
        eng = int(input('영어점수'))
        mat = int(input('수학점수'))

        return SungJukVO(name, kor, eng, mat)

    @staticmethod
    def add_sungjuk():
        # 성적데이터 입력받기
        sj = SungJukv8Lib.__input_sungjuk()

        # 입력받은 성적데이터 처리
        SungJukv8Lib.__compute_sungjuk(sj)

        if sjdao.insert_sungjuk(sj) > 0:
            print('성적데이터 추가완료!!')

    @staticmethod
    def read_sungjuk():
        hdr = '이름 국어 영어 수학\n'
        hdr += '---------------'
        print(hdr)

        rows = sjdao.select_sungjuk()

        result = '' # 출력할 결과를 담아둘 변수 선언
        for row in rows:
            result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'
        print(result)

    @staticmethod
    def readone_sungjuk():
        name = input('조회할 학생의 이름은?')

        hdr = '번호 이름 국어 영어 수학 총점 평균 학점\n'
        hdr += '-----------------------------\n'
        print(hdr)

        row = sjdao.selectone_sungjuk(name)

        print(f'{row[0]}  {row[1]}  {row[2]}  {row[3]}  {row[4]}  {row[5]}  {row[6]:.1f}, {row[7]}', '\n')
    @staticmethod
    def modify_sungjuk():
        name = input('수정할 학생의 이름은?')

        sj = sjdao.selectone_sungjuk(name)
        # 번호/이름/국어/영어/수학/총점/평균/학점/등록일

        # 새로운 값을 입력받음
        kor = int(input(f'국어점수 ({sj[2]})'))
        eng = int(input(f'영어점수 ({sj[3]})'))
        mat = int(input(f'수학점수 ({sj[4]})'))

        # 다시 성적 처리
        sj = SungJukVO(name, kor, eng, mat)
        SungJukv8Lib.__compute_sungjuk(sj)

        # 새롭게 입력된 성적데이터를 기존 성적데이터에 저장
        cnt = sjdao.update_sungjuk(sj)

        if cnt > 0:
            print('성공적으로 수정되었습니다.')
        else :
            print('수정실패!')

    @staticmethod
    def remove_sungjuk():
        name = input('삭제할 학생의 이름은?')

        cnt = sjdao.delete_sungjuk(name)

        if cnt > 0 :
            print('성공적으로 삭제되었어요!!')
        else :
            print('삭제실패!')

    @staticmethod
    def __compute_sungjuk(sj) :
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        if sj.avg >= 90: sj.grd = '수'
        elif sj.avg >= 80: sj.grd = '우'
        elif sj.avg >= 70: sj.grd = '미'
        elif sj.avg >= 60: sj.grd = '양'