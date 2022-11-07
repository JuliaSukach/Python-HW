# Найти заказчиков(customer) и обслуживающих их заказы сотрудкников(employees)
# Заказчики и сотрудники из города London, доставка осуществляется компанией Speedy Express.
# Вывести компанию заказчика и ФИО сотрудника.

from session import open_db_session
from models import Customers, Orders, Employees, Shippers
from sqlalchemy import and_


def find_customers_and_employees_from_London():
    with open_db_session() as session:
        res = session.query(Customers.company_name, Employees.first_name, Employees.last_name).join(
            Orders, Customers.customer_id == Orders.customer_id
        ).join(
            Employees, Orders.employee_id == Employees.employee_id
        ).join(
            Shippers, Orders.ship_via == Shippers.shipper_id
        ).filter(
            and_(
                Customers.city == 'London',
                Employees.city == 'London',
                Shippers.company_name == 'Speedy Express'
            )
        )
        for r in res:
            print(r)


find_customers_and_employees_from_London()


def find_customers_and_employees_from_London_raw():
    with open_db_session() as session:
        q = """
            SELECT customers.company_name, e.first_name, e.last_name
            FROM customers
            JOIN orders o
            ON customers.customer_id = o.customer_id
            JOIN employees e
            ON o.employee_id = e.employee_id
            JOIN shippers
            ON o.ship_via = shippers.shipper_id
            WHERE customers.city = 'London' AND e.city = 'London' AND shippers.company_name = 'Speedy Express'      
        """
        res = session.execute(q).all()
        for r in res:
            print(r)


find_customers_and_employees_from_London_raw()
