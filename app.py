from tkinter import *
from sqlite3 import *
from algorithm import logics

class apps(logics):
    
#  login app  ----------------------------- 

    def loginform(self):
        
    
        self.lform = Tk()        
        self.lform.geometry("200x300")
        

        welcome_text = Label(self.lform, text="خوش امدید", font=("Vazir", 20, "bold"))
        welcome_text.place(x=40, y=10)
        
        username_text = Label(self.lform, text="نام کاربری", font=("Vazir", 12))
        username_text.place(x=70, y=60)
        
        username_entry = Entry(self.lform)
        username_entry.place(x=40, y=100)

        
        # ------------ ----------------- radio button  ------------ ----------------- #
        
        self.role_var = StringVar()
        self.role_var.set("مشتری")
        
        def printer(rolevar):
            print("item : \n",self.role_var , "\n is seleted")
            

        
            

        admin_radio = Radiobutton(self.lform,text="مدیر",variable=self.role_var,value="مدیر" , font=("Vazir",12),command=lambda: printer(self.role_var.get()))
        admin_radio.place(x=30,y=130)

        customer_radio = Radiobutton(self.lform,text="مشتری",variable=self.role_var,value="مشتری" , font=("Vazir",12),command=lambda: printer(self.role_var.get()))
        customer_radio.place(x=100,y=130)

        # ------------ ----------------- when it pressed the submit  ------------ ----------------- #
        
        

        submit = Button(self.lform,text="ثبت",font=("Vazir",12,"bold"),padx=20,pady=5,command=lambda:logics.submitlogininfo(self,self.role_var.get(),username_entry.get()))
        submit.place(x=65,y=180)

       
        
        self.lform.mainloop()




obj = apps()
obj.loginform()