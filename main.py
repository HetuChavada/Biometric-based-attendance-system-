
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Biometric_based_attendance_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")
        
        #first Image
        img=Image.open(r"Resources\face-identification.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second Image
        img1=Image.open(r"Resources\glasses.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #third Image
        img2=Image.open(r"Resources\detection.jpg")
        img2=img2.resize((550,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        #f_lbl.place(x=0,y=0,width=550,height=130)

        #bg Image
        bg=Image.open(r"Resources\building1.jpg")
        bg=bg.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="BIOMETRIC BASED ATTENDANCE SYSTEM",font=("times new roman",36,"bold"),bg="White",fg="red")
        title_lbl.place(x=0,y=0,width=1535,height=45)

        # Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times bew roman",15,"bold"),background='white',foreground='darkblue')
        lbl.place(x=20,y=0,width=120,height=50)
        time()

        #Student Button
        st_img=Image.open(r"Resources\student.jpg")
        st_img=st_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(st_img)

        st_btn=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        st_btn.place(x=200,y=100,width=220,height=220)

        st_btn_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        st_btn_1.place(x=200,y=300,width=220,height=40)

        #Detect face Button
        face_detect_img=Image.open(r"Resources\facial_recognition_system.png")
        face_detect_img=face_detect_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(face_detect_img)

        detect_btn=Button(bg_img,image=self.photoimg5,command=self.face_detector,cursor="hand2")
        detect_btn.place(x=500,y=100,width=220,height=220)

        detect_btn_1=Button(bg_img,text="Face Detector",command=self.face_detector,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        detect_btn_1.place(x=500,y=300,width=220,height=40)

         #Attendance Button
        attendance_img=Image.open(r"Resources\attandence.jpeg")
        attendance_img=attendance_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(attendance_img)

        attendance_btn=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        attendance_btn.place(x=800,y=100,width=220,height=220)

        attendance_btn_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        attendance_btn_1.place(x=800,y=300,width=220,height=40)

         #Help Button
        help_img=Image.open(r"Resources\help.png")
        help_img=help_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(help_img)

        help_btn=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        help_btn.place(x=1100,y=100,width=220,height=220)

        help_btn_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        help_btn_1.place(x=1100,y=300,width=220,height=40)

         #Train face Button
        train_img=Image.open(r"Resources\facial_recognition.jpg")
        train_img=train_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(train_img)

        train_btn=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        train_btn.place(x=200,y=380,width=220,height=220)

        train_btn_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        train_btn_1.place(x=200,y=580,width=220,height=40)

         #Photos face Button
        photo_img=Image.open(r"Resources\photos.jpeg")
        photo_img=photo_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(photo_img)

        photo_btn=Button(bg_img,command=self.open_img,image=self.photoimg9,cursor="hand2")
        photo_btn.place(x=500,y=380,width=220,height=220)

        photo_btn_1=Button(bg_img,command=self.open_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        photo_btn_1.place(x=500,y=580,width=220,height=40)

        #developer Button
        developer_img=Image.open(r"Resources\group1.jpeg")
        developer_img=developer_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(developer_img)

        developer_btn=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        developer_btn.place(x=800,y=380,width=220,height=220)

        developer_btn_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        developer_btn_1.place(x=800,y=580,width=220,height=40)

        #Exit Button
        exit_img=Image.open(r"Resources\exit_btn.jpg")
        exit_img=exit_img.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(exit_img)

        exit_btn=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        exit_btn.place(x=1100,y=380,width=220,height=220)
 
        exit_btn_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        exit_btn_1.place(x=1100,y=580,width=220,height=40)

    #Open Photos Function
    def open_img(self):
        os.startfile("Data")

    #Exit
    def iExit(self):
        self.iExit=tk.messagebox.askyesno("Biometric Attendance System","Are you Sure Exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    

    #Function Buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_detector(self): 
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    
    def attendance_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    


    



if __name__=="__main__":
    root=Tk()
    obj=Biometric_based_attendance_system(root)
    root.mainloop()