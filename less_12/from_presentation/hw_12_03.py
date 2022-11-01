# сделать связь таблиц

import sqlite3

conn = sqlite3.connect('hwtable.sqlite')
cur = conn.cursor()


def create_connection_with_join_method():
    cur.execute(
        f"""
        SELECT students.name, students.age, auditoriums.subject, auditoriums.aud_num
        FROM auditoriums
        INNER JOIN students ON students.specialty = auditoriums.subject
        """
    )
    return cur.fetchall()


assert create_connection_with_join_method() == [('Nika', 17, 'math', 101), ('Yulia', 18, 'math', 101), ('Alex', 19, 'chemistry', 300)]


def create_connection_with_where_method():
    cur.execute(
        f"""
        SELECT students.name, students.age, auditoriums.subject, auditoriums.aud_num
        FROM students, auditoriums
        WHERE students.specialty = auditoriums.subject;
        """
    )
    return cur.fetchall()


assert create_connection_with_where_method() == [('Yulia', 18, 'math', 101), ('Alex', 19, 'chemistry', 300),
                                          ('Nika', 17, 'math', 101)]
