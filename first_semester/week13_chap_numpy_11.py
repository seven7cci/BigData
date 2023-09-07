import numpy as np

# rand 함수 : uniform distribution 0 <= n < 1

# np.random.seed(7)
# print(np.random.rand(3))
# print(np.random.rand(5, 4))  # 5행 4열 랜덤 매트릭스 생성 (각 원소는 0 <= n < 1)
#
# a = 10
# b = 20
# print((b - a) * np.random.rand(5) + a)

# randn 함수 : normal distribution (산술평균, 표준편차)
# print(np.random.randn(10))
print(np.random.randn(5, 5))  # 25개의 원소가 랜덤하게 생성 (평균 0이고 표쥰편차는 1.0)

# 25개의 원소가 랜덤하게 생성 (평균 10이고 표쥰편차는 2.0)
mean = 10
standard_deviation = 2
random_matrix = mean + standard_deviation * np.random.randn(5, 5)
print(random_matrix)