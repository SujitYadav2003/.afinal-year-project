from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")              
        self.root.title("face Recognition System")


        title_lb1 = Label(self.root,text="HELP ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1400,height=45)
        
        # 1 image
        img_top = Image.open(r"D:\face2\images\12.jpg")
        img_top = img_top.resize((1380,650),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x =0,y=50, width=1380,height=650)  


        dev_label=Label(f_lb1,text="Email:sujitkanhaiyalalyadav@gmail.com",font=('times new roman',30,'bold'),fg="blue",bg='white')
        dev_label.place(x=250,y=250)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()

