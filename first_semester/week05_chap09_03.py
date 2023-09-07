def print_kwargs(**kwargs):
    print('keyword  arguments:', kwargs)


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data, end=3)
print_data(data, end=5, start=1)

print_kwargs()
print_kwargs(fruit="apple")
print_kwargs(fruit="apple", coffee="latte")
