import tkinter
import tkinter.messagebox
import re
import sqlite3
import hashlib
import Database
import logging
logging.basicConfig(
    filename="Student.log",
    filemode='a',
    format=f"%(asctime)s - %(message)s",
    level=logging.DEBUG
)


class Signup:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='#FFEFD5')
        self.main_window.title('Sign up')
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

        self.title = tkinter.Label(self.signframe, text="Sign up", fg="red", font=('Calisto MT', 30), bg="#FFEFD5")

        self.title.grid(row=1, column=0)

        self.fName_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="* First Name:", bg='#FFEFD5',
                                         font=('Arial', 13))
        self.fName_entry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=25,
                                         highlightcolor="light green", highlightbackground="black")

        self.fName_label.grid(row=1, column=0, ipadx=50, pady=10)
        self.fName_entry.grid(row=1, column=1)
        self.fName_entry.focus()

        self.lName_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="* Last Name:", bg='#FFEFD5',
                                         font=('Arial', 13))
        self.lName_entry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=25,
                                         highlightcolor="light green", highlightbackground="black")

        self.lName_label.grid(row=2, column=0, ipadx=50, pady=10)
        self.lName_entry.grid(row=2, column=1)

        self.id_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="* Student ID:", bg='#FFEFD5',
                                      font=('Arial', 13))
        self.id_entry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=25,
                                      highlightcolor="light green", highlightbackground="black")

        self.id_label.grid(row=3, column=0, ipadx=50, pady=10)
        self.id_entry.grid(row=3, column=1)

        self.password_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="* Password:", bg='#FFEFD5',
                                            font=('Arial', 13))
        self.password_entry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=25,
                                            highlightcolor="light green", highlightbackground="black", show="*")

        self.password_label.grid(row=4, column=0, ipadx=50, pady=10)
        self.password_entry.grid(row=4, column=1)

        self.showVar = tkinter.IntVar(value=0)
        self.showPassword = tkinter.Checkbutton(self.Form, text="Show", bg='#FFEFD5', activebackground='#FFEFD5',
                                                variable=self.showVar, onvalue=1, offvalue=0, command=self.showPass)

        self.showPassword.grid(row=4, column=2)

        self.email_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="* Email Address:", bg='#FFEFD5',
                                         font=('Arial', 13))
        self.email_entry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=25,
                                         highlightcolor="light green", highlightbackground="black")

        self.email_label.grid(row=5, column=0, ipadx=50, pady=10)
        self.email_entry.grid(row=5, column=1)

        self.phone_label = tkinter.Label(self.Form, anchor=tkinter.CENTER, text="* Phone Number:", bg='#FFEFD5',
                                         font=('Arial', 13))
        self.phone_entry = tkinter.Entry(self.Form, border="1", highlightthickness="2", width=25,
                                         highlightcolor="light green", highlightbackground="black")
        self.phone_entry.insert(0, "05")

        self.phone_label.grid(row=6, column=0, ipadx=50, pady=10)
        self.phone_entry.grid(row=6, column=1)

        self.login_button = tkinter.Button(self.buttons_frame, anchor=tkinter.CENTER, text="Login", width="10",
                                           bg="#ff4040", border="2", fg="white", font=('Arial', 13),
                                           activebackground="light green", command=self.go_Login)

        self.login_button.grid(row=7, column=0, padx=35)

        self.submit_button = tkinter.Button(self.buttons_frame, anchor=tkinter.CENTER, text="Submit", width="10",
                                            bg="#ff4040", border="2", fg="white", font=('Arial', 13),
                                            activebackground="light green", command=self.validation)

        self.submit_button.grid(row=7, column=1, padx=25)

        self.imgframe.pack(side="left")
        self.logoframe.pack()
        self.signframe.pack(pady=0)
        self.Form.pack(pady=40)
        self.buttons_frame.pack(pady=0)
        self.bigFrame.pack(pady=0)

        self.users = Database.UserDatabase()

        tkinter.mainloop()

    def go_Login(self):
        self.main_window.destroy()
        import Login
        Login.Login()

    def showPass(self):
        if self.showVar.get() == 1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def validation(self):
        fName = self.fName_entry.get().rstrip(" ")
        lName = self.lName_entry.get().rstrip(" ")
        id = self.id_entry.get().rstrip(" ")
        password = self.password_entry.get()
        email = self.email_entry.get().rstrip(" ")
        phone = self.phone_entry.get().rstrip(" ")

        if fName == "" or lName == "" or id == "" or password == "" or email == "" or phone == "":
            tkinter.messagebox.showinfo("Warning", "All fields marked with * must be filled!")
            return

        valid = True
        count = 1
        massage = ""
        if not fName.isalpha():
            valid = False
            massage += f"{count}-First name must be in letters and one name.  \n"
            count += 1

        if not lName.isalpha():
            valid = False
            massage += f"{count}-Last name must be in letters and one name.  \n"
            count += 1

        reg = "^[0-9]{10}$"
        pat = re.compile(reg)
        x = re.search(pat, id.rstrip())
        if not x:
            valid = False
            massage += f"{count}-Student ID must be 10 digits only.  \n"
            count += 1

        reg = "^[A-Za-z0-9]{6,100}$"
        pat = re.compile(reg)
        x = re.search(pat, password)

        if not x:
            valid = False
            massage += f"{count}-Password must be at least 6 digits or letters without symbols. \n"
            count += 1

        reg = "^([a-zA-Z0-9\._-]+)(@ksu\.edu\.sa)$"
        pat = re.compile(reg)
        x = re.search(pat, email.rstrip())

        if not x:
            valid = False
            massage += f"{count}-Email must be in this format XXXXXXXX@ksu.edu.sa, symbols allowed are (. _ -).\n"
            count += 1

        reg = "^(05)[0-9]{8}$"
        pat = re.compile(reg)
        x = re.search(pat, phone)

        if not x:
            valid = False
            massage += f"{count}-Phone must be digits in this format 05XXXXXXXX.  \n"
            count += 1

        if not valid:
            tkinter.messagebox.showerror("Error", massage)

        if massage == "":
            hashedPass = (hashlib.sha256(password.encode())).hexdigest()
            try:
                query = 'INSERT INTO USER (FNAME,LNAME,ID,PASS,EMAIL,PHONE,USERTYPE,uEvent) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
                Database.conn.execute(query, (fName, lName, id, hashedPass, email, phone, 'STUDENT', "-"))

            except sqlite3.IntegrityError:
                tkinter.messagebox.showerror("Error", "The Student ID already exist, Please try to Login!")
                return
            logging.info(f"Transaction type: Signup - Student ID: {id}")
            tkinter.messagebox.showinfo("Info", "The User account has created successfully!")
            self.fName_entry.delete(0, 'end')
            self.lName_entry.delete(0, 'end')
            self.id_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.phone_entry.delete(0, 'end')
            self.phone_entry.insert(0, "05")
            self.fName_entry.focus()

            Database.conn.commit()


Signup()
