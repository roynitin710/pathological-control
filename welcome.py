from tkinter import *
from login import LoginWindow
from PIL import Image, ImageTk


class Welcome:

    def __init__(self):
        self.root = Tk()

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
        label = Label(self.root, text="Sanar-Vibra Hospital", bg='#000000', fg='#ff0000')  # Sanar Vibra (means: Heal vibe in english)
        label.place(x=455, y=65)
        label.configure(font=("Times New Roman", 30, "bold italic"))

        self.choose_user()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)

    # choose type of the user
    def choose_user(self):
        # center frame
        frame = Frame(self.root, bg="#000000")
        frame.place(x=468, y=200, width=340, height=400)

        # user persona
        user_persona = Image.open("img/avatar.png")
        user_persona = user_persona.resize((100, 100), Image.ANTIALIAS)
        user_persona = ImageTk.PhotoImage(user_persona)
        user_persona_label = Label(frame, image=user_persona, bg="#000000", borderwidth=0)
        user_persona_label.place(x=122, y=25)

        # sub heading
        sub_heading_label = Label(frame, text="Choose User Type", bg='#000000', fg='#ffff00')
        sub_heading_label.place(x=60, y=150)
        sub_heading_label.configure(font=("Times New Roman", 20, "bold"))

        # admin
        admin = Button(frame, text="Admin", bd=3, relief=RIDGE, bg='#8b0000', fg='#f6f0f0', cursor='hand2',
                       activebackground='#8b0000', activeforeground='#f6f0f0', command=lambda: self.login(0))
        admin.place(x=92, y=210, width=160, height=30)
        admin.configure(font=("Times New Roman", 10, "bold"))

        # doctor
        doctor = Button(frame, text="Doctor", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0', cursor='hand2',
                         activebackground='#050542', activeforeground='#f6f0f0', command=lambda: self.login(1))
        doctor.place(x=92, y=260, width=160, height=30)
        doctor.configure(font=("Times New Roman", 10, "bold"))

        # staff
        staff = Button(frame, text="Staff", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0', cursor='hand2',
                       activebackground='#050542', activeforeground='#f6f0f0', command=lambda: self.login(2))
        staff.place(x=92, y=310, width=160, height=30)
        staff.configure(font=("Times New Roman", 10, "bold"))

        self.root.mainloop()

    def login(self, user):  # 1)user 0: level 3 clearance  2)user 1: level 2 clearance 3) user 2: level 1 clearance
        self.root.destroy()
        LoginWindow(user)


if __name__ == '__main__':
    root = Welcome()
