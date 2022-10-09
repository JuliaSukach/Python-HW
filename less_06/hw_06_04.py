# Прочитать сохраненный json-файл и записать данные на диск в cvs-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон"
import csv
import json
from hw_06_03 import generate_id

columns = ['name', 'age', 'phone']

with open('data.json') as f:
    templates = json.load(f)

csv_file = open('data.csv', 'w')
with csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)
    for section, row in templates.items():
        row.append(generate_id())
        writer.writerow(row)

csv_file.close()

