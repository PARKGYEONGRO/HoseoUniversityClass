while True:
    try:
        a = int(input('첫 숫자: '))
        b = int(input('두 번째 숫자: '))
        print(f'결과: {a/b}')
        break
    
    except ValueError:
        print('숫자 입력하세요')