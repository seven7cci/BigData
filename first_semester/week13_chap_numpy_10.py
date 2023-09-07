import numpy as np

# print(np.linspace(0, 10, 100))  # 0에서 10까지의 총 100개의 수 생성
# temp = np.logspace(0, 5, num=10)  # log 스케일 수 생성, 10의 0승부터 10의 5승 사이의 수 10(기본값 50)개
# print(temp, temp[9])

y = np.array(range(12))  # y = np.arrange(12)
print(y)
y2d = y.reshape(4, 3)
print(y2d)
y3d = y.reshape(2, 3, 2)
print(y3d)
y_auto = y.reshape(6, -1)  # 행 값을 주고 열 값은 -1로 하면 열의 개수가 자동으로 맞추어진다
print(y_auto)


# 평탄화 함수 flatten
y = np.arange(12)
y2d = y.reshape(4, 3)
flatten_y = y2d.flatten()
print(y2d, flatten_y)
