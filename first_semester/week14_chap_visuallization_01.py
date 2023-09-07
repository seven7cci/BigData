import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505.0, 11865.3, 22105.3]

# plt.plot(years, gdp)  # 선 그래프
# x축 : years, y축 : gdp, 선 색상 빨강, 지점은 o로 표시, 선 스타일은 -----
plt.plot(years, gdp, color='red', marker='o', linestyle='dashed')
plt.title('GDP per Capita')  # 1인당 국민소득

# x, y축 레이블
plt.xlabel('year')
plt.ylabel('dollars')

# 저장
plt.savefig('GDP per Capita.png', dpi=1000)
plt.show()
