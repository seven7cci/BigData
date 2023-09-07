import matplotlib.pyplot as plt

# y1 = 2x, y2 = x^2 + 5, y3 = -x^2 - 5
# x의 범위 : -20 ~ 20
x = [x for x in range(-20, 20)]
y1 = [2*i for i in x]
y2 = [((i*i)+5) for i in x]
y3 = [((-i**2)-5) for i in x]

plt.plot(x, y1, 'r--', x, y2, 'b^-', x, y3, 'g+:')
# plt.plot(x, y1, marker='o', color='red')
# plt.plot(x, y2, marker='o', color='blue')
# plt.plot(x, y3, marker='o', color='green')
# plt.axis([-20, 20, -20 ,20])

plt.title('y = 2x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
