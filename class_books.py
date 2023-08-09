from main_menu_options import LIST_BOOK_NAME_TECH_LIST, LIST_BOOK_NAME_SCIENCE_LIST
from main_menu_options import LIST_BOOK_AUTHOR_SCIENCE_LIST, LIST_BOOK_AUTHOR_TECH_LIST

class Books:

    def __init__(self,
                 title='',
                 author='',
                 publisher='',
                 publishing_date='',
                 isbn_number=''):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._publishing_date = publishing_date
        self._isbn_number = isbn_number

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def publishing_date(self):
        return self._publishing_date

    @publishing_date.setter
    def publishing_date(self, value):
        self._publishing_date = value

    @property
    def isbn_number(self):
        return self._isbn_number

    @isbn_number.setter
    def isbn_number(self, value):
        self._isbn_number = value

    # @staticmethod
    def define_book_tech(self, list_books):

        book_data = []

        self.title = input('Enter the title of the tech book\n')
        if self.title in LIST_BOOK_NAME_TECH_LIST:
            print('This book is already in the list\n')
            return list_books
        else:
            book_data.append(self.title)
            LIST_BOOK_NAME_TECH_LIST.append(self.title)
            self.author = input('Enter the author of the tech book\n')
            book_data.append(self.author)
            LIST_BOOK_AUTHOR_TECH_LIST.append(self.author)
            self.publisher = input('Enter the publisher of the tech book\n')
            book_data.append(self.publisher)
            self.publishing_date = input('Enter the publishing tech date\n')
            book_data.append(self.publishing_date)
            self.isbn_number = input('Enter the isbn number\n')
            book_data.append(self.isbn_number)
            list_books.append(book_data)
            print(list_books)
            return list_books

    def define_book_science(self, list_books):
        book_data = []

        self.title = input('Enter the title of the science book\n')
        if self.title in LIST_BOOK_NAME_SCIENCE_LIST:
            print('This scientific book is already in the list\n')
            return list_books
        else:
            book_data.append(self.title)
            LIST_BOOK_NAME_SCIENCE_LIST.append(self.title)
            self.author = input('Enter the author of the book\n')
            book_data.append(self.author)
            self.publisher = input('Enter the publisher of the book\n')
            book_data.append(self.publisher)
            self.publishing_date = input('Enter the publishing date\n')
            book_data.append(self.publishing_date)
            self.isbn_number = input('Enter the isbn number\n')
            book_data.append(self.isbn_number)
            print(LIST_BOOK_NAME_SCIENCE_LIST)
            print(book_data)
            list_books.append(book_data)
            print(list_books)
            return list_books
