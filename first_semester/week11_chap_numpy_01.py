import numpy as np

n1 = np.array([3, 9, 7])
n2 = np.array([[1, 2], [3.14, 4], [5, 6]])
n3 = np.array(
    [
        [
            [1, 2], [3, 4], [5, 6]
        ],
        [
            [1, 2], [3, 4], [5, '6']
        ]
    ]
)
test = ['9', 1111, 2.98]
n4 = np.array(test)

# int < float < string
# np.array에 값 중 1개를 바꾸면 나머지도 바뀜

print(type(n1))
print(n1[1])  # scalar
print(n1.shape, n1.ndim)  # 1D array, vector
print(n2.shape, n2.ndim)  # 2D array, matrix
print(n3.shape, n3.ndim)  # 3D array, tensor
print(n1.size, n2.size, n3.size)
print(n1.dtype, n2.dtype, n3.dtype)
print(n1, n1.itemsize, n1.data)
print(n2, n2.itemsize, n2.data)
print(n3, n3.itemsize, n3.data)
print(n4, n4.itemsize, n4.data)
