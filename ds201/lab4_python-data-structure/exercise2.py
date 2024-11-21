inventory = {
    "apple": (50, 0.5),
    "banana": (100, 0.2),
    "orange": (75, 0.3),
    "pear": (20, 0.4),
}

# 1. Print the current inventory in a user-friendly format.
for k, v in inventory.items():
    print(f"Item: {k}, Quantity: {v[0]}, Price: {v[1]}")

# 2. Calculate and print the total value of the inventory.
for k, v in inventory.items():
    print(v[0] * v[1])

# 3. Add a new product "mango" with 30 items priced at $0.6 each to the inventory.
inventory["mango"] = (30, 0.6)

# 4. Update the quantity of "banana" to 120 and print the updated inventory.
inventory["banana"] = (120, 0.2)
print(inventory)

# 5. Remove "pear" from the inventory and print the updated inventory.
del inventory["pear"]
print(inventory)
