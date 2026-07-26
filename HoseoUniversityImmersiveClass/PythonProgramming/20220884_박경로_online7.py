# 쇼핑 할인 계산기 함수 라이브러리

# 상황: 온라인 쇼핑에서 할인·배송비를 자동 계산하고 싶다.

# 요구사항 — 아래 함수 3~5개를 만들어 활용

# discount_price(price, rate): 정가·할인율(%) → 할인가 반환
# shipping_fee(total): 총액이 30,000원 이상이면 0원, 아니면 3,000원 반환


# final_price(price, rate): 할인가 + 배송비 → 최종 결제액 반환
# (선택) point(price): 결제액의 5% 적립 포인트 반환


# 출력 예:
# 정가 50,000원 / 20% 할인
# 할인가: 40,000원 / 배송비: 0원
# 최종 결제: 40,000원 / 적립: 2,000P
# 힌트: 함수가 다른 함수를 호출해도 됨 (final_price 안에서 discount_price 호출)

def discount_price(price, rate):
    print(f'정가 {price:,}원 / {rate * 100:.0f}% 할인')
    discounted = price * (1 - rate)
    return int(discounted)

def shipping_fee(total):
    shipping = 3000
    if total >= 30000:
        shipping = 0
    return shipping

def point(price):
    return int(price * 0.05)

def final_price(price, rate):
    discounted = discount_price(price,rate)

    shipping = shipping_fee(discounted)
    print(f'할인가: {discounted:,}원 / 배송비: {shipping:,}원')

    final = discounted + shipping
    _point = point(final)

    print(f'최종 결제: {final:,}원 / 적립: {_point}P')
    return final


final_price(50000, 0.2)