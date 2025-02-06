class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f'You have borrowed {self.title} by {self.author}')
            return True
        else:   
            print(f'Sorry, {self.title} is not available')
            return False
    
    def return_book(self):
        self.available = True
        print(f'Thank you for returning {self.title}')

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'Sorry, {book.title} is not available')
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'You have not borrowed {book.title}')
    
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f'{book.title} has been added to the library')

    def add_user(self, user):
        self.users.append(user)
        print(f'{user.name} has been added to the library')

    def show_available_books(self):
        print('Available books:')
        for book in self.books:
            if book.available:
                print(f'{book.title} by {book.author} is available')

# crea los libros    

book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald')
book2 = Book('To Kill a Mockingbird', 'Harper Lee')
book3 = Book('1984', 'George Orwell')
book4 = Book('el principito', 'Antoine de Saint-Exupéry')

print('-'*50)
# crea usuarios
user1 = User('Fredy', 1)

print('-'*50)
# crear biblioteca
Library = Library()
Library.add_book(book1)
Library.add_book(book2)
Library.add_book(book3)
Library.add_book(book4)
Library.add_user(user1)

print('-'*50)
# muestra los libros disponibles
Library.show_available_books()
print('-'*50)
# el usuario toma prestado un libro
user1.borrow_book(book1)
print('-'*50)
# muestra los libros disponibles
Library.show_available_books()
print('-'*50)
# el usuario devuelve un libro
user1.return_book(book1)
user1.return_book(book2)
print('-'*50)
# muestra los libros disponibles
Library.show_available_books()