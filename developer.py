from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")              
        self.root.title("face Recognition System")


        title_lb1 = Label(self.root,text="DEVELOPER ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1400,height=45)
        
        # 1 image
        img_top = Image.open(r"D:\face2\images\12.jpg")
        img_top = img_top.resize((1380,650),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x =0,y=50, width=1380,height=650)  

        # making  a frame
        main_frame = Frame(f_lb1,bd=2,bg="white")
        main_frame.place(x=500,y=0,width=400,height=600)

        img_top1 = Image.open(r"image\sujit.jpg")
        img_top1 = img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lb1 = Label(main_frame,image=self.photoimg_top1)
        f_lb1.place(x =100,y=0, width=200,height=200)  

        # info_label=Label(main_frame,text="Hii I am Sujit Yadav",font=("times new roman",12,"bold"),bg="white")
        # info_label.place(X=0,y=210,height=200,width=100)
       

       # DEVELOPER INFO
        dev_label=Label(main_frame,text="Hello I am Sujit Yadav",font=('times new roman',20,'bold'),fg="blue",bg='white')
        dev_label.place(x=55,y=210)

        dev1_label=Label(main_frame,text="I am in BE Computer Engineering from Logmieer",font=('times new roman',13,'bold'),fg="blue",bg='white')
        dev1_label.place(x=0,y=270)

        



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
