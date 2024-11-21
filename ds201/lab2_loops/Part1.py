user_input_num = input("Enter a number: ")
user_input_n = input("Enter n: ")

# User input should always be integer value and
# is not allowed to be out of the range.
num = int(user_input_num)
n = int(user_input_n)

for i in range(n-1):
    num //= 10

print(num % 10)
