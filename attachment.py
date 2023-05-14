import mysql.connector as mysql
#class of management
class Management:
    #constructor
    def __init__(self):
        self.con = mysql.connect(host="localhost",
                                 port="3306",
                                 user="root",
                                 password="admin123#",
                                 database="formdata2")
        query = "create table if not exists school (rollno int primary key, name varchar(30) not null, address varchar(200) not null, contact varchar(30), gender enum('M','F'))"
        self.cur = self.con.cursor()
        self.cur.execute(query)
        
    #function to insert data
    def insert_data(self,rollno,name,address,contact,gender):
        query = "insert into school values ({},'{}','{}','{}','{}')".format(rollno,name,address,contact,gender)
        self.cur = self.con.cursor()
        self.cur.execute(query)
        self.con.commit()
        print("Student added successfully...")
    
    #fuction to view all data
    def view_data(self):
        query = "select * from school"
        self.cur = self.con.cursor()
        self.cur.execute(query)
        for i in self.cur:
            print("\nName:",i[1])
            print("Roll no:",i[0])
            print("Address:",i[2])
            print("Contact:",i[3])
            print("Gender:",i[4])

    #function to delete particular record
    def delete_data(self,Rollno):
        query = "select * from school"
        self.cur = self.con.cursor()
        self.cur.execute(query)
        check = 0
        for row in self.cur:
            if row[0] == Rollno:
                query= "delete from school where rollno={}".format(Rollno)
                self.cur = self.con.cursor()
                self.cur.execute(query)
                self.con.commit()
                check = 1
        if check == 0:
            print("Student not found")
        else:
            print("Student deleted successfully")
    
    #function to search data
    def search_data(self,rollno):
        query = "select * from school"
        self.cur = self.con.cursor()
        self.cur.execute(query)
        check = 0
        for row in self.cur:
            if row[0] == rollno:
                query = "select * from school where rollno={}".format(rollno)
                self.cur = self.con.cursor()
                self.cur.execute(query)
                print("Details of student",rollno,"is:---")
                for i in self.cur:
                    print("\nName: ",i[1])
                    print("Address: ",i[2])
                    print("Contact: ",i[3])
                    print("Gender: ",i[4])
                check = 1
        if check == 0:
            print("Student not found")
        else:
            pass    

    
   
    #function to update particular data
    def update_data(self,rollno):
        print("\n1.Full record\n2.Particular data from record\n")
        ch = int(input("Enter decision: "))
        if ch == 1:
            query = "select * from school"
            self.cur = self.con.cursor()
            self.cur.execute(query)
            check = 0
            for row in self.cur:
                if row[0] == rollno:
                    query = "select * from school where rollno={}".format(rollno)
                    self.cur = self.con.cursor()
                    self.cur.execute(query)
                    print("Details of student",rollno,"is:---")
                    for i in self.cur:
                        print("\nName: ",i[1])
                        print("Address: ",i[2])
                        print("Contact: ",i[3])
                        print("Gender: ",i[4])        
                    nam = input("\nEnter new name: ")
                    addd = input("Enter new address: ")
                    con = input("Enter new contact: ")
                    gen = input("Enter gender: M or F : ")
                    query  = "update school set name='{}',address='{}',contact='{}',gender='{}' where rollno={}".format(nam,addd,con,gen,rollno)
                    self.cur.execute(query)
                    self.con.commit()
                    check = 1
            if check == 0:
                print("Student not found")
            else:
                print("Student record updated successfully")        
        elif ch == 2:
            R = rollno
            print("\n 1.Name\n 2.Address\n 3.Contact\n 4.Gender\n")
            ch1 = int(input("Enter decision: "))
            #object_g = Management2()
            if ch1 == 1:
                from attachment2 import Management2
                object_g = Management2()
                object_g.update_particular_data(R,"name")
            elif ch1 == 2:
                from attachment2 import Management2
                object_g = Management2()
                object_g.update_particular_data(R,"address")
            elif ch1 == 3:
                from attachment2 import Management2
                object_g = Management2()
                object_g.update_particular_data(R,"contact")
            elif ch1 == 4:
                from attachment2 import Management2
                object_g = Management2()
                object_g.update_particular_data(R,"gender")
                # for row4 in cur:
                #     if row4[0] == rollno:
                #         query = "select * from school where rollno={}".format(rollno)
                #         cur = self.con.cursor()
                #         cur.execute(query)
                #         print("\nDetails of student",rollno,"is:---")
                #         for i in cur:
                #             print("\nName: ",i[1])
                #             print("Address: ",i[2])
                #             print("Contact: ",i[3])
                #             print("Gender: ",i[4])          
                #         gen = input("\nEnter gender:")                                                                 
                #         query  = "update school set gender='{}' where rollno={}".format(gen,rollno)
                #         cur.execute(query)
                #         self.con.commit()
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")
