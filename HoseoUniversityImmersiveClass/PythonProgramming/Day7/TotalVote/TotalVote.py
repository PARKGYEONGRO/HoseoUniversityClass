"""요구사항
• 항목을 반복 입력받아 집계 (q로 종료)
• 항목별 득표수 + 비율 출력
• 1위 항목 표시
"""

"""출력 예시
무엇을 먹을까요? (그만하려면 q)
투표: 피자
투표: 치킨
투표: 피자
투표: q
=== 결과 ===
피자: 2표 (67%)
# ... 계속
"""

votes = {}

while True:
    item = input('무엇을 먹을까요?\n' \
    '투표(q: 종료): ')
    
    if item == 'q':
        print('투표를 종료합니다.')
        break
    
    votes[item] = votes.get(item, 0) + 1

if not votes:
    print("투표가 없습니다.")

else:
    total = sum(votes.values())
    print('=== 결과 ===')
    for item, count in votes.items():
        print(f'{item}: {count}표 ({count/total * 100:.0f}%)')
    print(f'1위: {max(votes, key=votes.get)}')