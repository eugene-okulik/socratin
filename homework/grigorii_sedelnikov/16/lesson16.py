import os
import dotenv
import mysql.connector as mysql

dotenv.load_dotenv(override=True)
db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

path_to_csv = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'eugene_okulik', 'Lesson_16',
                           'hw_data', 'data.csv')

file_dict = {}
with open(path_to_csv, 'r') as file:
    for line_number, line in enumerate(file, 1):
        line = line.strip()
        file_dict[line_number] = line

cursor = db.cursor(dictionary=True)
del file_dict[1]
for key, value in file_dict.items():
    value = value.split(",")
    cursor.execute(f"select * from st4.students "
                   f"Join st4.books on st4.students.id = st4.books.taken_by_student_id "
                   f"Join st4.groups on st4.students.group_id = st4.groups.id "
                   f"Join st4.subjets on st4.books.title = st4.subjets.title "
                   f"Join st4.lessons on st4.subjets.id = st4.lessons.subject_id "
                   f"Join st4.marks on st4.lessons.id = st4.marks.lesson_id "
                   f"where students.name = '{value[0]}' "
                   f"and students.second_name = {value[1]} "
                   f"and groups.title = {value[2]} "
                   f"and books.title = {value[3]} "
                   f"and subjets.title = '{value[4]}' "
                   f"and lessons.title = {value[5]} "
                   f"and marks.value = {int(value[6])}")
    if cursor.lastrowid == 0:
        print(key, value)
