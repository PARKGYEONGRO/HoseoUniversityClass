#함수 만들어보기
def greet():
    print('안녕하세요')
    print('환영합니다.')
# greet()


#매개변수 - 입력 받기
def greet2(name):
    print(f'{name}님, 안녕하세요.')
# greet2('홍길동')


#매개변수, 인자
def add1(a,b): #매개변수
    print(a+b)
# add1(2,3) #인자


#return 과 print의 차이
#• print 는 보여주기만, return 은 값을 남김
def add2(a,b):
    print(a+b)
def add3(a,b):
    return a+b



#매개변수 여러 개
def introduce(name, age, city):
    print(f'{name}, {age}살, {city}거주')
# introduce('홍길동', 100, '한양')


#기본값 매개변수
# • 매개변수에 = 기본값 지정
# • 인자를 안 넣으면 기본값 사용, 넣으면 그 값 사용
def greet(name, greeting="안녕하세요"):
    print(f"{name}님, {greeting}!")
# greet("홍길동") # 홍길동님, 안녕하세요!
# greet("김철수", "반갑습니다") # 김철수님, 반갑습니다!


#위치 인자와 키워드 인자
def order(item, count):
    print(f"{item} {count}개")
# order("커피", 2) # 위치 인자 (순서대로)
# order(item="커피", count=2) # 키워드 인자 (이름 지정)
# order("커피", count=2) # 섞어쓰기 (위치 먼저!)


#가변 인자
#개수가 정해지지 않은 인자들을 튜플로 모음
def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
# print(add_all(1, 2, 3)) # 6
# print(add_all(1, 2, 3, 4, 5)) # 15

#가변인자 활용
def print_menu(*items):
    print('=== 메뉴 ===')
    for i, item in enumerate(items, 1):
        print(f'{i}, {item}')
# print_menu('아메리카노', ' 라떼', '콜드브루')



#키워드 가변 인자
def make_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
# make_profile(name="홍길동", age=24, city="서울")

#인자 정리
# 종류                  표기            모이는 형태
# 위치 인자             a, b            순서대로
# 기본값                a=10            안 주면 기본값
# 키워드 인자           a=10(호출)      이름으로
# *args                 *nums           튜플
# **kwargs              **info          딕셔너리


# 변수의 범위(스코프) -> 지역 변수, 전역 변수
# • 함수 안에서 만든 변수는 함수 안에서만 유효
# • 이걸 스코프(범위) 라고 함

def my_func():
    x = 10 # 함수 안에서 만든 변수
    print(x)
# my_func() # 10
# print(x) # 에러! 밖에서는 못 봄

#지역 변수
def calc():
    result = 100 # 지역 변수
    return result
# calc()
# print(result) # 에러

#전역 변수
count = 0 # 전역 변수 (함수 밖)
def show():
    print(count) # 읽기는 가능
# show() # 0

#전역 변수 수정의 함정
count = 0
def increase():
    count = count + 1 # 에러!

#해결: global 키워드
#• global 남용은 권장 안 함(버그 유발)
def increase():
    global count
    count += 1

#return으로 주고 받기(권장)
count = 0
def increase(n):
    return n + 1 # 값을 돌려줌

# count = increase(count) # 0 → 1
# count = increase(count) # 1 → 2
# print(count) # 2


#docstring """"""
'''
'''
"""
"""
def calculate_bmi(weight, height):
    '''몸무게와 키로 BMI를 계산해 반환'''
    return weight / ((height / 100) ** 2)
# help(calculate_bmi) #설명 볼 수 있음, help는 python 내장 함수


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False # 나누어지면 소수 아님
    return True
# for num in range(2, 20):
#     if is_prime(num):
#         print(num, end=" ") # 3 5 7 11 13 17 19


# import random

# #추첨
# names =['김철수','이영희','박민수']
# winner= random.choice(names)
# print(f'당첨자:{winner}')

# #랜덤 비밀번호용 숫자
# code = random.randint(1000,9999)
# print(f'인증번호: {code}')


#날짜 계산
# from datetime import date

# today = date.today()
# exam = date(2026, 12, 25)
# dday=(exam - today).days
# print(f'D-{dday}') #남은 일 수

# today = date.today()
# exam = date(2025, 12, 25)
# dday=(today-exam).days
# print(f'D+{dday}') #지난 일 수


# import os
# print(os.getcwd())
# print(os.listdir())

# import mytools #만든 모듈인데 이걸 사용하려면 같은 폴더에 두거나 아니면 os와 sys 모듈 불러와서 path에 부모 폴더 경로를 추가해야 가져올 수 있음
# print(mytools.add(1 ,2))

# import random
# import string

# length = int(input('비밀번호 길이: '))

# chars = string.ascii_letters + string.digits
# password = ''
# for _ in range(length):
#     password += random.choice(chars)
# print(f'생성된 비밀번호:{password}')


#심심해서 혼자 해보는 브루트 포스 알고리즘
# def crack_password():
#     import random as rd
#     password = str(rd.randint(0, 9999))

#     for guess in range(10000):
#         guess_str = f'{guess:04d}'
#         if guess_str == password:
#             return f'비밀번호는 {guess_str}'
#     return '실패'
# print(crack_password())


# #문자열 시퀀스
# s = 'hello'
# for ch in s:
#     print(ch)
# print(len(s))
# print('e'in s)

