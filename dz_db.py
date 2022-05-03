# Создать 2 таблицы в Базе Данных.
# Одна будет хранить текстовые данные (1 колонка).
# Другая - числовые (1 колонка).
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу.
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
# если нечётное, то записать в первую таблицу слово: «нечётное».
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello».

import sqlite3

a = ['dog', 53, 33, 'table', 'work', 856, 'house']
b = 'нечётное'

conn = sqlite3.connect('dz.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1
(id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT)
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2
(id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 INTEGER)
''')
for i in a:
    if i == str(i):
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (i,))
        l = len(i)
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (l,))
    elif i == int(i):
        if int(i) % 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (int(i),))
        else:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (b,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(f'Таблица_1: {k}')
cursor.execute('''SELECT*FROM tab_2''')
t = cursor.fetchall()
print(f'Таблица_2: {t}')
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello».
if len(t) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
    conn.commit()
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = 'hello' WHERE id=1''')
    conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(f'Таблица_1: {k}')
cursor.execute('''SELECT*FROM tab_2''')
t = cursor.fetchall()
print(f'Таблица_2: {t}')
