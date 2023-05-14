import mysql.connector as mysql
#from attachment import Management

class Management2():
    def __init__(self):
        self.con = mysql.connect(host="localhost",
                                port="3306",
                                user="root",
                                password="admin123#",
                                database="formdata2")
        self.cur = self.con.cursor()
    def update_particular_data(self,rollno,what):
        query = "select * from school"
        self.cur = self.con.cursor()
        self.cur.execute(query)
        for row1 in self.cur:
            if row1[0] == rollno:
                # query = "select * from school where rollno={}".format(rollno)
                # self.cursor = self.conn.cursor()
                # self.cursor.execute(query)
                print("\nDetails of student",rollno,"is:---")
                for row1 in self.cur:
                    print("\nName: ",row1[1])
                    print("Address: ",row1[2])
                    print("Contact: ",row1[3])
                    print("Gender: ",row1[4])          
                nam = input("\nEnter new {}: ".format(what))
                query  = "update school set {}='{}' where rollno={}".format(what,nam,rollno)
                self.cur.execute(query)
                self.con.commit()        
                print("Student",what,"updated successfully")