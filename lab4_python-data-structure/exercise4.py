library = {
    "978-3-16-148410-0": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
    },
    "978-0-14-028329-7": {"title": "1984", "author": "GeorgeOrwell", "year": 1949},
    "978-0-7432-7356-5": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
    },
    "978-0-452-28423-4": {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
    },
}

# 1. Print the details of all books in a user-friendly format.
for _, book in library.items():
    print(f"Title : {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")
    print("-----")


# 2. Find and print the details of the book with the ISBN "978-0-14-028329-7".
print(library["978-0-14-028329-7"])

# 3. Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", and year 1925.
library["978-1-4028-9462-6"] = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
}

# 4. Update the year of "To Kill a Mockingbird" to 1961 and print the updated details.
for book in library.values():
    if book["title"] == "To Kill a Mockingbird":
        book["year"] = 1961

for book in library.values():
    if book["title"] == "To Kill a Mockingbird":
        print(book)

# 5. Remove the book with ISBN "978-0-452-28423-4" and print the updated library.
del library["978-0-452-28423-4"]
print(library)
