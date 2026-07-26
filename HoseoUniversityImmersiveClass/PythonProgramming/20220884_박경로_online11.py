# 텍스트 분석기 완성하기

# 오늘 만든 텍스트 분석기에 기능을 추가해 제출하세요 :

# 가장 긴 단어 출력 (max(words, key=len))
# 평균 단어 길이 계산해 출력
# 불용어 제거(선택): "is", "a", "the" 같은 단어 빼고 빈도 집계
# 회문 단어 찾기: 문장 속 단어 중 거꾸로도 같은 단어 출력
# 출력 예:
# 단어 수: 8 / 평균 길이: 4.2
# 가장 긴 단어: programming
# 가장 많은 단어: python(3)
import re
from collections import Counter

def analyze_text(text):
    print("=== 텍스트 분석 결과 ===")
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    all_words = clean_text.split()
    
    if not all_words:
        print("분석할 단어가 없습니다.")
        return


    stopwords = {"is", "a", "the", "and", "in", "to"}
    words = [word for word in all_words if word not in stopwords]


    total_word_count = len(words)
    avg_word_len = sum(len(word) for word in words) / total_word_count
    
    print(f"단어 수: {total_word_count} / 평균 길이: {avg_word_len:.1f}")


    longest_word = max(words, key=len)
    print(f"가장 긴 단어: {longest_word} (길이: {len(longest_word)})")


    word_counts = Counter(words)
    most_common_word, highest_freq = word_counts.most_common(1)[0]
    print(f"가장 많은 단어: {most_common_word}({highest_freq})")


    palindromes = set([word for word in words if len(word) > 1 and word == word[::-1]])
    
    if palindromes:
        print(f"🔄 회문 단어: {', '.join(palindromes)}")
    else:
        print("🔄 회문 단어: 없음")


sample_text = "Python programming is a great language. Level racecar kayak python is python."

analyze_text(sample_text)