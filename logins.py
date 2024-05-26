import tkinter
from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import re




def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1560x800+0+0")
        # self.root.geometry("1400x700+0+0")

        self.bg=ImageTk.PhotoImage(file=r"D:\z\trial3\image\lo.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="black")
        frame.place(x=550 , y=170,width=340,height=450)

        img1=Image.open(r'D:\z\trial3\image\icon.png')
        img1=img1.resize((100, 100) , Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg= "black",borderwidth=0)
        lblimg1.place(x=675,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg= "black")
        get_str.place(x=95,y=100)

        # label making
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg= "black")
        username.place(x=65, y= 155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40, y=180, width=270)

# password code
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg= "black")
        password.place(x=65, y= 225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40, y=250, width=270)


        # =========== ICON Image ========
        img2=Image.open(r'D:\z\trial3\image\icon.png')
        img2=img2.resize((25, 25) , Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2,bg= "black",borderwidth=0)
        lblimg2.place(x=590,y=323,width=25,height=25)

        img3=Image.open(r'D:\z\trial3\image\pass.png')
        img3=img3.resize((25, 25) , Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3,bg= "black",borderwidth=0)
        lblimg3.place(x=590,y=395,width=25,height=25)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=105,y=300,width=110,height=35)

        # registation
        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        # forget password
        forgetbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0 ,bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=370,width=160)
      

    #   =========   conneting the registor page================
    def rigister_window(self):
        # self.new_window = Toplevel(self.new_window)
        self.new_window = Toplevel(self.root)
        # self.new_window = Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required.")
        elif self.txtuser.get()=="sujit" and self.txtpass.get()=="sky":
           messagebox.showinfo("Success","Welcome")
        else:
            # messagebox.showerror("Invalid","Invalid Username And Password")
            conn=mysql.connector.connect(host="localhost",user="root",password="4381",database="today")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()

 

                                                                                       ))
            
            row=my_cursor.fetchone()
        if row == None:
                messagebox.showerror("Error","Invalid Username & Password")
        else:
                open_main=messagebox.askyesno("YesNO","Access only Admin")
                if open_main>0:
                    # self.new_window=Toplevel(self.new_window)
                    self.new_window = Toplevel(self.root)     
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()


