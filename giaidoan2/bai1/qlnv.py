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
class EmployeeManager:
    def __init__(self,path):
        self.path = path
        self.listEmployee = list()
        self.database = ql__database(path)
    
    def add(self,employee):
        self.listEmployee.append(employee)
        self.database.insert_table(name=)

        