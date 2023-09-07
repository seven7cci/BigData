import numpy as np

scores = np.array([88, 72, 93, 94, 89, 78, 99])
# indexing
print(scores[1])
print(scores[-2], scores[5])

# slicing
print(scores[2:5])
print(scores[3:], scores[-4:])
print(scores[-3:-1], scores[4:6], scores[4:-1])

# comparison
y = scores >= 90
print(y)
print(scores[scores >= 90])

# BMI가 25이상만 출력
weight_kg = np.array([86, 74, 59, 95, 80, 68])
height_meter = np.array([183, 176, 169, 186, 177, 173]) * 0.01

# BMI = weight / height / height * 10000
BMI = weight_kg / (height_meter**2)
print(BMI[BMI >= 25])
