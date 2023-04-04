import tkinter
import tkinter.messagebox
import re
import hashlib
import Database
import logging
logging.basicConfig(
    filename="Student.log",
    filemode='a',
    format=f"%(asctime)s - %(message)s",
    level=logging.DEBUG
)


class Login:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='#FFEFD5')
        self.main_window.title('Login')
        self.main_window.iconbitmap("projectIcon.ico")
        # self.main_window.geometry('800x700')
        self.main_window.resizable(False, False)
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        window_width = 800
        window_height = 700
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.main_window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

        self.bigFrame = tkinter.LabelFrame(self.main_window, text="", bg="#FFEFD5", borderwidth="0")

        self.imgframe = tkinter.Frame(self.main_window, bg="black")
        self.logoframe = tkinter.Frame(self.main_window, bg="black")
        self.signframe = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.Form = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.buttons_frame = tkinter.Frame(self.bigFrame, bg='#FFEFD5')

        self.photo = tkinter.PhotoImage(file="asda.png")
        self.canvas = tkinter.Canvas(self.imgframe, width=330, height=800)
        self.canvas.create_image(100, 100, image=self.photo)
        self.canvas.pack(side="left")

        self.photo2 = tkinter.PhotoImage(file="projectLogo.png")
        self.canvas2 = tkinter.Canvas(self.logoframe, width=200, height=200,bg="#FFEFD5")
        self.canvas2.create_image(100, 100, image=self.photo2)
        self.canvas2.grid(row=0, column=0)

        self.title = tkinter.Label(self.signframe, text="Login", fg="red", font=('Calisto MT', 30), bg="#FFEFD5")
        self.title.grid(row=0, column=0)

        self.id_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="User ID :", bg='#FFEFD5',
                                      font=('Arial', 13))
        self.id_entry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=22,
                                      highlightcolor="light green", highlightbackground="black")
        self.id_label.grid(row=1, column=0, ipadx=40, pady=10)
        self.id_entry.grid(row=1, column=1)
        self.id_entry.focus()

        self.password_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="Password:", bg='#FFEFD5',
                                            font=('Arial', 13))
        self.passwordEntry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=22,
                                           highlightcolor="light green", highlightbackground="black", show="*")
        self.password_label.grid(row=2, column=0, ipadx=40, pady=10)
        self.passwordEntry.grid(row=2, column=1)

        self.showVar = tkinter.IntVar(value=0)
        self.showPassword = tkinter.Checkbutton(self.Form, text="Show", bg='#FFEFD5', activebackground='#FFEFD5',
                                                variable=self.showVar, onvalue=1, offvalue=0, command=self.showPass)
        self.showPassword.grid(row=2, column=2)

        self.login = tkinter.Button(self.buttons_frame, text="Login", width="10", bg="#ff4040", border="2", fg="white",
                                    font=('Arial', 13), activebackground="light green", command=self.validation)
        self.login.grid(row=3, column=0, pady=30)

        self.imgframe.pack(side="left")
        self.logoframe.pack(pady=10)
        self.signframe.pack()
        self.Form.pack(pady=40)
        self.buttons_frame.pack()
        self.bigFrame.pack(pady=0)

        self.users = Database.UserDatabase()

        tkinter.mainloop()

    def showPass(self):
        if self.showVar.get() == 1:
            self.passwordEntry.config(show="")
        else:
            self.passwordEntry.config(show="*")

    def validation(self):
        id = self.id_entry.get()
        password = self.passwordEntry.get()

        if id == "" or password == "":
            tkinter.messagebox.showinfo("Warning", "Enter your ID and Password!")
            return

        valid = True
        found = False
        count = 1
        message = ""
        reg = "^[0-9]{10}$"
        pat = re.compile(reg)
        x = re.search(pat, id.rstrip())

        if not x:
            valid = False
            message += f"{count}- ID must be 10 digits only.  \n"
            count += 1

        reg = "^[A-Za-z0-9]{6,100}$"
        pat = re.compile(reg)
        x = re.search(pat, password)

        if not x:
            valid = False
            message += f"{count}- Password must be at least 6 digits or letters without symbols. \n"
            count += 1

        if not valid:
            tkinter.messagebox.showerror("Error", message)

        if message == "":
            hashedPass = (hashlib.sha256(password.encode())).hexdigest()
            cursor = Database.conn.execute("SELECT ID,PASS,USERTYPE from USER")
            for row in cursor:
                if id == row[0] and hashedPass == row[1]:
                    found = True
                    if row[2] == "Admin":
                        self.main_window.destroy()
                        import Admin
                        Admin.Admin(id)
                    else:
                        logging.info(f"Transaction type: Login - Student ID: {id}")
                        self.main_window.destroy()
                        import Student
                        Student.Student(id)

            if not found:
                tkinter.messagebox.showerror("Warning", "The ID or password is invalid!")
                return
            Database.conn.close()
            print("The database has been closed!")

