"""요구사항
• 명언을 입력받아 파일에 추가
• 저장된 명언 중 랜덤으로 하나 출력
• 파일이 비어있으면 안내
"""

""" 출력결과
1.명언 추가 2.랜덤 명언 3.종료
선택: 2
"오늘 할 일을 내일로 미루지 말자"
"""
import random as rd

wisesaying = []

def add_wisesaying():
    content = input('추가할 명언(아무것도 입력 안 할시 추가 취소): ')
    if content:
        wisesaying.append(content)
        print(f'추가 완료\n{content}')
    else:
        print("추가 취소")

def random_wisesaying():
    rd_number = rd.randint(0,len(wisesaying)-1)
    print(f'"{wisesaying[rd_number]}"')


while True:
    response = input('1.명언 추가 2.랜덤 명언 3.종료\n' \
    '선택: ')
    if response.isdigit():
        if response == '1':
            add_wisesaying()
        
        elif response == '2':
            if wisesaying:
                random_wisesaying()
            else:
                print('명언 목록이 비어있어 명언 추가로 이동합니다...')
                add_wisesaying()
        
        elif response == '3':
            break
        
        else:
            print("1~3번중에 입력해주세요.")
    
    elif response == 'list_open':
        print(wisesaying)

    else:
        print("숫자를 입력해주세요.")