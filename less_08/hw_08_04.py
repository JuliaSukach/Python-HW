# Есть класс Account.
# Конструктор принимает person_id (уникальный), currency (реализовать через enum) и amount (кол-во денег на счету).
# Person_id можно релазиовать через uuid4.
# Реализовать свойство amount, которое при попытке записать в значение сумму <0 - выдает ошибку (либо предупреждение и не меняет значение)
# См. getter/setter

import uuid
import enum


class Currency(enum.Enum):
    USD = 1
    EUR = 2
    ZL = 3


class Account:
    def __init__(self, currency, amount):
        if amount < 0:
            raise ValueError('First deposit must be zero or more')
        self.person_id = uuid.uuid4()
        self.currency = currency
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount < 0:
            raise ValueError(f'Amount must be positive. Got {new_amount}')
        self._amount = new_amount


create_account = Account(currency=Currency.USD.value, amount=1000)

assert create_account.amount == 1000

create_account.amount = 2000
assert create_account.amount == 2000

create_account.amount = -2000


