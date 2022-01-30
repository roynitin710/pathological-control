from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from database import DB


class User:

    def __init__(self, user, user_id):
        self.root = Tk()
        # connect to database
        self.database = DB()
        # window
        self.fullScreenState = False
        self.root.state("zoomed")
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)
        self.root.minsize(1280, 695)

        # icon
        self.root.iconbitmap("img/icon.ico")

        # title
        self.root.title("PathCon")

        # background
        image = PhotoImage(file="img/background.png")
        label = Label(self.root, image=image)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # heading
        label = Label(self.root, text="Sanar-Vibra Hospital", bg='#000000',
                      fg='#ff0000')  # Sanar Vibra (means: Heal vibe in english)
        label.place(x=455, y=65)
        label.configure(font=("Times New Roman", 30, "bold italic"))

        self.profile(user, user_id)

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)

    # # input field
    # def input_field(self, x=0, y=0):
    #     get = ttk.Entry(self.frame)
    #     get.place(x=x, y=y, width=230)
    #     get.configure(font=("Times New Roman", 12))
    #     return get

    def profile(self, user, user_id):  # 1)user 0: ∞ clearance  2)user 1: level 1 clearance 3) user 2: level 2 clearance

        # center frame
        frame = Frame(self.root, bg="#000000")
        frame.place(x=20, y=200, width=1240, height=430)

        # fetch data
        data = self.database.fetch_user_data(user_id)

        # welcome
        label = Label(frame, text="Welcome, {}".format(data[0][4]), bg='#000000', fg='#0000ff')
        label.place(x=10, y=10)
        label.configure(font=("Times New Roman", 20, "bold italic"))

        # user persona
        profile_pic = Image.open("img/{}".format(data[0][5]))
        profile_pic = profile_pic.resize((100, 140), Image.ANTIALIAS)
        profile_pic = ImageTk.PhotoImage(profile_pic)
        profile_pic_label = Label(frame, image=profile_pic, bg="#000000", borderwidth=0)
        profile_pic_label.place(x=20, y=50)

        # department
        label = Label(frame, text="Department: {}".format(data[0][6]), bg='#000000', fg='#ffffff')
        label.place(x=130, y=60)
        label.configure(font=("Times New Roman", 11))

        # qualification
        label = Label(frame, text="Qualification: {}".format(data[0][7]), bg='#000000', fg='#ffffff')
        label.place(x=130, y=80)
        label.configure(font=("Times New Roman", 11))

        if data[0][8] != "N/A":
            # salary
            label = Label(frame, text="Salary: {} LPA".format(data[0][8]), bg='#000000', fg='#ffffff')
            label.place(x=130, y=100)
            label.configure(font=("Times New Roman", 11))

        if user == 0:
            # staff
            staffs = Button(frame, text="Staff Details", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0', cursor='hand2',
                           activebackground='#050542', activeforeground='#f6f0f0', command=lambda: self.temp())
            staffs.place(x=400, y=60, width=200, height=50)
            staffs.configure(font=("Times New Roman", 10, "bold"))

            # patient's data
            patients_data = Button(frame, text="Patient's Data", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0', cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0', command=lambda: self.temp())
            patients_data.place(x=650, y=60, width=200, height=50)
            patients_data.configure(font=("Times New Roman", 10, "bold"))

            # graph
            graph = Button(frame, text="Graph", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0',
                                   cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0',
                                   command=lambda: self.temp())
            graph.place(x=900, y=60, width=200, height=50)
            graph.configure(font=("Times New Roman", 10, "bold"))

        if user == 1:
            # staff
            staffs = Button(frame, text="Staff Details", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0', cursor='hand2',
                            activebackground='#050542', activeforeground='#f6f0f0', command=lambda: self.temp())
            staffs.place(x=400, y=60, width=200, height=50)
            staffs.configure(font=("Times New Roman", 10, "bold"))

            # patient's data
            patients_data = Button(frame, text="Patient's Data", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0',
                                   cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0',
                                   command=lambda: self.temp())
            patients_data.place(x=650, y=60, width=200, height=50)
            patients_data.configure(font=("Times New Roman", 10, "bold"))

            # graph
            graph = Button(frame, text="Graph", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0',
                           cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0',
                           command=lambda: self.temp())
            graph.place(x=900, y=60, width=200, height=50)
            graph.configure(font=("Times New Roman", 10, "bold"))

        if user == 2:
            # staff
            staffs = Button(frame, text="Doctor Details", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0', cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0', command=lambda: self.temp())
            staffs.place(x=400, y=60, width=200, height=50)
            staffs.configure(font=("Times New Roman", 10, "bold"))

            # patient's data
            patients_data = Button(frame, text="Patient's Data", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0',
                                   cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0',
                                   command=lambda: self.temp())
            patients_data.place(x=650, y=60, width=200, height=50)
            patients_data.configure(font=("Times New Roman", 10, "bold"))

            # graph
            graph = Button(frame, text="Graph", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0',
                           cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0',
                           command=lambda: self.temp())
            graph.place(x=900, y=60, width=200, height=50)
            graph.configure(font=("Times New Roman", 10, "bold"))

        self.root.mainloop()

    def temp(self):
        pass


if __name__ == '__main__':
    root = User(0, 1)
