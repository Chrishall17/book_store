from lib.book import Book

"""
Book constructs with an id, title and author name
"""
def test_book_constructs():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book) == "1 - Nineteen Eighty-Four - George Orwell"

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    book2 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book1 == book2