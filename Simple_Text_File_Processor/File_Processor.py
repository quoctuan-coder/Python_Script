from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("700x500+300+300")
root.title("File Processor")

frm = ttk.Frame(root,padding=10)
frm.grid()
title_lable= Label(root,text="File Processor-Generator")

#title_lable.grid(column=0,row=0)
title_lable.grid(column=0,row=0)

entry = Entry(root)
entry.grid(column=0,row=1)

btn_Select = Button(root,text="Browse Foler or File")
btn_Select.grid(column=1,row=1)

btn_Start = Button(root,text="Start")
btn_Start.grid(column=1,row=2)


root.mainloop()





