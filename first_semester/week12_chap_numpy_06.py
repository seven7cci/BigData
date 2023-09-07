import numpy as np

# BMI 계산 (몸무게를 키의 제곱으로 나눔, 단 키의 단위는 meter, 몸무게는 kg
# 6명의 몸무게(kg)와 키(cm)가 다음과 같을 때 각 학생의 체질량 지수(BMI)를 출력하시오
weight = np.array([86, 74, 59, 95, 80, 68])
height = np.array([183, 176, 169, 186, 177, 173])
height_meter = height * 0.01

# BMI = weight / height / height * 10000
BMI = weight / (height_meter**2)
print(BMI)
