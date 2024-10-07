members = [
    {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
    {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
    {"name": "Charlie", "age": 22, "books_borrowed": ["BraveNew World", "1984"]},
    {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]},
]

# 1. Print the names and ages of all members.
for member in members:
    print(f"Name: {member['name']}, Age: {member['age']}")

# 2. Find and print the books borrowed by "Charlie".
for member in members:
    if member["name"] == "Charlie":
        print(member["books_borrowed"])
        break

# 3. Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})

# 4. Update the age of "Bob" to 31 and print the updated list.
for member in members:
    if member["name"] == "Bob":
        member["age"] = 31
        break

print(members)

# 5. Remove "David" from the list and print the updated list.
members = list(filter(lambda x: x["name"] != "David", members))
print(members)
