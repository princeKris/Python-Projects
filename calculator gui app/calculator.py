from tkinter import *
from functools import partial
root=Tk()
root.title("calculator!")
e=Entry(root,width=50)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
taa=str(000)
def button_add(num):
	global taa
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(num))
	taa=str(current)+str(num)

def button_eq():
	e.delete(0,END)
	button_add(eval(taa))
def button_clear():
	e.delete(0,END)

def button_d():
	en=e.get()
	e.delete(0, END)
	button_add(en[0:-1])

for i in range(0,10):
	exec(f'button_{i}=Button(root,text="{i}",padx=40,pady=20,command=partial(button_add,"{i}"))')
button_clear=Button(root,text="clear",padx=70,pady=20,command=button_clear)
button_ad=Button(root,text="+",padx=40,pady=20,command=partial(button_add,"+"))
button_equal=Button(root,text="=",padx=80,pady=20,command=button_eq)
button_de=Button(root,text="<=",padx=40,pady=20,command=button_d)
button_divi=Button(root,text="/",padx=40,pady=20,command=partial(button_add,"/"))
button_multi=Button(root,text="*",padx=40,pady=20,command=partial(button_add,"*"))
button_sub=Button(root,text="-",padx=40,pady=20,command=partial(button_add,"-"))
button_point=Button(root,text=".",padx=40,pady=20,command=partial(button_add,"."))
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_divi.grid(row=3,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_ad.grid(row=2,column=3)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_de.grid(row=1,column=3)
button_0.grid(row=4,column=0)
button_point.grid(row=4,column=1)
button_clear.grid(row=4,column=2,columnspan=2)
button_sub.grid(row=5,column=0)
button_multi.grid(row=5,column=1)
button_equal.grid(row=5,column=2,columnspan=2)
root.mainloop()