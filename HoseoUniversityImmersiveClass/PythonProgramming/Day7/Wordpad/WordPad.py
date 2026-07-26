"""요구사항
• 단어(영어 + 뜻)를 추가하고 JSON 저장
• 퀴즈 모드: 단어를 랜덤 순서로 출제
• 입력한 답과 비교해 정답/오답 판정
• 마지막에 정답률(%) 출력
"""

"""출력 예시
1.단어 추가 2.퀴즈 시작 3.종료
선택: 2
'apple'의 뜻은? 사과 → 정답!
'book'의 뜻은? 채 → 오답. 정답: 책
정답률: 67% (2/3)
"""
import json
import random as rd


class Word:
    def __init__(self, eng, kor):
        self.eng = eng
        self.kor = kor

    def to_dict(self):
        return {
            'eng' : self.eng,
            'kor' : self.kor
        }
    
    def ask(self):
        answer = input(f'{self.eng}의 뜻은?: ')
        return answer.replace(' ', '') == self.kor.replace(' ', '')

def save(words):
    with open('words.json', 'w', encoding='utf-8') as f:
        json.dump([w.to_dict() for w in words], f, ensure_ascii=False, indent=2)

def load():
    try:
        with open('words.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            _words = [] #변수 앞에 _는 같은 변수명일 때 헷갈릴 수 있으니 로컬 변수는 앞에 _를 붙임
            for word in data:
                _words.append(Word(word['eng'], word['kor'] ))
            return _words
    except FileNotFoundError:
        return []

def add_word(words):
    eng = input('영어 단어: ')
    kor = input('뜻: ')
    words.append(Word(eng, kor))

def quiz(words):
    if not words:
        print('추가된 단어가 없습니다.')
        return
    copy_words = words[:]
    rd.shuffle(copy_words)
    score = 0
    for w in copy_words:
        if w.ask():
            print('정답!')
            score += 1
        else:
            print(f'오답. 정답: {w.kor}')
    print(f'\n정답률: {score/len(copy_words)*100}% ({score}/{len(copy_words)})')
words = load()

while True:
    try:
        choice = int(input('1.단어 추가 2.퀴즈 시작 3.종료\n' \
        '선택: '))
        if choice == 1:
            add_word(words)
            save(words)
        elif choice == 2:
            quiz(words)
        elif choice == 3:
            print('종료')
            save(words)
            break
        else:
            raise ValueError
    except ValueError:
        print('1~3까지 숫자를 입력해주세요.')