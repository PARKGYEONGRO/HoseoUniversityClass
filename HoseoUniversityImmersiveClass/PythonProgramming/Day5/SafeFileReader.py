filename = input('파일 이름: ')
try:
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print(f'{filename} 파일이 없습니다.')