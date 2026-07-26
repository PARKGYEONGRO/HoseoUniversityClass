# 온라인 13 과제 일기장이 잘못된 입력·없는 파일에 죽지 않게 만들자.

# 요구사항 — 온라인 13 과제 일기장에 예외 처리 추가

# 메뉴 선택에서 숫자 아닌 입력 시 안내 후 재입력 (try/except)
# 일기 파일이 없을 때 "아직 일기가 없습니다" 안내 (FileNotFoundError)
# 잘못된 메뉴 번호(1~3 외) 입력 시 안내
# (선택) 빈 일기 입력 막기

# 14과제를 위해서 예외처리 X, 및 프로그램 죽게끔 코딩

from datetime import date

today = date.today()

def writing_diary():
    print('=== 일기 작성중 ===')
    while True:
        try:
            with open('diary.txt', 'a', encoding='utf-8') as f:
                content = input(': ')
                if not content:
                    raise TypeError
                elif content == '종료':
                    break
                else:
                    f.write(f'[{today}] {content}\n')
        except TypeError:
            print('입력된 내용이 없습니다 다시 입력해주세요.\n작성 종료를 원하시면 "종료"를 입력해주세요.')

def loading_diary():
    try:
        with open('diary.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print('아직 일기가 없습니다.')


while True:
    try:
        choice = input('1.일기 쓰기 2.일기 보기 3.종료\n입력: ')
        if choice == '1':
            writing_diary()
        elif choice == '2':
            loading_diary()
        elif choice == '3':
            print('종료합니다.')
            break
        else:
            raise TypeError
    except TypeError:
        print('1~3의 숫자를 입력하세요.')