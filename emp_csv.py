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