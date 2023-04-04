import datetime
import tkinter
import tkinter.messagebox
import random
import csv
import Database


class Admin:
    def __init__(self, id):
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='#FFEFD5')
        self.main_window.title('Admin')
        self.main_window.iconbitmap("projectIcon.ico")
        # self.main_window.geometry('800x730')
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
        self.Rmgframe = tkinter.Frame(self.main_window, bg="black")
        self.headFrame = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.welcomeFrame = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.formFrame = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.choiceFrame = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.noteFrame = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.buttonsFrame = tkinter.Frame(self.bigFrame, bg="#FFEFD5")
        self.backupFrame = tkinter.Frame(self.bigFrame, bg="#FFEFD5")

        self.photo = tkinter.PhotoImage(file="asda.png")
        self.canvas = tkinter.Canvas(self.imgframe, width=150, height=800)
        self.canvas.create_image(100, 100, image=self.photo)
        self.canvas.pack(side="left")

        self.title = tkinter.Label(self.headFrame, text="Admin", fg="red", font=('Calisto MT', 30), bg="#FFEFD5")
        self.title.grid(row=0, column=0, pady=5)

        corser = Database.conn.execute(f"Select FNAME FROM USER WHERE ID = {id}")
        sName = list(corser)[0][0]
        self.welcomeLabel = tkinter.Label(self.welcomeFrame, text=f"Welcome {sName}", fg="red", font=('Calisto MT', 18),
                                          bg="#FFEFD5")
        self.welcomeLabel.grid(row=1, column=0, pady=10)

        self.eventName = tkinter.Label(self.formFrame, text="* Enter the sport event name:", bg='#FFEFD5',
                                       font=('Arial', 13))
        self.eventnameEntry = tkinter.Entry(self.formFrame, border="1", highlightthickness="2", width=22,
                                            highlightcolor="light green", highlightbackground="black")
        self.eventName.grid(row=0, column=0, padx=40)
        self.eventnameEntry.grid(row=0, column=1, padx=25)

        self.eventLocation = tkinter.Label(self.formFrame, text="* Enter the sport event location:", bg='#FFEFD5',
                                           font=('Arial', 13))
        self.eventLocationEntry = tkinter.Entry(self.formFrame, border="1", highlightthickness="2", width=22,
                                                highlightcolor="light green", highlightbackground="black")

        self.eventLocation.grid(row=1, column=0, pady=20)
        self.eventLocationEntry.grid(row=1, column=1)

        self.eventCapacity = tkinter.Label(self.formFrame, text="* Enter the sport event capacity:", bg='#FFEFD5',
                                           font=('Arial', 13))
        self.eventCapacityEntry = tkinter.Entry(self.formFrame, border="1", highlightthickness="2", width=22,
                                                highlightcolor="light green", highlightbackground="black")

        self.eventCapacity.grid(row=2, column=0)
        self.eventCapacityEntry.grid(row=2, column=1)

        self.eventDate = tkinter.Label(self.formFrame, text="* Enter the sport event date:", bg='#FFEFD5',
                                       font=('Arial', 13))
        self.eventDateEntry = tkinter.Entry(self.formFrame, border="1", highlightthickness="2", width=22,
                                            highlightcolor="light green", highlightbackground="black")

        self.eventDate.grid(row=3, column=0, pady=20)
        self.eventDateEntry.grid(row=3, column=1)

        self.eventTime = tkinter.Label(self.formFrame, text="* Enter the sport event time:", bg='#FFEFD5',
                                       font=('Arial', 13))
        self.eventTimeEntry = tkinter.Entry(self.formFrame, border="1", highlightthickness="2", width=22,
                                            highlightcolor="light green", highlightbackground="black")

        self.radioVar = tkinter.IntVar(value=1)
        self.choice1 = tkinter.Radiobutton(self.choiceFrame, text="AM", variable=self.radioVar, value=1, bg='#FFEFD5',
                                           font=('Arial', 10, 'bold'))
        self.choice2 = tkinter.Radiobutton(self.choiceFrame, text="PM", variable=self.radioVar, value=2, bg='#FFEFD5',
                                           font=('Arial', 10, 'bold'))

        self.eventTime.grid(row=4, column=0)
        self.eventTimeEntry.grid(row=4, column=1)
        self.choice1.pack(side="left")
        self.choice2.pack(side="left")

        self.note = tkinter.Label(self.noteFrame, text="Note:"
                                                       "\nThe format of date is: DD/MM/YYYY"
                                                       "\nThe format of time is: HH:MM", bg='#FFEFD5',
                                  font=('Arial', 9, "bold"))
        self.note.pack(pady=15)

        self.logoutButton = tkinter.Button(self.buttonsFrame, text="Logout", width="10", bg="#ff4040", border="2",
                                           fg="white",
                                           font=('Arial', 13), activebackground="light green", command=self.go_signup)
        self.logoutButton.grid(row=0, column=0, pady=15, padx=50)

        self.createButton = tkinter.Button(self.buttonsFrame, text="Create", width="10", bg="#ff4040", border="2",
                                           fg="white", font=('Arial', 13), activebackground="light green",
                                           command=self.insert_event)
        self.createButton.grid(row=0, column=1, padx=50)

        self.backupButton = tkinter.Button(self.backupFrame, text="Backup", width="10", bg="#ff4040", border="2",
                                           fg="white", font=('Arial', 13), activebackground="light green",
                                           command=self.backupCSV)

        self.backupButton.pack()

        self.photo2 = tkinter.PhotoImage(file=r"asda.png")
        self.canvas = tkinter.Canvas(self.Rmgframe, width=150, height=800)
        self.canvas.create_image(100, 100, image=self.photo2)
        self.canvas.pack()

        self.imgframe.pack(side="left")
        self.headFrame.pack()
        self.welcomeFrame.pack(pady=15)
        self.formFrame.pack(pady="10")
        self.bigFrame.pack(side="left", padx="20")
        self.choiceFrame.pack(pady=9)
        self.noteFrame.pack()
        self.buttonsFrame.pack()
        self.backupFrame.pack()
        self.Rmgframe.pack()

        self.users = Database.UserDatabase()
        self.events = Database.EventsDatabase()

        tkinter.mainloop()

    def go_signup(self):
        self.main_window.destroy()
        import Login
        Login.Login()

    def insert_event(self):
        eName = self.eventnameEntry.get()
        eLoc = self.eventLocationEntry.get()
        eCap = self.eventCapacityEntry.get()
        eDate = self.eventDateEntry.get()
        eTime = self.eventTimeEntry.get()

        message = ""
        count = 1
        valid = True
        date = self.eventDateEntry.get()
        eventDate = date.split("/")

        time = self.eventTimeEntry.get()
        eventTime = time.split(":")

        if eName == "" or eLoc == "" or eCap == "" or eDate == "" or eTime == "":
            tkinter.messagebox.showinfo("Warning", "All fields marked with * must be filled!")
            return

        if len(eventDate) != 3 or len(eventDate[0]) != 2 or len(eventDate[1]) != 2:
            tkinter.messagebox.showerror("Error", "The date must be in this format: DD/MM/YYYY")
            return

        try:

            if int(eventDate[0]) < 1 or int(eventDate[0]) > 31:
                message += f"{count}- The day must be between 1 to 31. \n"
                count += 1
                valid = False

            if int(eventDate[1]) < 1 or int(eventDate[1]) > 12:
                message += f"{count}- The month must be between 1 to 12. \n"
                count += 1
                valid = False

            try:
                temp = datetime.datetime(int(eventDate[2]), int(eventDate[1]),
                                         int(eventDate[0]))  # 2 = Year, 1 = Month, 0 = Day
            except ValueError:
                tkinter.messagebox.showerror("Error", "This day does not exist in this month!")
                return

            if len(eventTime) != 2 or eventTime[1] == "" or len(eventTime[1]) != 2 or len(eventTime[0]) != 2:
                tkinter.messagebox.showerror("Error", "The time must be in this format: HH:MM")
                return
            if int(eventTime[0]) < 1 or int(eventTime[0]) > 12:
                message += f"{count}- The hours must be between 1 to 12. \n"
                count += 1
                valid = False
            if int(eventTime[1]) < 0 or int(eventTime[1]) > 59:
                message += f"{count}- The minutes must be between 0 to 59."
                count += 1
                valid = False

            if not valid:
                tkinter.messagebox.showerror("Error", message)
                return

        except ValueError:
            tkinter.messagebox.showerror("Error", "The date and time must be numbers")
            return



        try:
            cap = int(eCap)
            if cap <= 0:
                tkinter.messagebox.showerror("Error", "Event capacity must be greater than zero!")
                return
        except ValueError:
            tkinter.messagebox.showerror("Error", "Event capacity must be integer number!")
            return

        uniquenumber = False
        eventID = str(random.randint(10000, 99999))
        while not uniquenumber:
            cursor = Database.conn.execute("SELECT ENUM from EVENT")
            if eventID in cursor:
                eventID = str(random.randint(10000, 99999))
            else:
                uniquenumber = True

        query = 'INSERT INTO EVENT (ENAME,ELOC,ENUM,ECAP,DATE,TIME,BOOKNUM) VALUES (?, ?, ?, ?, ?, ? ,?)'
        if self.radioVar.get() == 1:
            Database.conn.execute(query, (eName, eLoc, eventID, eCap, eDate, eTime + " AM", 0))
        else:
            Database.conn.execute(query, (eName, eLoc, eventID, eCap, eDate, eTime + " PM", 0))

        tkinter.messagebox.showinfo("Info", "The Event has created successfully!")
        self.radioVar.set(1)
        self.eventnameEntry.delete(0, 'end')
        self.eventLocationEntry.delete(0, 'end')
        self.eventCapacityEntry.delete(0, 'end')
        self.eventDateEntry.delete(0, 'end')
        self.eventTimeEntry.delete(0, 'end')
        self.eventnameEntry.focus()
        Database.conn.commit()

    def backupCSV(self):
        KsuCupFile = open("KsuCup.csv", 'a')

        csvWriterKsuCup = csv.writer(KsuCupFile)

        cursorUser = Database.conn.execute("SELECT FNAME,LNAME,ID,PASS,EMAIL,PHONE,USERTYPE,uEvent from USER")
        listOfUsers = list(cursorUser)
        for row in listOfUsers:
            csvWriterKsuCup.writerow(list(row))

        cursorEvent =  Database.conn.execute("SELECT ENAME,ELOC,ENUM,ECAP,DATE,TIME,BOOKNUM from EVENT")
        listOfEvents = list(cursorEvent)
        for row in listOfEvents:
            csvWriterKsuCup.writerow(list(row))

        tkinter.messagebox.showinfo("Info", "The database has been backed up successfully!")


Admin(1111111111)
