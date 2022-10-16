# Создать класс Employee.
# Конструктор принимает first_name, last_name, age, profession.
# Person должен иметь свойство onboarding_time (выставляется по-умолчанию при создании объекта)
# Person должен иметь свойство info, возвращающее словарь
# {
#     "fullname": полное_имя работника,
#     "age": возраст работника,
#     "working_time": количество времени, которое прошло с момента onboarding_time
# }

from datetime import datetime


class Person:
    onboarding_time = datetime.now()

    @property
    def info(self):
        return {
            'fullname': f'{self.first_name} {self.last_name}',
            'age': self.age,
            "working_time": (datetime.now() - Person.onboarding_time).total_seconds() * 1000,
            "department": Employee.department
        }


class Employee(Person):
    department = None

    def __init__(self, first_name: str, last_name: str, age: int, profession: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession


first_employee = Employee('Yulia', 'Sukach', 24, 'someone')
assert first_employee.info['fullname'] == 'Yulia Sukach'
assert first_employee.info['age'] == 24
assert first_employee.info['department'] is None
