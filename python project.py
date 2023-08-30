from os import system

employees = []

class Company:
    def __init__(self, cid, cname) -> None:
        self.cid = cid
        self.cname = cname
    
    def __str__(self) -> str:
        return str (self.cid)+ " " + self.cname 

class Employee(Company):
    def __init__(self, cid, cname,eid, ename, salary, designation,workHours):
        super().__init__(cid, cname)
        self.eid = eid
        self.ename = ename
        self.salary = salary
        self.designation = designation
        self.workHours = workHours
        
    def __str__(self) -> str:
        return str(self.eid) + " " + self.ename + " " + str(self.salary) + " " + self.designation + " " + str(self.workHours)

    def display(self):
        print(super().__str__())
        print(self.__str__())

  
    @staticmethod
    def addEmployee():
        print("{:>60}".format("-->> Add Employee Record <<--"))
        cid = int(input("Enter the company ID : "))
        cname = input("Enter the company name : ")
        
        eid = int(input("Enter Employee ID : "))
        ename = input("Enter Employee Name : ")
       
       
        
        salary = int(input("Enter Employee Salary : "))
        designation = input("Enter Employee Designation : ")
       
        workHours = int(input("Enter Employee work hours : "))

        emp = Employee(cid, cname, eid, ename, salary, designation, workHours)

        employees.append(emp)        

        print("Successfully Added Employee Record")
        press = input("Press Any Key TO Continue..")
        
        menu()

  

    @staticmethod
    def searchEmployee(parameter, value):
        print(parameter, value )
        for i in employees:
            if getattr(i, parameter) == value:
                i.display()
    
    

    
    @staticmethod
    def displayEmployee():
        if employees.__len__() == 0:
            print("Empty List")
            return
        for i in employees:
            i.display()
            print("---------------------------------")
        press = input("Press Any Key To Continue..")
        menu()




    # Calculate Salary
    def calculateSalary(self):
        overtime = 0
        gs = self.salary
        print(self.salary)
        if self.workHours > 45 :
            overtime = self.workHours - 45

        self.salary = self.salary + (overtime * (self.salary/45))

        print("Gross Salary is : ", gs)
        print("Overtime : ", overtime)
        print("Total Salary is : ", self.salary) 
        press = input("Press Any key to Continue..")
        menu()



def menu():
    system("cls")
    print("{:>60}".format(" Employee Management System "))

    print("1. Add Employee")
    print("2. Display All Employee")
    print("3. Search Employee")
    print("4. Calculate Salary")
    print("5. Exit")
    print("{:>60}".format(" Choice Options : [1/2/3/4/5] "))

    ch = int(input("Enter your Choice : "))

    if ch == 1:
        system("cls")
        Employee.addEmployee()

    elif ch == 2:
        system("cls")
        Employee.displayEmployee()

    elif ch == 3:
        system("cls")
        print("{:>60}".format("-->> Search Employee Record <<--"))
        searchMenu()

    elif ch == 4:
        id = int(input("Enter the Employee ID for which salary is calculated : "))
        ref = None
        for i in employees:
            if i.eid == id:
                ref = i
        Employee.calculateSalary(ref)

    elif ch == 5:
        exit();

    else:
        print("Invalid Choice!")
        press = input("Press Any key to Continue..")
        menu()

# Search Menu

def searchMenu(): 
    print("-->> 1. Search By ID <<--")
    print("-->> 2. Search By Name <<--")
    print("-->> 3. Search Employee Designation <<--")
    print("-->> 4. Search Employee DOJ <<--")
    print("-->> 5. Exit <<--")
    
    ch = int(input("Enter the choice : "))

    if ch == 1:
        id = int(input("Enter the Employee ID to be searched : "))
        Employee.searchEmployee('eid', id)
        press = input("Press Any key to Continue..")
        searchMenu()

    elif ch == 2:
        nm = input("Enter the Employee Name to be searched : ")
        Employee.searchEmployee('ename', nm)

        press = input("Press Any key to Continue..")
        searchMenu()
        
    elif ch == 3:
        deg = input("Enter the Employee Designation to be searched : ")
        Employee.searchEmployee('designation', deg)
        
        press = input("Press Any key to Continue..")
        searchMenu()
        
    elif ch == 4:
        doj = input("Enter the Employee DOJ to be searched : ")
        Employee.searchEmployee('doj', doj)
        
        press = input("Press Any key to Continue..")
        searchMenu()

    elif ch == 5:
        menu()
    else:
        print("Invalid Choice!")
        press = input("Press Any key to Continue..")
        menu()

menu()