

print("--- Python OOP Project: Employee Management System ---")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_dis(self):
        print(f"Person created with name: {self.name} and age: {self.age}.")

    def p_display(self):
        print("Person Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, ID, salary):
        super().__init__(name, age)
        self.__ID = ID
        self.__salary = salary

    def get_id(self):
        return self.__ID

    def set_id(self, ID):
        self.__ID = ID

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def employee_dis(self):
        print(f"Employee created with name: {self.name}, "
              f"age: {self.age}, ID: {self.get_id()}, "
              f"and salary: ${self.get_salary()}.")

    def e_display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_id())
        print("Salary:", f"${self.get_salary()}")


class Manager(Employee):

    def __init__(self, name, age, ID, salary, dep):
        super().__init__(name, age, ID, salary)
        self.dep = dep

    def manager_dis(self):
        print(f"Manager created with name: {self.name}, "
              f"age: {self.age}, ID: {self.get_id()}, "
              f"salary: ${self.get_salary()}, "
              f"and department: {self.dep}.")

    def m_display(self):
        print("Manager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_id())
        print("Salary:", f"${self.get_salary()}")
        print("Department:", self.dep)


person_list = []
employee_list = []
manager_list = []


while True:

    print("\n--- Choose an Operation ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)
        person_list.append(person)
        person.person_dis()

    elif ch == 2:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        ID = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, ID, salary)
        employee_list.append(employee)
        employee.employee_dis()

    elif ch == 3:

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        ID = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dep = input("Enter Department: ")

        manager = Manager(name, age, ID, salary, dep)
        manager_list.append(manager)
        manager.manager_dis()

    elif ch == 4:

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            if person_list:
                person_list[-1].p_display()
            else:
                print("No Person details available.")

        elif choice == 2:
            if employee_list:
                employee_list[-1].e_display()
            else:
                print("No Employee details available.")

        elif choice == 3:
            if manager_list:
                manager_list[-1].m_display()
            else:
                print("No Manager details available.")

        else:
            print("Invalid choice, Please enter between 1 to 3.")

    elif ch == 5:

        print("\nExiting the system. All resources have been freed.")
        print("Goodbye!")
        break

    else:

        print("Invalid choice, Please enter between 1 to 5.") 


        

        






