import matplotlib.pyplot as plt
import math

x = list()
sin = list()

for angle in range(360):
    x.append(angle)
    sin.append(math.sin(math.radians(angle)))

plt.plot(x, sin)
plt.title('sin wave')
plt.show()
