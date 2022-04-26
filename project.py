import pyodbc
import sys


class showData:

    menuChoice = ""
    id = "12"

    def showMenu(self):

        while (self.menuChoice != "q"):
            print("Show Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Show All Records")
            print("2 - Show 1 Record by ID")
            print("3 - Add a Record")

            self.menuChoice = input("Please select a query: \n")

            if (self.menuChoice == "1"):
                self.menuFunction1()
            elif(self.menuChoice == "2"):
                self.menuFunction2()
            elif(self.menuChoice.lower() == "q"):
                sys.exit()

    def menuFunction1(self):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from Tester')
        rows = cursor.fetchall()
        for row in rows:
            print(row.ID, "\t", row.LastName)

    def menuFunction2(self):
        self.id = input("Please provide id: \n")
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        cursor.execute(
            "select  * from Tester where id="+self.id + " order by Number desc")
        rows = cursor.fetchall()
        for row in rows:
            print(row.ID, "\t", row.LastName, "\t\t", row.FirstName, "\t", row.PlayerNumber)

        
class addData:
    menuChoice = " "
    def showMenu(self):

        while (self.menuChoice != "Q"):
            print("Show Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Insert a Record")
            print("2 - Print all Records")


            self.menuChoice = input("Please select a query: \n")

            if(self.menuChoice == "1"):
                self.menuFunction1()
            elif(self.menuChoice == "2"):
                self.menuFunction2()
            elif(self.menuChoice.lower() == "q"):
                sys.exit()


    def menuFunction1(self):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        Lname = input("Enter Last Name = ")
        Fname = input("Enter First Name = ")
        PNumber = input("Enter number = ")
        cursor.execute(
            "INSERT INTO Tester (LastName, FirstName, PlayerNumber) VALUES (" + "'" + Lname + "'" + "," + "'" + Fname + "'" + "," +  "'" + PNumber + " ' " + ")"
        )
        conn.commit()
        print(Fname, Lname, "has been added to the table")

    def menuFunction2(self):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from Tester')
        rows = cursor.fetchall()
        for row in rows:
            print(row.ID, "\t", row.LastName)    

class delData:
    #
    # Only marked up, no construction or logic 
    #
    #
    #
    #
    #
    #
    def showMenu(self):

        while (self.menuChoice != "Q"):
            print("Show Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Delete a Record")
            print("2 - Print all Records")

            self.menuChoice = input("Please select a query: \n")

            if(self.menuChoice == "1"):
                self.menuFunction1()
            elif(self.menuChoice == "2"):
                self.menuFunction2()
            elif(self.menuChoice.lower() == "q"):
                sys.exit()

    def menuFunction1(self):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        Lname = input("Enter Last Name = ")
        Fname = input("Enter First Name = ")
        PNumber = input("Enter number = ")
        cursor.execute(
            "INSERT INTO Tester (LastName, FirstName, PlayerNumber) VALUES (" + "'" + Lname + "'" + "," + "'" + Fname + "'" + "," +  "'" + PNumber + " ' " + ")"
        )
        conn.commit()
        print(Fname, Lname, "has been added to the table")
    
    def menuFunction2(self):
        print("Poggers")



class actionMenu:

    actionMenuChoice = ""

    def showMenu(self):

        while (self.actionMenuChoice != "Q"):
            print("Action Menu")
            print("---------------")
            print("Q - Quit")
            print("1 - Dump Data")
            print("2 - Insert Data")
            print("3 - Delete Data")
            self.actionMenuChoice = input("Please select an action?: \n")
            if(self.actionMenuChoice.lower() == "q"):
                sys.exit()

            if (self.actionMenuChoice == "1"):
                sd = showData()
                sd.showMenu()
            
            if (self.actionMenuChoice == "2"):
                ad = addData()
                ad.showMenu()

            if (self.actionMenuChoice == "3"):
                dd = delData()
                dd.showMenu()


class tableMenu:

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
                am = actionMenu()
                am.showMenu()
                table = "Students"
            elif(self.tableMenuChoice == "2"):
                am = actionMenu()
                am.showMenu()
                table = "Enrollment"
            elif(self.tableMenuChoice == "3"):
                am = actionMenu()
                am.showMenu()
                table = "Majors"
            elif(self.tableMenuChoice == "4"):
                am = actionMenu()
                am.showMenu()
                table = "Courses"
            elif(self.tableMenuChoice == "5"):
                am = actionMenu()
                am.showMenu()
                table = "Classes"
            elif(self.tableMenuChoice == "6"):
                am = actionMenu()
                am.showMenu()
                table = "Instructors"
            elif(self.tableMenuChoice == "7"):
                am = actionMenu()
                am.showMenu()
                table = "Departments"
            elif(self.tableMenuChoice == "8"):
                am = actionMenu()
                am.showMenu()
                table = "Buildings"


tm = tableMenu()
tm.showMenu()
