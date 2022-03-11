
class Employee:
    id = 0
    fname = ""
    lname = ""
    position = ""
    age = 0


    def setData(self, id, fname, lname, position, age):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.position = position
        self.age = age


    def showData(self):
        print("Id:", self.id)
        print("fname:", self.fname)
        print("lname:", self.lname)
        print("position:", self.position)
        print("age:", self.age)



def main():

    emp = Employee()
    emp.setData(123456,'Surabhi', 'kumari', 'trainee', 26)
    emp.showData()


if __name__ == "__main__":
    main()