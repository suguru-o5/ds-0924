import matplotlib.pyplot as plt

x = range(0, 20)
y = [value**2 for value in x]

plt.plot(x, y)
plt.annotate(
    "Highest",
    xy=(max(x), max(y)),
    ha="center",
    va="bottom",
)
plt.annotate(
    "Lowest",
    xy=(min(x), min(y)),
    ha="center",
    va="bottom",
)
plt.xlabel("Example x-label")
plt.ylabel("Example y-label")

plt.show()
