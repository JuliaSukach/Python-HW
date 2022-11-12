# Найти активные (поле discontinued) продукты из категории Condiments и Meat/Poultry,
# которых в продаже менее 100 единиц
# Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.

from session import open_db_session
from models import Products, Suppliers, Categories
from sqlalchemy import and_, or_


def find_active_products_raw():
    with open_db_session() as session:
        q = """
            SELECT p.product_name, p.units_in_stock, s.contact_name, s.phone
            FROM products p
            JOIN suppliers s
            ON p.supplier_id = s.supplier_id
            JOIN categories c
            ON p.category_id = c.category_id
            WHERE p.discontinued = 1 AND (c.category_id = 1 OR c.category_id = 6) AND p.units_in_stock < 100 
        """
        res = session.execute(q).all()
        for r in res:
            print(r)


find_active_products_raw()


def find_active_products():
    with open_db_session() as session:
        res = session.query(Products.product_name, Products.units_in_stock, Suppliers.contact_name, Suppliers.phone
        ).join(
            Suppliers, Products.supplier_id == Suppliers.supplier_id
        ).join(
            Categories, Products.category_id == Categories.category_id
        ).filter(
            and_(
                Products.discontinued == 1,
                or_(Categories.category_id == 1, Categories.category_id == 6),
                Products.units_in_stock < 100
            )
        )
        for r in res:
            print(r)


find_active_products()
