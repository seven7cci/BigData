import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505.0, 11865.3, 22105.3]

plt.bar(range(len(years)), gdp)  # 막대 그래프, x틱 범위 0~6
plt.title('GDP per Capita')  # 1인당 국민소득

# x, y축 레이블
plt.xlabel('year')
plt.ylabel('dollars')

plt.xticks(range(len(years)), years)  # x틱 값을 년도로
plt.show()
