import re

# Task 1: Extract Email Addresses from Job Applications
print('----- Task 1 -----')
text = """
Hi, my name is Sarah. Please contact me at sarah_123@outlook.com.
Or my backup: s.johnson99@gmail.com
"""
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print(emails)

# Task 2: Clean Up Product Reviews
print('----- Task 2 -----')
review = "This phone is awesome!! 😍😍   Buy now!!!  $$$"
cleaned_review = re.sub(r"[^\w\s.,!?]", "", review)
print(cleaned_review)

# Task 3: Extract Dates from News Articles
print('----- Task 3 -----')
text = "The events happened on 04/21/2023, 5/1/24, and 12/31/99."
dates = re.findall(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", text)
print(dates)

# Task 4: Validate Canadian Postal Codes
print('----- Task 4 -----')
text = "Please ship to V6E 1X4. Alternate: M5V-3L9 or wrong: 123 ABC"
postal_codes = re.findall(r"\b[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d\b|\b[A-Za-z]\d[A-Za-z]-\d[A-Za-z]\d\b", text)
print(postal_codes)

# Task 5: Extract Domain Names from URLs
print('----- Task 5 -----')
text = "Visit our site at https://openai.com or follow us at http://github.com/openai"
domains = re.findall(r"https?://([A-Za-z0-9.-]+)", text)
print(domains)

print('----- Bonus -----')
# Bonus: Extract First and Last Names
text = "Full Name: John Doe. Another person: Alice Smith"
names = re.findall(r"(?<=: )([A-Z][a-z]+ [A-Z][a-z]+)", text)
print(names)
