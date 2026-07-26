# f = open('memo.txt','w') #File 이름, 모드
# f.write('안녕하세요')
# f.close()


# #File mode - r, w, a
# #r - 읽기, w - 쓰기, a - 추가


# f = open('diary.txt','w', encoding='utf-8') #utf-8 -> 한글 깨짐 방지
# f.write('오늘은 파이썬을 배웠다.\n')
# f.write('파일 저장도 배웠다.\n')
# f.close()


# #close()를 하지 않으면 확정 저장이 안 됨, with문을 사용하면 close() 문제 해결
# with open('memo.txt', 'w', encoding='utf-8') as f:
#     f.write('안녕하세요')
# #블록을 벗어나면 자동으로 close()

# with open('data.txt', 'w', encoding='utf-8') as f:
#     f.write('첫 줄\n')
#     f.write('둘째 줄\n')
#     #블럭 안에서만 f 사용 가능
# print('저장완료!') #with 밖 => 이미 닫힘

#읽기 모드 r, read() *반드시 존재하는 파일을 열어야함
# with open('diary.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
# # print(content)


# #추가 모드 a (append)
# with open('log.txt', 'a', encoding='utf-8') as f:
#     f.write('새 기록 추가\n')


#CSV 모듈
import csv

# with open('score.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['이름', '점수']) #한 행 쓰기
#     writer.writerow(['홍길동', 90])
#     writer.writerow(['김철수', 85])

# with open('score.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


#CSV 활용 - 성적 처리 흐름
# total = 0
# count = 0
# with open('score.csv', 'r', encoding='utf=8') as f:
#     reader = csv.reader(f)
#     next(reader) #Data header 건너뜀
#     for name, score in reader:
#         total += int(score)
#         count += 1
# print(f'평균 : {total/count:.1f}')


#JSON = 구조화된 데이터 형식 (키 - 값 구조)
#JSON과 딕셔너리 모양이 거의 같음
#JSON 모듈 - 저장(dump)
import json
# data = {'name':'홍길동', 'age':'24', 'scores':[90, 85]}

# with open('profile.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False,
#               indent=2)
    
# #JSON 모듈 - 불러오기(load)
# with open('profile.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# print(data['name'])
# print(data['scores']) #리스트 그대로 출력


#dumps / loads (문자열 버전) -> 뭔 소린지 왜 쓰는지 이해가 안 됨 (개인공부 필요)
# data = {"name": "홍길동"}
# text = json.dumps(data, ensure_ascii=False) # 딕셔너리 → 문자열
# print(text)# {"name": "홍길동"}
# back = json.loads(text)# 문자열 → 딕셔너리
# print(back["name"])# 홍길동

"""      CSV                    JSON
모양     표(행/열)              키-값(중첩 가능)
적합     성적표·엑셀 데이터     설정·프로필·복잡한 구조
형변환   필요(전부 str)         불필요(타입 유지)
친구     엑셀, pandas           웹 API, 앱
"""


#예외 처리 try - except
# while True:
#     try:
#         age = int(input('나이: '))
#         print(f'내년엔 {age + 1}살')
#         break

#     except:
#         print('올바른 숫자를 입력하세요')

#지정 예외 처리
# while True:
#     try:
#         x = int(input('숫자: '))
#         print(10 / x)
#         break
#     except  ValueError:
#         print('숫자가 아닙니다.')
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')

#에러 메세지 활용 (as e)
# try:
#     x = int('안녕')
# except ValueError as e:
#     print(f'오류 발생: {e}') #오류 발생: invaild literal for int()...

#다중 예외 한 번에
# try:
#     x = int('안녕')
#     #print(10/0)
# except(ValueError, ZeroDivisionError) as e:
#     print(f'오류 발생: {e}')


#else = 오류가 안 났을 때 실행
# try:
#     x = int(input("숫자: "))
# except ValueError:
#     print("숫자 아님")
# else:
#     print(f"입력 성공: {x}") # 오류 없을 때만!

#finally = 무조건 실행 (성공·실패 상관없이)
# try:
#     f = open("data.txt")
#     ...
# except FileNotFoundError:
#     print("파일 없음")
# finally:
#     print("작업 종료") # 오류든 아니든 항상 실행!

#raise 로 내가 직접 예외를 일으킴
# def set_age(age):
#     if age < 0:
#         raise ValueError("나이는 0 이상이어야 합니다")
#     return age
# set_age(-5) # ValueError 발생


#디버깅 - 에러 메세지 읽기
#오류 종류와 원인
#가장 쉽고 강력한 디버깅 1단계 Print
# def calc(a, b):
#     print(f"디버그: a={a}, b={b}") # 값 확인
#     return a / b


#클래스 기초1
"""절차지향 vs 객체지향
            절차지향                객체지향
방식        순서대로 함수 실행      객체들이 협력
데이터      변수로 흩어짐           객체 안에 묶임
비유        요리 레시피 순서        요리사·재료·도구
적합        간단한 작업             크고 복잡한 프로그램
"""

