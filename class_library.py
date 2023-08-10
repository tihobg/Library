from typing import List
from enum_lib_name import LibName


class Library:
    def __init__(self,
                 lib_name=LibName.UNKNOWN,
                 book_list_tech=[],
                 book_list_science=[]
                 ):
        self._book_name = lib_name
        self._book_list_tech = book_list_tech
        self._book_list_science = book_list_science

    @property
    def name(self):
        return self._book_name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def book_list_tech(self):
        return self._book_list_tech

    @book_list_tech.setter
    def book_list_tech(self, value):
        self._book_list_tech = value

    @property
    def book_list_science(self):
        return self._book_list_science

    @book_list_science.setter
    def book_list_science(self, value):
        self._book_list_science = value

    def add_new_book_tech(self, lib_book: List, list_b: List):
        # self.name = LibName.TECHNICAL.value
        list_b.append(lib_book)
        self.book_list_tech = list_b
        return self.book_list_tech

    def add_new_book_science(self, lib_book: List, list_b: List):
        # self.name = LibName.SCIENCE.value
        lib_book.append(list_b)
        self.book_list_science = lib_book
        return self.book_list_science

    def search_book_name_tech(self, d: List):
        search_book = input('Please enter the name of the technical book for searching\n')
        self.book_list_tech = d

        for i in range(len(self.book_list_tech)):
            if search_book in self.book_list_tech[i][0]:
                print('The searching book is:\n')
                print(self.book_list_tech[i])
                break
            else:
                print('There is no such a book\n')

    def search_book_name_science(self, d: List):
        search_book = input('Please enter the name of the scientific book for searching\n')
        self.book_list_science = d
        for i in range(len(self.book_list_science)):
            if search_book in self.book_list_science[i][0]:
                print('The searching book is:\n')
                print(self.book_list_science[i])
                break
            else:
                print('There is no such a book\n')

    def search_book_author_tech(self, d: List):
        search_book = input('Please enter the author of the tech book for searching\n')
        self.book_list_tech = d
        new_book_list_tech = []
        for i in range(len(self.book_list_tech)):
            if search_book in self.book_list_tech[i][1]:
                print('The searching book is:\n')
                print(self.book_list_tech[i])
                # new_book_list_tech.append(self.book_list_tech[i])

            else:
                # print('There is no such books to delete')
                new_book_list_tech.append(self.book_list_tech[i])
        print(new_book_list_tech)
        return new_book_list_tech

    def search_book_author_science(self, d: List):
        search_book = input('Please enter the author of the science book for searching\n')
        self.book_list_science = d
        new_book_list_science = []
        for i in range(len(self.book_list_science)):
            if search_book in self.book_list_science[i][1]:
                print('The searching book is:\n')
                print(self.book_list_science[i])
            else:
                new_book_list_science.append(self.book_list_science[i])
        print(new_book_list_science)
        return new_book_list_science

    def book_information(self):
        pass

    def delete_tech_book(self, d: List):
        search_book = input('Please enter the name of the technical book to delete\n')
        self.book_list_tech = d
        del_index = -1
        for i in range(len(self.book_list_tech)):
            if search_book in self.book_list_tech[i][0]:
                print('The searching book is:\n')
                print(self.book_list_tech[i])
                del_index = i
            else:
                print('There is no such a book to delete\n')
        if del_index != -1:
            self.book_list_tech.pop(del_index)
        print(self.book_list_tech)

    def delete_science_book(self, d: List):
        search_book = input('Please enter the name of the science book to delete\n')
        self.book_list_science = d
        del_index = -1
        for i in range(len(self.book_list_science)):
            if search_book in self.book_list_science[i][0]:
                print('The searching book is:\n')
                print(self.book_list_science[i])
                del_index = i
            else:
                print('There is no such a book to delete')
        if del_index != -1:
            self.book_list_science.pop(del_index)
        print(self.book_list_science)
