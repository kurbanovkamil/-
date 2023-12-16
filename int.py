from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Подключение к базе данных
conn = sqlite3.connect('школа.db')
cursor = conn.cursor()

# Маршрут для отображения списка учеников
@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('students.html', students=students)

# Маршрут для отображения списка учителей
@app.route('/teachers')
def teachers():
    cursor.execute("SELECT * FROM teachers")
    teachers = cursor.fetchall()
    return render_template('teachers.html', teachers=teachers)

if __name__ == '__main__':
    app.run(debug=True)