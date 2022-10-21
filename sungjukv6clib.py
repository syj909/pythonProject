import csv

# 성적 데이터 저장할 변수 선언
sjs = []

# sungjuk.dat 파일을 읽어서 sjs 변수에 초기화
def loadSungJuk():
    global sjs
    try :
        with open('data/sungjukv6b.dat', encoding='UTF-8') as f:
            data = csv.reader(f)
            sjs = list(data)
    except:
        pass
# 성적데이터들을 sungjukv6b.dat 파일에 저장
#[[name, 77, 33, 86]
# [name, 77, 33, 86]
# [name, 77, 33, 86]]
def saveSungJuk(sjs):
    # new_line : 성적데이터 저장시 줄바꿈이 2번저장되는 것을 방지
    # 방금 입력한 성적데이터와 기존에 입력한 모든 성적데이터를 JSON형식으로 파일에 함께 저장
    # newline 줄바꿈 2번되는 것을 제거
    with open('data/sungjukv6b.dat', 'w', encoding='UTF-8', newline='') as f:
        wf = csv.writer(f) # csv 작업 초기화
        for sj in sjs:
            wf.writerow(sj) # sjs 리스트의 요소를 csv 행으로 저장

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
    sj = [name, kor, eng, mat]
    return sj

def addSungJuk(sjs):
    # 성적데이터 입력받기
    sj = inputSungJuk()

    # 입력받은 성적데이터 초기화
    tot, avg, grd = computeSungJuk(sj)
    # + : 2개의 리스트를 하나로 합쳐 하나의 리스트로 만듦
    sj = sj + [tot, avg, grd]

    sjs.append(sj)

    # sjs에 저장된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

    print('성적데이터추가완료')


def readSungJuk():
    hdr = '이름 국어 영어 수학\n'
    hdr += '---------------'
    print(hdr)
    for sj in sjs:
        print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]}')
    input('성적 데이터 조회 완료!')


def readOneSungJuk(sjs):
    name = input('조회할 학생의 이름은?')

    sj = None
    for item in sjs:
        if item['name'] == name: sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-----------------------------\n'
    print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]} {sj[4]} {sj[5]} {sj[6]}')

    input('\n성적 데이터 상세조회 완료!')


def modifySungJuk():
    name = input('수정할 학생의 이름은?')

    idx = None
    for i in range(len(sjs)):
        if (sjs[i])[0] == name:
            idx = i
            break

    kor = int(input(f'국어점수 ({sjs[idx][0]})'))
    eng = int(input(f'영어점수 ({sjs[idx][1]})'))
    mat = int(input(f'수학점수 ({sjs[idx][2]})'))

    sj = [name, kor, eng, mat]
    tot, avg, grd = computeSungJuk(sj)
    sj = sj + [tot, avg, grd]

    # 리스트에 다시 저장
    sjs[idx] = sj

    # 수정된 성적데이터를 파일에 저장
    saveSungJuk(sjs)
    input('성적 데이터 수정 완료!')


def removeSungJuk():
    name = input('삭제할 학생의 이름은?')

    for sj in sjs:
        if sj[0] == name:
            sjs.remove(sj)

            # 수정된 성적데이터를 파일에 저장
            saveSungJuk(sjs)

    input('\n성적 데이터 삭제 완료!')

def computeSungJuk(sj) :
    tot = sj[1] + sj[2] + sj[3]
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