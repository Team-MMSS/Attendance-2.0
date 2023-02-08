from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk
from subprocess import call
from datetime import date
from Attendance import markAttendance
from Mail import send_emails
import os

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("%dx%d" % (w, h))
root.title("Attendance")
root.configure(bg = "black")
bm = PhotoImage(file = "GUI_images/1.png")
bgimg = Label(root, i = bm)
bgimg.pack()
photo = PhotoImage(file="GUI_images/logo.png")
label = Label(root, image=photo)
label.place(x = 0, y = 0)
label2 = Label(root, text = "Attendance System", font = "times 30 bold", fg = "red")
label2.place(x = 600, y = 50)

options_list = ["AIE", "CSE-A","CSE-B","CYS","ECE","CCE","MECH"]
menu= StringVar(root)
menu.set("Please select the branch")
drop= OptionMenu(root, menu,*options_list)
drop.pack()
drop.place(x = 200, y = 300)
menu2= StringVar()
menu2.set("Please select the SEMESTER")
drop2= OptionMenu(root, menu2,"SEMESTER-1", "SEMESTER-2","SEMESTER-3","SEMESTER-4","SEMESTER-5","SEMESTER-6","SEMESTER-7","SEMESTER-7")
drop2.pack()
drop2.place(x = 650, y = 300)



menu3 = StringVar()
menu3.set("Please select the Course")
drop3= OptionMenu(root, menu3,"21AIE301", "21AIE302","21AIE303","21AIE304","19CSE202","21AIE103","21MAT301","21SSK301")
drop3.pack()
drop3.place(x = 1200, y = 300)




def Execute():
    c_name = menu3.get()
    email_list =[]
    if c_name == "21AIE301":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "21AIE302":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "21AIE303":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "21AIE303":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "21AIE304":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "21MAT301":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "19CSE202":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "21AIE103":
        email_list = ["sathwik7331@gmail.com"]
    elif c_name == "21SSK301":
        email_list = ["sathwik7331@gmail.com"]
    if menu.get() != "AIE" or menu2.get() != "SEMESTER-5" or menu3.get() != "21AIE303":
        messagebox.showerror("Sorry","This section is not available yet")
    else:
        import OpenCV
        from facemaster import predict
        from Face_align import FaceAligner
        file = date.today()
        Attend_path = "Attendance/"+str(c_name)+'_'+str(file)+'.csv'
        FaceAligner()
        test_path = "test-data/Aligned_images"
        images_names = os.listdir(test_path)
        for image_name in images_names:
            image_path = test_path + "/" + image_name
            predicted_img, label = predict(image_path)
            markAttendance(label, Attend_path)
        #send_emails(email_list, Attend_path)
              
button = Button(root, text="Take Attendance", command=Execute)
button.configure(background="lightgreen")
button.place(x = 700, y = 500)
root.mainloop()
