import sqlite3
conn=sqlite3.connect("contact.db")
print("connectioin established ")
def create():
	conn.execute('''CREATE TABLE IF NOT EXISTS CONTACT (NAME TEXT NOT NULL, NUMBER INT NOT NULL)''')
def insert():
	print("enter the contact detials\n-----------")
	cname=str(input("enter the conntact name : ")).lower()
	cnumber=int(input(f"enter the {cname} number : "))
	conn.execute(f"INSERT INTO CONTACT(NAME,NUMBER) VALUES('{cname}',{cnumber})")
	conn.commit()
def update(nam,num):
	print("the contact details is updated\n-----------")
	conn.execute(f"UPDATE CONTACT SET NUMBER={num} WHERE NAME='{nam}'")
	conn.commit()
def read():
	print("the contact detials\n-----------")
	cursor=conn.execute("SELECT NAME,NUMBER FROM CONTACT")
	for row in cursor:
		print(f"{row[0]} : {row[1]}")
def delete(nam):
	conn.execute(f"DELETE FROM CONTACT WHERE NAME='{nam}'")
	conn.commit()
	print(f"{nam} the contact detials are deletd\n-----------")
def search(sea):
	print("likely the contact detials\n-----------")
	cursor=conn.execute(f"SELECT * FROM CONTACT WHERE NAME LIKE'%{sea}%'")
	for row in cursor:
		print(f"{row[0]} : {row[1]}")

con=True
create()
while con:
	inputs=int(input("\n1.for insert values\n2.for delete contact\n3.for update contact\n4.for read contact\n5.search\n6.exit\n =>: "))
	if(inputs==1):
		insert()
	elif(inputs==2):
		nam=str(input("enter the name to delete contact details : "))
		delete(nam)
	elif(inputs==3):
		nam=str(input("enter the name to edit contact details : "))
		num=int(input("enter the number to edit contact details : "))
		update(nam,num)
	elif(inputs==4):
		read()
	elif(inputs==5):
		sea=str(input("enter the name to likely contact details : "))
		search(sea)
	else:
		con=False
conn.close()