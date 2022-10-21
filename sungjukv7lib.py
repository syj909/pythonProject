import pymysql

url = 'bigdata.cdvxhjnddlzx.ap-northeast-2.rds.amazonaws.com'
userid = 'admin'
passwd = 'bigdata_2022'
dbname = 'bigdata'


def displayMenu():
    main_menu = f'''
        성적 처리 프로그램v4
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

def inputSungJuk():
    name = input('이름은')
    kor = int(input('국어점수'))
    eng = int(input('영어점수'))
    mat = int(input('수학점수'))
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    return sj

def addSungJuk(sjs):
    # 성적데이터 입력받기
    sj = inputSungJuk()

    # 입력받은 성적데이터 초기화
    tot, avg, grd = computeSungJuk(sj)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd




def readSungJuk():
    hdr = '이름 국어 영어 수학\n'
    hdr += '---------------'
    print(hdr)
    # 성적테이블에서 '이름/국어/영어/수학'만 select해서 출력


def readOneSungJuk(sjs):
    name = input('조회할 학생의 이름은?')

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-----------------------------\n'
    print(hdr)

    # 입력한 학생이름으로 성적테이블을 조회해서
    # 조회된 결과를 출력


def modifySungJuk():
    name = input('수정할 학생의 이름은?')

    # 수정할 학생이름으로 기존데이터 조회

    # 새로운 값을 입력받음
    kor = int(input(f'국어점수 ({sj["kor"]})'))
    eng = int(input(f'영어점수 ({sj["eng"]})'))
    mat = int(input(f'수학점수 ({sj["mat"]})'))

    # 다시 성적 처리
    sj = [name, kor, eng, mat]
    tot, avg, grd = computeSungJuk(sj)
    sj = sj + [tot, avg, grd]

    # 새롭게 입력된 성적데이터를 기존 성적데이터에 저장


def removeSungJuk():
    name = input('삭제할 학생의 이름은?')

    # 삭제할 학생이름 입력받아
    # 성적테이블에서 해당 학생 데이터 삭제

def computeSungJuk(sj) :
    tot = sj['kor'] + sj['eng'] + sj['mat']
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'
    return tot, avg, grd