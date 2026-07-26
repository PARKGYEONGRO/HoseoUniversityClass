# 날짜별 일기장

# 상황: 매일 일기를 쓰고, 언제든 다시 읽고 싶다.

# 요구사항 — 메뉴를 반복하며 다음 기능 제공

# 1. 일기 쓰기: 오늘 날짜(datetime)와 내용을 파일에 저장(추가 모드)
# 2. 일기 보기: 저장된 모든 일기 불러와 출력
# 3. 종료
# 저장 형식 예: [2026-06-29] 오늘은 파이썬을 배웠다

# 14과제를 위해서 예외처리 X, 및 프로그램 죽게끔 코딩

from datetime import date

today = date.today()

def writing_diary():
    with open('diary.txt', 'a', encoding='utf-8') as f:
        f.write(f'[{today}] {input(': ')}\n')

def loading_diary():
    with open('diary.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


choice = input('1.일기 쓰기 2.일기 보기 3.종료\n입력: ')
if choice == '1':
    writing_diary()
elif choice == '2':
    loading_diary()
elif choice == '3':
    print('종료합니다.')
