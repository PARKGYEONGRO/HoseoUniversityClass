"""요구사항
• (준비) 샘플 CSV 파일 생성 또는 실제 CSV 사용
• pandas로 읽기 + 기본 통계(describe)
• 특징점 추출: 최고/최저 항목, 평균 이상 개수
• 막대그래프 생성 + 이미지 저장
"""

""" 출력 예시
매출 분석 리포트
- 총 매출: 1,250만원 / 평균: 250만원
- 최고: 강남점(420) / 최저: 분당점(90)
- 평균 이상 지점: 2개 [강남점, 잠실점]
→ report.png(그래프) + report.txt(리포트) 자동 생성!
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv',encoding='utf-8')
# print(df.head())
# print(df.describe())
# print(f'거래건수: {len(df)}건')

by_branch = df.groupby('지점')['매출'].sum().sort_values(ascending = False)

total = df['매출'].sum()

branch_avg = by_branch.mean()

top = by_branch.idxmax()
low = by_branch.idxmin()


above = [b for b in by_branch.index if by_branch[b] >= branch_avg]
print(f'\n총 매출: {total:,}원 / 건당 평균: {df['매출'].mean():,.0f}원')
print(f'\n최고 지점: {top} ({by_branch[top]:,})\n최저 지점: {low} ({by_branch[low]:,})\n지점 평균 이상: {len(above)} {above}')

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
by_branch.plot(kind='bar', color='skyblue')
plt.title('지점별 총매출')

plt.ylabel('매출(원)')
plt.savefig('report.png')
# plt.show()

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write('=== 매출 분석 리포트 ===\n')
    f.write(f'거래 건수: {len(df)}건\n')
    f.write(f'총 매출: {total:,}원\n')
    f.write(f'건당 평균: {df['매출'].mean():,.0f}원\n')
    f.write(f'최고 지점: {top} ({by_branch[top]:,}원)\n')
    f.write(f'최저 지점: {low} ({by_branch[low]:,}원)\n')
    f.write(f'지점 평균 이상: {len(above)} ({above})\n')
print('\nreport.png + report.txt 자동 생성 완료!')