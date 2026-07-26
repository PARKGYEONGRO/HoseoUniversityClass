import csv

#Save
data = [
    ['이름', '점수'],
    ['홍길동', 90],
    ['김철수', 85],
    ['이영희', 95]
]


with open('score2.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(data)

total, count = 0, 0

with open('score2.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for name, score in reader:
        total += int(score)
        count += 1

print(f'평균 점수: {total/count:.1f}')