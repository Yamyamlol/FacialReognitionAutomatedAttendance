from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class student_details:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Match")
        
        
        # ********* VARIABLES *********
        self.VarDept = StringVar()
        self.VarCourse = StringVar()
        self.VarYear = StringVar()
        self.VarSem = StringVar()
        self.VarStuID = IntVar()
        self.VarName = StringVar()
        self.VarSec = StringVar()
        self.VarRoll = StringVar()
        self.VarGender = StringVar()
        self.VarDOB = StringVar()
        self.VarEmail = StringVar()
        self.VarPhone = StringVar()
        self.VarTeacher = StringVar()
        
        
        
        
        # bg image
        bgimg = Image.open("D:\Coding\mini project\images\Vector_2640.jpg")
        bgimg = bgimg.resize((1920,1080),Image.ANTIALIAS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)
        
        bg_img = Label(self.root, image = self.photobgimg)
        bg_img.place(x=0,y=0,width = 1920, height = 1080)
        
        title_lbl = Label(bg_img, text="Student Data", font=("Satoshi-Bold", 35, "bold"), fg='black')
        title_lbl.place( x = 570, y = 25, width = 400, height = 45,)
        
        
        main_frame = Frame(bg_img, bd = 2,bg = "white")
        main_frame.place(x=10, y = 100, width = 1500, height = 700)
        
        #left label frame
        Left_frame = LabelFrame(main_frame, bd = 5,bg = "white", relief = RIDGE, text = "Student details", font=("Satoshi-Bold", 25, "bold"), fg='black')
        Left_frame.place(x=5, y = 10,width = 740, height = 680)
        
        # current course
        current_course = LabelFrame(Left_frame, bd = 3, bg = "white", relief=RIDGE, text = "Current Course", font=("Satoshi", 17, "bold"), fg='black')
        current_course.place(x=5,y=5,width = 720, height= 200)
        

        # department selection dropbox
        department_label = Label(current_course, text = "Department",  font=("Satoshi-Bold", 13, "bold"), fg='black', bg = "white")
        department_label.grid(row = 0, column= 0, sticky = W)
        # sticky = W helps in left alligning the contents
        
        dep_combo = ttk.Combobox(current_course,textvariable=self.VarDept, font=("Satoshi-Bold", 13),width=17, state = "readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "Mechanical", "Electrical")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx = 2, pady = 20, sticky = W)


        # COURSE selection dropbox
        course_label = Label(current_course, text = "Course",  font=("Satoshi-Bold", 13, "bold"), fg='black', bg = "white")
        course_label.grid(row = 0, column= 2, sticky = W)
        
        course_combo = ttk.Combobox(current_course,textvariable=self.VarCourse ,font=("Satoshi-Bold", 13),width=17, state = "readonly")
        course_combo["values"] = ("Select Course", "Bachelor", "Master", "Diploma")
        course_combo.current(0)
        course_combo.grid(row = 0, column = 3, padx = 2, pady = 20, sticky = W)


        # Year selection dropbox
        year_label = Label(current_course, text = "Year",  font=("Satoshi-Bold", 13, "bold"), fg='black', bg = "white")
        year_label.grid(row = 1, column= 0, sticky = W)
        
        year_combo = ttk.Combobox(current_course,textvariable=self.VarYear, font=("Satoshi-Bold", 13),width=17, state = "readonly")
        year_combo["values"] = ("Select year", "First", "Second", "Third", "Fourth")
        year_combo.current(0)
        year_combo.grid(row = 1, column = 1, padx = 2, pady = 20, sticky = W)


        # semester selection dropbox
        semester_label = Label(current_course, text = "Semester",  font=("Satoshi-Bold", 13, "bold"), fg='black', bg = "white")
        semester_label.grid(row = 1, column= 2)
        
        sem_combo = ttk.Combobox(current_course,textvariable=self.VarSem, font=("Satoshi-Bold", 13),width=17, state = "readonly")
        sem_combo["values"] = ("Select Semester", "Odd", "Even")
        sem_combo.current(0)
        sem_combo.grid(row = 1, column = 3, padx = 2, pady = 20, sticky = W)


        # Student informations in a class
        ClassStudentinfo = LabelFrame(Left_frame, bd = 3, bg = "white", relief=RIDGE, text = "Class Student Information", font=("Satoshi-Bold", 17, "bold"), fg='black')
        ClassStudentinfo.place(x=5,y=210,width = 720, height= 350)
        
        
        #  Student ID label
        StuIDlabel = Label(ClassStudentinfo, text = "Student ID:", font = ("Satoshi-Bold", 13, "bold"), bg = "white")
        StuIDlabel.grid(row = 0, column= 0, padx = 5, sticky=W)
        
        StudentIDEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarStuID, width = 15 , font = ("Satoshi-Bold", 13, "bold"))
        StudentIDEntry.grid(row = 0, column = 1, padx = 5, sticky=W)
        
        # Name Label
        NameLabel = Label(ClassStudentinfo, text = "Name:", font = ("Satoshi-Bold",13,"bold"), bg = "white")
        NameLabel.grid(row = 0, column = 2, padx = 5, sticky = W)
        
        NameEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarName, width = 17, font = ("Satoshi-Bold", 13, "bold"))
        NameEntry.grid(row= 0, column = 3, padx = 5, sticky = W)
        
        #Section label
        SectionLable = Label(ClassStudentinfo, text = "Section/Division:", font = ("Satoshi-Bold", 13, "bold"), bg = "white")
        SectionLable.grid(row=1,column=0,padx=5,sticky = W, pady = 5)
        
        SectionEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarSec, width = 5, font = ("Satoshi-Bold", 13, "bold"))
        SectionEntry.grid(row = 1, column=1,padx = 5,sticky = W, pady= 5)
        
        # Roll no Label
        RollLabel = Label(ClassStudentinfo, text = "Roll no:", font = ("Satoshi-Bold",13,"bold"), bg = "white")
        RollLabel.grid(row = 1, column = 2, padx = 5, sticky = W)
        
        RollEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarRoll, width = 17, font = ("Satoshi-Bold", 13, "bold"))
        RollEntry.grid(row= 1, column = 3, padx = 5, sticky = W)
        
        #Gender dropdown
        GenderLable = Label(ClassStudentinfo, text = "Gender:", font = ("Satoshi-Bold", 13, "bold"), bg = "white")
        GenderLable.grid(row=2,column=0,padx=5,sticky = W, pady = 5)
        
        GenderCombo = ttk.Combobox(ClassStudentinfo,textvariable=self.VarGender, width = 10, font = ("Satoshi-Bold", 13, "bold"),state = "readonly")
        GenderCombo["values"] = ("Male", "Female", "Mentally Ill")
        GenderCombo.grid(row = 2, column=1,padx = 5,sticky = W, pady= 5)
        
        # Date of birth DropBox
        DOBLabel = Label(ClassStudentinfo, text = "DOB:", font = ("Satoshi-Bold",13,"bold"), bg = "white")
        DOBLabel.grid(row = 2, column = 2, padx = 5, sticky = W)
        
        DOBEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarDOB, width = 17, font = ("Satoshi-Bold",13,"bold"))
        DOBEntry.grid(row= 2, column = 3, sticky = W,padx=5)
        
        #Email label
        EmailLable = Label(ClassStudentinfo, text = "Email:", font = ("Satoshi-Bold", 13, "bold"), bg = "white")
        EmailLable.grid(row=3,column=0,padx=5,sticky = W, pady = 5)
        
        EmailEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarEmail, width =13, font = ("Satoshi-Bold", 13, "bold"))
        EmailEntry.grid(row = 3, column=1,padx = 5,sticky = W, pady= 5)
        
        # Phone no Label
        PhoneLabel = Label(ClassStudentinfo, text = "Phone no:", font = ("Satoshi-Bold",13,"bold"), bg = "white")
        PhoneLabel.grid(row = 3, column = 2, padx = 5, sticky = W)
        
        PhoneEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarPhone, width = 17, font = ("Satoshi-Bold", 13, "bold"))
        PhoneEntry.grid(row= 3, column = 3, padx = 5, sticky = W)
        
        #Teacher's Name Label
        TeacherLabel = Label(ClassStudentinfo, text = "Teacher's Name:", font = ("Satoshi-Bold",13,"bold"), bg = "white")
        TeacherLabel.grid(row = 4, column = 0, padx = 5, sticky = W)
        
        TeacherEntry = ttk.Entry(ClassStudentinfo,textvariable=self.VarTeacher, width = 17, font = ("Satoshi-Bold", 13, "bold"))
        TeacherEntry.grid(row= 4, column = 1, padx = 5, sticky = W)
        
        # Radio 
        self.VarRadioButton = StringVar()
        
        RadioButton1 = ttk.Radiobutton(ClassStudentinfo,variable = self.VarRadioButton, text = "Take Photo Sample", value = "Yes", cursor="hand2")
        RadioButton1.grid(row = 5, column=0)

        RadioButton2 = ttk.Radiobutton(ClassStudentinfo,variable = self.VarRadioButton, text = "Do Not Take Photo Sample", value = "No", cursor="hand2")
        RadioButton2.grid(row = 5, column=1)
        
        # button frame
        ButtonFrame = Frame(ClassStudentinfo, bd = 2, relief= RIDGE, bg = "white")
        ButtonFrame.place(x=0,y=200,width = 710, height = 40)
        
        
        # save
        SaveButton = Button(ButtonFrame, text = "Save",command = self.AddData, font = ("Satoshi-Bold",13,"bold"), width = 15, height = 1 )
        SaveButton.grid(row = 0, column = 0,padx=8)
        
        # update
        UpdateButton = Button(ButtonFrame, text = "Update", font = ("Satoshi-Bold",13,"bold"), width = 15)
        UpdateButton.grid(row = 0 ,column = 1,padx = 8)
        
        # delete
        DeleteButton = Button(ButtonFrame, text = "Delete", font = ("Satoshi-Bold",13,"bold"),width = 15)
        DeleteButton.grid(row=0, column=2, padx = 8)
        
        # reset
        ResetButton = Button(ButtonFrame, text = "Reset", font = ("Satoshi-Bold",13,"bold"),width = 15)
        ResetButton.grid(row = 0, column = 3,padx=8)

        # Photo Sample frame
        PhotoSampleFrame = Frame(ClassStudentinfo, bd = 2, relief= RIDGE, bg = "white")
        PhotoSampleFrame.place(x=0,y=245,width = 710, height = 40)
        
        # Take Photo Sample
        TakePhotoSampleButton = Button(PhotoSampleFrame, text = "Take Photo Sample", font = ("Satoshi-Bold",13,"bold"),width = 33)
        TakePhotoSampleButton.grid(row = 0, column = 0,padx=6)
        
        # Update Photo Sample
        UpdatePhotoSampleButton = Button(PhotoSampleFrame, text = "Update Photo Sample", font = ("Satoshi-Bold",13,"bold"),width = 33)
        UpdatePhotoSampleButton.grid(row = 0, column = 1,padx=6)
        
        
        
        


        
        #right label frame
        right_frame = LabelFrame(main_frame, bd = 5,bg = "white", relief = RIDGE, text = "Student details", font=("Satoshi-Bold", 15, "bold"), fg='black')
        right_frame.place(x=750, y = 10,width = 740, height = 680)
        
        
        
        # search frame <------------
        SearchFrame = LabelFrame(right_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search System",  font = ("Satoshi-Bold",13,"bold"))
        SearchFrame.place(x=5, y = 0, width = 720, height = 70)
        
        
        
        
        # search bar
        SearchBar = Label(SearchFrame, text = "Search By ", font = ("Satoshi-Bold",13,"bold"), bg = "white")
        SearchBar.grid(row = 0, column = 0, pady = 5, padx = 10, sticky = W)
        
        SearchCombo = ttk.Combobox(SearchFrame,  font = ("Satoshi",11), state = "readonly",width = 13)
        SearchCombo["values"] = ("Select", "StudentID", "Name")
        SearchCombo.current(0)
        SearchCombo.grid(row= 0, column = 1, pady = 2,padx=5, sticky = W)
        
        SearchEntry = ttk.Entry(SearchFrame, width = 16,  font = ("Satoshi-Bold",13,"bold"))
        SearchEntry.grid(row = 0, column = 2, pady = 2, sticky = W, padx = 10)
        
        SearchButton = Button(SearchFrame, text = "Search", width = 14,  font = ("Satoshi-Bold",8,"bold"),)
        SearchButton.grid(row = 0, column = 3, pady = 2, sticky = W)

        ShowAllButton = Button(SearchFrame, text = "Show all", width = 14,  font = ("Satoshi-Bold",8,"bold"),)
        ShowAllButton.grid(row = 0, column = 4, pady = 2, sticky = W)
        
        # Table frame lable
        TableFrame = LabelFrame(right_frame, bd = 2, bg = "white", relief = RIDGE )
        TableFrame.place(x=5, y = 75, width = 720, height = 550)
        
        # this is a scrollbar <--
        XScroll = ttk.Scrollbar(TableFrame, orient = HORIZONTAL)
        YScroll = ttk.Scrollbar(TableFrame, orient = VERTICAL)
        self.StudentTable = ttk.Treeview(TableFrame, column = ("Name","Dept", "Course",  "Section","Year", "Sem", "ID", "DOB", "Email", "Phone", "Teacher", "Photo"), xscrollcommand=XScroll.set, yscrollcommand=YScroll.set)
        
        XScroll.pack(side = BOTTOM, fill = X)
        YScroll.pack(side = RIGHT, fill = Y)
        XScroll.config(command = self.StudentTable.xview)
        YScroll.config(command = self.StudentTable.yview)
        
        self.StudentTable.heading("Dept", text = "Department")
        self.StudentTable.heading("Course", text = "Course")
        self.StudentTable.heading("Year", text = "Year")
        self.StudentTable.heading("Sem", text = "Semester")
        self.StudentTable.heading("ID", text = "StudentID")
        self.StudentTable.heading("Name", text = "Name")
        self.StudentTable.heading("Section", text = "Section")
        self.StudentTable.heading("DOB", text = "DOB")
        self.StudentTable.heading("Email", text = "Email")
        self.StudentTable.heading("Phone", text = "Phone")
        self.StudentTable.heading("Teacher", text = "Teacher")
        self.StudentTable.heading("Photo", text = "PhotoSampleStatus")
        self.StudentTable["show"] = "headings"
        
        self.StudentTable.column("Name",width = 125)
        self.StudentTable.column("Dept",width = 100)
        self.StudentTable.column("Course",width = 100)
        self.StudentTable.column("Year",width = 50)
        self.StudentTable.column("Sem",width = 60)
        self.StudentTable.column("ID",width = 80)
        self.StudentTable.column("Section",width = 50)
        self.StudentTable.column("DOB",width = 100)
        self.StudentTable.column("Email",width = 100)
        self.StudentTable.column("Phone",width = 100)
        self.StudentTable.column("Teacher",width = 100)
        self.StudentTable.column("Photo",width = 150)

        self.StudentTable.pack(fill = BOTH, expand = 1)
        
    
    # ************* FUNCTION DECLARATIONS **************
    def AddData(self):
        if self.VarDept.get()=="Select Department" or self.VarStuID.get() == "" or self.VarName.get()=="" or self.VarCourse.get()=="Select Course" or self.VarYear.get() == "Select Year" or self.VarSem.get() == "Select Semester" or self.VarSec.get()==""or self.VarRoll.get()==""or self.VarGender.get()==""or self.VarDOB.get()==""or self.VarEmail.get()==""or self.VarPhone.get()=="" or self.VarTeacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent = self.root)
        else:
            try:
                Connection = mysql.connector.connect(host = "localhost", user = "yamyam", password = "S4NY4Mk1ng!123", database = "facerecognition")
                MyCursor = Connection.cursor()
                StringQuery = 'INSERT INTO student(StudentID, Name, Dept, Course, Year, Sem, Sec, Roll, Gender, Email, Phone, Teacher, Photosample) VALUES (%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                StringValues = (self.VarStuID.get(),self.VarName.get(),self.VarDept(), self.VarCourse.get(), self.VarYear.get(),self.VarSem.get(), self.VarSec.get(),self.VarRoll.get(),self.VarGender.get(),self.VarEmail.get(),self.VarPhone.get(),self.VarTeacher.get(),self.VarRadioButton.get())
                MyCursor.execute(StringQuery, StringValues)
                Connection.commit()
                Connection.close()
                messagebox.showinfo("Success", "Student Details has been added Succesfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = student_details(root)
    root.mainloop()