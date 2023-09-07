import numpy as np

n0 = np.zeros(2)
# n1 = np.ones(7)
n1 = np.ones(7, dtype=np.int64)  # 모든(7개) 원소를 1로 채우는 넘파이 배열 생성, 기본 값은 float이고 dtype속성으로 int 타입으로 변경
# n2 = np.arange(8)
n2 = np.arange(3, 40, 3)
n3 = np.array(range(3, 40, 3))

print(type(n1[0]))

print(n2 == n3)

print(n0, n1, n2)
print(n3)