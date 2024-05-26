from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import re


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
            messagebox.showerror("Error", "Please enter a valid email address.")
            return False

    def validate_contact(self):
        contact = self.var_contact.get()
        if re.match(r'^\d{10}$', contact):
            return True
        else:
            messagebox.showerror("Error", "Please enter a valid 10-digit contact number.")
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
                conn = mysql.connector.connect(host="localhost", user="root1", password="4381", database="today")
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


if __name__ == "__main__":
    root1 = Tk()
    app = Register(root1)
    root1.mainloop()
