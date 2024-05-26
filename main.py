import tkinter
from tkinter import*
import tkinter as tk

# from tkinter import ttk
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

    



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

