#------------- imports : 

from sqlite3 import *


# ------------ the algorithms -------------- #

class logics:
    def __init__(self) -> None:
        self.database = connect("database.db")
        self.cur = self.database.cursor()
        self.database.commit()        

        
    def submitlogininfo(self,radiobutton,useranme):
        if radiobutton == "مشتری":
            self.cur.execute("create table if not exists customer (id INTEGER PRIMARY KEY AUTOINCREMENT , name string)")
            self.cur.execute("insert into customer(name) values (?)",(useranme,))
            self.database.commit()
        elif radiobutton == "ادمین":
            self.cur.execute("create table if not exists admin (id INTEGER PRIMARY KEY AUTOINCREMENT , name string , password integer unique)")
            self.cur.execute("insert into admin(name) values (?)",(useranme,))
            self.database.commit()





