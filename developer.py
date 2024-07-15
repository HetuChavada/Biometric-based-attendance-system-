from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import pymysql
import cv2 #pip install opencv-python

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root,text="DEVELOPER INFORMATION",font=("times bew roman",36,"bold"),bg="White",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=46)

         #Back Button
        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=18,font=("times new roman",13,"bold"),relief=RIDGE,bg="white",fg="darkblue")
        back_btn.place(x=1390,y=0,width=120,height=40)


        img_top=Image.open(r"Resources\istockphoto.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        top_img_lbl=Label(self.root,image=self.photoimg_top)
        top_img_lbl.place(x=0,y=55,width=1530,height=720)

        # Main Frame
        main_frame=Frame(top_img_lbl,bd=2,bg="black")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_right=Image.open(r"Resources\group1.jpeg")
        img_right=img_right.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        right_img_lbl=Label(main_frame,image=self.photoimg_right)
        right_img_lbl.place(x=300,y=0,width=200,height=200)

        #Developer Info
        dev_label=Label(main_frame,text="Hello My Name is , Hetal.",font=("times new roman",16,"bold"),fg="white",bg="black")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text=" I'm Mca Student. ",font=("times new roman",16,"bold"),fg="blue",bg="black")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="Proficient in programming ",font=("times new roman",16,"bold"),fg="white",bg="black")
        dev_label.place(x=0,y=80)

        
        dev_label=Label(main_frame,text="languages such as Python,",font=("times new roman",16,"bold"),fg="white",bg="black")
        dev_label.place(x=0,y=120)

        dev_label=Label(main_frame,text="java and c++.",font=("times new roman",16,"bold"),fg="white",bg="black")
        dev_label.place(x=0,y=160)

        img2=Image.open(r"Resources\books.jpg")
        img2=img2.resize((550,390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=550,height=390)

    
    def return_main(self):
        self.root.destroy()

        



if __name__=="__main__": 
    root=Tk()
    obj=Developer(root)
    root.mainloop()