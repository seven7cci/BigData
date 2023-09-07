import matplotlib.pyplot as plt

# y = 2x
# x의 범위 : -10 ~ 10
x = [x for x in range(-10, 10)]
y = [2*i for i in x]

plt.plot(x, y, marker='o')
# plt.axis([-20, 20, -20 ,20])

plt.title('y = 2x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
