from functools import reduce

# Exercise 1
# Create a lambda function that adds 15 to a given number and prints the result.
add_15 = lambda x: x + 15
print(add_15(10))  # Output: 25

# Exercise 2:
# Write a lambda function that multiplies two numbers and prints the result.
multiply_two_numbers = lambda x, y: x * y
print(multiply_two_numbers(2, 3))  # Output: 6

# Exercise 3:
# Use a lambda function to find the square of a number.
find_square_number = lambda x: x**2
print(find_square_number(3))  # Output: 9

# Exercise 4:
# Use a lambda function with filter() to filter out even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Exercise 5:
# Use a lambda function with map()
# to convert a list of temperatures from Celsius to Fahrenheit.
temparetures = [0, 20, 40, 60, 80, 100]
celsius_to_fahrenheit = lambda x: (x * 9 / 5) + 32
print(
    list(map(celsius_to_fahrenheit, temparetures))
)  # Output: [32.0, 68.0, 104.0, 140.0, 176.0, 212.0]

# Exercise 6:
# Write a lambda function to find the maximum of two numbers.
find_max_number = lambda x, y: max([x, y])
print(find_max_number(100, 101))  # Output: 101

# Exercise 7:
# Use a lambda function with reduce() to find the product of all elements in a list.
numbers = [1, 2, 3, 4, 5]
number_product = reduce(multiply_two_numbers, numbers)
print(number_product)  # Output: 120

# Exercise 8:
# Create a lambda function that checks if a number is a multiple of 3.
is_multiple_of_three = lambda x: x % 3 == 0
print(is_multiple_of_three(9))  # Output: True
print(is_multiple_of_three(20))  # Output: False

# Exercise 9:
# Write a lambda function to calculate the area of a rectangle.
rectangle_area = lambda h, w: h * w
print(rectangle_area(5, 8))  # Output: 40

# Exercise 10:
# Use a lambda function with map() to increment each number in a list by 1.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
increment_by_one = lambda x: x + 1
print(list(map(increment_by_one, numbers)))  # Output:[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Exercise 11:
# Create a lambda function that takes a string and returns its length.
length_of_string = lambda str: len(str)
print(length_of_string("Hello"))  # Output: 5

# Exercise 12:
# Write a lambda function that concatenates two strings.
concat_string = lambda str1, str2: "".join([str1, str2])
print(concat_string("Hello", "World"))  # Output: HelloWorld

# Exercise 13:
# Use a lambda function with filter() to find all numbers greater than 5 in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_greater_than_five = lambda x: 5 < x
print(list(filter(is_greater_than_five, numbers)))  # Output: [6, 7, 8, 9, 10]

# Exercise 14:
# Create a lambda function that checks if a string contains a specific letter.
word = "Hello, World!"
is_involved = lambda str, letter: str.__contains__(letter)
print(is_involved(word, "H"))  # Output:True
print(is_involved(word, "w"))  # Output:False

# Exercise 15:
# Write a lambda function to double all elements in a list using map() .
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_number = lambda x: x * 2
print(list(map(double_number, numbers)))  # Output:[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Exercise 16:
# Create a lambda function to check if a given string is a palindrome.
is_palindrome = lambda str: str == str[::-1]
print(is_palindrome("level"))  # Output:True
print(is_palindrome("apple"))  # Output:False

# Exercise 17:
# Write a lambda function to sort a list of tuples based on the second element.
tuples = [(1, "one"), (2, "two"), (3, "three")]
sort_based_on_second_element = lambda x: sorted(x, key=lambda y: y[1])
print(
    sort_based_on_second_element(tuples)
)  # Output:[(1, 'one'), (3, 'three'), (2, 'two')]

# Exercise 18:
# Use a lambda function to filter out all words from a list that are longer than 4 characters.
words = ["apple", "bat", "cat", "dolphin"]
print(list(filter(lambda x: len(x) <= 4, words)))  # Output:['bat', 'cat']

# Exercise 19:
# Create a lambda function to find the factorial of a number using reduce() .
number = 5
factorial = lambda x: reduce(lambda y, z: y * z, range(1, x + 1))
print(factorial(5))  # Output:120

# Exercise 20:
# Use a lambda function to sort a list of dictionaries by a specific key.
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20},
]
sort_with_key = lambda dict_list, key_name: sorted(
    dict_list, key=lambda dict: dict[key_name]
)
print(sort_with_key(people, "age"))
# Output: [{'name': 'Charlie', 'age': 20}, {'name': 'Alice','age': 25}, {'name': 'Bob', 'age': 30}]

# Exercise 21:
# Write a lambda function to flatten a nested list.
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_list = lambda x: sum(x, [])
print(flatten_list(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exercise 22:
# Create a lambda function to count the number of vowels in a string.
count_vowels = lambda str: len(
    list(filter(lambda l: l in ["a", "e", "i", "o", "u"], str))
)
print(count_vowels("Hello"))  # Output:2

# Exercise 23:
# Use a lambda function to find the second largest number in a list.
numbers = [1, 2, 3, 4, 5, 6]
# Remove duplicates then sort them by decend order, and index 1 is the second largest.
second_largest_num = lambda x: sorted(list(dict.fromkeys(x)), reverse=True)[1]
print(second_largest_num(numbers))  # Output:5

# Exercise 24:
# Write a lambda function to remove duplicates from a list.
numbers = [1, 2, 2, 3, 4, 4, 5]
remove_duplicates = lambda x: list(dict.fromkeys(x))
print(remove_duplicates(numbers))  # Output:[1, 2, 3, 4, 5]

# Exercise 25:
# Create a lambda function to find the longest word in a list of words.
words = ["apple", "banana", "cherry", "date"]
longest_word = lambda w: max(w, key=len)
print(longest_word(words))  # Output:banana