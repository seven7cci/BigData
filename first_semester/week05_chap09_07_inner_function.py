# closure
def outer(a, b):
    def inner():
        return a + b
    return inner

# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)


result = outer(11, 2)
print(type(result))
print(result)
print(result())



print(outer(11, 2))
