"""
과제 ③ 제출: 택시 요금 계산기

상황: 택시는 기본요금 + 거리요금 + (심야 할증)으로 계산된다.
요구사항 — 이동 거리(km)와 심야 여부를 입력받아 요금 출력

기본요금 4,800원 (기본 2km 포함)
2km 초과분은 1km당 1,000원 추가
심야(y) 면 전체 요금에 20% 할증
출력 예:
거리: 5km / 심야: y
기본 4,800 + 추가 3,000 = 7,800원
심야 할증 20% → 9,360원
힌트: 추가거리 = 거리 - 2 (음수면 0), 할증 = 요금 * 1.2
"""

while True:
    # try:
        total_price = 4800 #기본요금 4,800원
        add_price = 0

        move_distance = float(input('이동거리(km): '))

        while True: #심야 운행 응답 부분 예외처리
            night_driving = input('심야 운행(y / n): ')
            

            #자주 하는 실수
            #if night_driving == 'y' or 'n'
            # 컴퓨터는 먼저 앞부분 night_driving == 'y'를 검사 (사용자가 n을 입력했다면 이 부분은 False가 됩니다.)
            # 그 다음 or 연산자를 넘어 뒷부분인 'n'을 봅니다.
            # 컴퓨터: "어? 뒤에 그냥 문자열 'n'이 덩그러니 있네? 파이썬 규칙에 따르면 글자가 들어있는 문자열은 True"
            # 결국 이 식은 if False or True:가 되어서 최종 결과가 무조건 True
            # 사용자가 'n'을 입력했든, 'abc'를 입력했든, 심지어 오타를 냈든 상관없이 언제나 True가 되어서 통과해 버리는 이유가 바로 이것 때문
            if night_driving in ['y', 'n']:
                break


            print('다시 입력해주세요. (y 또는 n만 입력 가능합니다.)')


        if move_distance > 2:
            add_price = (move_distance-2) // 1 * 1000 #초과 요금

            
        total_price += add_price


        if night_driving == 'y':
            total_price *= 1.2
            print(f'거리: {move_distance}km / 심야: {night_driving}')
            print(f'기본 4,800 + 추가 {add_price:,.0f} = {total_price:,.0f}')
            print(f'심야 할증 20% -> {total_price:,.0f}')
            break


        print(f'거리: {move_distance}km / 심야: {night_driving}')
        print(f'기본 4,800 + 추가 {add_price:,.0f} = {total_price:,.0f}')
        break

    # except:
    #     print('입력값이 잘못 되었습니다.\n다시 입력해주세요.')