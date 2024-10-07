cart = [
    {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
    {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
    {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
    {"item": "pear", "quantity": 2, "price_per_unit": 0.4},
]

# 1. Print the details of all items in the cart.
for item in cart:
    print(item)

# 2. Calculate and print the total cost of the cart.
total_cost = 0
for item in cart:
    total_cost += item["quantity"] * item["price_per_unit"]

print(total_cost)

# 3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})

# 4. Update the quantity of "banana" to 10 and print the updated cart.
for item in cart:
    if item["item"] == "banana":
        item["quantity"] = 10
        break

print(cart)

# 5. Remove "pear" from the cart and print the updated cart.
cart = list(filter(lambda row: row["item"] != "pear", cart))

print(cart)
