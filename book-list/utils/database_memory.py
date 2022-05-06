books = []


def create_book_table():
    pass


def get_all_books():
    return books


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': 0})


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = 1


def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
