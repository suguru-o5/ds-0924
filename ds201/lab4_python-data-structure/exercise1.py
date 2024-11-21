students = {
    "Alice": [85, 78, 92],
    "Bob": [79, 74, 81],
    "Charlie": [91, 82, 85],
    "David": [76, 85, 83],
    "Eve": [88, 79, 92],
}

def calcAverage(student_scores):
    return sum(student_scores) / len(student_scores)

# 1. Calculate and print the average score for each student
average_scores = {}

for key in students.keys():
    average_score = calcAverage(students[key])
    average_scores[key] = average_score
    print(average_score)

# 2. Find and print the name of the student with the highest average score.
for key, value in average_scores.items():
    if value == max(average_scores.values()):
        print(key)

# 3. Find and print the name of the student with the lowest average score.
for key, value in average_scores.items():
    if value == min(average_scores.values()):
        print(key)

# 4. Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary.
students["Frank"] = [80, 90, 85]
print(students)
