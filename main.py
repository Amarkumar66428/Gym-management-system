import tkinter
from tkinter import*
from tkinter import messagebox
root = tkinter.Tk() #to create a main window
#widget will go here....
lb=tkinter.Label(root,text="Ar gYm",font=("ROG Fonts",45),fg="#0C090A",bg="#dc7633").place(x=10,y=20)

class login:
    def __init__(self,root):
       self.root=root
       self.root.title("login system")
       self.root.geometry("900x600+500+100")
       self.root.configure(background="#dc7633")

       self.root.resizable(False,False)


      #=============================================================frame================================================================================================================
       Frame_login=Frame(self.root,bg="white")
       Frame_login.place(x=150,y=170,height=340,width=500)

      #===========================================================login=============================================================================================================
       title=Label(Frame_login,text="LOGIN HERE",font=("ROG Fonts",35,"bold",),fg="#d77337",bg="white").place(x=90,y=30)
       desc=Label(Frame_login,text="Use your Gym credentials to login :",font=("Trebuchet MS",12,"bold",),fg="black",bg="white").place(x=90,y=100)

      #==========================================================username===============================================================================================================
       lbl_user=Label(Frame_login,text="Username",font=("ROG Fonts",15,"bold",),fg="black",bg="white").place(x=90,y=140)
       self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="light grey")
       self.txt_user.place(x=90,y=170,width=350,height=35)

      #===========================================================password===========================================================================================================
       lbl_user=Label(Frame_login,text="Password",font=("ROG Fonts",15,"bold",),fg="black",bg="white").place(x=90,y=220)
       self.txt_pass= Entry(Frame_login, font=("times new roman", 15), bg="light grey",show='*')
       self.txt_pass.place(x=90, y=250, width=350, height=35)
      #===========================================================forget=============================================================================================================
       forget_btn=Button(Frame_login,text="forget password?",bd=0,bg="white",fg="blue",cursor="dot",font=("times new roman",12)).place(x=330,y=290)
      #========================================================for next window==================================================================================================
       Login_btn=Button(self.root,command=self.login_function,text="Login",bg="#38ACEC",fg="white",cursor="dot",font=("times new roman",20)).place(x=300,y=490,width=180,height=40)

    def login_function(self):
       if self.txt_pass.get()=="" or self.txt_user.get()=="":
           messagebox.showerror("ERROR","All field are required",parent=self.root)

       elif self.txt_user.get()!="z" or self.txt_pass.get()!="z":
          messagebox.showerror("ERROR","Invalid Username/Password",parent=self.root)
       else:
          self.newWindow = Toplevel(self.root)
          self.app = login2(self.newWindow)
    #====================================================new window==================================================================================================================
    def new_window(self):
       self.newWindow = Toplevel(self.root)
       self.app = login2(self.newWindow)


class login2:
   def __init__(self, root):
      self.root = root
      self.root.title("AR GYM")
      self.root.geometry("900x600+500+100")
      self.root.configure(background="white")
      self.root.resizable(False, False)

      lb = tkinter.Label(root, text="Welcome to  ar gYm", font=("ROG Fonts", 15), height=2, width=33).pack(side=LEFT,
                                                                                                           anchor=N)
      exitButton = Button(root,text ="Logout" ,width=8,command=root.destroy,font=("System", 15, "bold"), height=2, bd=0, bg="#d77337",fg="#000000").pack(side=RIGHT, anchor=N)

      btn2 = tkinter.Button(root, text="About us", width=8, font=("System", 15, "bold"), height=2, bd=0, bg="#d77337",fg="#000000")
      btn3 = tkinter.Button(root, text="Contact us", width=8, font=("System", 15, "bold"), height=2, bd=0, bg="#d77337",fg="#000000")
      btn4 = tkinter.Button(root, text="Profile", width=8, font=("System", 15, "bold"), height=2, bd=0, bg="#d77337",fg="#000000")
      btn2.pack(side=RIGHT, anchor=N)
      btn3.pack(side=RIGHT, anchor=N)
      btn4.pack(side=RIGHT, anchor=N)


      Frame_check = Frame(self.root, bg="black")
      Frame_check.place(x=8, y=62, height=530, width=350)

      mb = tkinter.Menubutton(Frame_check, text="GYM Equipment", bd=0, bg="#d77337", fg="black", cursor="dot",
                          font=("ROG Fonts", 16, "bold"), height=2, width=17)
      mb.menu = Menu(mb)
      mb["menu"] = mb.menu
      mb.menu.add_command(label="Add Equipment", command=lambda: print("Add Equipment is selected"))
      mb.menu.add_command(label="Delete Equipment", command=lambda: print("Delete Equipment is selected"))
      mb.menu.configure(bg="#fff0e6", fg="#1a0a00", font=("Segoe UI Emoji", 12,))
      mb.place(x=9, y=14)

      mb = tkinter.Menubutton(Frame_check, text="Exercises", bd=0, bg="#d77337", fg="black", cursor="dot",
                              font=("ROG Fonts", 16, "bold"), height=2, width=17)
      mb.menu = Menu(mb)
      mb["menu"] = mb.menu
      mb.menu.add_command(label="Push-Up", command=lambda: print("Push-Up is selected"))
      mb.menu.add_command(label="Chine-Up", command=lambda: print("Chine-Up is selected"))
      mb.menu.add_command(label="Standing overhead dumbbell presses", command=lambda: print("Standing overhead dumbbell presses is selected"))
      mb.menu.add_command(label="Deadlift", command=lambda: print("Deadlift is selected"))
      mb.menu.add_command(label="Dumbbell rows", command=lambda: print("Dumbbell rows is selected"))
      mb.menu.add_command(label="Squat", command=lambda: print("Squat is selected"))
      mb.menu.add_command(label="Leg press", command=lambda: print("Leg press is selected"))
      mb.menu.add_command(label="Burpees", command=lambda: print("Burpees is selected"))
      mb.menu.add_command(label="Push-Up", command=lambda: print("Push-Up is selected"))
      mb.menu.add_command(label="Chine-Up", command=lambda: print("Chine-Up is selected"))
      mb.menu.add_command(label="Standing overhead dumbbell presses", command=lambda: print("Standing overhead dumbbell presses is selected"))
      mb.menu.add_command(label="Deadlift", command=lambda: print("Deadlift is selected"))
      mb.menu.add_command(label="Dumbbell rows", command=lambda: print("Dumbbell rows is selected"))
      mb.menu.add_command(label="Squat", command=lambda: print("Squat is selected"))
      mb.menu.configure(bg="#fff0e6",fg="#1a0a00",font=("Segoe UI Emoji", 12,))
      mb.place(x=9, y=84)

      one_btn = Button(Frame_check, text="Messages", bd=0, bg="#d77337", fg="black", cursor="dot",
                          font=("ROG Fonts", 16, "bold"), height=2, width=18).place(x=11, y=157)
      one_btn = Button(Frame_check, text="Plans", bd=0, bg="#d77337", fg="black", cursor="dot",
                          font=("ROG Fonts", 16, "bold"), height=2, width=18).place(x=11, y=230)
      one_btn = Button(Frame_check, text="Fee statement", bd=0, bg="#d77337", fg="black", cursor="dot",
                          font=("ROG Fonts", 16, "bold"), height=2, width=18).place(x=11, y=303)
      one_btn = Button(Frame_check, text="Attendace", bd=0, bg="#d77337", fg="black", cursor="dot",
                          font=("ROG Fonts", 16, "bold"), height=2, width=18).place(x=11, y=376)
      one_btn = Button(Frame_check, text="New registration", bd=0, bg="#d77337", fg="black", cursor="dot",
                          font=("ROG Fonts", 16, "bold"), height=2,command=self.new_window2, width=18).place(x=11, y=450)



   def new_window2(self):
       self.newWindow = Toplevel(self.root)
       self.app = login3(self.newWindow)
