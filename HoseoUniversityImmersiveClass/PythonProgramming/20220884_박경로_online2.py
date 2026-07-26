#구분, 나이, 요금
# 어린이, 7세 이하, 5000
# 청소년, 8~18세, 9000
# 성인, 19~64세, 13000
# 경로, 65세이상 7000
# 출력 예: 26세 → 성인 / 요금 13,000원
# 도전: 화요일이면 2,000원 할인 (요일도 입력받아 조건 추가)


from datetime import datetime #도전과제
now = datetime.now()
day_number = now.weekday()  #0: 월, 1: 화, 2: 수, 3: 목, 4: 금, 5: 토, 6: 일
# print(day_number) #요일 확인
# day_number =1 #화요일 일 때 테스트 변수


price =  0
age_mod = ''

age = int(input('나이 입력: '))


if age <= 7:
    price = 5,000
    age_mod = '어린이'
elif age <= 18:
    price = 9000
    age_mod = '청소년'
elif age <= 64:
    price = 13000
    age_mod = '성인'
else:
    price = 7000
    age_mod = '경로'


if day_number == 1: #0: 월, 1: 화, 2: 수, 3: 목, 4: 금, 5: 토, 6: 일
    print(f'{age_mod} / 요금 {price-2000:,}')
else:
    print(f'{age_mod} / 요금 {price:,}')
    