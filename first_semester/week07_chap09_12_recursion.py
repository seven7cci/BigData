import my_utility

# memo = {}  # 한 번 수행한 피보나치 수(결과)를 저장
#
#
# def fibonacci_memorization(n):
#     """
#     DP를 적용하여 피보나치 재귀 함수의 성능개선 버전의 함수
#     :param n: 입력 값
#     :return: 피보나치 수
#     """
#     if n in memo:
#         return memo[n]  # key 값에 해당하는 value 리턴
#     if n == 0:
#         memo[0] = 0
#         return memo[0]
#     elif n == 1:
#         memo[1] = 1
#         return memo[1]
#     else:
#         memo[n] = fibonacci_memorization(n-2) + fibonacci_memorization(n-1)
#         return memo[n]


memo = {0: 0, 1: 1}  # 한 번 수행한 피보나치 수(결과)를 저장, 초기값 부여


def fibonacci_memorization(n):
    """
    DP를 적용하여 피보나치 재귀 함수의 성능개선 버전의 함수
    :param n: 입력 값
    :return: 피보나치 수
    """
    if n in memo:
        return memo[n]  # key 값에 해당하는 value 리턴
    memo[n] = fibonacci_memorization(n-2) + fibonacci_memorization(n-1)
    return memo[n]

def fibonacci_recursion(n):
    """
    재귀함수를 이용한 피보나치 수 구하기
    :param n: 입력값
    :return: 피보나치 수
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)


def fibonacci_repetition(n):
    """
    반복문을 사용한 피보나치 수 구하는 함수
    :param n: 입력 값
    :return: 피보나치 수
    """
    if n == 0 or n == 1:
        return n
    else:
        result = 0
        t1, t2 = 1, 0
        for i in range(2, n+1):
            result = t1 + t2
            t2 = t1
            t1 = result
    return result


# print(fibonacci_repetition(36))

frep = my_utility.time_check(fibonacci_repetition)
print(frep(50))

# print(fibonacci_recursion(50))

fmemo = my_utility.time_check(fibonacci_memorization)
print(fmemo(50))

fb = my_utility.time_check(fibonacci_recursion)
print(fb(35))

