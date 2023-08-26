from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="DEVELOPER ",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top=Image.open(r"collage_image\dev.jpg.jpg")
        img_top=img_top.resize((1550,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1550,height=650)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=500,height=600)

        img_top1=Image.open(r"collage_image\Photo.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=250,y=0,width=200,height=200)


        #developer info
        dev_label=Label(main_frame,text="hello my name,Harshada",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am TYIT Student",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img2=Image.open(r"collage_image\help.jpg.jpg")
        img2=img2.resize((460,360),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=220,width=460,height=360)












if  __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        