import numpy as np

# v = np.array([1, 3, -9, 2])
# v = np.array([1, 3, -9, 2], dtype='int64')
v = np.array([[1, 3, -9, 2],[71, 13, -22, 7]], dtype='int64')
print(v.ndim, v.shape, v.data, v.dtype, v.strides) # ndim : 차원, shape : 배열, data : 메모리 주소, : dtype : 데이터 타입, strides : 메모리 간격
