import sqlite3
import hashlib

conn = sqlite3.connect("KsuCupDatabase.db")

class UserDatabase:
    def __init__(self):
        try:
            conn.execute('''CREATE TABLE USER
            (
            FNAME           TEXT           NOT NULL,
            LNAME           TEXT           NOT NULL,
            ID         TEXT PRIMARY KEY   NOT NULL,
            PASS            TEXT           NOT NULL,
            EMAIL           TEXT          NOT NULL,
            PHONE           TEXT           NOT NULL,
            USERTYPE        TEXT           NOT NULL,
            uEvent          TEXT           NOT NULL);''')
            print("Table created successfully")

            # Create Admin
            try:
                hashedPass = (hashlib.sha256("admin1".encode())).hexdigest()
                query = 'INSERT INTO USER (FNAME,LNAME,ID,PASS,EMAIL,PHONE,USERTYPE,uEvent) VALUES (?, ?, ?, ?, ?, ?, ?,?)'
                conn.execute(query, ('DrMohammed', 'Alnajim', '1111111111', hashedPass, 'malnajim1@ksu.edu.sa',
                                          '0505000000', 'Admin', "-"))
                conn.commit()
                print("Admin records created successfully")
            except sqlite3.IntegrityError:
                print("The Admin is already exists")

        except sqlite3.OperationalError:
            print("The User table is already created")

# Please remove this code from line 35 to 39 !!!
        # cursor = conn.execute("SELECT FNAME,LNAME,ID,PASS,EMAIL,PHONE,USERTYPE,uEvent from USER")
        # delete = conn.execute("UPDATE USER SET uEvent = '' WHERE ID = '4421029150'")
        # conn.commit()
        # print(list(cursor))

# For check on Users (if you finish, set it as a comment!)
        # cursor = conn.execute("SELECT FNAME,LNAME,ID,PASS,EMAIL,PHONE,USERTYPE,uEvent from USER")
        # for row in cursor:
        #     print("First Name = ", row[0])
        #     print("Last Name = ", row[1])
        #     print("ID = ", row[2])
        #     print("Password = ", row[3])
        #     print("Email = ", row[4])
        #     print("Phone Number = ", row[5])
        #     print("User Type = ", row[6])
        #     print("User events = ", row[7], "\n")
        #
        # print("Operation done successfully")

# For check on Users (if you finish, set it as a comment!)
# UserDatabase()


class EventsDatabase:
    def __init__(self):
        try:
            conn.execute('''CREATE TABLE EVENT
            (
            ENAME          TEXT            NOT NULL,
            ELOC           TEXT            NOT NULL,
            ENUM      INT PRIMARY KEY     NOT NULL,
            ECAP           TEXT            NOT NULL,
            DATE           TEXT            NOT NULL,
            TIME           TEXT            NOT NULL,
            BOOKNUM         INT            NOT NULL);''')

            print("Table created successfully")
        except sqlite3.OperationalError:
            print("The Event table is already created")


# Please remove this code from line 78 to 83 !!!
        # query = 'INSERT INTO EVENT (ENAME,ELOC,ENUM,ECAP,DATE,TIME,BOOKNUM) VALUES (?, ?, ?, ?, ?, ?, ?)'
        # test = conn.execute(query,("nn","R",10001,"200","2022/30/11","12:36 AM",0))
        # conn.execute(f"UPDATE EVENT SET ECAP = ECAP-1  WHERE ENUM = 10000")
        # cursor = list(conn.execute("SELECT * from EVENT"))
        # print(cursor)

# For check on Events (if you finish, set it as a comment!)
#         cursor = list(conn.execute("SELECT * from EVENT"))
#         for row in cursor:
#             print("Event Name = ", row[0])
#             print("Event Location = ", row[1])
#             print("Event Number = ", row[2])
#             print("Event Capacity = ", row[3])
#             print("Evemt Date = ", row[4])
#             print("Event Time = ", row[5])
#             print("Book Number = ", row[6], "\n")
        #
        # print("Operation done successfully")

# For check on Events (if you finish, set it as a comment!)
# EventsDatabase()