# =================== Reset Password ======================
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror('Security Question','Please select a Security question',parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Entered the new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="4381",database="today")
            my_cursor=conn.cursor() 
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s ")
            # vlaue=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security())
            value=(self.txtuser.get(), self.combo_securiy_Q.get(), self.txt_security.get())

            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showinfo("Info","User please fill the correct Information",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password has been changed Successfully",parent=self.root2)
                self.root2.destroy()


# ====================== forget passwords ==================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="4381",database="today")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                # messagebox.showerror("Error","Email is not registered","Please Entered the Email")
                messagebox.showerror("Error", "Email is not registered\nPlease enter the Email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+545+170")

                
                # l= Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white").pack(anchor='white')
                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2, text="Select Security Question: ",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50, y=80)

                self.combo_securiy_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state='readonly')
                self.combo_securiy_Q['values']=( "Select" , "Your Birth Place","Your Mother name", "Your Pet Name")
                self.combo_securiy_Q.place(x=50, y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A = Label(self.root2,text="Security Answer", font=("times new roman", 15,"bold"), bg="white",fg="black")
                security_A.place(x=50, y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50, y=180,width=250)

                new_password = Label(self.root2,text="New Password", font=("times new roman", 15,"bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50, y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100, y=290)


            # registation 




            # change making

class Register:
    def __init__(self, root1):
        self.root1 = root1
        self.root1.title("Register")
        self.root1.geometry("1650x900+0+0")

        # ================= Variable for text data ==========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background image
        self.bg = ImageTk.PhotoImage(file=r"D:\z\trial3\image\re.jpg")
        bg_lb1 = Label(self.root1, image=self.bg)
        bg_lb1.place(x=0, y=0, relwidth=1, relheight=1)

        # left image of background
        self.bg1 = ImageTk.PhotoImage(file=r"D:\z\trial3\image\bg1.jpg")
        left_lb1 = Label(self.root1, image=self.bg1)
        left_lb1.place(x=50, y=100, width=470, height=550)

        # ==============main frame===============
        frame = Frame(self.root1, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lb1 = Label(frame, text="Registration", font=('times new roman', 20, "bold"), fg="darkgreen", bg="white")
        register_lb1.place(x=20, y=20)

        # =========== label entry ==============

        # row -1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # ============ row 2 ============

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # =========== row 3 ===============

        security_Q = Label(frame, text="Select Security Question: ", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_securiy_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state='readonly')
        self.combo_securiy_Q['values'] = ("Select", "Your Birth Place", "Your Mother name", "Your Pet Name")
        self.combo_securiy_Q.place(x=50, y=270, width=250)
        self.combo_securiy_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ===============row4======================

        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # =============== checkbutton ==============
        self.var_check = IntVar()  # check value variable
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Term & condition", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # ======== button ============
        img = Image.open(r"D:\z\trial3\image\bgReg.JPG")
        img = img.resize((200, 55), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"D:\z\trial3\image\lgin2.jpg")
        img1 = img1.resize((200, 55), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, command=self.login_destroy, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b2.place(x=330, y=420, width=200)

    def validate_email(self):
        email = self.var_email.get()
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return True
        else:
            messagebox.showerror("Error", "Please enter a valid email address.",parent=self.root1)
            return False

    def validate_contact(self):
        contact = self.var_contact.get()
        if re.match(r'^\d{10}$', contact):
            return True
        else:
            messagebox.showerror("Error", "Please enter a valid 10-digit contact number.",parent=self.root1)
            return False

    def login_destroy(self):
        self.root1.destroy()

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required.", parent=self.root1)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password do not match.", parent=self.root1)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree with the terms & conditions.", parent=self.root1)
        elif not self.validate_email() or not self.validate_contact():
            return  # Stop further execution if email or contact is invalid
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="4381", database="today")
                my_cursor = conn.cursor()
                
                # Check if email already exists
                query = ("SELECT * FROM register WHERE email = %s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                
                if row is not None:
                    messagebox.showerror("Error", "User already exists. Please use another email.", parent=self.root1)
                else:
                    # Insert new user data
                    insert_query = ("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)")
                    insert_values = (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                    )
                    my_cursor.execute(insert_query, insert_values)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Successfully Saved", parent=self.root1)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root1)


        
# ============= destroy login Button ========================
    def return_login(self):
        self.root.destroy()
        

# =================== main code ========================
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")               #  the size of Screen display
        self.root.title("face Recognition System")

        # image part
        #first images
        img1 = Image.open(r"D:\face2\images\2.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x =0,y=0, width=500,height=130)

        # Second Images
        img2 = Image.open(r"D:\face2\images\1.jpeg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2= ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x =500,y=0, width=500,height=130)

       # Third Images
        img3 = Image.open(r"D:\face2\images\3.jpg")
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

        title_lb1 = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1400,height=45)


        #================ time =========================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

            lbl=Label(title_lb1,font=('times new roman',14,'bold') ,background='white',foreground='blue')
            lbl.place(x=30,y=50,width=110,height=50)
            time()


        # student button
        img5 = Image.open(r"D:\face2\images\7.jpg")
        img5 = img5.resize((220,190),Image.ANTIALIAS)
        self.photoimg5= ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")  #change done
        b1.place(x =100,y=75,width=220,height=190)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=250,width=220,height=40)

        # Detect face button 
        img6 = Image.open(r"D:\face2\images\8.jpg")
        img6 = img6.resize((220,190),Image.ANTIALIAS)
        self.photoimg6= ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x =400,y=75,width=220,height=190)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=250,width=220,height=40)

        # Attendence face button 
        img7 = Image.open(r"D:\face2\images\5.jpg")
        img7 = img7.resize((220,190),Image.ANTIALIAS)
        self.photoimg7= ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7)
        b1.place(x =700,y=75,width=220,height=190)

        b1_1 = Button(bg_img,text="Attendences",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=250,width=220,height=40)

        

        # Help Desk button 
        img8 = Image.open(r"D:\face2\images\9.jpg")
        img8 = img8.resize((220,190),Image.ANTIALIAS)
        self.photoimg8= ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x =1000,y=75,width=220,height=190)

        b1_1 = Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=250,width=220,height=40)




        # Train data  button
        img9 = Image.open(r"D:\face2\images\17.jpeg")
        img9 = img9.resize((220,190),Image.ANTIALIAS)
        self.photoimg9= ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data,)
        b1.place(x =100,y=325,width=220,height=190)

        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=500,width=220,height=40)



        # photo for data
        img10 = Image.open(r"D:\face2\images\11.jpg")
        img10 = img10.resize((220,190),Image.ANTIALIAS)
        self.photoimg10= ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x =400,y=325,width=220,height=190)

        b1_1 = Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=500,width=220,height=40)


        # Developer button
        img11 = Image.open(r"D:\face2\images\12.jpg")
        img11 = img11.resize((220,190),Image.ANTIALIAS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,command=self.developer_data,)
        b1.place(x =700,y=325,width=220,height=190)

        b1_1 = Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=500,width=220,height=40)


        # Exit Button
        img12 = Image.open(r"D:\face2\images\16.png")
        img12 = img12.resize((220,190),Image.ANTIALIAS)
        self.photoimg12= ImageTk.PhotoImage(img12)

        b1 = Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x =1000,y=325,width=220,height=190)

        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=500,width=220,height=40)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


   

   # ================ Function Button ==================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

#=============================================  training Data =================================
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

#=============================================  face recongniion Data =================================
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

#=============================================  attendance display=================================
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Developer(self.new_window)

        #=============================================  help display=================================
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Help(self.new_window)

    




        

if __name__=="__main__":
    main()
    # root=Tk()
    # app=Login_Window(root)
    # root.mainloop()
