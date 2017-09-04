# Defining class department
class Department:
    def __init__(self, *managers):
        self.managers = managers

    def give_salary(self):
        for each in self.managers:
            for person in each.list_employees:
                print(person.first_name + ' ' + person.second_name + ': got salary ' + str(person.get_salary()))
        for manager in self.managers:
            print(manager.first_name + ' ' + manager.second_name + ': got salary ' + str(manager.get_salary()))


# Defining the Employee class
class Employee:
    def __init__(self, first_name, second_name, salary, experience, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        self.manager = manager

    def __repr__(self):
        return self.first_name + ' ' + self.second_name + ' manager: ' + self.manager.first_name + ' ' + self.manager.second_name + ' experience: ' + str(
            self.experience)

    def get_salary(self):
        if self.experience > 5:
            self.salary = self.salary * 1.2 + 500
        elif self.experience > 2:
            self.salary += 200
        return self.salary


# Class Developer inherited from Employee
class Developer(Employee):
    pass


# Class Designer inherited from Employee
class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experience, manager, coefficient):
        super().__init__(first_name, second_name, salary, experience, manager)
        if self.experience > 5:
            self.salary = self.salary * 1.2 + 500
        elif self.experience > 2:
            self.salary += 200
        self.coefficient = coefficient

    def get_salary(self):
        return self.salary * self.coefficient


# Class Manager inherited from Employee
class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experience, manager, list_employees=None):
        super().__init__(first_name, second_name, salary, experience, manager)
        if list_employees is None:
            self.list_employees = []
        else:
            self.list_employees = list_employees

    def get_salary(self):
        counter = 0
        if self.experience > 5:
            self.salary = self.salary * 1.2 + 500
        elif self.experience > 2:
            self.salary += 200
        if len(self.list_employees) > 10:
            self.salary += 500
        elif len(self.list_employees) > 5:
            self.salary += 200
        for body_type in self.list_employees:
            if type(body_type) is Developer:
                counter += 1
        if counter > len(self.list_employees) // 2:
            self.salary = self.salary * 1.1
        return self.salary


Tony = Manager('Tony', 'Stark', 9000, 3, None, None)
Bruce = Manager('Bruce', 'Wayne', 10000, 4, None, None)
Diana = Developer('Diana', 'Prince', 5000, 6, Bruce)
Barry = Developer('Barry', 'Allen', 4000, 4, Bruce)
Mark = Designer('Mark', 'Ruffalo', 600, 3, Tony, 2)
Bruce = Manager('Bruce', 'Wayne', 10000, 4, None, [Diana, Barry])
Tony = Manager('Tony', 'Stark', 9000, 3, None, [Mark])

myDep = Department(Bruce, Tony)
myDep.give_salary()

print(Diana)
