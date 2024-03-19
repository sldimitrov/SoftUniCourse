from typing import List


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def turn_page(self, page):
        self.pages = page

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.pages}."

    
class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.location = []

    def search_for(self, param, expected_value):
        return [b for b in self.books if b.param == expected_value]


    def add_book(self, book: str) -> str:
        book_match = [b for b in self.books if b == book]
        
        if book_match:
            raise ValueError("Book is already added to the collection")
        
        self.books.append(book) 
        return f"You have sucessfully added a book"

    def remove_book(self, book_title: str) -> str:
        matched_book = [b for b in self.books if b.title == book_title]
        
        if not matched_book:
            raise ValueError("There is no such book in the library!")
        
        self.books.remove(matched_book)
        return f"Succesfully removed the book"
    
    def search_by_author(self, author_name: str) -> str:
        matched_books = self.search_for("author", author_name)

        if not matched_books:
            raise ValueError("There is no books from this author.")
        
        return "\n".join(matched_books)
    
    def search_by_title(self, title: str):
        matched_books = [str(x) for x in self.books if x.title == title]

        if not matched_books:
            raise ValueError("There is no book with such title")
    

book = Book("ab", "Habibi", "22")
book2 = Book("abc", "Habibi", "2211")
book3 = Book("abdd", "Habibi", "223")

print(book)

lib = Library()

lib.add_book(book)
lib.add_book(book2)

print(lib.books)
print(lib.search_by_author("Habibi"))








