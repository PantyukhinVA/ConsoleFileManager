import random

stars = {'Name1': '01.02.2000',
         'Name2': '02.03.1987',
         'Name3': '03.04.2001',
         'Name4': '05.05.2002',
         'Name5': '06.06.1995',
         'Name6': '07.07.2000',
         'Name7': '06.08.1987',
         'Name8': '03.03.2001',
         'Name9': '10.03.2002',
         'Name10': '09.03.1995',
         }

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
          'Декабрь']
days = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое', 7: 'седьмое', 8: 'восьмое',
        9: 'девятое', 10: 'десятое'}


def get_game_stars():
    game_stars = random.sample(stars.keys(), 5)
    game_stars = {k: v for k, v in stars.items() if k in game_stars}

    return game_stars


def game():
    while True:
        countCorrect = 0

        game_stars = get_game_stars()

        for star in game_stars:
            date_birthday = input('Введите дату рождения (dd.mm.yyyy): ' + star + ': ')

            if (date_birthday in game_stars.values()):
                day, month, year = date_birthday.split('.')
                countCorrect += 1
                print(f'{days[int(day)]} {months[int(month) - 1]} {year}')
            else:
                print(date_birthday)

        print('Количество правильных ответов: ' + str(countCorrect))
        print('Количество ошибок: ' + str(len(game_stars) - countCorrect))

        print('Процент правильных ответов: ' + str((countCorrect * 100) / len(stars)))
        print('Процент неправильных ответов: ' + str(
            ((len(game_stars) - countCorrect) * 100) / len(game_stars) - countCorrect))

        if (input('Хотите начать игру сначала?: да/нет: ') != 'да'):
            break
