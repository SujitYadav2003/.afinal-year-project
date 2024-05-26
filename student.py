from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")               #  the size of Screen display
        self.root.title("face Recognition System")


        # =============== variable decleration for a Database=================
        self.var_dep= StringVar()
        self.var_course = StringVar()
        self.var_year= StringVar()
        self.var_semester= StringVar()    #check
        self.var_std_id= StringVar()
        self.var_std_name = StringVar()
        self.var_div= StringVar()
        self.var_roll= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()
        


        #first images
        img1 = Image.open(r"D:\face2\images\20.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x =0,y=0, width=500,height=130)

        # Second Images
        img2 = Image.open(r"D:\face2\images\18.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2= ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x =500,y=0, width=500,height=130)

       # Third Images
        img3 = Image.open(r"D:\face2\images\19.jpg")
        img3 = img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3= ImageTk.PhotoImage(img3)

        f_lb1 = Label(self.root,image=self.photoimg3)
        f_lb1.place(x =1000,y=0, width=500,height=130)

        # BackGround Images
        img4 = Image.open(r"D:\face2\images\4.jpg")
        img4 = img4.resize((1400,700),Image.ANTIALIAS)
        self.photoimg4= ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x =0,y=130, width=1400,height=700)

        title_lb1 = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1400,height=45)

        # making  a frame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1330,height=510)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=2,width=650,height=500)

        img_left = Image.open(r"D:\face2\images\22.jpg")
        img_left = img_left.resize((635,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb1 = Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x =5,y=0, width=635,height=70)      #chanage is making a height

        #current Course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=75,width=635,height=100)
        
        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=6,sticky=W)
       
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)           #width=17
        dep_combo["values"] =("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=7,sticky=W)

         # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2, padx=2,sticky=W)
       
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)          
        course_combo["values"] =("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=7,sticky=W)


        #years
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0, padx=10,sticky=W)
       
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)          
        year_combo["values"] =("Select Yaer","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=7,sticky=W)

         #Semesters
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2, padx=10,sticky=W)
       
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)          
        semester_combo["values"] =("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        # class Student INformation
        class_Student_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_course_frame.place(x=5,y=180,width=635,height=290)
        

        # student Id
        studentId_label=Label(class_Student_course_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0, padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        studentName_label=Label(class_Student_course_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2, padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         # class Division
        class_div_label=Label(class_Student_course_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0, padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_course_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)          
        div_combo["values"] =("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no_label=Label(class_Student_course_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2, padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_Student_course_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0, padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_course_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)          
        gender_combo["values"] =("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #DoB
        dob_label=Label(class_Student_course_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2, padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_Student_course_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0, padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone no
        phone_label=Label(class_Student_course_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2, padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_Student_course_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0, padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teachers
        teacher_label=Label(class_Student_course_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2, padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_course_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio Buttons
        self.var_radio1= StringVar()  # radio variable decleration
        radiobtn1= ttk.Radiobutton(class_Student_course_frame,variable=self.var_radio1,text="take Photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)


        # self.var_radio2= StringVar()  # radio variable decleration
        radiobtn2 =ttk.Radiobutton(class_Student_course_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # button frame
        btn_frame = Frame(class_Student_course_frame,bd=2,relief=RIDGE,bg="white")
        # btn_frame.place(x=0,y=200,width=618,height=35)  # OLD
        btn_frame.place(x=0,y=200,width=650,height=35) 


        save_btn =Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn =Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn =Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn =Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # take_photo_btn =Button(btn_frame,text="Take Photo Sample",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # take_photo_btn.grid(row=1,column=0)

        btn_frame1 = Frame(class_Student_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=650,height=35)

        take_photo_btn =Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=69,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=1)

        # update_photo_btn =Button(btn_frame1,text="Update Photo Sample",width=34,font=("times new roman",12,"bold"),bg="blue",fg="white")
        # update_photo_btn.grid(row=0,column=1)




        #Right label frame box
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=2,width=650,height=500)
        #Right_frame.place(x=670,y=10,width=650,height=480)


        img_right = Image.open(r"D:\face2\images\23.jpg")
        img_right = img_right.resize((635,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lb1 = Label(Right_frame,image=self.photoimg_right)
        f_lb1.place(x =5,y=0, width=635,height=70)      #chanage is making a height

        # =================== Search System =================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Systen",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=75,width=635,height=65)

        search_label=Label(Search_frame,text="Search By",font=("times new roman",14,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0, padx=10,pady=5,sticky=W)

        #          Searching new code added
        self.search_var = StringVar()

        search_combo=ttk.Combobox(Search_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),state="readonly",width=17)
        # changing the rollno name Roll_No to roll_no        
        search_combo["values"] =("Select ","roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=7,sticky=W)
        # new lin added  self.txt_search = StringVar()

        self.txt_search = StringVar()

        search_entry=ttk.Entry(Search_frame,textvariable=self.txt_search,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn =Button(Search_frame,text="Search",command=self.search,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn =Button(Search_frame,text="Show All",command=self.fetch_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

          # =================== TABLE FRAME =================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=145,width=635,height=300)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
         
        # setting the width

        self.student_table.column("dep",width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ================== function decleration ==============



        # ====================== function Decelerations for email and mobile number ================

    def validate_email(self):
        email = self.var_email.get()
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return True
        else:
            messagebox.showerror("Error", "Please enter a valid email address.",parent=self.root)
            return False
        
    def validate_contact(self):
        contact = self.var_phone.get()
        if contact.isdigit() and len(contact) == 10:
            return True
        else:
            messagebox.showerror("Error", "Please enter a valid 10-digit contact number.",parent=self.root)
            return False
        

       #==========Error for data is not fill ==============
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not self.validate_email():
            pass
        elif not self.validate_contact():
            pass
        else:
            try:
                conn =mysql.connector.connect(host="localhost",username="root",password="4381",database="today")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                    self.var_dep.get(),
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
                messagebox.showinfo("Success","Student Detail has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   


    #===================== fetch data ======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="4381",database="today")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================= Get cusor ================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
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

    # ============= update function =============
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Student Update Page","Do you want to Update this student",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="4381",database="today")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                       self.var_dep.get(),
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
                                                                                                                                                                                       self.var_std_id.get()  # in the above code it va
                                                                                                                                                                                       ))
                else:
                 if not Upadate:
                  return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                  # ================Delete function=================
    def delete_data(self):
        if self.var_std_id.get()=="":   # it used the va
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="4381",database="today")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


#                                ====================== Reset =========================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set(" Select Course")
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


        #                             ================= new function adding using tut ========================



# trying somthing new 
    def search(self):
     conn = mysql.connector.connect(host="localhost", username="root", password="4381", database="today")
     my_cursor = conn.cursor()

     search_column = self.search_var.get()
     search_value = self.txt_search.get()

     query = "SELECT * FROM student WHERE {} LIKE %s".format(search_column)
     my_cursor.execute(query, ('%' + search_value + '%',))

     rows = my_cursor.fetchall()

     if len(rows) != 0:
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=i)
        conn.commit()
     else:
        # Display a message when no results are found
        messagebox.showinfo("Not Found", "No records found with the specified criteria.",parent=self.root)

     conn.close()


    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="4381", database="today")
                my_cursor = conn.cursor()

                # Fetch the student ID entered in the Entry field
                student_id = self.var_std_id.get()

                # Update or insert student details based on the entered ID
                my_cursor.execute(
                    "SELECT * FROM student WHERE Student_id=%s", (student_id,)
                )
                result = my_cursor.fetchone()

                if result:
                    # Update existing student details
                    my_cursor.execute(
                        "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_dep.get(),
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
                            student_id
                        )
                    )
                else:
                    # Insert new student details
                    my_cursor.execute(
                        "INSERT INTO student (Student_id, Dep, course, Year, Semester, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            student_id,
                            self.var_dep.get(),
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
                        )
                    )

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    if len(faces) == 0:
                        return None
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed!!!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
 



