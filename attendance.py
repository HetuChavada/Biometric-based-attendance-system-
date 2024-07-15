from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import pymysql
from time import strftime
from datetime import datetime
import cv2 #pip install opencv-python
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")

        # Variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #first Image
        img=Image.open(r"Resources\photos_scan.jpeg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second Image
        img1=Image.open(r"Resources\class.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #bg Image
        bg=Image.open(r"Resources\building1.jpg")
        bg=bg.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=206,width=1530,height=710)

        
        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM ",font=("times bew roman",36,"bold"),bg="White",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times bew roman",15,"bold"),background='white',foreground='darkblue')
        lbl.place(x=20,y=0,width=120,height=50)
        time()

        #Back Button
        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=18,font=("times new roman",13,"bold"),relief=RIDGE,bg="white",fg="darkblue")
        back_btn.place(x=1390,y=0,width=120,height=40)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=520)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"),fg="red")
        Left_frame.place(x=10,y=10,width=780,height=500)

        img_left=Image.open(r"Resources\class.jpg")
        img_left=img_left.resize((770,120),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=770,height=120)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=770,height=180)

        #Label & Entry

        #Attendance ID
        attendanceId_label=Label(left_inside_frame,text="AttendanceId: ",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Roll
        roll_label=Label(left_inside_frame,text="Roll: ",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Name
        name_label=Label(left_inside_frame,text="Name: ",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name_entry.grid(row=1,column=1,padx=10,sticky=W)

        #Department
        dept_label=Label(left_inside_frame,text="Department: ",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_dept_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dept_entry.grid(row=1,column=3,padx=10,sticky=W)

        #Time
        time_label=Label(left_inside_frame,text="Time: ",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time_entry.grid(row=2,column=1,padx=10,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text="Date: ",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        atten_date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date_entry.grid(row=2,column=3,padx=10,sticky=W)
        
        
        #Attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font=("times new roman",12,"bold"))
        attendanceLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=18,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=10,sticky=W)
        self.atten_status.current(0)
        
        #Buttons Frame
        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=26,y=360,width=717,height=42)

        #import csv Button
        import_csv_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        import_csv_btn.grid(row=0,column=0)

         #export csv Button
        export_csv_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=18,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        export_csv_btn.grid(row=0,column=1)

         #update  Button
        #update_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",13,"bold"),bg="white",fg="darkblue")
        #update_btn.grid(row=0,column=2)

         #Reset Button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        reset_btn.grid(row=0,column=3)

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),fg="red")
        Right_frame.place(x=800,y=10,width=670,height=500)

        #Table Frame
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=656,height=465)

        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # Fetch Data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        #fln=filedialog.askopenfilename(initial=os.getcwd(),title="Open Csv",filetypes=("CSV File","*csv"),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")

    def return_main(self):
        self.root.destroy()


if __name__=="__main__":
    
    root=Tk()
    obj=Attendance(root)
    root.mainloop()