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
    query = ("SELECT * FROM st4.students "
             "JOIN st4.books ON st4.students.id = st4.books.taken_by_student_id "
             "JOIN st4.groups ON st4.students.group_id = st4.groups.id "
             "JOIN st4.subjets ON st4.books.title = st4.subjets.title "
             "JOIN st4.lessons ON st4.subjets.id = st4.lessons.subject_id "
             "JOIN st4.marks ON st4.lessons.id = st4.marks.lesson_id "
             "WHERE students.name = %s "
             "AND students.second_name = %s "
             "AND groups.title = %s "
             "AND books.title = %s "
             "AND subjets.title = %s "
             "AND lessons.title = %s "
             "AND marks.value = %s")
    cursor.execute(query, (value[0], value[1], value[2], value[3], value[4], value[5], int(value[6])))
    if cursor.lastrowid == 0:
        print(key, value)
