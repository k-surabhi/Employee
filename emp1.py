class Employee:
    def __init__(self, e_id ,f_name, l_name, birth_day, birth_month, birth_year, position, graduation):
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
        f_name = self.__read_first_name()
        l_name = self.__read_last_name()
        date = self.__read_date_of_birth()
        month = self.__read_month_of_birth()
        year = self.__read_year_of_birth()

        self.employee_dict[e_id] = Employee(e_id ,f_name, l_name, birth_day, birth_month, birth_year, position, graduation)
        print("Employee Added!!")

    def remove_employee(self):
        e_id = input(f"Please Enter Employee Id  :")
        if e_id in self.employee_dict:
            self.employee_dict.pop(e_id, None)
            print("Employee Removed!!")
        else:
            print("Employee Id is not valid")

    def update_employee(self):
        e_id = input(f"Please Enter Employee Id  :")
        if e_id in self.employee_dict:
            f_name = self.__read_first_name()
            l_name = self.__read_last_name()
            date = self.__read_date_of_birth()
            month = self.__read_month_of_birth()
            year = self.__read_year_of_birth()
            self.employee_dict[e_id] = Employee(e_id, f_name, l_name, date, month, year)
            print("Employee updated!!")
        else:
            print("Employee Id is not valid")

    def total_employee(self):
        print("Total Employees : " + str(len(self.employee_dict.keys())))

    def print_all(self):
        for i in self.employee_dict:
            print("--> Employee " + str(i) + "=========")
            self.employee_dict[i].print_details()

    def find_employee(self):
        e_id = input(f"Please Enter Employee Id  :")
        if e_id in self.employee_dict:
            self.employee_dict[e_id].print_details()
        else:
            print("Employee Id is not valid")

    def __read_first_name(self):
        name_var = ""
        while True:
            name_var = input(f"Please Enter The first name:")
            if len(name_var.strip()) < 2:
                print("Error: Length of the first name should be more then 2 character ")
            else:
                break
        return name_var

    def __read_last_name(self):
        name_var = ""
        while True:
            name_var = input(f"Please Enter The last name:")
            if len(name_var.strip()) < 2:
                print("Error: Length of the last name should be more then 2 character ")
            else:
                break
        return name_var

    def __read_date_of_birth(self):
        date = 0
        while True:
            date = int(input("Please Enter date of Birth (dd):"))
            if date <= 31:
                break
        return date

    def __read_month_of_birth(self):
        month = 0
        while True:
            month = int(input("Please Enter month of Birth (MM):"))
            if month <= 12:
                break
        return month

    def __read_year_of_birth(self):
        year = 0
        while True:
            year = int(input("Please Enter year of Birth (YYYY):"))
            if year <= 2021:
                break
            else:
                print("year is incorrect")
        return year


if __name__ == "__main__":
    employee_manager = EmployeeManager()
    while True:
        print("Select from the following option -")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update employee")
        print("4. Total employees")
        print("5. Print employees")
        print("6. Find employees")

        user_choice = int(input("Select 1,2,3,4,5,6: "))

        if user_choice == 1:
            employee_manager.add_employee()
        elif user_choice == 2:
            employee_manager.remove_employee()
        elif user_choice == 3:
            employee_manager.update_employee()
        elif user_choice == 4:
            employee_manager.total_employee()
        elif user_choice == 5:
            employee_manager.print_all()
        elif user_choice == 6:
            employee_manager.find_employee()
        else:
            print("Invalid choice !!")

        next_entry = input("Next selection? (yes/no): ")
        if next_entry == "no":
            break

