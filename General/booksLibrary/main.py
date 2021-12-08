class Library:
    def __init__(self, list_of_books):
        self.books = list_of_books

    def display_books(self):
        for index, book in enumerate(self.books):
            print(f'{index+1}. {book}')

    def borrow_book(self, bookname):
        if bookname in self.books:
            print(f'Book is successfully assigned to you {bookname}. Please keep is safe and return in 30 days')
            self.books.remove(bookname)
            return True
        else:
            print(f'Book is not available now. Please try later')
            return False

    def return_book(self, bookname):
        self.books.append(bookname)
        print('Thanks for returning it.')


class Student:
    def __init__(self, booklist):
        self.books = booklist

    def request_book(self):
        self.books = input('Please Enter the book name you want to borrow: ')
        return self.books

    def return_book(self):
        self.books = input('Please enter the book name you want to return/add: ')
        return self.books


if __name__ == '__main__':
    library = Library(['Python', 'Java', 'Algorithms', 'Deep Learning', 'Maths'])
    library.display_books()
    student = Student('maths')

    while True:
        welcome_msg = '==========welcome to Central Library=========== \n' \
                      'Please Choose an option: \n' \
                      '1. Listing all the books \n' \
                      '2. Request a book \n' \
                      '3. Add/Return a book \n' \
                      '4. Exit the library \n'

        print(welcome_msg)

        case = int(input("Enter a choice: "))

        if case == 1:
            library.display_books()
        elif case == 2:
            library.borrow_book(student.request_book())
        elif case == 3:
            library.return_book(student.return_book())
        elif case == 4:
            print('Thanks for choosing central library!!')
            exit()
        else:
            print('Invalid Choice')



