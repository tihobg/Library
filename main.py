from class_books import Books
from class_library import Library
from ui import print_user_options, current_list_books
from enum_lib_name import LibName

b = Books()
lib_class = Library()
lib_class1 = Library()
res_new_book_tech_list = []
res_new_book_science_list = []
l_lib = LibName
l_name = LibName
tech_dict = {
    l_lib.TECHNICAL.value: res_new_book_tech_list,
    l_lib.SCIENCE.value: res_new_book_science_list
}

print_user_options()
select_option = int(input('Please select your option\n'))
while 1 <= select_option <= 7:
    if select_option == 1:
        current_list_books(res_new_book_tech_list, res_new_book_science_list)
        res_new_book_tech_list = b.define_book_tech(res_new_book_tech_list)
        print(len(res_new_book_tech_list))
        print(f"New technical list book is: {res_new_book_tech_list}")
        add_book_question = input('Do you want to add a new Book (Yes / No)?\n')
        print(add_book_question)
        while add_book_question != 'Yes' and add_book_question != 'No':
            add_book_question = input('Please, answer correctly: Yes / No\n')
        if add_book_question == 'Yes':
            select_option = 1
        else:
            select_option = int(input('Please select your option\n'))
# select_option = int(input('Please select your option\n'))
    if select_option == 2:
        current_list_books(res_new_book_tech_list, res_new_book_science_list)

        # while select_option == 2:
        b1 = b.define_book_science(res_new_book_science_list)
        print(len(b1))
        print(f"New science list book is: {b1}")
        add_book_question = input('Do you want to add a new scientific Book (Yes / No)?\n')
        while add_book_question != 'Yes' and add_book_question != 'No':
            add_book_question = input('Please, answer correctly: Yes / No\n')
        if add_book_question == 'Yes':
            select_option = 2
        else:
            select_option = int(input('Please select your option\n'))
    if select_option == 3:
        if res_new_book_tech_list:
            current_list_books(res_new_book_tech_list, res_new_book_science_list)

            dict_tech = tech_dict[l_lib.TECHNICAL.value]
            lib_class.search_book_name_tech(dict_tech)
            add_book_question = input('Do you want to search a new technical Book (Yes / No)?\n')
            while add_book_question != 'Yes' and add_book_question != 'No':
                add_book_question = input('Please, answer correctly: Yes / No\n')
            if add_book_question == 'Yes':
                select_option = 3
            else:
                select_option = int(input('Please select your option\n'))
        else:
            select_option = int(input('The list is empty! Please select different option\n'))
    if select_option == 4:
        if res_new_book_science_list:
            current_list_books(res_new_book_tech_list, res_new_book_science_list)

            dict_scientific = tech_dict[l_lib.SCIENCE.value]
            lib_class.search_book_name_science(dict_scientific)
            add_book_question = input('Do you want to search a new scientific Book (Yew / No)?\n')
            while add_book_question != 'Yes' and add_book_question != 'No':
                add_book_question = input('Please, answer correctly: Yes / No\n')
            if add_book_question == 'Yes':
                select_option = 4
            else:
                select_option = int(input('Please select your option\n'))
        else:
            select_option = int(input('The list is empty! Please select different option\n'))
    if select_option == 5:
        if res_new_book_tech_list:
            current_list_books(res_new_book_tech_list, res_new_book_science_list)

            # dict_tech = tech_dict[l_lib.TECHNICAL.value]
            # print(dict_tech)
            # print(res_new_book_tech_list)
            lib_class.delete_tech_book(res_new_book_tech_list)
            print(f"New technical book list: {res_new_book_tech_list}")
            add_book_question = input('Do you want to delete a new tech Book (Yes / No)?\n')
            while add_book_question != 'Yes' and add_book_question != 'No':
                add_book_question = input('Please, answer correctly: Yes / No\n')
            if add_book_question == 'Yes':
                select_option = 5
            else:
                select_option = int(input('Please select your option\n'))
        else:
            select_option = int(input('The list is empty! Please select different option\n'))
    if select_option == 6:
        if res_new_book_science_list:
            current_list_books(res_new_book_tech_list, res_new_book_science_list)

            # dict_scientific = tech_dict[l_lib.SCIENCE.value]
            lib_class.delete_science_book(res_new_book_science_list)
            print(f"New science book list: {res_new_book_science_list}")
            add_book_question = input('Do you want to delete a new scientific Book (Yes / No)?\n')
            while add_book_question != 'Yes' and add_book_question != 'No':
                add_book_question = input('Please, answer correctly: Yes / No\n')
            if add_book_question == 'Yes':
                select_option = 6
            else:
                select_option = int(input('Please select your option\n'))
        else:
            select_option = int(input('The list is empty! Please select different option\n'))
    if select_option == 7:
        current_list_books(res_new_book_tech_list, res_new_book_science_list)

        lib_class.search_book_author_tech(res_new_book_tech_list)
        lib_class.search_book_author_science(res_new_book_science_list)
        # lib_class.search_book_author_tech(tech_dict[l_lib.TECHNICAL.value])
        # lib_class.search_book_author_science(tech_dict[l_lib.SCIENCE.value])
        add_book_question = input('Do you want to delete a new scientific Book (Yes / No)?\n')
        while add_book_question != 'Yes' and add_book_question != 'No':
            add_book_question = input('Please, answer correctly: Yes / No\n')
        if add_book_question == 'Yes':
            select_option = 7
        else:
            select_option = int(input('Please select your option\n'))

print(f"The technical book list is: {res_new_book_tech_list}")
print(f"The science book list is: {res_new_book_science_list}")
# print(tech_dict[l_lib.TECHNICAL.value])
# print(tech_dict[l_lib.SCIENCE.value])
# print(res_new_book_tech_list)
if select_option == 8:
    exit()


