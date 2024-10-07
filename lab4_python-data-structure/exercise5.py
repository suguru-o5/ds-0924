cities = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000,
}

# 1. Print the population of each city in a user-friendly format.
for k, v in cities.items():
    print(f"City: {k} , Population: {v}")

# 2. Find and print the city with the highest population.
for k, v in cities.items():
    if v == max(cities.values()):
        print(k)

# 3. Find and print the city with the lowest population.
for k, v in cities.items():
    if v == min(cities.values()):
        print(k)

# 4. Update the population of "Phoenix" to 1700000 and print the updated data.
cities["Phoenix"] = 1700000
print(cities)

# 5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
cities["San Francisco"] = 884000
print(cities)
