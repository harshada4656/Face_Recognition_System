from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION ",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=45)


        #first image
        img_top=Image.open(r"collage_image\recognition.jpg.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #second image
        img_bottom=Image.open(r"collage_image\recognition1.jpg.jpg")
        img_bottom=img_bottom.resize((850,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=850,height=700)

        #button
        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="darkblue",fg="yellow")
        b1.place(x=350,y=580,width=200,height=40)


    #===================Attendance====================
    def mark_attendance(self,n,r,d,i):
        with open("Marc.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list) and (r not in name_list) and (d not in name_list) and (i not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{r},{d},{i},{dtString},{d1},Present")   





    #===============face recognition==============
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="n".join(n)

                my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="r".join(r)

                my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="d".join(d)

                my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="i".join(i)

                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID:{i}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,r,d,i)
                   
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)

                coord=[x,y,w,y] 

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
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()    



if  __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()        