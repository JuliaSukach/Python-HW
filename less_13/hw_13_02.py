# Найти заказчиков, у которых нет ни одного заказа. Вывести имя заказчика и order_id.

from session import open_db_session
from models import Customers, Orders


# first

def find_customers_with_no_orders_raw():
    with open_db_session() as session:
        q = """
            SELECT customers.contact_name
            FROM customers
            WHERE customer_id NOT IN (SELECT customer_id FROM orders)     
        """
        res = session.execute(q).all()
        for r in res:
            print(r)


find_customers_with_no_orders_raw()


# second

def find_customers_with_no_orders_raw_using_left_join():
    with open_db_session() as session:
        q = """
            SELECT customers.contact_name FROM customers
            LEFT OUTER JOIN orders ON customers.customer_id = orders.customer_id
            WHERE orders.customer_id IS NULL  
        """
        res = session.execute(q).all()
        for r in res:
            print(r)


find_customers_with_no_orders_raw()


def find_customers_with_no_orders():
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


find_customers_with_no_orders()
