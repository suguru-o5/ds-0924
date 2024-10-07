movies = {
    "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
    "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
    "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
    "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
    "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"},
}

def calculate_highest_and_lowest(nested_dictionary: dict, key: any):
    temp_list = []
    for detail in nested_dictionary.values():
        temp_list.append(detail[key])
    return {"highest": max(temp_list), "lowest": min(temp_list)}

# 1. Print the details of all movies in a user-friendly format.
for k, v in movies.items():
    print(f"Title: {k}, Year: {v['year']}, Rating: {v['rating']}, Genre: {v['genre']}")

# 2. Find and print the highest-rated movie.
highest_rate = calculate_highest_and_lowest(movies,"rating")["highest"]

for title, detail in movies.items():
    if detail["rating"] == highest_rate:
        print(title)

# 3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

# 4. Update the rating of "Inception" to 9.0 and print the updated details.
movies["Inception"]["rating"] = 9.0
for title, detail in movies.items():
    print(title)
    print(detail)

# 5. Remove "Pulp Fiction" from the database and print the updated list.
del movies["Pulp Fiction"]
print(movies)
