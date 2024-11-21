import matplotlib.pyplot as plt
import numpy as np

dataset1 = np.random.normal(60, 10, 100)  # 100 data points around mean 60
dataset2 = np.random.normal(70, 15, 100)  # 100 data points around mean 70
dataset3 = np.random.normal(80, 5, 100)  # 100 data points around mean 80

# Create subplots
fig, ax = plt.subplots(nrows=1, ncols=3)

ax[0].boxplot(dataset1)
ax[0].set_title("Example Box Plot1")
ax[1].boxplot(dataset2)
ax[1].set_title("Example Box Plot2")
ax[2].boxplot(dataset3)
ax[2].set_title("Example Box Plot3")
plt.show()
