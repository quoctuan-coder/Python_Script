import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
win = tk.Tk()
win.title("Python GUI")
# win.resizable(0,0)

# modify adding label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# button click event
def clickMe():
    action.configure(text='Hello ' + name.get())

# text box entry
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
# action.configure(state='disabled')

# drop down menu
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(4)

# checkbutton 1 (disabled)
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W, columnspan=3)

# checkbutton 2 (unchecked)
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W, columnspan=3)

# checkbutton 3 (enabled)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W, columnspan=3)

# GUI callback function
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:       check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:       check2.configure(state='normal')

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())

# scrolled text
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

# radio button global variables
colors = ["Blue", "Gold", "Red"]

# Radiobutton callback function
def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar.
radVar.set(99)

# Now we are creating all three Radiobutton widgets within one loop.
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# direct keyboard input to text box entry
nameEntered.focus()

win.mainloop()