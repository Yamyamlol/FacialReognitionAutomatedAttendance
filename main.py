from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import student_details



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Match")
        
        # bg image
        bgimg = Image.open("D:\Coding\mini project\images\Vector_2640.jpg")
        bgimg = bgimg.resize((1920,1080),Image.ANTIALIAS)
        # antialias isn't used anymore but i am using an older version of pillow
        self.photobgimg = ImageTk.PhotoImage(bgimg)
        
        bg_img = Label(self.root, image = self.photobgimg)
        bg_img.place(x=0,y=0,width = 1920, height = 1080)
        
        title_lbl = Label(bg_img, text="ATTENDANCE", font=("Satoshi-Bold", 35, "bold"), fg='black')
        title_lbl.place( x = 570, y = 25, width = 400, height = 45,)
        
        # stduent button
        stuimg = Image.open("D:\Coding\mini project\images\student.jpg")
        stuimg = stuimg.resize((220,220),Image.ANTIALIAS)
        self.photostuimg = ImageTk.PhotoImage(stuimg)

        b1 = Button(bg_img,command = self.student_detail, image = self.photostuimg, cursor = "hand2",bg = "black", fg = "black")
        b1.place(x = 220, y = 100, width = 220, height = 220)
        
        b1_1 = Button(bg_img,command = self.student_detail, text = "Student Data", cursor = "hand2", font=("Satoshi-Bold", 15, "bold"), fg =  "black" )
        b1_1.place(x = 220, y = 320, width = 220, height = 40)
        
        # new face button
        facepng = Image.open("D:\Coding\mini project\images\cial-recognition.png")
        facepng = facepng.resize((220, 220), Image.ANTIALIAS)
        self.photofacepng = ImageTk.PhotoImage(facepng)
        
        b2 = Button(bg_img, image = self.photofacepng, cursor = "hand2",)
        b2.place(x = 660, y = 100, width = 220, height = 220)
        
        b2_2 = Button(bg_img, text = "Facial Match", cursor = "hand2", font=("Satoshi-Bold", 15, "bold"), fg =  "black" )
        b2_2.place(x = 660, y = 320, width = 220, height = 40)
        
        # attendance button
        attendancebutton = Image.open("D:\Coding\mini project\images\\attendance-icon-11.jpg")
        attendancebutton = attendancebutton.resize((220, 220), Image.ANTIALIAS)
        self.photoattendancebutton = ImageTk.PhotoImage(attendancebutton)
        
        b3 = Button(bg_img, image = self.photoattendancebutton, cursor = "hand2",)
        b3.place(x = 1110, y = 100, width = 220, height = 220)
        
        b3_2 = Button(bg_img, text = "Attendance summary", cursor = "hand2", font=("Satoshi-Bold", 15, "bold"), fg =  "black" )
        b3_2.place(x = 1110, y = 320, width = 220, height = 40)
        
        # train button
        trainbutton = Image.open("D:\Coding\mini project\images\pngwing.com.png")
        trainbutton = trainbutton.resize((220, 220), Image.ANTIALIAS)
        self.phototrainbutton = ImageTk.PhotoImage(trainbutton)
        
        b4 = Button(bg_img, image = self.phototrainbutton, cursor = "hand2",)
        b4.place(x = 220, y = 420, width = 220, height = 220)
        
        b4_2 = Button(bg_img, text = "Train", cursor = "hand2", font=("Satoshi-Bold", 15, "bold"), fg =  "black" )
        b4_2.place(x = 220, y = 640, width = 220, height = 40)

        # photos button
        photosbutton = Image.open("D:\Coding\mini project\images\pngwing.com (1).png")
        photosbutton = photosbutton.resize((220, 220), Image.ANTIALIAS)
        self.photophotosbutton = ImageTk.PhotoImage(photosbutton)
        
        b5 = Button(bg_img, image = self.photophotosbutton, cursor = "hand2",)
        b5.place(x = 660, y = 420, width = 220, height = 220)
        
        b5_2 = Button(bg_img, text = "Photos", cursor = "hand2", font=("Satoshi-Bold", 15, "bold"), fg =  "black" )
        b5_2.place(x = 660, y = 640, width = 220, height = 40)

        # exit button
        exitbutton = Image.open("D:\Coding\mini project\images\pngwing2.com.png")
        exitbutton = exitbutton.resize((220, 220), Image.ANTIALIAS)
        self.exitbutton = ImageTk.PhotoImage(exitbutton)
        
        b6 = Button(bg_img, image = self.exitbutton, cursor = "hand2",)
        b6.place(x = 1110, y = 420, width = 220, height = 220)
        
        b6_2 = Button(bg_img, text = "Exit", cursor = "hand2", font=("Satoshi-Bold", 15, "bold"), fg =  "black" )
        b6_2.place(x = 1110, y = 640, width = 220, height = 40)
        
    
    # *************** BUTTON FUNCTIONALITY ***************
    #         also import the class from the file first
    def student_detail(self):
        self.NewWindow = Toplevel(self.root)
        self.app = student_details(self.NewWindow)





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()