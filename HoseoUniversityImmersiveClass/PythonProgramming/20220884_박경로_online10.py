# 성적 관리 프로그램 확장

# 오늘 만든 성적 관리 프로그램에 기능을 추가해 제출하세요 :

# 검색: 이름으로 점수 찾기 (get 으로 없으면 안내)
# 삭제: 이름으로 학생 삭제 (del 또는 pop)
# 1등 찾기: 가장 높은 점수의 학생 이름 출력
# 힌트: max(students, key=students.get)
# 등급 분포: A/B/C/F 가 각각 몇 명인지
import csv

#1. CSV 파일 생성 (기존 코드 유지)
data = [
    ['이름', '점수'],
    ['홍길동', 90],
    ['김철수', 85],
    ['이영희', 95]
]

with open('score2.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(data)

#2. CSV 파일 읽기 및 딕셔너리로 변환
students = {}
total, count = 0, 0

with open('score2.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # 헤더 스킵
    for name, score in reader:
        score_int = int(score)
        students[name] = score_int
        total += score_int
        count += 1

print(f'평균 점수: {total/count:.1f}')
print("-" * 40)

# ==================== [추가 기능 구현] ====================

#1. 검색: 이름으로 점수 찾기
def search_student(name):
    score = students.get(name)
    if score is not None:
        print(f"검색 결과 -> {name} 학생의 점수는 {score}점입니다.")
    else:
        print(f"검색 결과 -> {name} 학생을 찾을 수 없습니다.")

#2. 1등 찾기 (최고 점수 학생)
def find_top_student():
    if not students:
        print("1등 찾기 -> 등록된 학생이 없습니다.")
        return
    top_student = max(students, key=students.get)
    print(f"1등 학생 -> {top_student} ({students[top_student]}점)")

#3. 등급 분포 계산 (A/B/C/F)
def show_grade_distribution():
    distribution = {'A': 0, 'B': 0, 'C': 0, 'F': 0}
    
    for score in students.values():
        if score >= 90:
            distribution['A'] += 1
        elif score >= 80:
            distribution['B'] += 1
        elif score >= 70:
            distribution['C'] += 1
        else:
            distribution['F'] += 1
            
    print("등급 분포 -> ", end="")
    print(", ".join([f"{grade}: {cnt}명" for grade, cnt in distribution.items()]))

#4. 삭제: 이름으로 학생 삭제
def delete_student(name):
    # pop(key, default)을 쓰면 데이터가 없을 때 에러 대신 default를 반환합니다.
    removed_score = students.pop(name, None)
    if removed_score is not None:
        print(f"삭제 완료 -> {name} 학생(점수: {removed_score}점)이 삭제되었습니다.")
    else:
        print(f"삭제 실패 -> 삭제할 {name} 학생이 존재하지 않습니다.")

# ==================== [기능 실행 및 테스트] ====================

#[테스트 1] 검색 기능
search_student('홍길동')
search_student('이영희')
search_student('전우치')  # 없는 학생 안내

#[테스트 2] 1등 찾기
find_top_student()

#[테스트 3] 등급 분포
show_grade_distribution()

print("-" * 40)
#[테스트 4] 삭제 기능 및 반영 확인
delete_student('김철수')
delete_student('전우치')  # 없는 학생 삭제 시도
print(f"현재 남은 학생 현황: {students}")