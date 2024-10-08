import matplotlib.pyplot as plt
import numpy as np

categories = ["Group 1", "Group 2", "Group 3"]
value1 = np.array([5, 7, 3])
value2 = np.array([6, 8, 4])
value3 = np.array([4, 3, 5])

plt.bar(categories, value1, color="b")
plt.bar(categories, value2, bottom=value1, color="r")
plt.bar(categories, value3, bottom=value1 + value2, color="g")

plt.xlabel("Example x-label")
plt.ylabel("Example y-label")
plt.legend(["Round 1", "Round 2", "Round 3"])

plt.show()
