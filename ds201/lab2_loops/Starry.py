user_input = input("Enter the count of rows: ")
# User input should always be integer value.
n = int(user_input)

# pattern1
print("---pattern1---")

max_stars = 2 * n - 1

for i in range(1, n + 1):
    current_stars = 2 * i - 1
    for j in range((max_stars - current_stars) // 2):
        print(" ", end="")
    for k in range(current_stars):
        print("*", end="")
    for l in range((max_stars - current_stars) // 2):
        print(" ", end="")
    print()

# pattern2
print("---pattern2---")

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# pattern3
print("---pattern3---")

for i in range(n // 2):
    for j in range(i + 1):
        print("*", end="")
    print()

# Check if n is even
if n % 2 != 0:
    for i in range(n // 2 + 1):
        print("*", end="")
    print()

for i in range(n // 2 - 1, -1, -1):
    for j in range(i + 1):
        print("*", end="")
    print()

# pattern4
print("---pattern4---")

for i in range(n // 2):
    for j in range(i):
        print(" ", end="")
    for k in range(n - 2 * i):
        print("*", end="")
    for l in range(i):
        print(" ", end="")
    print()
# Check if n is even
if n % 2 != 0:
    for i in range((n - 1) // 2):
        print(" ", end="")
    print("*", end="")
    for i in range((n - 1) // 2):
        print(" ", end="")
    print()
for i in range(n // 2 - 1, -1, -1):
    for j in range(i):
        print(" ", end="")
    for k in range(n - 2 * i):
        print("*", end="")
    for l in range(i):
        print(" ", end="")
    print()

# pattern5
print("---pattern5---")

for i in range(n // 2, 0, -1):
    if n - 2 * i == 0:
        continue
    for j in range(i):
        print(" ", end="")
    for k in range(n - 2 * i):
        print("*", end="")
    for l in range(i):
        print(" ", end="")
    print()
# Check if n is even
if n % 2 != 0:
    for i in range(n):
        print("*", end="")
    print()
for i in range(1, n // 2 + 1):
    if n - 2 * i == 0:
        continue
    for j in range(i):
        print(" ", end="")
    for k in range(n - 2 * i):
        print("*", end="")
    for l in range(i):
        print(" ", end="")
    print()
