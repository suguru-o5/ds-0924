import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 500)  # 500 data points from a normal distribution

plt.hist(data, bins=20, edgecolor="b")
plt.xlabel("Example-x-label")
plt.ylabel("Example-y-label")
plt.title("Example-title")

plt.show()
