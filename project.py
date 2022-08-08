import sys
import pyodbc


class showData:

    menuChoice = ""
    id = "12"

    def showMenu(self, table):

        while (self.menuChoice.lower() != "q"):
            print()
            print("Print Data Menu")
            print("---------------")
            print("Q - Back to Action Menu")
            print("1 - Show All " , table, "Records")
            print("2 - Show 1 Record by ID")

            self.menuChoice = input("Please select a query: \n")
            if(self.menuChoice.lower() == "q"):
                print("Your working table is [" ,table, "]")              
            elif (self.menuChoice == "1"):
                self.menuFunction1(table)
            elif(self.menuChoice == "2"):
                self.menuFunction2(table)
            

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
            field_names = [i[0] for i in cursor.description]
            print(field_names)
            print(row)

        
class addData:
    menuChoice = " "
    def showMenu(self,table):

        while (self.menuChoice.lower() != "q"):
            print()
            print("Create Record Menu")
            print("---------------")
            print("Q - Back to Action Menu")
            print("1 - Print all",table," records")
            print("2 - Add a record")


            self.menuChoice = input("Please select a query: \n")
            if(self.menuChoice.lower() == "q"):
                print("Your working table is [" ,table, "]") 
            elif(self.menuChoice == "1"):
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
            

    def menuFunction1(self,table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from ' + table)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

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
        cTaken = input("Enter Courses taken = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(StudentID, Major, Status, CoursesTaken) VALUES (" + "'" + StuID + "' ," + "'" + Major + "'" + "," +  "'" + Status +  "'" + "'" + cTaken + "'" + ")"
        )
        conn.commit()
        print("Record has been added to the table")


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

    #
    #
    def addClasses(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Class= input("Enter Course name = ")
        instructor = input("Enter instructor name = ")
        Room= input("Enter Room Number = ")
        building = input("Enter building = ")
        numStudents = input("Number of Students = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(Course, Instructor, Room, Building, NumStudents) VALUES (" + "'" + Class + "' ," + "'" + instructor + "'" + "," + "'" + Room + "'" +  "," + "'" + building + "'" + "," +  "'" + numStudents +  "' )"
        )
        conn.commit()
        print(Class, Room, " has been added to the table")
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


    def addDepartments(self, table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        Bname= input("Enter Department Name = ")
        depHead= input("Enter Department Head= ")
        location = input("Enter Department Building = ")
        
        cursor.execute(
            "INSERT INTO " + table + "(Dep_Name, Dep_Head, DepBuilding) VALUES (" + "'" + Bname + "' ," + "'" + depHead + "'" + "," +  "'" + location +  "' )"
        )
        conn.commit()
        print(Bname," has been added to the table")


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

        while (self.menuChoice.lower() != "q"):
            print()
            print("Delete Record Menu")
            print("---------------")
            print("Q - Back to Action Menu")
            print("1 - Print all ", table, "Records")
            print("2 - Delete a Record")
            

            self.menuChoice = input("Please select a query: \n")

            if(self.menuChoice.lower() == "q"):
                print("Your working table is [" ,table, "]") 
                actionMenu()
            elif(self.menuChoice == "1"):
                self.menuFunction2(table)
            elif(self.menuChoice == "2"):
                self.menuFunction1(table)
            
            
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
            print(row[0], row[1], row[2])

class updateData:
    menuChoice = " "
    def showMenu(self,table):

        while (self.menuChoice.lower() != "q"):
            print()
            print("Update Record Menu")
            print("---------------")
            print("Q - Back to Action Menu")
            print("1 - Print all",table," records")
            print("2 - Update a record")

            self.menuChoice = input("Please select a query: \n")
            if(self.menuChoice.lower() == "q"):
                print("Your working table is [" ,table, "]")
            elif(self.menuChoice == "1"):
                self.menuFunction1(table)
            elif(self.menuChoice == "2"):
                self.menuFunction2(table)


    def menuFunction1(self,table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from ' + table)
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
        print("Which Field would you like to update? Choices are... ") 
        for row in rows:
            field_names = [i[0] for i in cursor.description]
            j = 1
            for name in field_names:
                print(j, name)
                j += 1
        x = int(input("Select = "))
        wField = (field_names[x-1])
        value = input("Enter updated value = ")

        conn2 = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')

        cursor2 = conn2.cursor()
        cursor2.execute("UPDATE " + table + " SET " + wField + " = '"+ value + "' WHERE ID = "+ self.id)
        conn2.commit()
        print("[",table, "] Record has been updated")


class actionMenu:

    actionMenuChoice = ""

    def showMenu(self, table):

        while (self.actionMenuChoice != "Q"):
            print()
            print("Action Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Print Data")
            print("2 - Create Record")
            print("3 - Update Record")
            print("4 - Delete Record")

            self.actionMenuChoice = input("Please select an action: \n")
            if(self.actionMenuChoice.lower() == "q"):
                print("Quitting Program")
                sys.exit()

            elif (self.actionMenuChoice == "1"):
                sd = showData()
                sd.showMenu(table)
            
            elif (self.actionMenuChoice == "2"):
                ad = addData()
                ad.showMenu(table)
            
            elif (self.actionMenuChoice == "3"):
                ud = updateData()
                ud.showMenu(table)

            elif (self.actionMenuChoice == "4"):
                dd = delData()
                dd.showMenu(table)

            

class showReports:
    recordSelection = ""
   
    def showMenu(self):

        while (self.recordSelection != "Q"):
            print()
            print("Report Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Record 1")
            print("2 - Record 2")

            recordSelection = input("Select a Report - ")
            if(recordSelection.lower() == "q"):
                print("Exiting program")
                sys.exit()
            if(recordSelection == "1"):
                showReports.reports1(self)
            elif(recordSelection == "2"):
                showReports.reports2(self)
            

    def reports1(self):
        conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('''SELECT Buildings.ID, Sum(Classes.NumStudents) AS numPeople FROM Buildings INNER JOIN 
        Classes ON Buildings.ID = Classes.Building GROUP BY Buildings.ID HAVING (((Buildings.ID)=1));''')
        rows = cursor.fetchall()
        for row in rows:
            print ("Number of students in the west building", row.numPeople)
        
    def reports2(self):
        conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('''SELECT Students.ID, Students.LastName, Students.FirstName, Students.Stu_State, Enrollment.Major
            FROM Students, Majors INNER JOIN Enrollment ON Majors.ID = Enrollment.Major
            GROUP BY Students.ID, Students.LastName, Students.FirstName, Students.Stu_State, Enrollment.Major
            HAVING (((Students.Stu_State)='PA') AND ((Enrollment.Major)=1))
            ORDER BY Students.ID;''')
        rows = cursor.fetchall()
        for row in rows:
            print (row[0], row[1], row[2], row[3])

    def reports3(self):
        conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Database1.accdb;')
        cursor = conn.cursor()

        
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
            print("9 - Records")

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
            elif(self.tableMenuChoice == "9"):
                sr = showReports()
                sr.showMenu()
                
tm = tableMenu()
tm.showMenu()
