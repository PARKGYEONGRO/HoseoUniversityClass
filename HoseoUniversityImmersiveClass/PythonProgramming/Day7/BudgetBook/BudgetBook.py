"""요구사항
• 지출(분류 + 금액) 추가, 전체 보기
• 분류별 통계(합계 + 비율) 출력
• 금액에 글자· 0· 음수 넣으면 막기
• JSON 저장
"""

""" 출력 예시
1.지출 추가 2.전체 보기 3.통계 4.종료
선택: 1
분류(식비/교통/여가): 식비
금액: abc
금액은 0보다 큰 숫자로 입력하세요
선택: 3
총 지출: 53,000원
# ... 계속
"""

import json

def budgetbook_load():
    try:
        with open('budget.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def budgetbook_save(data):
    with open('budget.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent = 4)

def add_expense(data):
    try:
        category = input('분류(식비/교통/여가): ')
        amount = int(input('금액: '))
        if amount <= 0:
            raise ValueError #에러 발생
    except ValueError:
        print('금액은 0보다 큰 숫자로 입력하세요.')

    item = {
        'category' : category,
        'amount' : amount
    }
    data.append(item)

def show_all(data):
    for item in data:
        print(f'{item['category']}: {item['amount']:,}원')

def show_stats(data):
    if not data:
        print('기록이 없습니다.')
        return
    total = sum(item['amount'] for item in data)
    print(f'총 지출: {total:,}원')
    by_category = {}
    for item in data:
        by_category[item['category']] = by_category.get(item['category'], 0) + item['amount']
    
    for cate, amt in by_category.items():
        print(f'{cate}: {amt:,}원 ({amt / total * 100:.0f}%)')


data = budgetbook_load()

while True:
    try:
        choice = int(input('1.지출 추가 2.전체 보기 3.통계 4.종료\n' \
        '선택:'))

        if choice == 1:
            add_expense(data)
        elif choice == 2:
            show_all(data)
        elif choice == 3:
            show_stats(data)
        elif choice == 4:
            budgetbook_save(data)
            print('종료')
            break
        else:
            raise ValueError
    except ValueError:
        print('1~4까지의 숫자를 입력해주세요.')