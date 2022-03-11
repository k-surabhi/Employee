employeeList = []


def dict_data(eId, fname, lname, date, month, year):
    return {"EmployeeId": eId, "FirstName": fname, "LastName": lname, "DateOfBirth": date, "MonthOfBirth": month,
            "YearOfBirth": year }


def read_first_name():
    name_var = ""
    while True:
        name_var = input(f"Please Enter The first name:")
        if len(name_var.strip()) < 2:
            print("Error: Length of the first name should be more then 2 character ")
        else:
            break
    return name_var


def read_last_name():
    name_var = ""
    while True:
        name_var = input(f"Please Enter The last name:")
        if len(name_var.strip()) < 2:
            print("Error: Length of the last name should be more then 2 character ")
        else:
            break
    return name_var


def read_date_of_birth():
    date = 0
    while True:
        date = int(input("Please Enter date of Birth (dd):"))
        if date <= 31:
            break
    return date


def read_month_of_birth():
    month = 0
    while True:
        month = int(input("Please Enter month of Birth (MM):"))
        if month <= 12:
            break
    return month


def read_year_of_birth():
    year = 0
    while True:
        year = int(input("Please Enter year of Birth (YYYY):"))
        if year <= 2021:
            break
        else:
            print("year is incorrect")
    return year

def emp_position():
    position = input("Employee position:")
    return position


def add_employee():
    eId = input("Enter Employee Id:")
    fname = read_first_name()
    lname = read_last_name()
    date = read_date_of_birth()
    month = read_month_of_birth()
    year = read_year_of_birth()
    position = emp_position()
    graduated = bool(input("Whether graduated or not yes/no?") == "yes")
    employeeList.append(dict_data(eId, fname, lname, date, month, year))
    print("Employee Added!!")

def remove_employee():
    eId = int(input("Enter Employee Id:"))
    for i in range(len(employeeList)):
        if int(employeeList[i]['EmployeeId']) == int(eId):
            del employeeList[i]
            break
    print("Employee Removed!!")


def total_employee():
    print("Total No of Employee : " + str(len(employeeList)))


def list_employee():
    if len(employeeList) == 0:
        print("The employee list is empty.")

    for emp in employeeList:
        print("Employee Id:" + str(emp.get("EmployeeId")))
        print("Employee Name:" + emp.get("FirstName") + " " + emp.get("LastName"))
        print("Date Of Birth (dd/mm/yyyy):" + str(emp.get("DateOfBirth")) + "/" + str(
            emp.get("MonthOfBirth")) + "/" + str(emp.get("YearOfBirth")))


def update_employee():
    eId = int(input("Enter employee Id to update:"))

    fname = read_first_name()
    lname = read_last_name()
    date = read_date_of_birth()
    month = read_month_of_birth()
    year = read_year_of_birth()
    Position = position()

    for i in range(len(employeeList)):
        if int(employeeList[i]['EmployeeId']) == int(eId):
            del employeeList[i]
            break
    employeeList.append(dict_data(eId, fname, lname, date, month, year))

    print("Employee updated!!")


def find_employee():
    eId = int(input("Enter employee Id to find:"))

    emp = [x for x in employeeList if int(x['EmployeeId']) == int(eId)]

    if emp == []:
        print("Employee Id is not present")
    else:
        print("Employee Id:" + str(emp[0].get("EmployeeId")))
        print("Employee Name:" + emp[0].get("FirstName") + " " + emp[0].get("LastName"))
        print("Date Of Birth (dd/mm/yyyy):" + str(emp[0].get("DateOfBirth")) + "/" + str(
            emp[0].get("MonthOfBirth")) + "/" + str(emp[0].get("YearOfBirth")))


while True:
    print("Select from the following option -")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Total employees")
    print("4. List of employees")
    print("5. Enter employee ID for employee data")
    print("6. Update employee")

    user_choice = int(input("select 1,2,3,4,5,6"))

    if user_choice == 1:
        add_employee()
    elif user_choice == 2:
        remove_employee()
    elif user_choice == 3:
        total_employee()
    elif user_choice == 4:
        list_employee()
    elif user_choice == 5:
        find_employee()
    elif user_choice == 6:
        update_employee()

    next_entry = input("Next selection? (yes/no): ")
    if next_entry == "no":
        break
