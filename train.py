from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import pymysql
import cv2 #pip install opencv-python
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root,text="Photo Sample Training",font=("times bew roman",36,"bold"),bg="White",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=46)
        
        #Back Button
        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=18,font=("times new roman",13,"bold"),relief=RIDGE,bg="white",fg="red")
        back_btn.place(x=1390,y=0,width=120,height=40)

        img_top=Image.open(r"Resources\scan.jpeg")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        top_img_lbl=Label(self.root,image=self.photoimg_top)
        top_img_lbl.place(x=0,y=55,width=1530,height=325)

        train_btn=Button(self.root,text="Train Data",command=self.Train_classifier,cursor="hand2",font=("times bew roman",30,"bold"),bg="darkblue",fg="white")
        train_btn.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open(r"Resources\face-identification.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        bottom_img_lbl=Label(self.root,image=self.photoimg_bottom)
        bottom_img_lbl.place(x=0,y=440,width=1530,height=325)
    
    def Train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Gray Scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!",parent=self.root)
    
    def return_main(self):
        self.root.destroy()
    
            





if __name__=="__main__":
    
    root=Tk()
    obj=Train(root)
    root.mainloop()
