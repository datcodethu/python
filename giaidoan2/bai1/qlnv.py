# Ứng dụng quản lý nhân viên – Sử dụng OOP, xử lý ngoại lệ và thao tác với SQL.
    # Ứng dụng "Quản lý nhân viên" sẽ thực hiện các chức năng sau:

    # Thêm mới nhân viên vào hệ thống.
    # Cập nhật thông tin nhân viên hiện có (ví dụ: tên, chức vụ, lương, phòng ban).
    # Xóa nhân viên khỏi hệ thống dựa trên mã nhân viên.
    # Tìm kiếm nhân viên dựa trên các tiêu chí như mã nhân viên hoặc tên.
    # Liệt kê danh sách nhân viên hiện có trong hệ thống.
    # Lưu trữ và truy xuất dữ liệu từ cơ sở dữ liệu SQL.
import os
import sys
import sqlite3
import logging
from employee import Employee
from ql_employee_database import ql__database
import pandas
import os
import sys
import sqlite3
import logging
from employee import Employee
from ql_employee_database import ql__database

class EmployeeManager:
    table_name = 'employee'
    def __init__(self, path):
        self.path = path
        self.database = ql__database(path)

    def add(self, employee):
        # Kiểm tra nếu đối tượng employee là instance của class Employee
        if isinstance(employee, Employee):
            try:
                # Thực hiện thêm vào database
                self.database.insert_table(
                    name_table="employee",
                    name=employee.name,
                    phone=employee.phone,
                    email=employee.email,
                    position=employee.position,
                    salary=employee.salary
                )
            except Exception as e:
                print("Không thể thêm nhân viên vào cơ sở dữ liệu.")
            else:
                print(f"Nhân viên {employee.name} đã được thêm thành công.")
        else:
            print("Bạn cần truyền vào một đối tượng nhân viên hợp lệ!")
    
    def delete(self,name):
        con = f"name = '{name}' "
        self.database.delete_table(name_table=self.table_name,condition=con)
    
    def update(self,employee):
        self.database.update_table(self.table_name,condition="name = 'Đạt'",
                    phone=employee.phone,
                    email=employee.email,
                    position=employee.position,
                    salary=employee.salary)
        
    # def getAll(self):
    #     data =self.database.getAll("employee")
    #     print(data)