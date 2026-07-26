# 기념일 D-Day 계산기

# 상황: 시험, 생일, 기념일까지 며칠 남았는지 한 번에 보고 싶다.

# 요구사항 — 표준 라이브러리 2개 이상 활용

# datetime 으로 오늘 날짜 가져오기
# 여러 기념일(이름 + 날짜)을 딕셔너리/리스트로 저장
# 각 기념일까지 D-Day 계산해 출력 (지났으면 D+)
# (선택) 가장 가까운 기념일을 강조 출력
# 출력 예:
# 오늘: 2026-06-25
# 🎂 내 생일(2026-08-15): D-51
# 📚 기말고사(2026-06-20): D+5 (지남)
# 🎄 크리스마스(2026-12-25): D-183
# 👉 가장 가까운: 내 생일
# 힌트: from datetime import date, (목표 - 오늘).days, 반복문으로 여러 개 처리

from datetime import date
import sys

def calculate_dday():
    today = date.today()
    print(f'오늘: {today}\n')

    anniversary = [
        {'name': '🎂 내 생일', 'date': date(2026, 8, 15)},
        {'name': '📚 기말고사', 'date': date(2026, 6, 20)},
        {'name': '🎄 크리스마스', 'date': date(2026, 12, 25)}
    ]

    closest_event = None
    min_days_left = float('inf')

    for event in anniversary:
        target_date = event['date']
        days_diff = (target_date - today).days

        if days_diff > 0:
            dday_str = f"D-{days_diff}"
        elif days_diff < 0:
            dday_str = f"D+{abs(days_diff)} (지남)"
        else:
            dday_str = "D-Day (오늘!)"

        print(f'{event['name']}({target_date}): {dday_str}')

        if days_diff >= 0 and days_diff < min_days_left:
            min_days_left = days_diff
            closest_event = event['name']

    if closest_event:
        print(f'👉 가장 가까운: {closest_event}')
    else:
        print('👉 남은 기념일이 없습니다.')

calculate_dday()