#Save
memo = input('메모 내용: ')


with open('memo.txt', 'w', encoding='utf-8') as f:
    f.write(memo)
print('저장 완료')

#load
with open('memo.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print('불러오기 완료')