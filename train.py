from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")               #  the size of Screen display
        self.root.title("face Recognition System")

        title_lb1 = Label(self.root,text="TRAIN DATA SET ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1400,height=45)
         # top image
        img_top = Image.open(r"D:\face2\images\24.jpg")
        img_top = img_top.resize((1400,350),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x =0,y=45, width=1400,height=350)      #chanage is making a height
        
        # Button
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1440,height=60)
        

        # bottton image
        img_bottom = Image.open(r"D:\face2\images\27.jpg")
        img_bottom = img_bottom.resize((1400,325),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x =0,y=440, width=1400,height=325)   

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')    #  gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])               #id=int(os.path.split(image)[-1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ================== Train the classifier and save ================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!",parent=self.root)  # make a change parent=self.root


           






if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
