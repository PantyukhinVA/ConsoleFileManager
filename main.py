from functions import *
from victory import game
from banc_schet import work_with_sc
import menu

result = ''

while True:

    cls()
    menu.show_menu()

    print(f'Результат выполнения: {result}' if result != '' else '')

    sel = input('Выберите пункт меню: ')

    if sel == '1':
        result = create_new_dir()
    elif sel == '2':
        result = del_file_or_dir()
    elif sel == '3':
        result = copy_file_dir()
    elif sel == '4':
        result = dir_info()
    elif sel == '5':
        result = dir_info(1)
    elif sel == '6':
        result = dir_info(2)
    elif sel == '7':
        result = os_info()
    elif sel == '8':
        result = 'Создатель!'
    elif sel == '9':
        cls()
        game()
    elif sel == '10':
        cls()
        work_with_sc()
    elif sel == '11':
        result = change_work_dir()
    elif sel == '0':
        break
    else:
        result = 'Повторите выбор меню!'


