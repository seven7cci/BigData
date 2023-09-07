import copy

a = [["ace", 9], 2, 3]
b = a.copy()  # copy - copy()는 모든 리스트값이 Immutable해야한다.
c = list(a)  # copy
d = a[:]  # copy
e = a  # reference - 주소가 같다.
f = copy.deepcopy(a)  # deepcopy - 새로운 메모리공간에 값을 만듦, 메모리공간을 더 많이 차지함

print(a, b, c)
print(d, e, f)
print(id(a), id(b), id(c))
print(id(d), id(e), id(f))
a[0][1] = "C++은 어려워"
print(a, b, c)
print(d, e, f)

a = [2, 1, 7]
b = [2, 1, 6, 1]
print(a <= b)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x'")

# numbers = []
# for i in range(1, 10, 3):
#     numbers.append(i)  # 아래와 같이 사용가능
numbers = [i**2 for i in range(1, 10, 3)]
print(numbers)

numbers = []
# for i in range(1, 10):
#     if i % 2 == 0:
#        numbers.append(i**2)  # 아래와 같이 사용가능
numbers = [i**2 for i in range(1, 10) if i % 2 == 0]
print(numbers)
