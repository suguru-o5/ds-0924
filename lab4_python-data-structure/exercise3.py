employees = [
    ("John Doe", "Accounting", "john.doe@example.com"),
    ("Jane Smith", "Marketing", "jane.smith@example.com"),
    ("Emily Davis", "HR", "emily.davis@example.com"),
    ("Michael Brown", "IT", "michael.brown@example.com"),
]

# 1. Print the names and departments of all employees.
for row in employees:
    print(row[0] + " , " + row[1])

# 2. Print the email addresses of all employees in alphabetical order by their last names.
sorted_employees = sorted(
    employees, key=lambda x: x[2][x[2].find(".") + 1 : x[2].find("@")]
)

for row in sorted_employees:
    print(row[2])

# 3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com") and print the updated list.
employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
print(employees)


# 4. Find and print the department of "Jane Smith".
for row in employees:
    if row[0] == "Jane Smith":
        print(row[1])
        break
