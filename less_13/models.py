from sqlalchemy import (
    Column, String, SmallInteger, BINARY, CHAR, DATE, BLOB, TEXT, REAL, Integer
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'

    category_id = Column(SmallInteger, primary_key=True)
    category_name = Column(String(15), nullable=False)
    description = Column(String)
    picture = Column(BINARY)

    def as_dict(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'description': self.description,
        }

    def __repr__(self):
        return f"category_id={self.category_id}, category_name={self.category_name}, description={self.description}"


class Customers(Base):
    __tablename__ = 'customers'

    customer_id = Column(CHAR, primary_key=True, nullable=False)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))

    def as_dict(self):
        return {
            'customer_id': self.customer_id,
            'company_name': self.company_name,
            'contact_name': self.contact_name,
            'contact_title': self.contact_title,
            'address': self.address,
            'city': self.city,
            'region': self.region,
            'postal_code': self.postal_code,
            'country': self.country,
            'phone': self.phone,
            'fax': self.fax
        }

    def __repr__(self):
        return f'customer_id={self.customer_id}, company_name={self.company_name}, contact_name={self.contact_name}, ' \
               f'contact_title={self.contact_title}, address={self.address}, city={self.city}, region={self.region}, ' \
               f'postal_code={self.postal_code}, country={self.country}, phone={self.phone}, fax={self.fax}'


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(SmallInteger, primary_key=True, nullable=False)
    last_name = Column(String(20), nullable=False)
    first_name = Column(String(10), nullable=False)
    title = Column(String(30))
    title_of_courtesy = Column(String(25))
    birth_date = Column(DATE)
    hire_date = Column(DATE)
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    home_phone = Column(String(24))
    extension = Column(String(4))
    photo = Column(BLOB)
    notes = Column(TEXT)
    reports_to = Column(SmallInteger)
    photo_path = Column(String(255))

    def as_dict(self):
        return {
            'employee_id': self.employee_id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'title': self.title,
            'title_of_courtesy': self.title_of_courtesy,
            'birth_date': self.birth_date,
            'hire_date': self.hire_date,
            'address': self.address,
            'city': self.city,
            'region': self.region,
            'postal_code': self.postal_code,
            'country': self.country,
            'home_phone': self.home_phone,
            'extension': self.extension,
            'photo': self.photo,
            'notes': self.notes,
            'reports_to': self.reports_to,
            'photo_path': self.photo_path
        }

    def __repr__(self):
        return f'employee_id={self.employee_id}, last_name={self.last_name}, first_name={self.first_name}, ' \
               f'title={self.title}, title_of_courtesy={self.title_of_courtesy}, birth_date={self.birth_date}, ' \
               f'hire_date={self.hire_date}, address={self.address}, city={self.city}, region={self.region}, ' \
               f'postal_code={self.postal_code}, country={self.country}, home_phone={self.home_phone}' \
               f'extension={self.extension}, photo={self.photo}, notes={self.notes}, reports_to={self.reports_to}, ' \
               f'photo_path={self.photo_path} '


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(SmallInteger, primary_key=True)
    customer_id = Column(CHAR)
    employee_id = Column(SmallInteger)
    order_date = Column(DATE)
    required_date = Column(DATE)
    shipped_date = Column(DATE)
    ship_via = Column(SmallInteger)
    freight = Column(REAL)
    ship_name = Column(String(40))
    ship_address = Column(String(60))
    ship_city = Column(String(15))
    ship_region = Column(String(15))
    ship_postal_code = Column(String(10))
    ship_country = Column(String(15))

    def as_dict(self):
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'employee_id': self.employee_id,
            'order_date': self.order_date,
            'required_date': self.required_date,
            'shipped_date': self.shipped_date,
            'ship_via': self.ship_via,
            'freight': self.freight,
            'ship_name': self.ship_name,
            'ship_address': self.ship_address,
            'ship_city': self.ship_city,
            'ship_region': self.ship_region,
            'ship_postal_code': self.ship_postal_code,
            'ship_country': self.ship_country
        }

    def __repr__(self):
        return f'order_id={self.order_id}, customer_id={self.customer_id}, employee_id={self.employee_id}, ' \
               f'order_date={self.order_date}, required_date={self.required_date}, shipped_date={self.shipped_date}, ' \
               f'ship_via={self.ship_via}, freight={self.freight}, ship_name={self.ship_name},' \
               f'ship_address={self.ship_address}, ship_city={self.ship_city}, ship_region={self.ship_region},' \
               f'ship_postal_code={self.ship_postal_code}, ship_country={self.ship_country}'


class Shippers(Base):
    __tablename__ = 'shippers'

    shipper_id = Column(SmallInteger, primary_key=True, nullable=False)
    company_name = Column(String(40), nullable=False)
    phone = Column(String(24))

    def as_dict(self):
        return {
            'shipper_id': self.shipper_id,
            'company_name': self.company_name,
            'phone': self.phone,
        }

    def __repr__(self):
        return f"shipper_id={self.shipper_id}, company_name={self.company_name}, phone={self.phone}"


class Products(Base):
    __tablename__ = 'products'

    product_id = Column(SmallInteger, primary_key=True, nullable=False)
    product_name = Column(String(20), nullable=False)
    supplier_id = Column(SmallInteger)
    category_id = Column(SmallInteger)
    quantity_per_unit = Column(String(20))
    unit_price = Column(REAL)
    units_in_stock = Column(SmallInteger)
    units_on_order = Column(SmallInteger)
    reorder_level = Column(SmallInteger)
    discontinued = Column(Integer, nullable=False)

    def as_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'supplier_id': self.supplier_id,
            'category_id': self.category_id,
            'quantity_per_unit': self.quantity_per_unit,
            'unit_price': self.unit_price,
            'units_in_stock': self.units_in_stock,
            'units_on_order': self.units_on_order,
            'reorder_level': self.reorder_level,
            'discontinued': self.discontinued
        }

    def __repr__(self):
        return f'product_id={self.product_id}, product_name={self.product_name}, supplier_id={self.supplier_id}, ' \
               f'category_id={self.category_id}, quantity_per_unit={self.quantity_per_unit},' \
               f'unit_price={self.unit_price}, units_in_stock={self.units_in_stock},' \
               f'units_on_order={self.units_on_order}, reorder_level={self.reorder_level},' \
               f'discontinued={self.discontinued}'


class Suppliers(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(SmallInteger, primary_key=True, nullable=False)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))
    homepage = Column(TEXT)

    def as_dict(self):
        return {
            'supplier_id ': self.supplier_id,
            'company_name': self.company_name,
            'contact_name': self.contact_name,
            'contact_title': self.contact_title,
            'address': self.address,
            'city': self.city,
            'region': self.region,
            'postal_code': self.postal_code,
            'country': self.country,
            'phone': self.phone,
            'fax': self.fax,
            'homepage': self.homepage
        }
