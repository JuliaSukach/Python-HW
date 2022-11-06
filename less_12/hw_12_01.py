from session import glob_cursor as cursor
from values import values


def create_department_table():
    q = """
    CREATE TABLE IF NOT EXISTS departments (
        name TEXT NOT NULL,
        manager_id INTEGER NOT NULL,
        location_id INTEGER NOT NULL,
        PRIMARY KEY(manager_id)
    );
    """
    cursor.execute(q)
    cursor.commit()

    insert_data('departments')


def insert_data(table_name):
    q = f"""
    INSERT INTO {table_name}
    VALUES (?, ?, ?)
    """
    cursor.executemany(q, values[table_name])
    cursor.commit()
    cursor.fetchall()


create_department_table()


def create_employee_table():
    q = """
    CREATE TABLE IF NOT EXISTS employee(
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone_number INTEGER NOT NULL,
        hire_date DATE,
        job_id TEXT NOT NULL,
        manager_id INTEGER NOT NULL,
        department_id INTEGER NOT NULL,
        PRIMARY KEY(first_name, last_name, phone_number)
    );
    """
    cursor.execute(q)
    cursor.commit()

    insert_data_into_employee('employee')


def insert_data_into_employee(table_name):
    q = f"""
    INSERT INTO {table_name}
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(q, values[table_name])
    cursor.commit()
    cursor.fetchall()


create_employee_table()


def create_jobs_table():
    q = """
    CREATE TABLE IF NOT EXISTS jobs(
        title TEXT PRIMARY KEY NOT NULL,
        min_salary REAL NOT NULL,
        max_salary REAL NOT NULL,
        CONSTRAINT min_salary_chk CHECK(min_salary > 0 AND min_salary < max_salary)
    );
    """
    cursor.execute(q)
    cursor.commit()

    insert_data('jobs')


create_jobs_table()


def create_location_table():
    q = """
    CREATE TABLE IF NOT EXISTS location(
        street_address TEXT NOT NULL,
        postal_code TEXT NOT NULL,
        city TEXT NOT NULL,
        department_id INTEGER PRIMARY KEY NOT NULL
    );
    """
    cursor.execute(q)
    cursor.commit()

    insert_data_into_location_table('location')


def insert_data_into_location_table(table_name):
    q = f"""
    INSERT INTO {table_name}
    VALUES (?, ?, ?, ?)
    """
    cursor.executemany(q, values[table_name])
    cursor.commit()
    cursor.fetchall()


create_location_table()


def create_countries_table():
    q = """
    CREATE TABLE IF NOT EXISTS countries(
        name TEXT NOT NULL
    );
    """
    cursor.execute(q)
    cursor.commit()

    insert_data_into_countries_table('countries')


def insert_data_into_countries_table(table_name):
    q = f"""
    INSERT INTO {table_name}
    VALUES (?)
    """
    cursor.executemany(q, values[table_name])
    cursor.commit()
    cursor.fetchall()


create_countries_table()


#update table

def update_data(table_name: str, column: str):
    q = f"""
    UPDATE {table_name}
    SET {column} = {column} + 1000
    WHERE last_name = 'BAYLEY'
    """
    cursor.execute(q)
    cursor.commit()
    cursor.fetchall()


update_data('employee', 'department_id')


#remove data

def remove_data(table_name: str, column: str):
    q = f"""
    DELETE FROM {table_name}
    WHERE {column} == 2001
    """
    cursor.execute(q)
    cursor.commit()
    cursor.fetchall()


remove_data('employee', 'department_id')


def count_employee_in_department():
    q = """
    SELECT first_name, last_name, department_id FROM employee
    WHERE department_id == 2001;
    """
    cursor.execute(q)
    data = cursor.fetchall()
    assert len(data) == 1


count_employee_in_department()

# count employees

def count_employee():
    q = """
    SELECT COUNT(*)
    FROM employee
    WHERE department_id == 3001;
    """
    cursor.execute(q)
    result = cursor.fetchall()
    assert result == [(2,)]


count_employee()


# count managers

def count_managers():
    q = """
    SELECT COUNT(*)
    FROM employee
    """
    cursor.execute(q)
    result = cursor.fetchall()
    assert result == [(4,)]


count_managers()


# count average salary

def count_average_salary():
    q = """
    SELECT AVG((min_salary + max_salary)/2) AS average_salary FROM jobs;
    """
    cursor.execute(q)
    result = cursor.fetchall()
    assert result == [(3293.75,)]


count_average_salary()


# cities in alphabetical order

def sort_cities():
    q = """
    SELECT DISTINCT location.city FROM location, employee
    WHERE employee.department_id == location.department_id
    ORDER BY location.city;
    """
    cursor.execute(q)
    result = cursor.fetchall()
    assert result == [('Roma',), ('Tokyo',)]


sort_cities()
