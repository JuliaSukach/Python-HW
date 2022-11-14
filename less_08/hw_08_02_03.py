# Добавить в Employee атрибут класса department = None
# Унаследовать от Employee класс TechnicalStaff в котором реализовать метод класса change_department, позволяющий
# менять департамент
# Добавить в свойство info данные о департаменте

# Добавить в TechnicalStaff статичный метод get_info(employee), получающий данные от работника и если работник из того же
# департамента - выдавать приветствие.

from hw_08_01 import Employee


class TechnicalStaff(Employee):
    department = 'Practical medicine'

    @staticmethod
    def get_info(employee):
        if TechnicalStaff.department == employee.department:
            return 'hi'
        return 'You are from different department'


first_employee = Employee('Yulia', 'Sukach', 24, 'someone')
assert first_employee.info['fullname'] == 'Yulia Sukach'
assert first_employee.info['age'] == 24


first_employee.change_department('Preventive medicine')


second_employee = TechnicalStaff('Alesia', 'Ivanova', 25, 'dentist')
assert second_employee.info['fullname'] == 'Alesia Ivanova'
assert second_employee.info['age'] == 25

assert TechnicalStaff.get_info(first_employee) == 'You are from different department'

second_employee.change_department('Preventive medicine')

assert TechnicalStaff.get_info(first_employee) == 'hi'




