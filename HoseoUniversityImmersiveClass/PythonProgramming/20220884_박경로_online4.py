# 용돈 가계부 통계 프로그램

# 상황: 일주일 동안 쓴 돈을 입력해 통계를 내고 싶다.

# 요구사항

# 지출 금액을 여러 개 입력받아 리스트에 저장(0 입력 시 종료)
# 다음을 출력:
# 총 지출, 지출 횟수, 평균 지출
# 가장 많이 쓴 금액(max), 가장 적게 쓴 금액(min)
# 출력 예:
# 총 지출: 85,000원 / 7회
# 평균: 12,142원 / 최대: 30,000원 / 최소: 3,000원


expenses = input('지출 금액 입력(여러개 입력시 띄어쓰기로 구분): ').split()

if expenses[0] != '0':
    total = 0
    value_typecasting = []

    for i in expenses:
        value_typecasting.append(int(i))
        total += int(i)

    average_expenses = total/len(expenses)
    print(f'총 지출: {total:,}원 / {len(expenses)}회\n평균: {average_expenses:,.0f}원 / 최대: {max(value_typecasting):,}원 / 최소: {min(value_typecasting):,}원')