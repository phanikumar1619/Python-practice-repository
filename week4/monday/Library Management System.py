class Library():

    library_name = "Central Library"
    total_books = 0

    def __init__(self , book_name , author):
        self.book_name = book_name
        self.author = author
        Library.total_books += 1
        self.is_borrowed = False

    def display_book(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Library:", self.library_name)
        status = "Borrowed" if self.is_borrowed else "Available"
        print("Book Status:", status)
        print()

    def borrow_book(self):
        if(self.is_borrowed):
            print("Book is already borrowed")
        else:
            self.is_borrowed = True
            print("Book borrowed successfully")

    def return_book(self):
        if(self.is_borrowed):
            self.is_borrowed = False
            print("Book returned successfully")
        else:
            print("This book is already available")

    @classmethod
    def change_library_name(cls , new_name):
        cls.library_name = new_name

    @staticmethod
    def check_book_eligibility(age):
        if(age >= 18):
            return True
        else:
            return False


b1 = Library("Python Basics", "Guido")
b2 = Library("Java Programming", "James Gosling")
b3 = Library("Clean Code", "Robert Martin")

b1.display_book()
b2.display_book()

Library.change_library_name("KL University Library")

b1.display_book()

print("Total Books:", Library.total_books)

print(Library.check_book_eligibility(20))
print(Library.check_book_eligibility(15))

b1.borrow_book()
# b1.borrow_book()
# b1.return_book()
# b1.return_book()
b2.borrow_book()
b3.borrow_book()
b1.return_book()
b2.borrow_book()
b3.return_book()
b1.return_book()