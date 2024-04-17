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
            self.cur.execute("create table if not exists customer (id integer autoincremeant , name string)")
            self.cur.execute("insert into customer(name) values ({0})".format(useranme))
            self.database.commit()
        elif radiobutton == "ادمین":
            self.cur.execute("create table if not exists admin (id integer autoincremeant , name string , password)")
            self.cur.execute("insert into customer(name) values ({0})".format(useranme))
            self.database.commit()





