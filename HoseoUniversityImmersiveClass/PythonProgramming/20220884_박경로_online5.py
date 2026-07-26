# 영화 평점 관리 프로그램

# 상황: 내가 본 영화들의 평점을 기록·관리하고 싶다.

# 요구사항
# 영화 제목과 평점(0~10)을 여러 개 입력받아 저장
# (제목 리스트 + 평점 리스트, 또는 딕셔너리 {제목: 평점})
# 다음을 출력:
# 전체 영화 목록과 평점
# 평균 평점
# 가장 높은 평점의 영화 제목
# 출력 예:
# [기록한 영화]
# 인터스텔라: 9.5 / 어벤져스: 8.0 / 라라랜드: 9.0
# 평균 평점: 8.8 / 최고: 인터스텔라(9.5)

class Movie:

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __str__(self):
        return f'{self.title}: {self.rating}'
    
movie_list = []

while True:
    title = input('영화 제목과 평점을 입력하세요. (입력을 멈추려면 종료 입력)\n' \
    '영화 제목: ').strip()
    if title == '종료':
        break

    try:
        rating = float(input(f'{title}의 평점 (0~10): '))
        if 0 <= rating <= 10:
            movie = Movie(title, rating)
            movie_list.append(movie)
        else:
            print('평점은 0~10 사이로 입력해주세요.')
    except ValueError:
        print('숫자 입력 해주세요.')

if movie_list:
    # 1. 전체 영화 목록 출력 (각 객체의 __str__ 메서드가 자동 호출됨)
    movie_list_str = " / ".join([str(movie) for movie in movie_list])

    # 2. 평균 평점 계산 (각 movie 객체의 rating 속성에 접근)
    total_rating = sum([movie.rating for movie in movie_list])
    avg_rating = total_rating / len(movie_list)

    # 3. 최고 평점 영화 찾기 (기준은 movie.rating)
    best_movie = max(movie_list, key=lambda movie: movie.rating)

    # 결과 출력
    print("[기록한 영화]")
    print(movie_list_str)
    print(
        f"평균 평점: {avg_rating:.1f} / 최고: {best_movie.title}({best_movie.rating})"
    )
else:
    print("입력된 영화 정보가 없습니다.")