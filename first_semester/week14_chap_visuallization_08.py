import matplotlib.pyplot as plt
import numpy as np

x_data = np.arange(20, 50)
y_data = x_data + 2 * np.random.randn(30)

plt.plot(range(20, 50), range(20, 50))
plt.title('Real age vs Physical age')
plt.scatter(x_data, y_data)
plt.xlabel('Real age')
plt.ylabel('Physical age')

plt.savefig('age.png', dpi=500)
plt.show()
