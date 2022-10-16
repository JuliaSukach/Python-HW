# Добавить в Employee атрибут класса department = None
# Унаследовать от Employee класс TechnicalStaff в котором реализовать метод класса change_department, позволяющий
# менять департамент
# Добавить в свойство info данные о департаменте

# Добавить в TechnicalStaff статичный метод get_info(employee), получающий данные от работника и если работник из того же
# департамента - выдавать приветствие.

from hw_08_01 import Employee


class TechnicalStaff(Employee):
    @classmethod
    def change_department(cls, new_department):
        cls.department = new_department

    @staticmethod
    def get_info(employee):
        print()


second_employee = TechnicalStaff('Alesia', 'Ivanova', 25, 'dentist')
assert second_employee.info['fullname'] == 'Yulia Sukach'
assert second_employee.info['age'] == 24
assert second_employee.info['department'] is None
second_employee.change_department('surgeon')
assert TechnicalStaff.department == 'surgeon'
