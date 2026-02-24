books = [
    {
        "title": "one Hundred Years of Solitude",
        "author": "Gabriel Garcia MArquez",
        "published": '1967',
    }
    {
        "title": The Book of Kells",
        "author": "Multiple Authors",
        "published": "800",
    },
    {
        "title": "War and Peace",
        "author": "Leo tolstoy",
        "published": "1869",
    },
]

def published_year(book):
    return int(book['published'])

sorted_books = sorted(books, key=published_year)
print(sorted books)