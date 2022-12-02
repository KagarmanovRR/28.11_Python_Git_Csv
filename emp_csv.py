import csv

csv_file = []

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

# Вывод данных
def show_csv():
    if len(csv_file) == 0:
        print(type(csv_file))
    else:
        print('{:<10}{:<20}{:<5}{:<8}{:<15}{:<20}{:<10}{:<5}'.format(
            'студбилет', 'ФИО', 'пол', 'возраст', 'телефон', 'почта', 'группа', 'курс',
        ))
        for el in csv_file:
            print('{:<10}{:<20}{:<5}{:<8}{:<15}{:<20}{:<10}{:<5}'.format(el["студбилет"],
                                                        el["ФИО"],
                                                        el["пол"],
                                                        el["возраст"],
                                                        el["телефон"],
                                                        el['почта'],
                                                        el['группа'],
                                                        el['курс']))

# Сохранение
def save():
    with open('data.csv', "w", encoding="utf-8", newline="") as file:
        columns = ['студбилет', 'ФИО', 'пол', 'возраст', 'телефон', 'почта', 'группа', 'курс']
        writer = csv.DictWriter(file, delimiter=";", fieldnames=columns)
        writer.writeheader()
        writer.writerows(csv_file)
        print("Данные добавлены в файл")