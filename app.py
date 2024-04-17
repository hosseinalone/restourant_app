from tkinter import *
from sqlite3 import *
from algorithm import logics

class apps(logics):
    
    # ------------ ----------------- login app  ------------ ----------------- #

    def loginform(self):
        
        self.lform = Tk()
        
        self.lform.geometry("200x200")

        welcome_text = Label(self.lform, text="خوش امدید", font=("Vazir", 20, "bold"))
        welcome_text.place(x=40, y=10)
        
        username_text = Label(self.lform, text="نام کاربری", font=("Vazir", 12))
        username_text.place(x=70, y=60)
        
        username_entry = Entry(self.lform)
        username_entry.place(x=40, y=100)

        self.lform.mainloop()





obj = apps()
obj.loginform()