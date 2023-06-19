class Book:

    def __init__(self, name, author, publication_year, available = True):
        self.name = name
        self.author = author
        self.publication_year = publication_year
        self.available = available
    
    def setAvailability(self,value):
        self.available = value
    
class Library:
    books = []
    def __init__(self, name, author, publication_year):
        book = Book(name=name,author=author,publication_year=publication_year)
        self.books.append(book)
    def displayAllBooks(self):
        return self.books    
    def availableBooks(self):
        return [book for book in self.books if book.available]
    def unavailableBooks(self):
        return [book for book in self.books if not book.available]
    def removeBook(self,book):
        for book in self.books:
            if book.name == book.name and book.author == book.author and book.publication_year == book.publication_year:
                self.books.remove(book)
                return True


while True:
   
   print("1. Add Book")
   print("2. Remove Book")
   print("3. Display Available Books")
   print("4. Display unavailable Books")
   print("5. Display All Books")
   print("6. Quit")
   
   choice = input()
   print(choice)
   match choice:
       case "1": 
              name = input("Enter Book Name: ")
              author = input("Enter Author Name: ")
              publication_year = input("Enter Publication Year: ")
              library = Library(name=name,author=author,publication_year=publication_year)
              print("Book Added Successfully")
       case "2":
                try:
                 name = input("Enter Book Name: ")
                 author = input("Enter Author Name: ")
                 publication_year = input("Enter Publication Year: ")
                 book = Book(name=name,author=author,publication_year=publication_year)
                 library.removeBook(book)
                 print("Book Removed Successfully")
                except:
                    print("Book Not Found")

       case "3":
                if len(library.availableBooks()) == 0:
                    print("No Books Available")
                else:
                    print("Available Books")
                    for book in library.availableBooks():
                        print(book.name)
       case "4":
                if len(library.unavailableBooks()) == 0:
                    print("No Books Unavailable")
                else:
                    print("Unavailable Books")
                    for book in library.unavailableBooks():
                        print(book.name)
       case "5":
                if len(library.displayAllBooks()) == 0:
                    print("No Books Available")
                else:
                    print("All Books")
                    for book in library.displayAllBooks():
                        print(book.name)
       case "6":
             print("Quit")
             exit()
       case _:
             print("Invalid Choice")




