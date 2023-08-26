from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x700+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="HELP DESK ",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        img_top=Image.open(r"collage_image\help1.jpg.jpg")
        img_top=img_top.resize((1550,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1550,height=650)

        dev_label=Label(f_lbl,text="Email:harshumane56@gmail.com",font=("times new roman",20,"bold"),fg="purple",bg="white")
        dev_label.place(x=530,y=260)
        



if  __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()         