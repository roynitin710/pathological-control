from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from database import DB


class LoginWindow:

    def __init__(self, user):
        self.root = Tk()
        # connect to database
        self.database = DB()
        # window
        self.fullScreenState = False
        self.root.state("zoomed")
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)
        self.root.minsize(1280, 695)
        # self.root.maxsize(1280, 695)

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

        self.login(user)

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)

    # input field
    def input_field(self, x=0, y=0):
        get = ttk.Entry(self.frame)
        get.place(x=x, y=y, width=230)
        get.configure(font=("Times New Roman", 12))
        return get

    def login(self, user):  # 1)user 0: ∞ clearance  2)user 1: level 1 clearance 3) user 2: level 2 clearance
        # adding text to the screen
        def create_label(text="Blank", x=0, y=0, fg='#ffff00', bg='#000000', font_style="Times New Roman", font_size=20, font_type="bold"):
            label = Label(self.frame, text=text, bg=bg, fg=fg)
            label.place(x=x, y=y)
            label.configure(font=(font_style, font_size, font_type))
            return label

        # center frame
        self.frame = Frame(self.root, bg="#000000")
        self.frame.place(x=468, y=200, width=340, height=430)

        # user persona
        user_persona = Image.open("img/avatar.png")
        user_persona = user_persona.resize((100, 100), Image.ANTIALIAS)
        user_persona = ImageTk.PhotoImage(user_persona)
        user_persona_label = Label(self.frame, image=user_persona, bg="#000000", borderwidth=0)
        user_persona_label.place(x=122, y=25)

        if user == 0:
            create_label(text="Admin", x=125, y=130, fg='#ffff00', bg='#000000')
        elif user == 1:
            create_label(text="Patient", x=125, y=130, fg='#ffff00', bg='#000000')
        elif user == 2:
            create_label(text="Staff", x=141, y=130, fg='#ffff00', bg='#000000')
        else:
            messagebox.showerror("PathCon", "Some Error Occurred")

        # username
        username_persona = Image.open("img/avatar.png")
        username_persona = username_persona.resize((20, 20), Image.ANTIALIAS)
        username_persona = ImageTk.PhotoImage(username_persona)
        username_persona_label = Label(self.frame, image=username_persona, bg="#000000", borderwidth=0)
        username_persona_label.place(x=55, y=185)
        create_label(text="Username", x=80, y=180, fg='#ffffff', bg='#000000', font_size=15)
        if user != 0:
            self.username = self.input_field(x=55, y=210)
        else:
            create_label(text="Admin                                           ", x=55, y=210, fg='#8b0000', bg='#ffffff', font_size=12, font_style="underline")
            username = "admin"

        # password
        password_persona = Image.open("img/lock.png")
        password_persona = password_persona.resize((20, 20), Image.ANTIALIAS)
        password_persona = ImageTk.PhotoImage(password_persona)
        password_persona_label = Label(self.frame, image=password_persona, bg="#000000", borderwidth=0)
        password_persona_label.place(x=55, y=245)
        create_label(text="Password", x=80, y=240, fg='#ffffff', bg='#000000', font_size=15)
        self.password = self.input_field(x=55, y=270)

        # login
        log_in = Button(self.frame, text="Log In", bd=3, relief=RIDGE, bg='#050542', fg='#f6f0f0', cursor='hand2', activebackground='#050542', activeforeground='#f6f0f0', command=lambda: self.perform_login(user))
        log_in.place(x=97, y=310, width=160, height=30)
        log_in.configure(font=("Times New Roman", 10, "bold"))

        # divider
        create_label(text="                                                         ", x=55, y=340, fg='#808080', bg='#000000', font_style="arial", font_size=10, font_type="underline")

        if user == 0:
            create_label(text="Password", x=80, y=240, fg='#ffffff', bg='#000000', font_size=15)
        elif user == 1:
            # forgot password
            forgot_password = Button(self.frame, text="Forgot password?", bd=0, bg='#000000', fg='#0000ff', cursor='hand2', activebackground='#000000', activeforeground='#ff000f', command=lambda: self.registration())
            forgot_password.place(x=97, y=360, width=160, height=30)
            forgot_password.configure(font=("Times New Roman", 10, "bold"))

            # register for new user
            register = Button(self.frame, text="Create New Account", bd=0, bg='#000000', fg='#0000ff', cursor='hand2', activebackground='#000000', activeforeground='#ff000f', command=lambda: self.registration())
            register.place(x=97, y=390, width=160)
            register.configure(font=("Times New Roman", 10, "bold"))

        self.root.mainloop()

    def perform_login(self, user):
        # fetch input provided by the user
        if user == 0:
            username = "admin"
        else:
            username = self.username.get()
        password = self.password.get()
        print(username)
        print(password)
        # check and login
        data = self.database.login_user(username, password)
        if data == 0:
            messagebox.showerror("PathCon", "Some error occurred!")
        else:
            if len(data) == 0:
                messagebox.showerror("PathCon", "Incorrect username or password")
            else:
                # save user info of logged in user
                user_id = data[0][0]
                messagebox.showinfo(f"PathCon", f"Successfully logged in | User ID: {user_id}")

    def registration(self):
        pass


if __name__ == '__main__':
    root = LoginWindow(0)
