import pyodbc
import sys

class showData:
    
    menuChoice=""
    id="12"
    
    def showMenu(self):

        while (self.menuChoice!="Q"):
            print("Show Menu");      
            print("---------------")       
            print("Q - Quit")      
            print("1 - Show All Records")
            print("2 - Show 1 Record by ID")   

            self.menuChoice = input("Please select a query: \n")          


            if (self.menuChoice=="1"):
                self.menuFunction1()
            elif(self.menuChoice=="2"):
                self.menuFunction2()
            elif(self.menuChoice.lower() == "q"):
                sys.exit()       

    def menuFunction1(self):
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ari\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute('select * from Student')
        rows = cursor.fetchall()
        for row in rows:
            print (row.ID,"\t", row.Stu_fname)

    def menuFunction2(self):
        self.id = input("Please provide id: \n")   
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ari\Documents\Database1.accdb;')
        cursor = conn.cursor()
        cursor.execute("select  * from [in] where id="+self.id+ " order by age desc")
        rows = cursor.fetchall()
        for row in rows:
            print (row.ID,"\t", row.Name,"\t\t", row.Age,"\t", row.Sex)



class actionMenu:
    
    actionMenuChoice=""
    
    def showMenu(self):

        while (self.actionMenuChoice!="Q"):
            print("Action Menu");      
            print("---------------")       
            print("Q - Quit")      
            print("1 - Dump Data")
            print("2 - Insert Data")       
            print("3 - Update data")
            print("4 - Delete Data")
            self.actionMenuChoice = input("Please select an action?: \n")
            if(self.actionMenuChoice.lower() == "q"):
                sys.exit()    
            
            if (self.actionMenuChoice=="1"):
                sd=showData()
                sd.showMenu()
        
        
class tableMenu:
    
    menuTable=""
    tableMenuChoice=""
    
    def showMenu(self):
        
        while (self.tableMenuChoice!="Q"):
            print("Table Menu");    
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

            if (self.tableMenuChoice.lower() =="q"):
                sys.exit()
            if (self.tableMenuChoice=="1"):
                am=actionMenu()
                am.showMenu()   

        
        

tm=tableMenu()
tm.showMenu()