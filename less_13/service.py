from typing import List
from config import db_conf
from session import open_db_session
from models import Categories


def hello_world():
    with open_db_session() as session:
        res = session.execute("select 'Hello, World!'").scalar()
        assert res == 'Hello, World!'


hello_world()


def get_cat_raw():
    with open_db_session() as session:
        res = session.execute('select * from categories').all()
        print(res)

get_cat_raw()


def get_cat():
    with open_db_session() as session:
        res: List[Categories] = session.query(Categories).all()
        for r in res:
            print(type(r), r.category_name)


# get_cat()


# def get_cat_by_name():
#     with open_db_session() as session:
#         res: List[Categories] = session.query(Categories).filter(Categories.category_name.in_(['Beverages'])).all()
#         for r in res:
#             print(type(r), r.category_name)
#
#
# get_cat_by_name()

def get_cat_by_name():
    with open_db_session() as session:
        # res: List[Categories] = session.query(Categories).filter(Categories.category_name == 'Beverages').all()
        res: List[Categories] = session.query(Categories)
        for r in res:
            print(type(r), r.category_name)


# get_cat_by_name()
