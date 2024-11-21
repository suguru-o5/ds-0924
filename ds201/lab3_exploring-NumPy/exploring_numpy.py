import numpy as np

# Task1
array1 = np.arange(1, 31)
print(array1)
print(array1.shape)
print(array1[10])

# Task2
array2 = array1.reshape(6, 5)
print(array2)
print(array2[2, 3])

# Task3
print(array2[2])
print(array2[0:2, 2:5])

# Task4
random_array1 = np.random.randint(low=10, high=101, size=15)
print(random_array1)
print(random_array1.max())
print(random_array1.min())

# Task5
random_array2 = np.random.randint(low=0, high=51, size=[4, 4])
print(random_array2)
print(random_array2.sum())

# Task6
random_array3 = np.random.randint(low=0, high=21, size=[5, 5])
print(random_array3)
random_array3[1, :] = 0
print(random_array3)
random_array3 = np.where(random_array3 > 10, 99, random_array3)
print(random_array3)

# Task7
random_array4 = np.random.randint(low=1, high=11, size=5)
random_array5 = np.random.randint(low=1, high=11, size=5)
print(random_array4 + random_array5)
print(random_array4 - random_array5)
print(random_array4 * random_array5)

# Task8
array3 = np.arange(2, 10, 2)
print(array3)
random_array6 = np.random.randint(low=1, high=6, size=[3, 4])
print(random_array6)
print(array3 + random_array6)

# Task9
random_array7 = np.random.randint(low=1, high=101, size=20)
print(random_array7[random_array7 > 50])
random_array7[random_array7 < 30] = -1
print(random_array7)

# Task10
random_array8 = np.random.randint(low=1, high=51, size=12)
random_array8 = random_array8.reshape([3, 4])
print(random_array8)
random_array8 = random_array8.transpose()
print(random_array8)
