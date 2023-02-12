balance = 0
purchase_history = {}


def add_balance(bal):
    bal += int(input('Введите сумму пополнения : '))


def buy(bal):
    purchase = input('Введите покупку: ')
    cost = int(input('Стоимость? '))

    if bal < cost:
        print('На балансе не достаточно средств!')
    else:
        bal -= cost

    purchase_history[purchase] = cost


def print_hist():
    print('История покупок: ')
    print(purchase_history)


def work_with_sc():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            add_balance(balance)
        elif choice == '2':
            buy(balance)
        elif choice == '3':
            print_hist()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')