#
class login3:
   def __init__(self, root):
      self.root = root
      self.root.title("NEW REGISTRATION")
      self.root.geometry("900x600+500+100")
      self.root.configure(background="#d77337")
      self.root.resizable(False, False)

      lb = tkinter.Label(root, text="NEW REGISTRATION", font=("ROG Fonts", 15), height=2,width=47,bg="black",fg="white").pack(side=RIGHT,
                                                                                                           anchor=N)
      exitButton = Button(root, text="<- Back", width=9, command=root.destroy, font=("System", 15, "bold"), height=2,bg="#d77337", fg="#000000").pack(side=LEFT, anchor=N)
      lbl_fname = Label(root, text="First Name", font=("ROG Fonts", 15, "bold",), fg="black", bg="#d77337").place(x=60, y=80)
      self.txt_fname = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_fname.place(x=60, y=110, width=350, height=35)

      lbl_lname = Label(root, text="Last Name", font=("ROG Fonts", 15, "bold",), fg="black", bg="#d77337").place(x=60,
                                                                                                                 y=180)
      self.txt_lname = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_lname.place(x=60, y=210, width=350, height=35)

      lbl_dob = Label(root, text="D.O.B", font=("ROG Fonts", 15, "bold",), fg="black", bg="#d77337").place(x=60,
                                                                                                                 y=280)
      self.txt_dob = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_dob.place(x=60, y=310, width=350, height=35)

      lbl_age = Label(root, text="AGE", font=("ROG Fonts", 15, "bold",), fg="black", bg="#d77337").place(x=60,
                                                                                                                 y=380)
      self.txt_age = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_age.place(x=60, y=410, width=350, height=35)

      lbl_add = Label(root, text="Address", font=("ROG Fonts", 15, "bold",), fg="black", bg="#d77337").place(x=490, y=80)
      self.txt_add = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_add.place(x=490, y=110, width=350, height=35)

      lbl_uname = Label(root, text="Username", font=("ROG Fonts", 15, "bold",), fg="black", bg="#d77337").place(x=490,
                                                                                                                 y=180)
      self.txt_uname = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_uname.place(x=490, y=210, width=350, height=35)

      lbl_eid = Label(root, text="Email ID", font=("ROG Fonts", 15, "bold",), fg="black", bg="#d77337").place(x=490,
                                                                                                                 y=280)
      self.txt_eid = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_eid.place(x=490, y=310, width=350, height=35)

      lbl_mob = Label(root, text="Mobile", font=("ROG Fonts", 15, "bold"), fg="black", bg="#d77337").place(x=490,
                                                                                                                 y=380)
      self.txt_mob = Entry(root, font=("times new roman", 15), bg="white")
      self.txt_mob.place(x=490, y=410, width=350, height=35)

      clearbtn = tkinter.Button(root, text="Clear",command=self.cleardata,width=8, font=("System", 15, "bold"), height=2, bg="black",fg="white").place(x=160,
                                                                                                                 y=450)

      Insertbtn = tkinter.Button(root, text="Register", width=9, font=("System", 15, "bold"),
                                height=2, bg="black", fg="white").place(x=60,
                                                                        y=450)

   import mysql.connector
   mydb = mysql.connector.connect(host="localhost", user="root", passwd="Amar0009#")



   def cleardata(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_dob.delete(0, END)
        self.txt_age.delete(0, END)
        self.txt_add.delete(0, END)
        self.txt_uname.delete(0, END)
        self.txt_eid.delete(0, END)
        self.txt_mob.delete(0, END)




obj=login(root)
root.mainloop()


