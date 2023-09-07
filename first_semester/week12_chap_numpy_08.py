import numpy as np

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 2D array (matrix)
# print(type(x))
# d2_array = np.array(x)
# print(type(d2_array), d2_array.shape, d2_array.ndim)
#
# # list_style
# print(d2_array[2][0], d2_array[-1][-3], d2_array[2][-3])
#
# # numpy_style
# print(d2_array[2, -3], d2_array[-1, 0])
#
# d2_array[0, 0] = 11
# print(d2_array)
#
# d2_array[0, 0] = 22.71  # truncation
# print(d2_array)

d2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(d2)
# print(d2[0])
print(d2[::2][::2])  # 첫 슬라이싱 : 0행, 2행 선택, 두번째 슬라이싱 : 0행 선택
print(d2[::2, ::2])  # 첫 슬라이싱 : 0행, 2행 선택, 두번째 슬라이싱 : 0열, 2열 선택
#
# print(d2[0:2, 2:])
# print(d2[:, 2])
print(d2[1::2, 1::2])