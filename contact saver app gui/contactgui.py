from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
conn=sqlite3.connect("sqll.db")
print("connection eastablished")
def cr():
	conn.execute('''CREATE TABLE IF NOT EXISTS TEST (NAME TEXT NOT NULL, NUMBER INT NOT NULL)''')
cr()
root=Tk()
root.title("contacts ?")
root.geometry("425x678")
canvas=Canvas(width=425,height=678,bg="blue")
filename=ImageTk.PhotoImage(Image.open("bg.jpg"))
ba=Label(root,image=filename)
ba.place(x=0,y=0,relwidth=1,relheight=1)
canvas.pack()
def cr():
	conn.execute('''CREATE TABLE IF NOT EXISTS TEST (NAME TEXT NOT NULL, NUMBER INT NOT NULL)''')
def create():
	contactName=str(name.get()).lower()
	contactNumber=int(number.get())
	conn.execute(f"INSERT INTO TEST (NAME,NUMBER) VALUES('{contactName}',{contactNumber})")
	conn.commit()
	read()
def update():
	contactName=(name.get()).lower()
	contactNumber=(number.get())
	if ((len(contactNumber)!=0) and (len(contactName)!=0)):
		response=messagebox.askokcancel("edit",f"{contactName} number changed into {contactNumber} ?")
		Label(root,text=response).pack()
		if (response==1):
			conn.execute(f"UPDATE TEST SET NUMBER={int(contactNumber)} WHERE NAME='{str(contactName)}'")
	else:
		response=messagebox.showinfo("cancel",f"{contactName} name or number doesn't exist {contactNumber}\n pleas check the name and number ?")
		Label(root,text=response).pack()
	conn.commit()
	read()
def read():
	mylist.delete(0,END)
	cursor=conn.execute("SELECT NAME,NUMBER FROM TEST")
	for row in cursor:
		mylist.insert(END,f"{row[0]} : {row[1]}")
def delete():
	contactName=(name.get()).lower()
	conn.execute(f"DELETE FROM TEST WHERE NAME='{contactName}'")
	conn.commit()
	read()
def search():
	contactName=(name.get()).lower()
	cursor=conn.execute(f"SELECT * FROM TEST WHERE NAME LIKE'%{contactName}%'")
	mylist.delete(0,END)
	for row in cursor:
		mylist.insert(END,f"{row[0]} : {row[1]}")

button_create=Button(root,text="create",padx=20,pady=20,command=create)
button_update=Button(root,text="update",padx=20,pady=20,command=update)
button_read=Button(root,text=" show  ",padx=20,pady=20,command=read)
button_delete=Button(root,text="delete",padx=20,pady=20,command=delete)
button_search=Button(root,text="search",padx=20,pady=20,command=search)
button_create.place(height=35,relx=0,rely=0,anchor='nw')
button_update.place(height=35,relx=0.20,rely=0,anchor='nw')
button_read.place(height=35,relx=0.40,rely=0,anchor='nw')
button_delete.place(height=35,relx=0.60,rely=0,anchor='nw')
button_search.place(height=35,relx=0.80,rely=0,anchor='nw')
label_name=Label(root,text="name",padx=20,pady=20)
name=Entry(root,width=36)
label_number=Label(root,text="number",padx=20,pady=20)
number=Entry(root,width=36)
label_name.place(height=35,relx=0,rely=0.07,anchor='nw')
name.place(height=35,relx=0.25,rely=0.07,anchor='nw')
label_number.place(height=35,relx=0,rely=0.14,anchor='nw')
number.place(height=35,relx=0.25,rely=0.14,anchor='nw')

sb=Scrollbar(root)
sb.place(height=490,relx=0.90,rely=0.21,anchor='nw')
mylist=Listbox(root,width=43,yscrollcommand=sb.set)
mylist.place(height=490,relx=0.07,rely=0.21,anchor='nw')
sb.config(comman=mylist.yview)
root.mainloop()