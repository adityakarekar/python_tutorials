class Library:
    no_of_books = 0
    books=[]


    def add_book(self, book):
        self.books.append(book)
        Library.no_of_books += 1

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

    def show_count(self):
        print(f"Total number of books in the library : {Library.no_of_books}")


book1=Library()
book1.add_book("Python Programming")
book1.add_book("Data Science")

book1.display_books()
book1.show_count()