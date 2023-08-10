from main_menu_options import MAIN_MENU_OPTIONS


def print_user_options():

    for i, option in enumerate(MAIN_MENU_OPTIONS, start=1):
        print(f"#{i} {option}")


def current_list_books(book_tech_list, book_science_list):
    print(f"Current technical book list: {book_tech_list}")
    print(f"Current science book list: {book_science_list}")


def try_except_condition() -> int:
    while True:
        try:
            select_option = int(input('Please select your option\n'))
            break
        except ValueError:
            print('Not a number')
            print('Try again')

    return select_option

