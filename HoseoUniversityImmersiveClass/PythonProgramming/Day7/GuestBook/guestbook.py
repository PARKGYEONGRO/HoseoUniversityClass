"""요구사항
• 이름과 한마디를 입력받아 파일에 저장
• 방명록 전체 목록 보기
• 지금까지 남긴 글 개수 표시
"""

"""출력 예시
방명록에 글 남기기
이름: 홍길동
한마디: 수업 재밌어요!
등록 완료!
=== 방명록 ===
홍길동 님: 수업 재밌어요!
김철수 님: 화이팅!
"""

def write_guestbook():
    name = input('이름: ')
    content = input('한마디: ')
    with open('guestbook.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{name} 님: {content}')
        print('등록 완료!')

def load_guestbook():
    try:
        with open('guestbook.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        if content:
            print(content)
        else:
            print('방명록이 없습니다.')
    except FileNotFoundError:
        print('방명록이 없습니다.')

while True:
    response = input('방명록\n' \
    '1. 방명록에 글 남기기\n' \
    '2. 전체 방명록 확인하기\n' \
    '3. 종료\n' \
    '선택: ')

    if response.isdigit():
        if response == '1':
            write_guestbook()
        elif response == '2':
            load_guestbook()
        elif response == '3':
            print('종료합니다.')
            break
        else:
            print("1~3번중에 입력해주세요.")
    
    else:
        print("숫자를 입력해주세요.")