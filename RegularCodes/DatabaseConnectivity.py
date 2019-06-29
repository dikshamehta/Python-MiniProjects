import sqlite3
conn= None;

def create_conn():
    global conn
    conn= sqlite3.connect("stms.db")
    print("database created successfully")

def create_table():
    global conn
    conn.execute('''create table student(
    rno int not null,
    name varchar[20] not null,
    age int not null
    )''')
    print("table student created successfully")

def insert_record():
    rno= int(input("Enter Your roll no."))
    name= input("Enter ur name")
    age= int(input("enter your age"))
    global conn
    conn.execute("insert into student(rno,name,age) values(?,?,?)",(rno,name,age))
    conn.commit()
    print("record is entered")

def view_record():
    global conn
    rno=int(input("enter the roll number to view record of"))
    cursors = conn.execute("select * from student")
    for row in cursors:
        print(row[0],row[1],row[2])

def search_record():
    global conn
    rno=int(input("enter the roll number to view record of"))
    cursors = conn.execute("select * from student where rno=?",(rno,))
    data= cursors.fetchall()
    if len(data)==0:
        print("no record found")
    else:
        for row in data:
            print(row[0],row[1],row[2])

def update_record():
    global conn
    rno=int(input("enter the roll number to update"))
    age=int(input("enter the new age"))
    conn.execute("update student set age=? where rno=?",(age,rno))
    conn.commit()
    print("record updated")

def delete_record():
    global conn
    rno=int(input("enter the roll number to delete"))
    conn.execute("delete from student where rno=?",(rno,))
    conn.commit()
    print("record is deleted")




create_conn()
#create_table()
#insert_record()
#view_record()
search_record()
update_record()
delete_record()