# #대소문자 변환
# s = "Hello World"
# print(s.upper()) # HELLO WORLD
# print(s.lower()) # hello world
# print(s.title()) # Hello World (단어 첫글자)
# print(s.capitalize()) # Hello world (문장 첫글자)

# #공백제거 strip
# s = " 안녕하세요 "
# print(s.strip()) # "안녕하세요" (양끝 공백 제거)
# print(s.lstrip()) # 왼쪽만
# print(s.rstrip()) # 오른쪽만
# email = " test@test.com \n"
# print(email.strip()) # 깔끔하게

# #바꾸기 replace
# s = "I like cats"
# print(s.replace("cats", "dogs")) # I like dogs
# print("010-1234-5678".replace("-", "")) # 01012345678
# # 여러 번 바꾸기
# print("aaa".replace("a", "b")) # bbb

# #★나누기 split -> List 형태로 변환
# s = "사과,바나나,포도"
# print(s.split(",")) # ['사과', '바나나', '포도']
# sentence = "나는 파이썬을 배운다"
# print(sentence.split()) # ['나는', '파이썬을', '배운다']

# #★합치기 join
# words = ["사과", "바나나", "포도"]
# print(",".join(words)) # 사과,바나나,포도
# print(" ".join(words)) # 사과 바나나 포도
# print("".join(words)) # 사과바나나포도

#찾기 find, index
# s = "Hello World"
# print(s.find("World")) # 6 (위치)
# print(s.find("Python")) # -1 (없으면 -1)
# print(s.index("o")) # 4 (첫 번째 o)

# #세기 count
# s = "banana"
# print(s.count("a")) # 3
# print(s.count("an")) # 2
# text = "도 레 미 도 도"
# print(text.count("도")) # 3

# # 시작 끝 확인 startswith, endswith
# file = "report.pdf"
# print(file.endswith(".pdf")) # True
# print(file.startswith("report")) # True
# url = "https://google.com"
# print(url.startswith("https")) # True (보안 확인)

# #검사 메서드 isdigit, isalpha
# print("12345".isdigit()) # True (전부 숫자?)
# print("abc".isalpha()) # True (전부 글자?)
# print("abc123".isalnum()) # True (글자+숫자?)
# print(" ".isspace()) # True (전부 공백?)

#이스케이프 문자
# print("줄1\n줄2") # \n = 줄바꿈
# print("이름\t나이") # \t = 탭
# print("그는 \"안녕\"") # \" = 따옴표
# print("C:\\Users") # \\ = 백슬래시

# 문자열 메서드 정리
# 메서드                기능
# upper/lower       대소문자
# strip 공백        제거
# replace           바꾸기
# split/join        나누기/합치기
# find/count        찾기/세기
# startswith        시작 확인
# isdigit           숫자인지


# #문장 분석기 실습
# text = input('문장을 입력하세요: ')

# print(f'전체 길이: {len(text)}자')
# print(f'공백 제외: {len(text.replace(' ',''))}자')
# print(f'단어 수: {len(text.split())}개')
# print(f'대문자: {text.upper()}')
# words = text.split()
# print(f'단어 목록: {words}')


#정규표현식 re모듈
import re

# text = '내 번호는 010-1234-1234 입니다'
# result = re.search(r'\d{3}-\d{4}-\d{4}', text)
# print(result.group())

# text = "apple 100 banana 200"
# re.search(r"\d+", text) # 첫 매칭 (100)
# re.findall(r"\d+", text) # 모두 찾기 ['100','200']
# re.match(r"apple", text) # 맨 앞부터 매칭
# re.sub(r"\d+", "X", text) # 치환 'apple X banana X'

#메타문자
#자주 사용 \d, \w, \s 각각 숫자, 글자/숫자, 공백
#\D 숫자 아닌거, \S 공백 아닌거
#+ 1개 이상, * 0개 이상, ? 0또는 1개
#\d+ 연속적인 숫자
#{n} 개수 지정 {3} -> 3글자
#[] 문자 집합, 안의 글자 중 하나라도 매칭
#ex) [0-9], [a-z], [가-힣]
#^ 문자열 시작 $ 문자열 끝 (유효성 검사의 핵심)
#findall 모두 추출
#sub 찾아서 바꾸기

# #실전 패턴 예시
# # 전화번호: 010-1234-5678
# r"010-\d{4}-\d{4}"
# # 이메일: id@domain.com
# r"^[\w.]+@[\w]+\.[a-z]+$"
# # 우편번호(5자리)
# r"^\d{5}$"

#  re 모듈: search(첫), findall(모두), sub(치환)
# • 자주: \d(숫자) \w(글자) +(1개+) {n}(개수) [](집합) ^$(시작끝)
# • 완벽히 외우지 말 것 — 패턴은 검색/AI로, 읽는 감각이 중요
# • 강력하지만 남용 금지(간단한 건 문자열 메서드로)

#실습
email = input('이메일: ')
phone = input('전화번호(010-0000-0000): ')
if re.match(r'^[\w]+@[\w]+\.[a-z]+$',email):
    print('올바른 이메일')
else:
    print('이메일 형식 오류')
if re.match(r'^010-\d{4}-\d{4}$', phone):
    print('올바른 전화번호')
else:
    print('전화번호 형식 오류')
