#сделать связь таблиц

import sqlite3

conn = sqlite3.connect('hwtable.sqlite')
cur = conn.cursor()

result = [('Yulia', 18, 'math', 101), ('Alex', 19, 'physics', 200), ('Nika', 17, 'chemistry', 300)]


def create_connection_with_join():
    cur.execute(
        f"""
        SELECT students.name, students.age, auditoriums.subject, auditoriums.aud_num
        FROM auditoriums
        LEFT JOIN students ON students.student_id = auditoriums.id
        """
    )
    return cur.fetchall()


assert create_connection_with_join() == result


def create_connection_with_where():
    cur.execute(
        f"""
        SELECT students.name, students.age, auditoriums.subject, auditoriums.aud_num
        FROM students, auditoriums
        WHERE students.student_id = auditoriums.id;
        """
    )
    return cur.fetchall()


assert create_connection_with_where() == result
