from book import Book


# Создаем список книг (библиотеку)

library = [
    Book ("1984", "George Orwell"),
    Book ("The Great Gatsby", "F. Scott Fitzgerald"),
    Book ("The Catcher in the Rye","J.D. Salinger")
]

for book in library:
 print(f"{book.title} - {book.author}")
