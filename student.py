from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
from time import strftime
from datetime import datetime
import pymysql
import cv2 #pip install opencv-python

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Biometric Based Attendance System")
        self.root.geometry("1530x790+0+0")

        #Varaibles
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


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

        #bg Image
        bg=Image.open(r"Resources\building1.jpg")
        bg=bg.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times bew roman",36,"bold"),bg="White",fg="darkblue")
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
        back_btn=Button(title_lbl,text="Back",command=self.return_main,width=18,font=("times new roman",13,"bold"),relief=RIDGE,bg="white",fg="red")
        back_btn.place(x=1390,y=0,width=120,height=40)



        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="red")
        Left_frame.place(x=10,y=10,width=780,height=580)

        img_left=Image.open(r"Resources\class.jpg")
        img_left=img_left.resize((770,120),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=770,height=120)

        #Current Course Information

        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",fg="green",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=115,width=770,height=110)

        #Department
        dep_label=Label(Current_course_frame,text="Department : ",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width=20,state="readonly")
        dept_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(Current_course_frame,text="Course : ",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(Current_course_frame,text="Year : ",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(Current_course_frame,text="Semester : ",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student Class Information

        student_class_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Class information",fg="green",font=("times new roman",12,"bold"))
        student_class_frame.place(x=5,y=225,width=770,height=330)

        #Student ID
        studentId_label=Label(student_class_frame,text="StudentID: ",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(student_class_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        
        #Student Name
        studentName_label=Label(student_class_frame,text="Student Name: ",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(student_class_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        class_div_label=Label(student_class_frame,text="Class Division: ",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(student_class_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(student_class_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        class_div_combo["values"]=("Select Division ","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=6,sticky=W)

        #Roll No
        Roll_no_label=Label(student_class_frame,text="Roll No: ",font=("times new roman",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(student_class_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        Gender_label=Label(student_class_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #Gender_entry=ttk.Entry(student_class_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        Gender_combo=ttk.Combobox(student_class_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=6,sticky=W)

        #BirthDate
        dob_label=Label(student_class_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(student_class_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        Email_label=Label(student_class_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(student_class_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        PhoneNo_label=Label(student_class_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        PhoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        PhoneNo_entry=ttk.Entry(student_class_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        PhoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        Address_label=Label(student_class_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(student_class_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label=Label(student_class_frame,text="Teacher Name: ",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(student_class_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(student_class_frame,text="Take Photo Sample",value="Yes",variable=self.var_radio1)
        radiobtn1.grid(row=6,column=0)

        #self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(student_class_frame,text="No Photo Sample",value="NO",variable=self.var_radio1)
        radiobtn2.grid(row=6,column=1)

        #Buttons Frame
        btn_frame=Frame(student_class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=220,width=765,height=35)

        #Save Button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="darkblue")
        save_btn.grid(row=0,column=0)

         #Update Button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="darkblue")
        update_btn.grid(row=0,column=1)

         #Delete Button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="darkblue")
        delete_btn.grid(row=0,column=2)

         #Reset Button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="darkblue")
        reset_btn.grid(row=0,column=3)

        # take Photo Frame
        take_photo_frame=Frame(student_class_frame,bd=2,relief=RIDGE,bg="white")
        take_photo_frame.place(x=12,y=260,width=735,height=35)

        #Add photo Button
        Add_photo_btn=Button(take_photo_frame,command=self.generate_dataset,text="Add Photo Sample",width=72,font=("times new roman",13,"bold"),bg="white",fg="darkblue")
        Add_photo_btn.grid(row=0,column=0)

        
        #Update photo Button
        #update_photo_btn=Button(take_photo_frame,text="Update Photo Sample",width=37,font=("times new roman",13,"bold"),bg="white",fg="darkblue")
        #update_photo_btn.grid(row=0,column=1)

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="red")
        Right_frame.place(x=800,y=10,width=660,height=580)

        img_right=Image.open(r"Resources\class.jpg")
        img_right=img_right.resize((770,120),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=650,height=120)

        #Search System
        
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="View Student Details & Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=125,width=650,height=80)

        #Search Label
        search_label=Label(search_frame,text="Search By",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",12,"bold"),width=15,state="readonly")
        #search_combo["values"]=("Select Option","Roll_No","Phone_No","Student_id")
        search_combo["values"]=("Select Option","Roll","phone","student_id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)   

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

          #Search Button
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

          #Show All Button
        show_all_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=3)

         #Table Frame
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll",
                                                            "gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division") 
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100) 
        self.student_table.column("phone",width=100)  
        self.student_table.column("address",width=100) 
        self.student_table.column("teacher",width=100) 
        self.student_table.column("photo",width=115) 

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # Function Declaration
    
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Error","All Fields are Required !",parent=self.root)
        else:
            try:
              conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                              self.var_dept.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_std_id.get(),
                                                                                                              self.var_std_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get()
                                                                                                            ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Student Details has been added Successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    # Fetch Data
    def fetch_data(self):
      conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()

      if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
              self.student_table.insert("",END,values=i)
          conn.commit()
      conn.close()

    # get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #Update Function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","All Fields are Required !",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update Student Details ?",parent=self.root)
                if Upadate>0:
                     conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,name=%s,Division=%s,Roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,PhotoSample=%s where student_id=%s",(                                                                                                                                                                                                                              
                                                                                                              self.var_dept.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_std_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_std_id.get()                                                                                                                                                                                       
                                                                                                            ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details Successfully Updated.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    #Delete Function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be Required.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to Delete this Student ?",parent=self.root)
                if delete>0:
                  conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
                  my_cursor=conn.cursor()
                  sql="delete from student where student_id=%s"
                  val=(self.var_std_id.get(),)
                  my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted Student Details.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Reset Function
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #search Data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select Option!")
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+ " LIKE '%" +str(self.var_search.get())+ "%'")
                data=my_cursor.fetchall()
                #query = "SELECT * FROM student WHERE %s LIKE %s"
                #params = (self.var_com_search.get(), f"%{self.var_search.get()}%")
                #my_cursor.execute(query, params)
                #data = my_cursor.fetchall()                
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #Generate Data set & Take Photo samples
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_radio1.get()=="":
            messagebox.showerror("Error","All Fields are Required !",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",db="biometric_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dept=%s,course=%s,year=%s,semester=%s,name=%s,Division=%s,Roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,PhotoSample=%s where student_id=%s",(                                                                                                                                                                                                                              
                                                                                                              self.var_dept.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_std_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_std_id.get()==id+1                                                                                                                                                                                       
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #Load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==30:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complted!!!",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def return_main(self):
        self.root.destroy()

        
        
                
        
        


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()