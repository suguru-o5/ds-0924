import matplotlib.pyplot as plt
import numpy as np

# Line Plot Dataset
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Bar Plot Dataset
categories = ["A", "B", "C", "D", "E"]
values = [5, 7, 3, 8, 6]

# Histogram Dataset
data = np.random.randn(1000)

# Scatter Plot Dataset
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Create subplots
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0, 0].plot(x, y)
ax[0, 0].set_title("Example Line Plot")
ax[0, 1].bar(categories, values)
ax[0, 1].set_title("Example Bar Plot")
ax[1, 0].hist(data)
ax[1, 0].set_title("Example Histgram")
ax[1, 1].scatter(x_scatter, y_scatter)
ax[1, 1].set_title("Example Scatter Plot")

plt.show()
