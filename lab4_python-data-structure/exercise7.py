countries = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
}

# 1. Print the names of all countries and their capitals.
for k, v in countries.items():
    print(f"Name: {k}, Capital: {v}")

# 2. Find and print the capital of Germany.
print(countries["Germany"])

# 3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
countries["Australia"] = "Canberra"

# 4. Update the capital of "USA" to "New Washington" and print the updated dictionary.
countries["USA"] = "New Washington"
print(countries)

# 5. Remove "France" from the dictionary and print the updated dictionary.
del countries["France"]
print(countries)
