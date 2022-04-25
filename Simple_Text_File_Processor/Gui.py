from argparse import FileType
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD

from turtle import window_height, window_width
from tkinter import filedialog as fd
from tkinter.messagebox import showerror,showinfo,showwarning
import os,glob


# Variable
flag_folder = True
folder_select = ""
flag_select = False
list_file_txt = []
list_file_wxt = []

root = Tk()

root.title("File Processor - Generator")
root.resizable(width=0, height=0)

# Function call
def center():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int ((screen_width/2) - (window_width()/2))
    y = int ((screen_height/2) - (window_height()/2))
    root.geometry("{}x{}+{}+{}".format(screen_width,screen_height,x,y))

def rad_call():
    global flag_folder
    radSel=radVar.get()
    if radSel == 0:
        flag_folder = True
    else:
        flag_folder = False

def btn_start_call():
    if (flag_select):
        generate_rxt()
        generate_sxt()


def btn_select_call():
    global folder_select,flag_select
    if (flag_folder):
        folder_select = fd.askdirectory()
        flag_exist_status = check_file_exist_folder(folder_select)

        if (flag_exist_status):
            lbl_show_folder.config(text=folder_select)
            flag_select = True

    else:
        filetypes = (
            ('Text files','*.txt'),
            ('Write files','*.wxt'),
            ('All files','*.*')
        )
        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)
         
def check_file_exist_folder(folder):
    flag_txt = False
    flag_wxt = False
    for file in os.listdir(folder):
        if (file.endswith(('.txt'))):
            list_file_txt.append(file)
            flag_txt = True
        if (file.endswith(('.wxt'))):
            list_file_wxt.append(file)
            flag_wxt = True

    if (flag_txt == False and flag_wxt == True):
        showwarning(
                title='Warning',
                message="Extension .txt don't exist")
        return False
    elif (flag_wxt == False and flag_txt == True):
        showwarning(
                title='Warning',
                message="Extension .wxt don't exist")
        return False
    elif (flag_wxt == False and flag_txt == False):
        showwarning(
                title='Warning',
                message="Extension .txt and .wxt don't exist")
        return False
    else:
        #showinfo(title="Info",message="File *.txt and *.wxt exist")
        return True

def generate_rxt():
    for file in list_file_txt:
        file_txt = folder_select + "/" + file
        out_file = folder_select + "/" + file.split('.')[0] + '.rxt'
        out_write = open(out_file,'w')
        add_character = ''
        lines_txt = open(file_txt).readlines()
        index = -1
        number_character = 1
        for cnt,line in enumerate(lines_txt):
            if (cnt % 26 == 0 and cnt != 0):
                number_character = cnt // 26 + 1
                index = 0
            else:
                index = index + 1
                number_character = cnt // 26 + 1

            if number_character == 1:
                add_character = chr(97+index)
            elif number_character >= 2:
                add_character = chr(97+number_character-2) + chr(97+index)

            out_line = line.replace('\n','') + '\t' + add_character + '\n'
            out_write.write(out_line)

        out_write.close()

def generate_sxt():
    for file in list_file_txt:
        file_txt = folder_select + "/" + file
        file_wxt = 'Simple_Text_File_Processor/filename01.wxt'
        lines_txt = open(file_txt).readlines()
        lines_wxt = open(file_wxt).readlines()
        out_file = folder_select + "/" + file.split('.')[0] + '.sxt'
        out_write = open(out_file,'w')

        # print(lines_txt)
        for cnt,line in enumerate(lines_txt):
            line = line.replace('\n','').split('\t')[0]
            origin_digits = line.split('.')[0]
            get_three_digits = line.split('.')[1]
            current_convert = ('{},{}'.format(convert2seconds(int(origin_digits)),get_three_digits[0:3]))

            if cnt == 0:
                previous_convert = current_convert
                continue

            out_line = '{} --> {}\n'.format(previous_convert,current_convert)
            previous_convert = current_convert

            out_write.write(out_line)
            
        out_write.close

def convert2seconds(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    ret = '{}:{}:{}'.format(str(hour).zfill(2),str(minutes).zfill(2),str(seconds).zfill(2))
    return ret

# Create title frame
title_frame = Frame(root)
title_frame.pack(padx=20, pady=30)

# Create a label frame
radio_frame = Frame(root,highlightbackground="black", highlightthickness=2)
radio_frame.pack(padx=20, pady=10)

# Create browse fram
browse_frame = Frame(root)
browse_frame.pack(padx=20, pady=10)

# Title
lbl_title= Label(title_frame,text="File Processor/Generator",font=("Arial",30,BOLD))
lbl_title.pack()

lbl_chose= Label(radio_frame,text="Chose:",font=("Arial",15))
lbl_chose.grid(column=0,row=0)

radVar = IntVar()
# Create two radio buttons
radio_folder = Radiobutton(radio_frame,text="Folder (Default)",variable=radVar,value=0,command = rad_call,font=("Arial",15))
radio_folder.select()
radio_folder.grid(column=1,row=0,sticky='w',padx=20)

radio_file = Radiobutton(radio_frame,text="File",variable=radVar,value=1,command = rad_call,font=("Arial",15))
radio_file.grid(column=1,row=1,sticky='w',padx=20)

# Create entry data and button select
#entry_browse = Entry(browse_frame,font=("Arial",15))
#entry_browse.grid(column=0,row=0, padx=20)
lbl_show_folder = Label(browse_frame,font=("Arial",8),width=40,bg='white')
lbl_show_folder.grid(column=0,row=0, padx=20)

btn_select = Button(browse_frame,text="Browse Foler or File",font=("Arial",15),command=btn_select_call)
btn_select.grid(column=1,row=0, padx=20)

btn_Start = Button(root,text="Start",font=("Arial",15),command=btn_start_call)
btn_Start.pack(fill =X, padx=30,pady=30)

root.mainloop()
