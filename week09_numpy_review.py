import numpy as np

def info(x):
    print(f"배열의 차원(rank)은 {x.ndim}입니다.")
    print(f"배열의 shape은 {x.shape}입니다.")
    print(f"배열의 원소의 개수는 {x.size}입니다.")


np_1d = np.arange(1, 20, 2)
print(np_1d)
info(np_1d)
np_1d = np_1d.reshape(1, 2, 5)
print(np_1d)
info(np_1d)
