class Employee:
    def __init__(self, employee_id ,f_name, l_name, birth_day, birth_month, birth_year, position, graduation):
        self.employee_id = e_id
        self.first_name = f_name
        self.last_name = l_name
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.position = position
        self.graduation = graduation


    def print_details(self):
        print(f"Employee Id : {employee_id}")
        print(f"First Name  : {first_name}")
        print(f"Last name is .{last_name}")
        print(f"Birth day is .{birth_day}")
        print(f"Birth month is .{birth_month}")
        print(f"birth year is .{birth_year}")
        print(f"position is .{position}")
        print(f"graduation is .{graduation}")


class EmployeeManager:
    def __init__(self):
        self.employee_dict = {}

    def add_employee(self):
        e_id = input(f"Please Enter Employee Id  :")
        f_name = input(f"Please Enter First Name:")
        l_name = input(f"Please Enter Last Name:")
        birth_day = input(f"Please Enter Employee birth day:")
        birth_month = input(f"Please Enter Employee birth month:")
        birth_year = input(f"Please Enter Employee birth year:")
        position = input(f"Please Enter Employee position:")
        graduation = input(f"Please Enter Employee graduation:")

        self.employee_dict[e_id] = Employee(e_id, f_name, l_name, birth_day, birth_month, birth_year, position, graduation)

    def remove_employee(self):
        e_id = input(f"Please Enter Employee Id  :")
        self.employee_dict.pop(e_id, None)

    def total_employee(self):
        print("Total Employees : " + str(len(self.employee_dict.keys())))


if __name__ == "__main__":
    employee_manager = EmployeeManager()
    while True:
        print("Select from the following option -")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Total employees")

        user_choice = int(input("select 1,2,3 : "))

        if user_choice == 1:
            employee_manager.add_employee()
        elif user_choice == 2:
            employee_manager.remove_employee()
        elif user_choice == 3:
            employee_manager.total_employee()
        else:
            print("Invalid choice !!")

        next_entry = input("Next selection? (yes/no): ")
        if next_entry == "no":
            break