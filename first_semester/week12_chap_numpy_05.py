import numpy as np

# a1 = np.array(range(1, 11)) + np.array(range(10, 101, 10))
# print(a1, a1.shape, a1.size, a1.ndim)

# 1. 0에서 9까지 정수값을 가지는 ndarry 책체 array_a를 넘파이를 이용하여 작성하고 출력
# 2. range()를 사용하여 0에서 9까지의 정수 값을 가지는 array 객체 array_b를 만들고 [0, 1, 2..., 9] 형태로 출력
# 3. 문제2의 코드를 수정하여 0에서 9까지의 정수 값 중에 0과 짝수만 가지는 ndarry 객체 array_c
# 4. arrray_c의 shape, ndim, dtype, size, itemsize 출력
# 5. 직원 3명의 월급이 250만원, 220만원, 230만원이다.
# 사장은 보너스로 월급의 2.1배를 지급하려고 한다. 해당 월급을 넘파이배열로 출력하는 코드를 작성하시오

# array_a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# array_a = np.array(range(10))
array_a = np.arange(10)
print(array_a)

array_b = np.array(range(10))
print(array_b)

array_c = np.array(range(0, 10 ,2))
print(array_c)
print(array_c.shape, array_c.ndim, array_c.dtype, array_c.size, array_c.itemsize)

salary = np.array([250, 220, 230])
bonus = salary * 2.1
print(bonus)

mixed = np.array([-9, 'daelim', False, 2.71])
print(mixed)
# 넘파이 배열은 파이썬의 리스트처럼 서로 다른 타입의 원소를 가질 수 없다.
# 위 예제의 경우 가장 우선순위가 높은 문자열 타입으로 모두 변환된다.