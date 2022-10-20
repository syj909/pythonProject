# 함수 정의부
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

    sjs.append(sj)

    print('성적데이터추가완료')


def readSungJuk(sjs):
    hdr = '이름 국어 영어 수학\n'
    hdr += '---------------'
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}')
    input('성적 데이터 조회 완료!')


def readOneSungJuk(sjs):
    name = input('조회할 학생의 이름은?')

    sj = None
    for item in sjs:
        if item['name'] == name: sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-----------------------------\n'
    for k in sj.keys():
        print(sj.get(k), end=' ')

    input('\n성적 데이터 상세조회 완료!')


def modifySungJuk(sjs):
    name = input('수정할 학생의 이름은?')

    sj = None
    for i in range(len(sjs)):
        if (sjs[i])['name'] == name: idx = i
    sj = (sjs[idx])
    kor = int(input(f'국어점수 ({sj["kor"]})'))
    eng = int(input(f'영어점수 ({sj["eng"]})'))
    mat = int(input(f'수학점수 ({sj["mat"]})'))

    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    tot, avg, grd = computeSungJuk(sj)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd']= grd

    # 리스트에 다시 저장
    sjs[idx] = sj

    input('성적 데이터 수정 완료!')


def removeSungJuk(sjs):
    name = input('삭제할 학생의 이름은?')

    sj = None
    i = 0
    for i in range(len(sjs)):
        item = sjs[i]
        if item['name'] == name: idx = i
    sjs.pop(idx)
    input('\n성적 데이터 삭제 완료!')

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