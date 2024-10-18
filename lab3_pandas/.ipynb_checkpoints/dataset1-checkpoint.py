import pandas as pd

# Load the dataset into a Pandas DataFrame.
students_grades: pd.DataFrame = pd.read_csv("lab3_pandas/students_grades.csv")
# Display the first 5 rows of the DataFrame.
print(students_grades.head())

# Display the summary statistics of the DataFrame.
# print(students_grades.sum())

# Display the column names of the DataFrame.
print(students_grades.columns)

# Count the number of male and female students.
print(students_grades["Gender"].value_counts())
