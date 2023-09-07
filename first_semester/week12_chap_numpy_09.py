import numpy as np

z = np.array([
    [1.83, 1.76, 1.69, 1.86, 1.77, 1.73],
    [86, 74, 59, 95, 80, 68]
])
print(z)
# z1 = z[0:2, 1:3]
# z2 = z[0:2][1:3]
# print(z1, z2)
bmi_2d = z[1] / (z[0]**2)
print(bmi_2d)
