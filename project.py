import pyodbc
import sys


class showData:

    menuChoice = ""
    id = "12"

    def showMenu(self, table):

        while (self.menuChoice != "q"):
            print("Show Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Show All Records")
            print("2 - Show 1 Record by ID")

            self.menuChoice = input("Please select a query: \n")

            if (self.menuChoice == "1"):
                self.menuFunction1(table)
            elif(self.menuChoice == "2"):
                self.menuFunction2(table)
            elif(self.menuChoice.lower() == "q"):
                print("Quitting Program")
                tableMenu()

    def menuFunction1(self,table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from ' + table )
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2])

    def menuFunction2(self,table):
        self.id = input("Please provide id: \n")
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute(
            "select  * from  " + table + " where id="+self.id)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        
class addData:
    menuChoice = " "
    def showMenu(self,table):

        while (self.menuChoice != "Q"):
            print("Show Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Print all records")
            print("2 - Add a record")


            self.menuChoice = input("Please select a query: \n")

            if(self.menuChoice == "1"):
                self.menuFunction1(table)
            elif(self.menuChoice == "2"):
                if(table == "Students"):
                    self.addStudent(table)
                elif(table == "Enrollment"):
                    self.addEnrollment(table)
                elif(table == "Majors"):
                    self.addMajors(table)
                elif(table == "Courses"):
                    self.addCourses(table)
                elif(table == "Classes"):
                    self.addClasses(table)
                elif(table == "Instructors"):
                    self.addInstructors(table)
                elif(table == "Departments"):
                    self.addDepartments(table)
                elif(table == "Buildings"):
                    self.addBuildings(table)
            elif(self.menuChoice.lower() == "q"):
                print("Quitting Program")
                actionMenu()

    def menuFunction1(self,table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from ' + table)
        rows = cursor.fetchall()
        for row in rows:
            print(row.ID, ") ", row[1], ", ", row[2])

    def addStudent(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Lname = input("Enter Last Name = ")
        Fname = input("Enter First Name = ")
        address = input("Enter Student Address = ")
        city = input("Enter Student City = ")
        state = input("Enter Student state = ")
        cursor.execute(
            "INSERT INTO " + table + "(LastName, FirstName, Stu_Address, Stu_City, Stu_State) VALUES (" + "'" + Lname + "' ," + "'" + Fname + "'" + "," +  "'" + address + "' , '" + 
             city + "' , '" + state + "' )"
        )
        conn.commit()
        print(Fname, Lname, "has been added to the table")

    def addEnrollment(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        StuID = input("Enter Student ID = ")
        Major = input("Enter Studnet Major = ")
        Status = input("Enter Student Status = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(Student_ID, Major, Status) VALUES (" + "'" + StuID + "' ," + "'" + Major + "'" + "," +  "'" + Status +  "' )"
        )
        conn.commit()
        print("Record has been added to the table")

    #Department is a reference / lookup - ask prof
    #
    def addMajors(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Major= input("Enter Major Name = ")
        Department = input("Enter Student Department = ")
        Transfer = input("Transferrable (Yes/No) = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(Major_Name, Department, Transfer) VALUES (" + "'" + Major + "' ," + "'" + Department + "'" + "," +  "'" + Transfer +  "' )"
        )
        conn.commit()
        print(Major," has been added to the table")
    #
    #

    def addCourses(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Course= input("Enter Course name = ")
        Credits= input("Enter Course credits = ")
        Description = input("Course Description = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(Course_name, Credits, Description) VALUES (" + "'" + Course + "' ," + "'" + Credits + "'" + "," +  "'" + Description +  "' )"
        )
        conn.commit()
        print(Course," has been added to the table")

    #This sucks, all lookup, ask professor
    #
    def addClasses(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Class= input("Enter Course name = ")
        Credits= input("Enter Course credits = ")
        Description = input("Course Description = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(Course_name, Credits, Description) VALUES (" + "'" + Class + "' ," + "'" + Credits + "'" + "," +  "'" + Description +  "' )"
        )
        conn.commit()
        print(Class," has been added to the table")
    #
    #
    def addInstructors(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Fname= input("Enter First Name = ")
        Lname= input("Enter Last Name = ")
        Department = input("Enter Instructor Department = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(FName, LName, Department) VALUES (" + "'" + Fname + "' ," + "'" + Lname + "'" + "," +  "'" + Department +  "' )"
        )
        conn.commit()
        print(Fname," " , Lname ," has been added to the table")

    
    #More lookup
    #
    def addDepartments(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Fname= input("Enter First Name = ")
        Lname= input("Enter Last Name = ")
        Department = input("Enter Instructor Department = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(FName, LName, Department) VALUES (" + "'" + Fname + "' ," + "'" + Lname + "'" + "," +  "'" + Department +  "' )"
        )
        conn.commit()
        print(Fname," " , Lname ," has been added to the table")

    #
    #

    def addBuildings(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        BName= input("Enter Building Name = ")
        BDep= input("Enter Building Department = ")
        BLoc = input("Enter Building Location = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(Building_Name, Building_Department, Building_Location) VALUES (" + "'" + BName + "' ," + "'" + BDep + "'" + "," +  "'" + BLoc +  "' )"
        )
        conn.commit()
        print(BName, " has been added to the table")


class delData:
    menuChoice = ""
    def showMenu(self,table):

        while (self.menuChoice != "Q"):
            print("Show Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Delete a Record")
            print("2 - Print all Records")

            self.menuChoice = input("Please select a query: \n")

            if(self.menuChoice == "1"):
                self.menuFunction1(table)
            elif(self.menuChoice == "2"):
                self.menuFunction2(table)
            elif(self.menuChoice.lower() == "q"):
                print("Quitting Program")
                sys.exit()

    def menuFunction1(self,table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        delID = input("Enter ID of Record to delete = ")
        cursor.execute(
            "DELETE FROM "+ table + " WHERE ID = " + delID
        )
        conn.commit()
        print("Record Number " + delID + " has been deleted from the table")
    
    def menuFunction2(self,table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from ' + table)
        rows = cursor.fetchall()
        for row in rows:
            print(row)



class actionMenu:

    actionMenuChoice = ""

    def showMenu(self, table):

        while (self.actionMenuChoice != "Q"):
            print("Action Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Dump Data")
            print("2 - Insert Data")
            print("3 - Delete Data")
            self.actionMenuChoice = input("Please select an action?: \n")
            if(self.actionMenuChoice.lower() == "q"):
                print("Quitting Program")
                tableMenu()

            elif (self.actionMenuChoice == "1"):
                sd = showData()
                sd.showMenu(table)
            
            elif (self.actionMenuChoice == "2"):
                ad = addData()
                ad.showMenu(table)

            elif (self.actionMenuChoice == "3"):
                dd = delData()
                dd.showMenu(table)


class tableMenu():
    

    
    menuTable = ""
    tableMenuChoice = ""

    

    def showMenu(self):
        

        while (self.tableMenuChoice != "Q"):
            print("Table Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Students")
            print("2 - Enrollment")
            print("3 - Majors")
            print("4 - Courses")
            print("5 - Classes")
            print("6 - Instructors")
            print("7 - Departments")
            print("8 - Buildings")

            self.tableMenuChoice = input("Please select a table: \n")


            if (self.tableMenuChoice.lower() == "q"):
                sys.exit()
            if (self.tableMenuChoice == "1"):
                table = "Students"
                am = actionMenu()
                am.showMenu(table)
            elif(self.tableMenuChoice == "2"):
                table = "Enrollment"
                am = actionMenu()
                am.showMenu(table)
            elif(self.tableMenuChoice == "3"):
                table = "Majors"
                am = actionMenu()
                am.showMenu(table)            
            elif(self.tableMenuChoice == "4"):
                table = "Courses"
                am = actionMenu()
                am.showMenu(table)               
            elif(self.tableMenuChoice == "5"):
                table = "Classes"
                am = actionMenu()
                am.showMenu(table)                
            elif(self.tableMenuChoice == "6"):
                table = "Instructors"
                am = actionMenu()
                am.showMenu(table)   
            elif(self.tableMenuChoice == "7"):
                table = "Departments"
                am = actionMenu()
                am.showMenu(table)             
            elif(self.tableMenuChoice == "8"):
                table = "Buildings"
                am = actionMenu()
                am.showMenu(table)   
                



tm = tableMenu()
tm.showMenu()
