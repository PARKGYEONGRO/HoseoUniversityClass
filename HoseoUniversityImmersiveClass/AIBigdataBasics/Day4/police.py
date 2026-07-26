# 앞선 데이터를 바탕으로 강력범죄와 지능범죄를 한눈에 비교할 수 있는 통합 차트 생성
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드 및 처리
df = pd.read_csv('C:\WorkSpace\AIBigdataBasics\경찰청_범죄 발생 시간대 및 요일_20191231.csv', encoding='cp949')
days = ['월', '화', '수', '목', '금', '토', '일']
days_eng = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 각 범죄 대분류별 요일 합계 추출
violent_sum = df[df['범죄대분류'] == '강력범죄'][days].sum().reindex(days)
intel_sum = df[df['범죄대분류'] == '지능범죄'][days].sum().reindex(days)

# 데이터프레임 형태로 변환
plot_df = pd.DataFrame({
    'Day': days_eng,
    'Violent': violent_sum.values,
    'Intellectual': intel_sum.values
})

# 두 범죄의 스케일 차이가 크므로 조형적으로 보기 쉽게 두 개의 서브플롯(Subplot)으로 구성
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 1. 강력범죄 차트 (좌)
sns.barplot(x='Day', y='Violent', data=plot_df, ax=axes[0], palette='Reds_r')
axes[0].set_title('Violent Crimes by Day (2019)', fontsize=14, fontweight='bold', pad=10)
axes[0].set_xlabel('Day of the Week', fontsize=11)
axes[0].set_ylabel('Number of Cases', fontsize=11)
axes[0].grid(axis='y', linestyle='--', alpha=0.5)
for i, v in enumerate(plot_df['Violent']):
    axes[0].text(i, v + 40, f"{int(v):,}", ha='center', fontweight='bold', fontsize=9)

# 2. 지능범죄 차트 (우)
sns.barplot(x='Day', y='Intellectual', data=plot_df, ax=axes[1], palette='Purples_r')
axes[1].set_title('Intellectual Crimes by Day (2019)', fontsize=14, fontweight='bold', pad=10)
axes[1].set_xlabel('Day of the Week', fontsize=11)
axes[1].set_ylabel('Number of Cases', fontsize=11)
axes[1].grid(axis='y', linestyle='--', alpha=0.5)
for i, v in enumerate(plot_df['Intellectual']):
    axes[1].text(i, v + 1000, f"{int(v):,}", ha='center', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig('combined_crimes_by_day.png', dpi=300)
plt.close()