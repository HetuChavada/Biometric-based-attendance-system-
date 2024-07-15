from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import pymysql
import cv2 #pip install opencv-python

class Help:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root,text="  Help Desk",font=("times bew roman",36,"bold"),bg="White",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=46)

         #Back Button
        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=18,font=("times new roman",13,"bold"),relief=RIDGE,bg="white",fg="darkblue")
        back_btn.place(x=1390,y=0,width=120,height=40)

        img_top=Image.open(r"Resources\helpdesk.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        top_img_lbl=Label(self.root,image=self.photoimg_top)
        top_img_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(top_img_lbl,text="Support:Hetal.chavada122337@marwadiuniversity.ac.in",font=("times new roman",18,"bold"),fg="darkblue",bg="white")
        dev_label.place(x=510,y=45)

    
    
    def return_main(self):
        self.root.destroy()


if __name__=="__main__": 
    root=Tk()
    obj=Help(root)
    root.mainloop()