from qlnv import EmployeeManager
from employee import Employee
manager = EmployeeManager("qlnv.db")
emp = Employee("Đạt", "0123456789", "example@gmail.com", "code dạo", 1000)
# manager.add(emp)
# manager.delete("Nguyen Van A")
manager.update(employee=emp)