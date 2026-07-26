total = int(input('총 주문 금액: '))
people = int(input('인원수: '))
n_bbang = int(f'{total / people:.0f}')

print(f'총 금액: {total:,}원 / 인원: {people}명')
print(f'1인당 {n_bbang}원 (총 {n_bbang*people}원 걷힘)')