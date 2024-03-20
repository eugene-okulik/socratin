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
    query = ("SELECT * FROM students "
             "JOIN books ON students.id = books.taken_by_student_id "
             "JOIN groups ON students.group_id = groups.id "
             "JOIN subjets"
             "JOIN lessons ON subjets.id = lessons.subject_id "
             "JOIN marks ON lessons.id = marks.lesson_id "
             "WHERE students.name = %s "
             "AND students.second_name = %s "
             "AND groups.title = %s "
             "AND books.title = %s "
             "AND subjets.title = %s "
             "AND lessons.title = %s "
             "AND marks.value = %s")
    cursor.execute(query, (value[0], value[1], value[2], value[3], value[4], value[5], int(value[6])))
    if not cursor.fetchall():
        print(key, value)
