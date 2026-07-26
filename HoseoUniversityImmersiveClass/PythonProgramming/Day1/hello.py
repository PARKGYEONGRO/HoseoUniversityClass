# print('박경로')
# print('빅데이터AI')
# print('ESTJ')

# print('박경로\n빅데이터AI\nESTJ') #\n -> 줄바꿈


#변수 할당 및 재할당
# #돈 1만 원
# money = 10000
# print(money)

# #돈 3천 원 사용
# money -= 3000
# print(money)


# #변수끼리 계산하기
# korean = 90
# english = 85
# math = 95

# total = korean + english + math
# average = total / 3

# print(total)
# print(average)

#변수를 왜 쓰냐? -> 코드 재사용이 편리함

#변수 규칙(사용가능)
#• 영문자, 숫자, 밑줄(_) 사용
#• 대소문자 구분: Age 와 age 는 다른 변수
#• 길어도 됨 — 오히려 의미 있게:
#• 관례: 단어 사이를 _ 로 연결 (snake_case)

#변수 규칙(사용 불가능)
#• 숫자로 시작: 1age (X) → age1 (O)
#• 공백 포함: user name (X) → user_name (O)
#• 특수문자: price$, total! (X)
#• 예약어: if, for, print, class 등은 이미 쓰임

#변수명을 지을 때 해당 값을 명확히 나타내는 변수명을 지향하자


#Date Type 4가지 -> 정수 Int, 실수 Float, 문자열 Str, 불리언 Bool
#나눗셈(/) 결과는 항상 실수형으로 나옴

# #Date Type 확인하기
# print(type(24))
# print(type(3.14))
# print(type("안녕"))
# print(type(True))
# print(type(10/2))

# #숫자 + vs 글자 +
# print(3 + 5)
# print("3" + "5")
# print("안녕" + "하세요")
# print("하하" * 3)


# #Type Casting 자료형 변환
# print(type(int('24')))
# print(type(float('3.14')))
# print(type(str(100)))

# num = '10'
# num = int(num)
# print(num + 5)

#Type Casting 주의점
#• int() 는 소수점을 버림(내림 아님, 그냥 잘라냄)
#• 변환 불가능한 값은 에러 → 입력값 확인 필요
#int("안녕") #에러! 숫자가 아닌글자
#int(3.9) #3 (반올림 X, 소수점 버림!)
#round(3.9) #4 (반올림은round)
#int("3.5") #에러(소수글자는 int 불가)
#int(float('3.5')) #3 (float 거쳐서)

#실습
# print(3 + 5)
# print("3" + "5")
# print("안녕" + "하세요")
# print("=" * 20)
# print(int("3") + int("5"))

# name = "김파이"
# age = 20
# height = 168.5
# is_freshman = True
# print("이름:", name, "/ 타입:", type(name))
# print("나이:", age, "/ 타입:", type(age))
# print("키:", height, "/ 타입:", type(height))
# print("신입생?", is_freshman, "/ 타입:", type(is_freshman))

# print(10 + 20) # 30
# print("10" + "20") # 1020
# print(int("10") + 20) # 30
# print(str(10) + "20") # 1020
# print(int(3.9)) # 3
# print("10" * 3) # 101010


#입력과 출력
#print() 옵션 (sep, end)
#• sep = 값 사이에 넣을 구분자 (기본: 공백)
#• end = 출력 끝에 넣을 것 (기본: 줄바꿈)
# print("2025", "06", "23", sep="-") # 2025-06-23
# print("안녕", end=" ")
# print("하세요") # 안녕하세요

#input 실습
# name = input('이름을 입력하세요: ')
# print(f'안녕하세요, {name} 님!')

#input 동작 원리
#• 프로그램이 멈추고 사용자 입력을 기다림
#• 사용자가 타이핑 후 Enter
#• 입력한 값이 변수에 저장되고 다음 줄로

#Input의 결과 값은 항상 문자형임
#Input과 Type Casting
#age = int(input('나이를 입력하세요: '))
#print(type(age))

# #f-string
# age = 20
# name = '홍길동'
# print(f'{name}님은 {age}살 입니다.')
# print(f'내년에 {age + 1}살 됩니다.')
# price = 3000
# print(f'{price}원이 3개, {price * 3}원 입니다.~')

# #소수점 포맷팅
# pi = 3.141592
# print(f'{pi:.1f}') #소수점 1자리까지

# price = 1200000
# print(f"{price:,}") # 1,200,000 (천 단위콤마)
# print(f"{price:,}원") # 1,200,000원
# name = "홍길동"
# print(f"[{name:>10}]") # [ 홍길동] (오른쪽 정렬)
# print(f"[{name:<10}]") # [홍길동 ] (왼쪽정렬)
#a = 3.6일때 int(a)의 값은 3이고 print(f'{a:.0f}')의 값은 4임


#실습
#단위 변환기 모음
# # ①cm → inch
# cm = float(input("cm: "))
# print(f"{cm}cm = {cm / 2.54:.2f}inch")
# # ②섭씨→ 화씨
# c = float(input("섭씨: "))
# print(f"{c}°C = {c * 9/5 + 32:.1f}°F")
# # ③달러→ 원화(1달러=1350원)
# usd = float(input("달러: "))
# print(f"${usd} = {usd * 1350:,.0f}원")

# #BMI Caculator
# print("=== BMI 계산기 ===")
# weight = float(input("몸무게(kg): "))
# height = float(input("키(cm): "))
# height_m = height / 100
# bmi = weight / (height_m * height_m)
# print(f"당신의 BMI는 {bmi:.1f} 입니다")

# #나만의 변환기 심심풀이
# price = int(input('현재 가격: '))
# want_price_rate = float(input('원하는 수익률: '))
# print(f'수익률 {want_price_rate*100}%의 예약 판매 금액: {int(price + price * want_price_rate)}')


# age = 22
# print( age >= 20 and age < 30)
# print( age >= 20 and age < 21)

# print( age< 20 or age > 60)
# print( age < 20 or age == 22)


# is_member = True
# print(not is_member) # False (뒤집기)
# age = 25
# print(18 <= age and age <= 64) # True (성인범위)
# print(not (age < 18)) # True (미성년이아니다)

# a = int(input("첫 숫자: "))
# b = int(input("둘째숫자: "))
# print(f"{a} + {b} = {a + b}")
# print(f"{a} - {b} = {a - b}")
# print(f"{a} × {b} = {a * b}")
# print(f"{a} ÷ {b} = {a / b:.2f}")
# print(f"몫={a // b}, 나머지={a % b}")
# print(f"{a}가 {b}보다큰가? {a > b}")
# print(f"{a}와 {b}가 같은가? {a == b}")


# input_hour = int(input('시간 입력: '))
# want_mode = input('분 or 초: ')
# if want_mode == '분':
#     print(input_hour * 60)
# else:
#     print(input_hour * 3600)


# score = 81
# if score >= 80:
#     print('와 80이상')
# else:
#     print('와 80미만')
# print('프로그램 끝')


# age = int(input('나이 입력: '))

# if age >= 19:
#     print('성인')
# else:
#     print('미성년자')


# score = int(input('점수: '))
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# else:
#     print('재수강')


# age = int(input("나이: "))
# has_ticket = input("표 있나요?(y/n): ")
# if age >= 19:
#     if has_ticket == "y":
#         print("입장환영! ")
#     else:
#         print("표를먼저구매하세요")
# else:
#     print("미성년자입장불가")