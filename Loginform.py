from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import random
import time
from time import strftime
import datetime
import pymysql #pip install pymysql
from register import Register
from main import Biometric_based_attendance_system

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")
        
        #first Image
        img=Image.open(r"Resources\photos_scan.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second Image
        img1=Image.open(r"Resources\class.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #third Image
        img2=Image.open(r"Resources\group1.jpeg")
        img2=img2.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        #f_lbl.place(x=0,y=0,width=550,height=130)

        #bg Image
        bg=Image.open(r"Resources\humans-robot.jpg")
        bg=bg.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="BIOMETRIC BASED ATTENDANCE SYSTEM",font=("times new roman",36,"bold"),bg="White",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1535,height=45)

        # Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times bew roman",16,"bold"),background='white',foreground='red')
        lbl.place(x=30,y=0,width=120,height=50)
        time()

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=520,y=66,width=480,height=500)

        img1=Image.open(r"Resources/user (2).png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        lblimg1=Label(main_frame,image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=200,y=0,width=100,height=100)

        get_start_lbl=Label(main_frame,text="Get Started",font=("times new roman",22,"bold"),bg="white",borderwidth=0,fg="darkblue")
        get_start_lbl.place(x=166,y=110,width=160,height=30)

        username=Label(main_frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=100,y=170)

        img2=Image.open(r"Resources/user (2).png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(main_frame,image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=70,y=170,width=25,height=25)

        self.txtuser=ttk.Entry(main_frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=70,y=200,width=360)
        
        password=Label(main_frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=100,y=250)

        img3=Image.open(r"Resources/pass.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(main_frame,image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=70,y=250,width=25,height=25)

        self.txtpass=ttk.Entry(main_frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=70,y=280,width=360)
        self.txtpass.config(show="*")
        
        #Login button
        loginbtn=Button(main_frame,command=self.login,text="Login",font=("times new roman",16,"bold"),bd=3,relief=RIDGE,fg="White",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=160,y=330,width=150,height=35)
        
        #register button
        registerbtn=Button(main_frame,text=" New User Register ",command=self.register_window,font=("times new roman",13,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        registerbtn.place(x=70,y=390,width=160)

        #forgetpass button
        forgetbtn=Button(main_frame,text="Forget Password ",command=self.forget_password_window,font=("times new roman",13,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgetbtn.place(x=65,y=420,width=160)

        footer_lbl=Label(bg_img,text="Note: First input valid Username and valid Password ",font=("times new roman",20,"bold"),bg="White",fg="darkblue")
        footer_lbl.place(x=0,y=630,width=1530,height=36)

    #Register  button function
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    

    def login(self):
        if self.txtuser.get()=="" or  self.txtpass.get()=="":
            messagebox.showerror("Error","All fields Required",parent=self.root)
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",
                               (
                                  self.txtuser.get(),
                                  self.txtpass.get()
                                ))
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Usernsme & password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authority Person",parent=self.root)
                #self.root.destroy()
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Biometric_based_attendance_system(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="select":
            messagebox.showerror("Error,","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif  self.txt_newpass.get()=="":
             messagebox.showerror("Error","Please enter the New password",parent=self.root2)
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                 messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()
                
    
    #forget password window
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password",parent=self.root)
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget password",font=("times new roman",20,"bold") , bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)
                
                #Security Questions
                security_Q=Label(self.root2,text="select security", font=("times new roman",15,"bold") , bg="white",fg="black")
                security_Q.place(x=50,y=80)
                #Combobox
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold") ,state="readonly")
                self.combo_security_Q["values"]=("select","Your birth place","Your friend name","Tour pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                #security Answer
                security_A=Label(self.root2,text="security Answer", font=("times new roman",15,"bold") ,fg="black",bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New password",font=("times new roman",15,"bold") ,fg="black",bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

  

if __name__== "__main__":
    main()

        
'''
if __name__== "__main__":
    root=Tk()
    obj=Login_window(root)
    root.mainloop()
'''

    
