import tkinter
import tkinter.messagebox
from tkinter import ttk
import datetime
import logging
import Database

logging.basicConfig(
    filename="Student.log",
    filemode='a',
    format=f"%(asctime)s - %(message)s",
    level=logging.DEBUG
)


class Student:
    def __init__(self, id):
        self.main_window = tkinter.Tk()
        self.main_window.configure(bg='#FFEFD5')
        self.main_window.title('Student')
        self.main_window.iconbitmap("projectIcon.ico")
        # self.main_window.geometry("1007x693")
        self.main_window.resizable(False, False)
        self.notebook = ttk.Notebook(self.main_window)

        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        window_width = 1007
        window_height = 693
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.main_window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

        self.users = Database.UserDatabase()
        self.events = Database.EventsDatabase()

        self.ticketsTab = tkinter.LabelFrame(self.main_window, text="", bg="#FFEFD5", borderwidth="0")
        self.viewTab = tkinter.LabelFrame(self.main_window, text="", bg="#FFEFD5", borderwidth="0")
        self.welcome_frame = tkinter.Frame(self.ticketsTab, bg="#FFEFD5")
        self.eventsFrame = tkinter.Frame(self.ticketsTab, bg="#FFEFD5")
        self.selectFrame = tkinter.Frame(self.ticketsTab, bg="#FFEFD5")
        self.treeView = tkinter.Frame(self.ticketsTab, bg="#FFEFD5")

        self.bookFrame = tkinter.Frame(self.ticketsTab, bg="#FFEFD5")
        self.logoutFrame = tkinter.Frame(self.ticketsTab, bg="#FFEFD5")
        self.showframe = None
        self.buttomFrame = None

        corser = Database.conn.execute(f"Select FNAME FROM USER WHERE ID = {id}")
        sName = list(corser)[0][0]
        self.welcomeLabel = tkinter.Label(self.ticketsTab, text=f"Welcome {sName}:", fg="red", font=('Calisto MT', 20),
                                        bg="#FFEFD5")
        self.eventLabel = tkinter.Label(self.eventsFrame, text="Available Events:", fg="red", font=('Calisto MT', 30),
                                        bg="#FFEFD5")
        self.selectLabel = tkinter.Label(self.selectFrame, text="Select one or more events", fg="red",
                                         font=('Calisto MT', 16), bg="#FFEFD5")

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview", background="#BBBBB", foreground="Black", rowheight=25, fieldbackground="White")
        self.style.map("Treeview", background=[('selected', "blue")])
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.viewEvents = ttk.Treeview(self.treeView, columns=('1', '2', '3', '4', '5'), show='headings', height=11)

        self.viewEvents.heading(1, text="Event Name")
        self.viewEvents.heading(2, text="Event Location")
        self.viewEvents.heading(3, text="Event Number")
        self.viewEvents.heading(4, text="Event Date")
        self.viewEvents.heading(5, text="Event Time")

        self.cursor = Database.conn.execute("SELECT ENAME,ELOC,ENUM,DATE,TIME from EVENT")
        self.count = 0

        # --------------------------   BEGIN OF EDITING   --------------------------------------------

        arrDateEvent = []
        arrTimeEvent = []

        for row in self.cursor:
            arrDateEvent.append(row[3])
            arrTimeEvent.append(row[4])


        n = len(arrDateEvent)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                firstDate = arrDateEvent[j].split("/")
                secondDate = arrDateEvent[j + 1].split("/")

                firstTime = arrTimeEvent[j].split(":")
                secondTime = arrTimeEvent[j + 1].split(":")

                # -------------------------  SORTING BY EVENTS DATE FROM NEAREST TO FARTHEST ---------------------------
                if firstDate[2] > secondDate[2]:
                    t = arrDateEvent[j]
                    arrDateEvent[j] = arrDateEvent[j + 1]
                    arrDateEvent[j + 1] = t

                    t = arrTimeEvent[j]
                    arrTimeEvent[j] = arrTimeEvent[j + 1]
                    arrTimeEvent[j + 1] = t
                else:
                    if firstDate[2] == secondDate[2] and firstDate[1] > secondDate[1]:
                        t = arrDateEvent[j]
                        arrDateEvent[j] = arrDateEvent[j + 1]
                        arrDateEvent[j + 1] = t

                        t = arrTimeEvent[j]
                        arrTimeEvent[j] = arrTimeEvent[j + 1]
                        arrTimeEvent[j + 1] = t
                    else:
                        if firstDate[1] == secondDate[1] and firstDate[0] > secondDate[0]:
                            t = arrDateEvent[j]
                            arrDateEvent[j] = arrDateEvent[j + 1]
                            arrDateEvent[j + 1] = t

                            t = arrTimeEvent[j]
                            arrTimeEvent[j] = arrTimeEvent[j + 1]
                            arrTimeEvent[j + 1] = t
                # --------------------------  SORTING BY EVENTS DATE FROM NEAREST TO FARTHEST --------------------------

                        else:
                # --------------------------  SORTING BY EVENTS TIME FROM NEAREST TO FARTHEST --------------------------
                            if firstDate[2] == secondDate[2] and firstDate[1] == secondDate[1] and firstDate[0] == \
                                    secondDate[0]:
                                # if "AM" in arrTimeEvent[j] and "PM" in arrTimeEvent[j + 1]:
                                #     t = arrDateEvent[j]
                                #     arrDateEvent[j] = arrDateEvent[j + 1]
                                #     arrDateEvent[j + 1] = t
                                #
                                #     t = arrTimeEvent[j]
                                #     arrTimeEvent[j] = arrTimeEvent[j + 1]
                                #     arrTimeEvent[j + 1] = t

                                if "PM" in arrTimeEvent[j] and "AM" in arrTimeEvent[j + 1]:
                                    t = arrDateEvent[j]
                                    arrDateEvent[j] = arrDateEvent[j + 1]
                                    arrDateEvent[j + 1] = t

                                    t = arrTimeEvent[j]
                                    arrTimeEvent[j] = arrTimeEvent[j + 1]
                                    arrTimeEvent[j + 1] = t

                                elif "PM" in arrTimeEvent[j] and "PM" in arrTimeEvent[j + 1]:
                                    if int(firstTime[0][0:2]) >= int(secondTime[0][0:2]):
                                        t = arrDateEvent[j]
                                        arrDateEvent[j] = arrDateEvent[j + 1]
                                        arrDateEvent[j + 1] = t

                                        t = arrTimeEvent[j]
                                        arrTimeEvent[j] = arrTimeEvent[j + 1]
                                        arrTimeEvent[j + 1] = t
                                    else:
                                        if int(firstTime[0][0:2]) == int(secondTime[0][0:2]) and int(
                                                firstTime[1][0:2]) <= int(secondTime[1][0:2]):
                                            t = arrDateEvent[j]
                                            arrDateEvent[j] = arrDateEvent[j + 1]
                                            arrDateEvent[j + 1] = t

                                            t = arrTimeEvent[j]
                                            arrTimeEvent[j] = arrTimeEvent[j + 1]
                                            arrTimeEvent[j + 1] = t

                                elif "AM" in arrTimeEvent[j] and "AM" in arrTimeEvent[j + 1]:
                                    if int(firstTime[0][0:2]) != 12 and int (firstTime[0][0:2]) - int(
                                            secondTime[0][0:2]) <= 1:
                                        t = arrDateEvent[j]
                                        arrDateEvent[j] = arrDateEvent[j + 1]
                                        arrDateEvent[j + 1] = t

                                        t = arrTimeEvent[j]
                                        arrTimeEvent[j] = arrTimeEvent[j + 1]
                                        arrTimeEvent[j + 1] = t
                                    else:
                                        if int(firstTime[0][0:2]) == int(secondTime[0][0:2]) and int(
                                                firstTime[1][0:2]) <= int(secondTime[1][0:2]):
                                            t = arrDateEvent[j]
                                            arrDateEvent[j] = arrDateEvent[j + 1]
                                            arrDateEvent[j + 1] = t

                                            t = arrTimeEvent[j]
                                            arrTimeEvent[j] = arrTimeEvent[j + 1]
                                            arrTimeEvent[j + 1] = t
            # --------------------------  SORTING BY EVENTS TIME FROM NEAREST TO FARTHEST ------------------------------



        for x in range(len(arrDateEvent)):
            cursor = Database.conn.execute(
                f"SELECT ENAME,ELOC,ENUM,DATE,TIME from EVENT where TIME ='{arrTimeEvent[x]}' AND DATE = '{arrDateEvent[x]}'")
            eventInfo = list(cursor)

            eventDate = arrDateEvent[x].split("/")
            temp = datetime.datetime(int(eventDate[2]), int(eventDate[1]),
                                     int(eventDate[0]))  # 2 = Year , 1 = Month , 0 = Day
            nowDate = str(temp.now().date().strftime("%d/%m/%Y")).split("/")

            eventTime = arrTimeEvent[x].split(":")
            tempNowTime = str(temp.now().time().strftime("%I:%M %p"))
            NowTime = tempNowTime.split(":")

            # --------------------------   ADD TO THE TREEVIEW BASED ON NOWDATE AND TIME   -----------------------------
            if int(eventDate[2]) > int(nowDate[2]):  # Year = 2
                self.viewEvents.insert(parent='', index=self.count, text='',
                                       values=(
                                               eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                               eventInfo[0][3], eventInfo[0][4]))
                self.count += 1
            else:
                if int(eventDate[2]) == int(nowDate[2]) and int(eventDate[1]) > int(nowDate[1]):  # Month = 1
                    self.viewEvents.insert(parent='', index=self.count, text='',
                                           values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                   eventInfo[0][3], eventInfo[0][4]))
                    self.count += 1
                else:
                    if int(eventDate[1]) == int(nowDate[1]) and int(eventDate[0]) > int(nowDate[0]):  # Day = 0
                        self.viewEvents.insert(parent='', index=self.count, text='',
                                               values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                       eventInfo[0][3], eventInfo[0][4]))
                        self.count += 1
                    else:
                        if int(eventDate[0]) == int(nowDate[0]) and int(eventDate[1]) == int(nowDate[1]) and int(
                                eventDate[2]) == int(nowDate[2]):
                            if "AM" in tempNowTime and "PM" in arrTimeEvent[x]:
                                self.viewEvents.insert(parent='', index=self.count, text='', values=(
                                                    eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                    eventInfo[0][3], eventInfo[0][4]))
                                self.count += 1
                            elif "PM" in tempNowTime and "AM" in arrTimeEvent[x]:
                                return
                            elif "PM" in tempNowTime and "PM" in arrTimeEvent[x]:
                                if int(eventTime[0][0:2]) > int(NowTime[0][0:2]):
                                    self.viewEvents.insert(parent='', index=self.count, text='',
                                                           values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                                   eventInfo[0][3], eventInfo[0][4]))
                                    self.count += 1
                                else:
                                    if int(eventTime[0][0:2]) == int(NowTime[0][0:2]) and int(eventTime[1][0:2]) >= int(
                                            NowTime[1][0:2]):
                                        self.viewEvents.insert(parent='', index=self.count, text='',
                                                               values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                                       eventInfo[0][3], eventInfo[0][4]))
                                        self.count += 1

                            elif "AM" in tempNowTime and "AM" in arrTimeEvent[x]:
                                if int(eventTime[0]) != 12 and (int(eventTime[0]) - int(NowTime[0])) >= 1:
                                    self.viewEvents.insert(parent='', index=self.count, text='',
                                                           values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                                   eventInfo[0][3], eventInfo[0][4]))
                                    self.count += 1
                                else:
                                    if int(eventTime[0][0:2]) == int(NowTime[0][0:2]) and int(eventDate[1][0:2]) >= int(
                                            NowTime[1][0:2]):
                                        self.viewEvents.insert(parent='', index=self.count, text='',
                                                               values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                                       eventInfo[0][3], eventInfo[0][4]))
                                        self.count += 1
            # --------------------------   ADD TO THE TREEVIEW BASED ON NOWDATE AND TIME   -----------------------------

            # --------------------------   END OF EDITING   --------------------------------------------

        # self.bookEntry = tkinter.Entry(self.bookFrame, border=1, highlightthickness=2, width=25)
        self.bookButton = tkinter.Button(self.bookFrame, text="Book", bg="#ff4040",width=10, border="2", fg="white",
                                         font=('Calisto MT', 11), command=lambda: self.booking(id))

        self.showbutton = tkinter.Button(self.viewTab, text="Show my events", bg="#ff4040", border="2", fg="white",
                                         font=('Calisto MT', 20), command=lambda: self.showEvents(id))

        self.logoutButton = tkinter.Button(self.logoutFrame, text="Logout", width="10", bg="#ff4040", border="2",
                                           fg="white", font=('Calisto MT', 13), command=lambda: self.logout(id))

        self.showbutton.pack(pady=150)
        self.notebook.pack()
        self.ticketsTab.pack()
        self.viewTab.pack()
        self.welcome_frame.pack(pady=25)
        self.welcomeLabel.place(x=0,y=30)
        self.eventsFrame.pack(pady=25)
        self.eventLabel.pack()
        self.selectFrame.pack()
        self.selectLabel.pack()
        self.treeView.pack()
        self.viewEvents.pack(pady=20)

        self.bookFrame.pack()
        # self.bookEntry.pack(side='left', pady=20)
        self.bookButton.pack(ipadx=25, padx=30, pady=20)

        self.logoutFrame.pack()
        self.logoutButton.pack(pady=25, ipadx=25)

        ttk.Style().configure("TNotebook", background="#FFEFD5", foreground='black')
        self.notebook.add(self.ticketsTab, text='Book a Ticket')
        self.notebook.add(self.viewTab, text='View my tickets')

        self.main_window.mainloop()


    def booking(self, StudentId):

        selectedEventID = []
        message = ""
        t = self.viewEvents.selection()
        for id in t:
            selectedEventID.append(str(self.viewEvents.item(id)['values'][2]))

        tmpStudentEvents = Database.conn.execute(f"SELECT uEvent from USER WHERE ID ='{StudentId}'")
        studentEvent = list(tmpStudentEvents)[0][0]
        if len(selectedEventID) == 0:
            tkinter.messagebox.showerror("Error", "You must select one or more events to book!")
            return

        for eID in selectedEventID:
            theEvent = list(Database.conn.execute(f"SELECT ECAP,BOOKNUM from EVENT WHERE ENUM ={eID}"))
            eventcapacity = int(theEvent[0][0])
            eventBookNum = int(theEvent[0][1])

            if eventBookNum == eventcapacity:
                tkinter.messagebox.showerror("Error", "The event is reached the max capacity!")
                return

            tmpStudentEvents = Database.conn.execute(f"SELECT uEvent from USER WHERE ID ='{StudentId}'")
            studentEvent = list(tmpStudentEvents)[0][0]

            arrOfEvents = str(studentEvent).split(",")
            for i in arrOfEvents:
                if i == eID and len(selectedEventID) == 1:
                    tkinter.messagebox.showerror("Error", "The event is already chosen!")
                    return
                if i == eID and len(selectedEventID) > 1:
                    tkinter.messagebox.showerror("Error", "There is an event already chosen, Please try again with out it")
                    return


        if studentEvent == "-":
            studentEvent = selectedEventID[0] + ","
            Database.conn.execute(f"UPDATE USER SET uEvent ='{studentEvent}' WHERE ID ='{StudentId}'")
            Database.conn.commit()
            message += f"The event {selectedEventID[0]} has been booked successfully.\n"
            if self.showframe is not None:
                self.showframe.destroy()
                self.buttomFrame.destroy()
                self.showbutton = tkinter.Button(self.viewTab, text="Show my events", bg="#ff4040", border="2",
                                                 fg="white", font=('Calisto MT', 20),
                                                 command=lambda: self.showEvents(StudentId))
                self.showbutton.pack(pady=150)

            logTemp = list(
                Database.conn.execute(f"SELECT ENAME,ELOC FROM EVENT WHERE ENUM = {selectedEventID[0]}"))
            logging.info(
                f"Event Name: {list(logTemp[0])[0]} - Event Location: {list(logTemp[0])[1]} - Student ID: {StudentId}")

            #self.bookEntry.delete(0, tkinter.END)
            # eventcapacity -=1
            # self.events.conn.execute(f"UPDATE EVENT SET ECAP = ECAP-1 WHERE ENUM ={eID}") #Wrong
            Database.conn.execute(f"UPDATE EVENT SET BOOKNUM = BOOKNUM+1 WHERE ENUM ={selectedEventID[0]}")
            Database.conn.commit()
            selectedEventID.remove(selectedEventID[0])



        for eID in selectedEventID:

            tmpStudentEvents = Database.conn.execute(f"SELECT uEvent from USER WHERE ID ='{StudentId}'")
            studentEvent = list(tmpStudentEvents)[0][0]


            #self.bookEntry.insert(0, eID)
            studentEvent += eID+","
            Database.conn.execute(f"UPDATE USER SET uEvent ='{studentEvent}' WHERE ID ='{StudentId}'")
            Database.conn.commit()
            message += f"The event {eID} has been booked successfully.\n"
            if self.showframe is not None:
                self.showframe.destroy()
                self.buttomFrame.destroy()
                self.showbutton = tkinter.Button(self.viewTab, text="Show my events", bg="#ff4040", border="2",
                                                 fg="white", font=('Calisto MT', 20),
                                                 command=lambda: self.showEvents(StudentId))
                self.showbutton.pack(pady=150)

            logTemp = list(Database.conn.execute(f"SELECT ENAME,ELOC FROM EVENT WHERE ENUM = {eID}"))
            logging.info(f"Transaction type: Book Event - Event Name: {list(logTemp[0])[0]} - "
                         f"Event Location: {list(logTemp[0])[1]} - "
                         f"Student ID: {StudentId}")
            #self.bookEntry.delete(0, tkinter.END)

            Database.conn.execute(f"UPDATE EVENT SET BOOKNUM = BOOKNUM+1 WHERE ENUM ={eID}")
            Database.conn.commit()

        if message != "":
            tkinter.messagebox.showinfo("Info", message)


    def showEvents(self, studentID):

        arrDate = []
        arrTime = []
        try:
            tmpStudentEvents = Database.conn.execute(f"SELECT uEvent from USER WHERE ID ='{studentID}'")
            studentEvent = list(tmpStudentEvents)[0][0]

            if studentEvent == "-":
                tkinter.messagebox.showerror("Error", "Error: The student have not booked any event")
                return

            arrOfEvents = str(studentEvent).split(",")
            self.showframe = tkinter.Frame(self.viewTab, bg="#FFEFD5")
            self.showLable = tkinter.Label(self.showframe, text="Booked Events:", fg="red", font=('Calisto MT', 30),
                                           bg="#FFEFD5")
            self.bookedEvents = ttk.Treeview(self.showframe, columns=('1', '2', '3', '4', '5'), show='headings', height=11)
            self.buttomFrame = tkinter.Frame(self.viewTab, bg="#FFEFD5")

            self.bookedEvents.heading(1, text="Event Name")
            self.bookedEvents.heading(2, text="Event Location")
            self.bookedEvents.heading(3, text="Event Number")
            self.bookedEvents.heading(4, text="Event Date")
            self.bookedEvents.heading(5, text="Event Time")

            self.viewlogoutButton = tkinter.Button(self.buttomFrame, text="Logout", width="10", bg="#ff4040",
                                                   border="2", fg="white", font=('Calisto MT', 15),
                                                   command=lambda: self.logout(studentID))

            self.count = 0

            # --------------------------   BEGIN OF EDITING   --------------------------------------------

            for Eid in arrOfEvents:
                if Eid != "":
                    cursor = Database.conn.execute(f"SELECT DATE from EVENT where ENUM ={Eid}")
                    cursorT = Database.conn.execute(f"SELECT TIME from EVENT where ENUM ={Eid}")
                    date = list(cursor)[0][0]
                    timeE = list(cursorT)[0][0]
                    arrDate.append(date)
                    arrTime.append(timeE)


            n = len(arrDate)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    firstDate = arrDate[j].split("/")
                    secondDate = arrDate[j + 1].split("/")

                    firstTime = arrTime[j].split(":")
                    secondTime = arrTime[j+1].split(":")

                # --------------------------   SORTING BY DATE   --------------------------------------------

                    if firstDate[2] > secondDate[2]:
                        t = arrDate[j]
                        arrDate[j] = arrDate[j + 1]
                        arrDate[j + 1] = t

                        t = arrTime[j]
                        arrTime[j] = arrTime[j + 1]
                        arrTime[j + 1] = t
                    else:
                        if firstDate[2] == secondDate[2] and firstDate[1] > secondDate[1]:
                            t = arrDate[j]
                            arrDate[j] = arrDate[j + 1]
                            arrDate[j + 1] = t

                            t = arrTime[j]
                            arrTime[j] = arrTime[j + 1]
                            arrTime[j + 1] = t
                        else:
                            if firstDate[1] == secondDate[1] and firstDate[0] > secondDate[0]:
                                t = arrDate[j]
                                arrDate[j] = arrDate[j + 1]
                                arrDate[j + 1] = t

                                t = arrTime[j]
                                arrTime[j] = arrTime[j + 1]
                                arrTime[j + 1] = t

                # --------------------------   SORTING BY DATE   --------------------------------------------


                            else:
                # --------------------------   SORTING BY TIME   --------------------------------------------
                                if firstDate[2] == secondDate[2] and firstDate[1] == secondDate[1] and firstDate[0] == secondDate[0]:
                                    # if "AM" in arrTime[j] and "PM" in arrTime[j+1]:
                                    #     t = arrDate[j]
                                    #     arrDate[j] = arrDate[j + 1]
                                    #     arrDate[j + 1] = t
                                    #
                                    #     t = arrTime[j]
                                    #     arrTime[j] = arrTime[j + 1]
                                    #     arrTime[j + 1] = t

                                    if "PM" in arrTime[j] and "AM" in arrTime[j+1]:
                                        t = arrDate[j]
                                        arrDate[j] = arrDate[j + 1]
                                        arrDate[j + 1] = t

                                        t = arrTime[j]
                                        arrTime[j] = arrTime[j + 1]
                                        arrTime[j + 1] = t

                                    elif "PM" in arrTime[j] and "PM" in arrTime[j+1]:
                                        if int(firstTime[0][0:2]) >= int(secondTime[0][0:2]):
                                            t = arrDate[j]
                                            arrDate[j] = arrDate[j + 1]
                                            arrDate[j + 1] = t

                                            t = arrTime[j]
                                            arrTime[j] = arrTime[j + 1]
                                            arrTime[j + 1] = t
                                        else:
                                            if int(firstTime[0][0:2]) == int(secondTime[0][0:2]) and int(firstTime[1][0:2]) <= int(secondTime[1][0:2]):
                                                t = arrDate[j]
                                                arrDate[j] = arrDate[j + 1]
                                                arrDate[j + 1] = t

                                                t = arrTime[j]
                                                arrTime[j] = arrTime[j + 1]
                                                arrTime[j + 1] = t

                                    elif "AM" in arrTime[j] and "AM" in arrTime[j+1]:
                                        if int(firstTime[0][0:2]) != 12 and int(firstTime[0][0:2]) - int(secondTime[0][0:2]) <= 1:
                                            t = arrDate[j]
                                            arrDate[j] = arrDate[j + 1]
                                            arrDate[j + 1] = t

                                            t = arrTime[j]
                                            arrTime[j] = arrTime[j + 1]
                                            arrTime[j + 1] = t
                                        else:
                                            if int(firstTime[0][0:2]) == int(secondTime[0][0:2]) and int(firstTime[1][0:2]) <= int(secondTime[1][0:2]):
                                                t = arrDate[j]
                                                arrDate[j] = arrDate[j + 1]
                                                arrDate[j + 1] = t

                                                t = arrTime[j]
                                                arrTime[j] = arrTime[j + 1]
                                                arrTime[j + 1] = t

                # --------------------------   SORTING BY TIME   --------------------------------------------



                # --------------------------   ADD TO THE TREEVIEW BASED ON NOWDATE AND TIME   --------------------------------------------
            for x in range(len(arrDate)):
                cursor = Database.conn.execute(f"SELECT ENAME,ELOC,ENUM,DATE,TIME from EVENT where TIME ='{arrTime[x]}' AND DATE = '{arrDate[x]}'")
                eventInfo = list(cursor)

                eventDate = arrDate[x].split("/")
                temp = datetime.datetime(int(eventDate[2]), int(eventDate[1]), int(eventDate[0]))  # 2 = Year , 1 = Month , 0 = Day
                nowDate = str(temp.now().date().strftime("%d/%m/%Y")).split("/")

                eventTime = arrTime[x].split(":")
                tempNowTime = str(temp.now().time().strftime("%I:%M %p"))
                NowTime = tempNowTime.split(":")

                if int(eventDate[2]) > int(nowDate[2]):  # Year = 2
                    self.bookedEvents.insert(parent='', index=self.count, text='',
                                             values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2], eventInfo[0][3],
                                                     eventInfo[0][4]))
                    self.count += 1
                else:
                    if int(eventDate[2]) == int(nowDate[2]) and int(eventDate[1]) > int(nowDate[1]):  # Month = 1
                        self.bookedEvents.insert(parent='', index=self.count, text='',
                                                 values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                         eventInfo[0][3], eventInfo[0][4]))
                        self.count += 1
                    else:
                        if int(eventDate[1]) == int(nowDate[1]) and int(eventDate[0]) > int(nowDate[0]):  # Day = 0
                            self.bookedEvents.insert(parent='', index=self.count, text='',
                                                     values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2],
                                                             eventInfo[0][3], eventInfo[0][4]))
                            self.count += 1
                        else:
                            if int(eventDate[0]) == int(nowDate[0]) and int(eventDate[1]) == int(nowDate[1]) and int(eventDate[2]) == int(nowDate[2]):
                                if "AM" in tempNowTime and "PM" in arrTime[x]:
                                    self.bookedEvents.insert(parent='', index=self.count, text='', values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2], eventInfo[0][3], eventInfo[0][4]))
                                    self.count += 1
                                elif "PM" in tempNowTime and "AM" in arrTime[x]:
                                    return
                                elif "PM" in tempNowTime and "PM" in arrTime[x]:
                                    if int(eventTime[0][0:2]) > int(NowTime[0][0:2]):
                                        self.bookedEvents.insert(parent='', index=self.count, text='',
                                                                 values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2], eventInfo[0][3], eventInfo[0][4]))
                                        self.count += 1
                                    else:
                                        if int(eventTime[0][0:2]) == int(NowTime[0][0:2]) and int(eventTime[1][0:2]) >= int(NowTime[1][0:2]):
                                            self.bookedEvents.insert(parent='', index=self.count, text='',
                                                                     values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2], eventInfo[0][3], eventInfo[0][4]))
                                            self.count += 1

                                elif "AM" in tempNowTime and "AM" in arrTime[x]:
                                    if int(eventTime[0]) != 12 and (int(eventTime[0]) - int(NowTime[0])) >= 1:
                                        self.bookedEvents.insert(parent='', index=self.count, text='',
                                                                 values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2], eventInfo[0][3], eventInfo[0][4]))
                                        self.count += 1
                                    else:
                                        if int(eventTime[0][0:2]) == int(NowTime[0][0:2]) and int(eventDate[1][0:2]) >= int(NowTime[1][0:2]):
                                            self.bookedEvents.insert(parent='', index=self.count, text='', values=(eventInfo[0][0], eventInfo[0][1], eventInfo[0][2], eventInfo[0][3], eventInfo[0][4]))
                                        self.count += 1

            # --------------------------   ADD TO THE TREEVIEW BASED ON NOWDATE AND TIME   -----------------------------



            # --------------------------   END OF EDITING   --------------------------------------------

            self.showbutton.destroy()
            self.showframe.pack()
            self.showLable.pack(pady=25)
            self.bookedEvents.pack(pady=20)
            self.viewlogoutButton.pack(padx=15, side="left")
            self.buttomFrame.pack(pady="50")
            logging.info(f"Transaction type: Show Events - Student ID: {studentID}")

        except IndexError:
            tkinter.messagebox.showerror("Error", "The student didn't book events")
            return

    def logout(self, studentID):
        logging.info(f"Transaction type: Logout - Student ID: {studentID}")
        self.main_window.destroy()

Student(4421021060)