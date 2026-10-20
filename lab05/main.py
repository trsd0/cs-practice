from tablestats import read_rows, count_types, total_minutes, to_csv

filename = input().strip()
with open(filename, 'r', encoding='utf-8') as table:
    rows = read_rows(table)

types = count_types(rows)
error_minutes = total_minutes(rows, 'ошибка')

print(len(rows))
print(len(types))
print(error_minutes)

with open('summary.csv', 'w', encoding='utf-8') as out:
    out.write(to_csv(types))








