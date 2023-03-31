# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):

        super().display_info()
        print("Department:", self.department)


class Engineer(Employee):

    def __init__(self, name, salary, skill):
        super().__init__(name, salary)
        self.skill = skill

    def display_info(self):
        super().display_info()
        print("Skill:", self.skill)


employee1 = Employee("Arhan", 5000)
manager1 = Manager("Shanbin", 7000, "Marketing")
engineer1 = Engineer("Matthew", 6000, "Python")


employee1.display_info()  
manager1.display_info()  
engineer1.display_info()  