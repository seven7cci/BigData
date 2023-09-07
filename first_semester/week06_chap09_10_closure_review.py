import time


def time_check(func):  # closure
    def inner(*args, **kwargs):
        print(f"함수 이름 : {func.__name__}")
        print(f"함수 설명 : {func.__doc__}")
        s = time.time()
        r = func(*args, **kwargs)
        e = time.time()
        print(f"함수를 처리하는데 걸린 시간 : {e-s}")
        return r
    return inner


#@time_check
def factorial_recursion(n):
    """
    팩토리얼 함수 (재귀함수 사용)
    :param n: 입력 값, 정수
    :return: 팩토리얼 계산 결과 값
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)


@time_check
def factorial(n):
    """
    팩토리얼 함수 (반복문 사용)
    :return: 팩토리얼 계산 결과 값
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result


@time_check
def power(base, exponent):
    """
    거듭제곱 함수, 빌트인 함수 pow와 같이 동작 또는 **연산자와 동일한 결과 출력
    :param base: 밑, int
    :param exponent: 지수, int
    :return: 거듭제곱 결과 값, int
    """
    result = 1
    for _ in range(exponent):
        result = result * base
    return result


def do_something():
    """
    뭔가를 하는 무의미한 함수
    :return: void
    """
    total = 0
    print("함수에서 무언가 작업을 합니다")
    for k in range(1, 1000000):
        total = total + k


# print(do_something.__doc__)

# func2 = time_check(power)
# print(func2(2,4))
print(power(exponent=10, base=2))

print(f"{factorial(6)}")
print(factorial_recursion(6))


func1 = time_check(do_something)
func1()
#
# daelim_func2 = time_check(factorial)
# daelim_func2()


## 매 함수마다 시간을 재는 코드를 넣는 것은 비효율적
# import time
#
#
# def do_something():
#     s = time.time()
#     total = 0
#     print("함수에서 무언가 작업을 합니다")
#     for k in range(1, 1000000):
#         total = total + k
#     e = time.time()
#     print(f"함수를 처리하는데 걸린 시간 : {e-s}")
#
#
# do_something()
