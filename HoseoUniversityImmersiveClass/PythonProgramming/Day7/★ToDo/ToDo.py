"""요구사항
• 할 일 추가 / 완료 표시 / 삭제
• 각 항목은 완료 여부(상태) 를 가짐
• JSON 파일로 저장 (껐다 켜도 유지)
"""

"""출력 예시
=== 할 일 목록 ===
1. 파이썬 공부
2. 운동하기
1.추가 2.완료 3.삭제 4.종료
선택: 2
완료할 번호: 2 → 2. 운동하기
"""
import json

def todos_show(todos):
    if todos:
        print('=== 할 일 목록 ===')
        for i, todo in enumerate(todos, 1):
            check = 'V' if todo['done'] else ""
            print(f'{i}. {check} {todo['task']}')

    else:
        print('할 일이 없습니다.')

def todos_save(todos):
    with open('todo.json', 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii = False, indent = 4)

def todos_load():
    try:
        with open('todo.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

todos = todos_load()

while True:
    todos_show(todos)
    choice = int(input('1.추가 2.완료 3.삭제 4.종료\n' \
    '선택: '))
    try:
        if choice == 1:
            todo = {
                'task' : input('할 일: '),
                'done' : False
            }
            todos.append(todo)

        elif choice == 2:
            n = int(input('완료할 번호: ')) - 1
            todos[n]['done'] = True

        elif choice == 3:
            n = int(input('삭제할 번호: ')) - 1
            todos.pop(n)

        elif choice == 4:
            print("종료합니다.")
            break

    except (ValueError, IndexError):
        print('올바른 번호를 입력하세요.')
    
todos_save(todos)