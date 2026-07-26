while True:
    line = input('일기(끝:q): ')
    
    
    with open('diary.txt', 'a', encoding = 'utf-8') as f:
        f.write(line + '\n')
    
    
    if line == 'q':
        with open('diary.txt', 'r', encoding='utf-8') as f:
            diary_data = f.read()
            print(diary_data)
        break
