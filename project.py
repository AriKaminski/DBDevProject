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
            print("3 - Add a Record")

            self.menuChoice = input("Please select a query: \n")

            if (self.menuChoice == "1"):
                self.menuFunction1(table)
            elif(self.menuChoice == "2"):
                self.menuFunction2(table)
            elif(self.menuChoice.lower() == "q"):
                print("Quitting Program")
                sys.exit()

    def menuFunction1(self,table):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from ' + table )
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2])

    def menuFunction2(self,table):
        self.id = input("Please provide id: \n")
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        cursor.execute(
            "select  * from  " + table + " where id="+self.id)
        self.id = int(self.id)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        
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
                print("Quitting Program")
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
    menuChoice = ""
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
                print("Quitting Program")
                sys.exit()

    def menuFunction1(self):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        delID = input("Enter ID of Record to delete = ")
        cursor.execute(
            "DELETE FROM Tester WHERE ID = " + delID
        )
        conn.commit()
        print("Record Number" + delID + " has been deleted from the table")
    
    def menuFunction2(self):
        conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\devar\Documents\Phillies.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from Tester')
        rows = cursor.fetchall()
        for row in rows:
            print(row.ID, "\t", row.LastName)



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
                sys.exit()

            if (self.actionMenuChoice == "1"):
                sd = showData()
                sd.showMenu(table)
            
            if (self.actionMenuChoice == "2"):
                ad = addData()
                ad.showMenu()

            if (self.actionMenuChoice == "3"):
                dd = delData()
                dd.showMenu()


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
                table = "Tester"
                am = actionMenu()
                am.showMenu(table)
            elif(self.tableMenuChoice == "2"):
                table = "Games"
                am = actionMenu()
                am.showMenu(table)
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
