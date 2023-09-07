# lambda

# def squares(n):
#     return n * n
#
#
# numbers = [i for i in range(10)]
# ss = list(map(squares, numbers))
#
# print(ss)


numbers = [i for i in range(10)]
ss = list(map(lambda n: n*n, numbers))

print(ss)
