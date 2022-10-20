# 예외처리
# 프로그램을 만들다 보면 수많은 에러가 발생함
# 코드를 잘못 작성하거나, 실행상의 문제로 인해
# 에러가 발생하면 프로그램 실행이 중단되기도 함

# 하지만, 프로그램이 중단되는 것을 피하기 위해
# 이러한 에러는 무시하고 넘어가줬으면 하는때도 있음
# 에러에 따른 적절한 처리를 하고 싶을때도 있을 것임

# 파이썬에서는 try-except 구문으로
# 예외처리를 할 수 있음

# error와 except 차이 비교
# 에러 : 프로그램 실행 중 오작동이나 비정상적 종료를
# 유발하게 하는 원인

# 컴파일 오류 : 주로 문법적 오류를 의미 - 개발자 조치 가능
# 논리 오류 : 실행가능, 하지만 예상한 결과가 안나오는 오류 - 개발자 조치 가능
# 시스템 오류 : 메모리 초과, 서버접속 불가 등등의 오류 - 조치 불가
# 실행 오류 : 프로그램 실행 중 발생하는 예외적인 오류

# 예외 : 개발자가 완전히 조치할 수 없지만
# 어느정도 수습할 수 있는 수준의 덜 심각한 오류
# 예외처리를 통해 프로그램의 비정상 종료를 막을 수 있음

# 오류 발생 1
print('- 프로그램 시작-')
print(10/5)
print('- 프로그램 끝-')

# 오류 발생 2
print('- 프로그램 시작-')
print(10/0)
print('- 프로그램 끝-')

# 오류 발생 3
print('- 프로그램 시작-')
nums = [1, 2, 3]
print(nums[100])
print('- 프로그램 끝-')

# 발생한 오류 처리하기
# try :
#       오류가 발생할만한 코드
# except :
#       오류가 발생할 때 실행할 코드

# 예외처리 1
print('- 프로그램 시작-')
try :
    print(10/0)         # 오류가 발생하더라도
except:
    print('오류발생')     # 중단되지않고 끝까지 실행
print('- 프로그램 끝-')

# 예외처리 2
try :
    print('- 프로그램 시작-')
    print(10/0)         # 오류가 발생하더라도
    print('- 프로그램 끝-')
except:
    print('오류발생')     # 중단되지않고 끝까지 실행

# 예외처리 3
print('- 프로그램 시작-')
nums = [1, 2, 3]
print(nums[100])
print('- 프로그램 끝-')

# 발생한 오류를 특정지어 처리하기
# try :
#       오류가 발생할만한 코드
# except 발생한 오류 유형:
#       오류가 발생할 때 실행할 코드

# 예외처리 4
# 다양하게 발생하는 예외상황에 대한 적절한 코드 작성
# 아래코드 실행시 발생하는 오류 수는 3가지
# 1. 리스트 인덱스 초과 2. 0으로 나누려고 할 때 3. 문자 입력 시
nums = [1, 10, 20, 50]
try:
    idx = int(input('nums에서 사용할 값의 index는?'))
    divr = int(input('앞에서 선택한 값을 나눌 정수는?'))
    print(nums[idx] / divr)
except:
    print('오류발생')

# 예외처리 5
nums = [1, 10, 20, 50]
try:
    idx = int(input('nums에서 사용할 값의 index는?'))
    divr = int(input('앞에서 선택한 값을 나눌 정수는?'))
    print(nums[idx] / divr)
except IndexError:
    print('리스트의 인덱스가 너무 큼')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요')
except ValueError:
    print('숫자만 입력하세요')

# 파이썬에서 제공하는 예외처리 모듈
import builtins
dir(builtins) # 다양한 예외 관련 모듈이 표시

# 예외처리 6
nums = [1, 10, 20, 50]
try:
    idx = int(input('nums에서 사용할 값의 index는?'))
    divr = int(input('앞에서 선택한 값을 나눌 정수는?'))
    print(nums[idx] / divr)
except IndexError as ie:
    print('리스트의 인덱스가 너무 큼', ie)
except ZeroDivisionError as zde:
    print('0으로 나눌 수 없어요', zde)
except ValueError as ve:
    print('숫자만 입력하세요', ve)

# 예외처리 7
import sys
nums = [1, 10, 20, 50]
try:
    idx = int(input('nums에서 사용할 값의 index는?'))
    divr = int(input('앞에서 선택한 값을 나눌 정수는?'))
    print(nums[idx] / divr)
except:
    extype, exval, trackback = sys.exc_info()
    print(extype.__name__, trackback.tb_frame.f_code.co_filenmae, trackback.tb_lineno, exval.message)
        # 예외이름          # 파일명                                   # 예외발생 위치       # 예외메세지

# 예외발생과 상관없이 항상 코드 실행 : finally
# 주로 자원반납과 관련된 코드들에 사용
# try
#    코드
# except:
#   예외처리
# finally:
#   항상실행될코드

# 예외처리 8
try :
    print('- 프로그램 시작-')
    print(10/0)         # 오류가 발생하더라도
except:
    print('오류발생')     # 중단되지않고 끝까지 실행
finally:
    print('- 프로그램 끝-')