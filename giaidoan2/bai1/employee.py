class Employee:
    def __init__(self,name,phone,email,position,salary):
        self.name = name
        self.phone = phone
        self.email = email
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"name: {self.name} phone: {self.phone} email: {self.email} position: {self.position} salary: {self.salary}"
    