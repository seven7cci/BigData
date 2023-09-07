import matplotlib.pyplot as plt

x = [n for n in range(0, 20)]
y = [pow(n, 2) for n in range(0, 20)]
z = [n**3 for n in range(0, 20)]
power = [pow(2, n) for n in range(0, 20)]

plt.plot(x, x, label='linear')
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='qubic')
plt.plot(x, power, label='power')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('graph')
plt.legend()
plt.show()
