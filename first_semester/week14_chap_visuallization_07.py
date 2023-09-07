import matplotlib.pyplot as plt
import numpy as np

years = [1965, 1975, 1985, 1995, 2005, 2015]
korea = [130, 650, 2450, 11600, 17790, 27250]
japan = [890, 5120, 11500, 42130, 40560, 38780]
china = [100, 200, 290, 540, 1760, 7940]

# x_range = range(len(years))  # numpy 미사용시 실수를 더할경우 에러 출력
x_range = np.arange(len(years))  # numpy 사용시 실수를 더할경우 실수형태로 바뀜
plt.bar(x_range - 0.3, korea, width=0.25, label='korea')
plt.bar(x_range + 0.0, japan, width=0.25, label='japan')
plt.bar(x_range + 0.3, china, width=0.25, label='china')

plt.legend()
plt.xticks(range(len(years)), years)
plt.show()