# • 클래스 = 붕어빵 틀 (설계도)
# • 인스턴스 = 붕어빵 (틀로 찍어낸 실제물건)
# • 틀(클래스) 하나로 붕어빵(인스턴스) 여러 개!

#클래스 정의 class / 첫 글자 대문자 관례
# class Dog:
#     def bark(self):
#         print('멍')

# #인스턴스
# my_dog = Dog()
# my_dog.bark()

#속성(Attribute)
# class Dog:
#     pass

# my_dog = Dog()
# my_dog.name ='바둑이'
# my_dog.age = 3
# print(my_dog.name)

# __init__ 생성자
#인스턴스 생성 시 자동 실행되는 메서드
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog('바둑이',3)
# print(my_dog.name)

""" self의 의미
self = 그 인스턴스 자기 자신
메서드 호출 시 인스턴스가 self를 자동 전달
class 안 메서드 첫 매개변수는 항상 self
"""
# your_dog = Dog('뽀삐',3)
# print(your_dog.name)
# print(your_dog.age)

#속성 수정
# print(my_dog.age)
# my_dog.age = 4
# print(my_dog.age)

#메서드 = 클래스 안의 함수
class Dogg:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name}: 멍멍')

# d = Dogg('바둑이',3)
# d.bark()


#메서드가 속성을 활용
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def is_pass(self):
        return self.score >= 60

s = Student('홍길동',60)
# print(s.is_pass())

# #여러 인스턴스
# s1 = Student('홍길동', 90)
# s2 = Student('김철수', 50)
# print(s1.is_pass())
# print(s2.is_pass())


#클래스 기초2
#메서드로 상태 바꾸기 - 메서드가 속성을 변경
#객체가 자신의 상태를 기억하고 관리
class Counter:
    def __init__(self):
        self.count = 0
    def increase(self):
        self.count += 1
    def reset(self):
        self.count = 0
c = Counter()
c.increase(); c.increase()
# print(c.count) # 2

#기본값 속성
#__init__에도 기본값 매개변수 사용 가능, 안 넘기면 기본값 적용
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance #기본 잔액 0
a = BankAccount('홍길동')
b = BankAccount('김철수', 10000)
# print(a.balance)
# print(b.balance)

#메서드가 다른 메서드 호출
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def grade(self):
        return '합격' if self.score >= 60 else '불합격'
    
    def report(self):
        print(f'{self.name}: {self.score}점 ({self.grade()})')

c = Student('홍길동',60)
# c.report()

#메서드 vs 일반 함수
#함수는 값을 받아 처리, 메서드는 자기 속성(self)으로 처리
#메서드는 객체에 소속된 함수


#__str__ 객체를 예쁘게 출력 -> 왜 써야하나 생각한 결과 기본 출력 결과를 보기 좋게 출력하려고?
#print(객체)를 보기 좋게 출력
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}({self.score}점)"
s = Student("홍길동", 90)
# print(s) # 홍길동(90점) ← __str__ 덕분!

#객체 리스트
students = [
Student("홍길동", 90),
Student("김철수", 85),
Student("이영희", 95),
]

# for s in students:
#     print(s) # __str__로 예쁘게

#객체를 함수에 넘기기
def print_report(self): # 객체를 매개변수로
    print(f"{self.name}: {self.score}점")

def is_top(self):
    return self.score >= 90

s = Student("홍길동", 95)
# print_report(s)
# print(is_top(s)) # True

#리스트 컴프리헨션
total = sum(s.score for s in students)
# print(f'평균: {total/len(students):.1f}')


#인스턴스 변수 vs 클래스 변수
"""
• 인스턴스 변수(self.) = 객체마다 다름
• 클래스 변수 = 모든 객체가 공유
"""
class Dog:
    species = "개" # 클래스 변수 (모두 공유)
    def __init__(self, name):
        self.name = name # 인스턴스 변수 (각자)
a = Dog("바둑이")
print(a.name, a.species) # 바둑이 개


#클래스 + 예외 처리 결합
#• 메서드 안에서 검증 + raise (3교시 결합)
#• 잘못된 동작을 객체 스스로 막음

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액 부족!")
        self.balance -= amount

#클래스 설계 팁
#• 하나의 클래스 = 하나의 사물/개념 (Student, Car, Account)
#• 속성: 그 사물이 가진 데이터

#클래스 흔한 실수
#핵심 개념
#• self 빼먹기: def bark(): → def bark(self):
#• 속성 앞에 self 안 붙임: name = name → self.name =na…

#오늘 총정리
#• 파일 입출력: 데이터를 영구 저장 (꺼도 안 사라짐)
#• 예외 처리: 오류에도 안 죽는 튼튼함
#• 클래스: 데이터+기능을 사물 단위로 묶기
#• 이 셋을 합치면 → 진짜 프로그램! (미니 프로젝트로!)