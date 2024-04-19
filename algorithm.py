#------------- imports : 

from sqlite3 import *
from tkinter import *

# ------------ the algorithms -------------- #

class logics:

    def __init__(self) -> None:
        self.database = connect("database.db")
        self.cur = self.database.cursor()
        self.cur.execute("create table if not exists customer (id INTEGER PRIMARY KEY AUTOINCREMENT , name STRING)")
        self.cur.execute("create table if not exists admin (id INTEGER PRIMARY KEY AUTOINCREMENT , name STRING , password INTEGER UNIQUE)")
        self.database.commit()        
        self.database.close()
        
    def submitlogininfo(self,radiobutton,useranme):
        
        try:
            
            self.database = connect("database.db")
            self.cur = self.database.cursor()

            if radiobutton == "مشتری":
                
                self.cur.execute("INSERT INTO customer(name) values (?)",(useranme,))
                self.database.commit()
                

            elif radiobutton == "مدیر":
                adminname1  = self.cur.execute('select name from admin')
                print(adminname1)

            

        except IntegrityError:
                print("The data could not be inserted!", "Error")

        finally:
             self.database.close()




