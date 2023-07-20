from PIL import Image
import tkinter as tk
from tkinter import ttk, StringVar, Label, messagebox
from tkinter import filedialog as fd
def opf():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    mll = list(filenames)
    create(mll)

def create(mlls):
	mll=mlls
	im1=Image.open(f'{mll[0]}').convert('RGB')
	ml=mll[1:]
	images = [Image.open(f'{imgNumber}').convert('RGB') for imgNumber in ml]
	inp = inputtxt.get(1.0, "end-1c")
	im1.save(f"{inp}.pdf", save_all=True, append_images=images)
	messagebox.showinfo("img to pdf", "sucessfuly convert")
	
r = tk.Tk()
r.title('img to pdf')
w = Label(r, text ='Enter pdf name', font = "50") 
w.pack()
inputtxt = tk.Text(r,height = 2,width = 20)
inputtxt.pack()
button = tk.Button(r, text='open', width=25, command=opf)
button.pack()
r.mainloop()