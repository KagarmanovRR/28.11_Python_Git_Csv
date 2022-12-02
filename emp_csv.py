import csv

csv_file = []
csv_file_otch = []

# Открываю csv файл
def file_open():
    global csv_file
    # newline нужен для внешнего фала. delimiter - разделитель
    with open('data.csv', "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
    print('Файл открыт. Записей:', len(csv_file))

# Добавление данных
def insert(fio, gender, age, tel, email, group, kurs):
    global csv_file
    try:
        mx = max(csv_file, key=lambda x: int(x['студбилет']))
        csv_file.append({'студбилет': int(mx['студбилет']) + 1, 'ФИО': fio, 'пол': gender, 'возраст': age, 'телефон': tel, 'почта': email, 'группа': group, 'курс': kurs})
    except Exception as e:
        return f'Ошибка при добавленнии новой записи {e}'
    return "Данные добавлены."

# Перевод студентов на следующий курс
def perevod():
    global csv_file
    global csv_file_otch
    try:
        for el in csv_file:
            el["курс"] += 1;
            if el["курс"] == 5:
                mx = max(csv_file_otch, key=lambda x: int(x['студбилет']))
                csv_file_otch.append(
                    {'студбилет': int(mx['студбилет']) + 1, 'ФИО': el["ФИО"], 'пол': el["пол"], 'возраст': el["возраст"], 'телефон': el["телефон"],
                     'почта': el['почта'], 'группа':  el['группа'], 'курс': el['курс']})
                drop_by_arg(el["курс"], col_name='студбилет')
            else:
                mx = max(csv_file, key=lambda x: int(x['студбилет']))
                csv_file_otch.append(
                    {'студбилет': int(mx['студбилет']) + 1, 'ФИО': el["ФИО"], 'пол': el["пол"],
                     'возраст': el["возраст"], 'телефон': el["телефон"],
                     'почта': el['почта'], 'группа': el['группа'], 'курс': el['курс']})
                drop_by_arg(el["курс"], col_name='студбилет')

    except Exception as e:
        return f'Ошибка при добавленнии новой записи {e}'
    return "Данные добавлены."

# Вывод данных
def show_csv():
    if len(csv_file) == 0:
        print(type(csv_file))
    else:
        for el in csv_file:
            if ((el['пол']) == 'м'):
                print(f'Студент: {el["ФИО"]} в группе {el["группа"]} на {el["курс"]} курсе, номер студ.билета: {el["студбилет"]}')
            else:
                print(f'Студентка: {el["ФИО"]} в группе {el["группа"]} на {el["курс"]} курсе, номер студ.билета: {el["студбилет"]}')
    show_csvotc()

def show_csvotc():
    for el in csv_file_otch:
        if ((el['пол']) == 'м'):
            print(f'Студент: {el["ФИО"]} в группе {el["группа"]} на {el["курс"]} курсе, номер студ.билета: {el["студбилет"]}')
        else:
            print(f'Студентка: {el["ФИО"]} в группе {el["группа"]} на {el["курс"]} курсе, номер студ.билета: {el["студбилет"]}')


# Сохранение
def save():
    with open('data.csv', "w", encoding="utf-8", newline="") as file:
        columns = ['студбилет', 'ФИО', 'пол', 'возраст', 'телефон', 'почта', 'группа', 'курс']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print("Данные добавлены в файл")

# Удалить по аргументу
def drop_by_arg(val, col_name='студбилет'):
    global csv_file
    try:
        csv_file = list(filter(lambda x: x[col_name] != val, csv_file))
        save()
    except Exception as e:
        return f'Строка со значением {val} поля {col_name} не найдена'
    return (f'Строка со значением "{val}" столбца "{col_name}" удалена.')

# Поиск
def find(val, col_name='ФИО'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)))

# Вывести ФИО студентов из указанной группы
def group(val, col_name='группа'):
    print(*list(filter(lambda x: x[col_name] == val, csv_file)), sep='\n')

# Вывести студентов старше 18 лет
def age18():
    print(*list(filter(lambda x: int(x['возраст']) > 18, csv_file)), sep='\n')
