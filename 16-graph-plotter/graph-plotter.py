# Install library matplotlib
# pip3 install matplotlib

import matplotlib.pyplot as plt

# Coordinates for the graph
x = [2, 4, 5, 6]
y = [2, 3, 6, 7]

plt.plot(x, y)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph')

plt.show()