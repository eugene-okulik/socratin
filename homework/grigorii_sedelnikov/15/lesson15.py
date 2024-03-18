import mysql.connector as mysql

db = mysql.connect(
    user='',
    passwd='',
    host='',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

# Создание студента и возврат его id
cursor = db.cursor()
name = "Тест"
second_name = "Тестович"
cursor.execute(f"INSERT INTO st4.students (name, second_name) VALUES('{name}', '{second_name}')")
global_id = cursor.lastrowid
print(global_id)
db.commit()

# Создание книги
book_name = ["Тестовая книга", "Тестовая книга 2"]
cursor.execute(f"INSERT INTO st4.books (title, taken_by_student_id) VALUES('{book_name[0]}', '{global_id}')")
cursor.execute(f"INSERT INTO st4.books (title, taken_by_student_id) VALUES('{book_name[1]}', '{global_id}')")
db.commit()

# Создание группы и прикрепление студента к группе
book_name = ["Тестовая книга", "Тестовая книга 2"]
cursor.execute(
    f"INSERT INTO st4.groups (title, start_date, end_date) VALUES('тестировщики 2024', '2024-01-01', '2024-12-31')")
id_group = cursor.lastrowid
cursor.execute(f"UPDATE st4.students SET group_id = {id_group} WHERE id = {global_id}")
db.commit()

# Создание учебных предметов
subjects = ["НАукография", "Наукология"]
cursor.execute(f"INSERT INTO st4.subjets (title) VALUES('{subjects[0]}')")
subjects_id_1 = cursor.lastrowid
cursor.execute(f"INSERT INTO st4.subjets (title) VALUES('{subjects[1]}')")
subjects_id_2 = cursor.lastrowid
db.commit()

# Создание занятия
names_lessons = ["Урок 56472", "Урок 56473"]
cursor.execute(f"INSERT INTO st4.lessons (title, subject_id) VALUES('{names_lessons[0]}', {subjects_id_1})")
lesson_id_1 = cursor.lastrowid
cursor.execute(f"INSERT INTO st4.lessons (title, subject_id) VALUES('{names_lessons[1]}', {subjects_id_2})")
lesson_id_2 = cursor.lastrowid
db.commit()

# Ставлю оценки
cursor.execute(f"INSERT INTO st4.marks (value, lesson_id, student_id) VALUES(200, {lesson_id_1}, {global_id})")
cursor.execute(f"INSERT INTO st4.marks (value, lesson_id, student_id) VALUES(200, {lesson_id_2}, {global_id})")
db.commit()

# Показать оценки студента
cursor.execute(f"select * from st4.marks where student_id = {global_id}")
results = cursor.fetchall()
for rom in results:
    print(rom)

# Показать книги у студента

cursor.execute(f"select * from st4.books where taken_by_student_id = {global_id}")
results = cursor.fetchall()
for rom in results:
    print(rom)

# Все что есть о студенте в базе
cursor.execute(f"select * from st4.students "
               f"Join st4.books on st4.students.id = st4.books.taken_by_student_id "
               f"Join st4.groups on st4.students.group_id = st4.groups.id "
               f"Join st4.subjets on st4.books.title = st4.subjets.title "
               f"Join st4.lessons on st4.subjets.id = st4.lessons.subject_id "
               f"Join st4.marks on st4.lessons.id = st4.marks.lesson_id "
               f"where students.id = {global_id}")
final = cursor.fetchall()
for rom in final:
    print(rom)
