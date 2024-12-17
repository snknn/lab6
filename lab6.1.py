import pandas as pd
import sqlite3

try:
    connection = sqlite3.connect('sqlite_python.db')
    connection.execute("""drop table if exists podarki""")
    sqlite_create_table_query = '''CREATE TABLE if not exists podarki (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                gift TEXT NOT NULL,
                                price INTEGER NOT NULL,
                                status TEXT NOT NULL);'''

    cursor = connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    connection.commit()
    print("Таблица SQLite создана")

    cursor = connection.cursor()
    print("Подключен к SQLite")

    sqlite_insert_query = """INSERT INTO podarki
                          (id, name, gift, price, status)
                          VALUES
                          (1, 'Васин Петр Андреевич', 'Кресло', 10000, "Куплен"),
                          (2, 'Попов Виталий Алексеевич', 'удочка', 1000, "Куплен"),
                          (3, 'Минин Петр Андреевич', 'кубок', 5000, "Не куплен"),
                          (4, 'Прозоров Михимл Андреевич', 'Подушка', 10000, "Не куплен"),
                          (5, 'Мамронтов Михаил Андреевич', 'Одеяло', 10000, "Куплен"),
                          (6, 'Фридман Петр Андреевич', 'Ручка', 5000, "Куплен"),
                          (7, 'Березуцкий Василий Александрович', 'Кресло', 10000, "Куплен"),
                          (8, 'Берестов Петр Андреевич', 'Монитор', 23000, "Не куплен"),
                          (9, 'Кляузин Петр Андреевич', 'Шампунь', 900, "Куплен"),
                          (10, 'Ваксин Петр Андреевич', 'Мыло', 100, "Не kуплен");"""
    count = cursor.execute(sqlite_insert_query)
    connection.commit()
    print("Запись успешно вставлена ​​в таблицу podarki ", cursor.rowcount)
    cursor.close()
    
    sql = '''SELECT * FROM podarki ;'''

    print(pd.read_sql(sql, connection))

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if connection:
        connection.close()
        print("Соединение с SQLite закрыто")


