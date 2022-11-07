# Подсчитать количество товаров в каждой категории,
# вывести по убыванию

from session import open_db_session
from models import Products
from sqlalchemy import func, desc


def count_products_in_category_raw():
    with open_db_session() as session:
        q = """
            SELECT p.category_id, SUM(p.units_in_stock) AS TotalCount
            FROM products p
            GROUP BY p.category_id
            ORDER BY p.category_id DESC 
        """
        res = session.execute(q).all()
        for r in res:
            print(r)


count_products_in_category_raw()


def count_products_in_category():
    with open_db_session() as session:
        res = session.query(
            Products.category_id, func.sum(Products.units_in_stock).label('TotalCount')
        ).group_by(
            Products.category_id
        ).order_by(
            desc(Products.category_id)
        )
        for r in res:
            print(r)


count_products_in_category()
