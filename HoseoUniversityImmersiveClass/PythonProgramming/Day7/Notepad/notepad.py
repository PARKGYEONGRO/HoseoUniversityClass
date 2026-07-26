""" 요구사항
• 메모를 입력받아 날짜와 함께 파일에 저장
• 저장된 메모 전체 보기
• 메뉴(쓰기/보기/종료) 반복
"""

""" 출력 예시
1.메모 쓰기 2.전체 보기 3.종료
선택: 1
오늘의 메모: 프로젝트 완성하기
저장 완료!
선택: 2
[2026-07-01] 프로젝트 완성하기
"""


from datetime import date

def write_memo():
    content = input('오늘의 메모: ')
    with open('memo.txt', 'a', encoding='utf-8') as f:
        f.write(f'[{date.today()}] {content}\n')
    print('저장 완료!')

def read_memo():
    try:
        with open('memo.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            if content:
                print(content)
            else:
                print("메모 내용이 없습니다.")

    except FileNotFoundError:
        print('아직 메모가 없습니다.')


while True:
    response = input('1.메모쓰기 2.전체보기 3.종료\n' \
        '선택: ')
    if response.isdigit():
        if response == '1':
            write_memo()
        elif response == '2':
            read_memo()
        elif response == '3':
            break
        else:
            print('1~3 중에 입력해주세요')
    else:
        print('숫자를 입력하세요')