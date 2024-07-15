from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import pymysql
from time import strftime
from datetime import datetime
import cv2 #pip install opencv-python
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times bew roman",36,"bold"),bg="White",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=46)

         #Back Button
        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=18,font=("times new roman",13,"bold"),relief=RIDGE,bg="white",fg="darkblue")
        back_btn.place(x=1390,y=0,width=120,height=40)

        # First Image
        img_top=Image.open(r"Resources\facial_recognition.jpg")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        top_img_lbl=Label(self.root,image=self.photoimg_top)
        top_img_lbl.place(x=0,y=55,width=650,height=700)
        
        # Second Image
        img_bottom=Image.open(r"Resources\facial_recognition_system.png")
        img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        bottom_img_lbl=Label(self.root,image=self.photoimg_bottom)
        bottom_img_lbl.place(x=650,y=55,width=950,height=700)

        #Button
        train_btn=Button(bottom_img_lbl,text="Face Detector",command=self.face_recog,cursor="hand2",font=("times bew roman",18,"bold"),bg="darkblue",fg="white")
        train_btn.place(x=365,y=620,width=200,height=40)

        #Footer Label
        title_lbl=Label(self.root,text="Frontal Face Detector",font=("times bew roman",18,"bold"),bg="White",fg="darkblue")
        title_lbl.place(x=0,y=755,width=1530,height=30)

    # Attendance
    def mark_attendance(self,i,r,n,d):
        with open("Student.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%D/%M/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")




    # Face Recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_imgage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_imgage,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_imgage[y:y+h,x:x+w])  
                confidence=int((100*(1-predict/300))) 

                conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                    
                my_cursor.execute("select Roll from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dept from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>70:
                    cv2.putText(img,f"ID:{i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
                
            return coord
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
    
    
    def return_main(self):
        self.root.destroy()

                        
    
            





if __name__=="__main__":
    
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
