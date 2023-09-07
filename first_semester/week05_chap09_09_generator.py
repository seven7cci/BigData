# generator
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number = number + step  # number += step


print(my_range)
ranger = my_range()

for i in ranger:
    print(i, end=' ')

for i in ranger:
    print(i, end=' ')

# print(range(1, 11))
# print(type(range(1, 11)))
# print(list(map(lambda x: x*x, range(1, 11))))
