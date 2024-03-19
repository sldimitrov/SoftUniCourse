class Book:
    """
    Dependency Inversion relies on abstractions to work properly and to protect
    """
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class AdvancedFormatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content[::-1]


class Printer:
    @staticmethod
    def get_book(book: Book, format_style):
        return format_style.format(book)


base_formatter = Formatter()
book = Book("Some content")
advanced_formatter = AdvancedFormatter()

p = Printer()

print(p.get_book(book, base_formatter))
print(p.get_book(book, advanced_formatter))

