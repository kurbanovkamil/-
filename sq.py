import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('школа.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы учеников
cursor.execute('''CREATE TABLE students
             (id INTEGER PRIMARY KEY,
              name TEXT,
              grade INTEGER)''')

# Создание таблицы учителей
cursor.execute('''CREATE TABLE teachers
             (id INTEGER PRIMARY KEY,
              name TEXT,
              subject TEXT)''')

# Вставка данных в таблицу учеников
cursor.execute("INSERT INTO students (name, grade) VALUES ('Иванов', 10)")
cursor.execute("INSERT INTO students (name, grade) VALUES ('Петров', 11)")

# Вставка данных в таблицу учителей
cursor.execute("INSERT INTO teachers (name, subject) VALUES ('Сидорова', 'Математика')")
cursor.execute("INSERT INTO teachers (name, subject) VALUES ('Васильев', 'История')")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()