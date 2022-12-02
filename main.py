from emp_csv import file_open, insert, show_csv, save, drop_by_arg, find, age18, group

FILENAME = "data.csv"

MENU = {
    '1': 'Добавление нового студента',
    '2': 'Удаление студента по номеру студ. билета',
    '3': 'Поиск студента по ФИО',
    '4': 'Вывести ФИО студентов из указанной группы',
    '5': 'Перевод студентов на следующий курс',
    '6': 'Вывести студентов старше 18 лет.',
    '7': 'Вывести данные о студенте',
    '0': '<-Меню',
    'exit': 'Выход'
}

# Вывод меню пользователю
for key, val in MENU.items():
    print(key, '-', val)        # написать "номер действия" - "описание действия"
file_open()
while True:
    action = input('>_ ')
    if action == '1': # если - действие Добавление
        print(insert(input('ФИО: '), input('пол: '), int(input('возраст: ')), input('телефон: '), input('почта: '), input('группа: '), int(input('курс: '))))
        save()
    elif action == '2':  # если - действие Удаление
        val = input('Значение: ')
        print(drop_by_arg(val, col_name='студбилет'))
    elif action == '3':  # если - действие Поиск
        val = input('Значение: ')
        find(val, col_name='ФИО')
    elif action == '4':  # если - действие найти по значению
        val = input('Значение: ')
        group(val, col_name='группа')
    elif action == '5':  # если - действие ввести средний возраст
        pass
    elif action == '6':     # если - действие старше 18
        age18()
    elif action == '7':     # если - ввывести записи
        show_csv()
    elif action == '0':     # если - действие меню
        for key, val in MENU.items():
            print(key, '-', val)
    elif action == 'exit':  # если - действие выйти
        break