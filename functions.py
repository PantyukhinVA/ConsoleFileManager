import os
import shutil
import platform

__curDir = os.getcwd()


def get_cur_dir():
    return __curDir


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def correct_name(name):
    return __curDir + '\\' + name


def create_new_dir():
    name = input('Введите наименование новой папки: ')
    path = correct_name(name)
    if os.path.exists(path):
        return 'Папка уже существует на диске!'

    os.mkdir(path)
    return f'Папка {name} успешно создана!'


def del_file_or_dir():
    name = input('Введите наименование удаляемого файла/папки: ')
    path = correct_name(name)

    if os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
            return f'Папка {name} успешкно удалена!'
        elif os.path.isfile(path):
            os.remove(path)
            return f'Файл {name} успешно удален!'
    else:
        return 'Файл/папка отсутствую на диске!'


def change_work_dir():
    name = input('Введите путь к рабочей дирректории: ')

    if os.path.exists(name) and os.path.isdir(name):
        __curDir = name
        return 'Рабочая дирректория успешно изменена!'
    else:
        return 'Ошибка смены рабочей дирректории.1'


def copy_file_dir():
    name = input('Введите наименование (файла/папки для копирования: ')
    new_name = input('Введите новое имя файла/папки): ')

    if not os.path.exists(correct_name(name)):
        return 'Ффайл/папка отсутствует на диске!'

    if os.path.isdir(correct_name(name)):
        shutil.copytree(correct_name(name), correct_name(new_name))
    else:
        shutil.copy(correct_name(name), correct_name(new_name))

    return 'Файл/папка успешно скопирован!'


def dir_info(p=0):
    # 0 - Все файлы и папки; 1-только папки; 2 - только файлы
    res = ''

    for address, dirs, files in os.walk(get_cur_dir()):
        if p == 0 or p == 2:
            for name in files:
                res += os.path.join(address, name) + '\n'
        if p == 0 or p == 1:
            for name in dirs:
                res += os.path.join(address, name) + '\n'

    return res


def os_info():
    return platform.system()

