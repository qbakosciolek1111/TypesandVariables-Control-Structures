import json

book = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "pages": 310,
    "genres": ["fantasy", "adventure"],
    "rating": 9.5,
    "read": True
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(book, file, indent=4, ensure_ascii=False)

print("Data has been written to favourite.json")