''' Quản lý danh sách mua sắm
o Mô tả: Xây dựng một chương trình cho phép người dùng thêm, xóa, sửa
các mặt hàng trong danh sách mua sắm.
o Áp dụng: Sử dụng vòng lặp, câu điều kiện, và thao tác với file JSON hoặc
CSV để lưu trữ danh sách.'''
import csv
import json



class MatHang:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def show(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }
class MuaSam:
    def __init__(self,path):
        self.path = path
        self.gioHang = {}
    def save(self):
        try:
            with open(self.path,'w',encoding="utf-8") as file:
                json.dump(self.gioHang,file,indent=4)
        except FileNotFoundError as e:
            print('lỗi lưu file',e)
    def load(self):
        try:
            with open(self.path,'r') as file:
                json.load(file)
        except FileNotFoundError as e:
            print('lối đọc file',e)
    def add(self,matHang):
        i = len(self.gioHang)
        self.gioHang[i] = matHang.show()
    def get(self):
        self.load()
        return self.gioHang
    def remove (self,name):
        for i in self.gioHang:
            if self.gioHang[i]['name'] == name:
                del self.gioHang[i]
                return True
        return False
    def update(self,id,matHang):
        if id in self.gioHang:
            self.gioHang[id] = matHang.show()
# Ví dụ sử dụng
path = "gio_hang.json"
mua_sam = MuaSam(path)

# Thêm mặt hàng mới
mat_hang1 = MatHang("Tao", 10, 2.5)
mua_sam.add(mat_hang1)

# Hiển thị giỏ hàng
print("Giỏ hàng hiện tại:", mua_sam.get())

# Lưu giỏ hàng vào file
mua_sam.save()

# Xóa một mặt hàng
# mua_sam.remove("Tao")

# Cập nhật mặt hàng
mat_hang2 = MatHang("Chuối", 5, 1.5)
mua_sam.update(0, mat_hang2)

# Lưu sau khi cập nhật
mua_sam.save()

print("Giỏ hàng sau khi cập nhật:", mua_sam.get())



