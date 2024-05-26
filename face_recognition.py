from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1400x700+0+0")               #  the size of Screen display
        self.root.title("face Recognition System")

        title_lb1 = Label(self.root,text="FACE RECOGNITION ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1400,height=45)
        
        # 1 image
        img_top = Image.open(r"D:\face2\images\29.jpg")
        img_top = img_top.resize((600,650),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x =0,y=45, width=600,height=650)      

        # 2 image
        img_bottom = Image.open(r"D:\face2\images\28.jpg")
        img_bottom = img_bottom.resize((900,650),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x =600,y=45, width=900,height=650) 
        

        # Button
        b1_1 = Button(f_lb1,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",14,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=355,y=570,width=200,height=40)

        #============ attendence ====================
    def mark_attendance(self,i,r,n,d):
        with open("skyy.csv","r+",newline="\n") as f:
            myDataList =f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and(n not in name_list) and(d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},preset")




        #============ face recognition ====================
    
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn =mysql.connector.connect(host="localhost",username="root",password="4381",database="today")
                
                
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n =my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r =my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d =my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i =my_cursor.fetchone()
                i="+".join(i)


                # if confidence>82:
                if confidence>82:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]    #h

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
