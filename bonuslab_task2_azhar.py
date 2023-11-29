class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# Создаем экземпляры класса Book
book_first= Book("It starts with us", "Colleen Hoover", "234-7-267-4566-3")
book_second= Book("Little woman", "Louisa May Alcott", "456-3-06-13578-5")
book_third= Book("Will", "Mark Manson", "235-5-452-224960-7")

# Выводим информацию о каждой книге
print(f"Книга первая: {book_first.title} написанная  {book_first.author}, ISBN: {book_first.isbn}")
print(f"Книга вторая: {book_second.title} by {book_second.author}, ISBN: {book_second.isbn}")
print(f"Книга третья: {book_third.title} by {book_third.author}, ISBN: {book_third.isbn}")