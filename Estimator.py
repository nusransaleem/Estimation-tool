import tkinter as tk
import tkinter.filedialog as tkFileDialog
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from IP_Model.DataHandler import DataHandler as dHandle
from IP_Model.FileHandler import FileHandler as fHandle

from SendEmail import *
from Executer import Execute

# Call data handler to access paths.
dh = dHandle()
is_generated = False


# To Copy files to the input folder.
def get_files():
    has_pdf = True
    files = tkFileDialog.askopenfilenames(parent=root, title='Choose a file')
    files = root.tk.splitlist(files)
    msg_upload = "Your files successfully uploaded"
    if len(files) == 0:
        has_pdf = False
        msg_upload = "Please select files."
    elif len(files) != 0:
        for f in files:
            if '.pdf' not in f:
                has_pdf = False
                msg_upload = "Error\nPlease upload PDF only."

    messagebox.showinfo("information", msg_upload)

    if has_pdf:
        for f in files:
            fHandle.CopyFiles(f, dh.IN_FOLDER)


def generate_files():
    exe = Execute()
    if exe.is_file_exists:
        print("Generate")
        tempList = exe.lst_estimations
        tempList.sort(key=lambda e: e[1], reverse=True)
        global is_generated
        is_generated = True
        for i, (name, time) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(name, time))
    else:
        print("Input your files")
       # messagebox.showinfo("information", "Input your files")


def export_file():
    #if is_generated:
        messagebox.showinfo("information", "Exported!")
        print("Exported")
    #else:
     #   messagebox.showinfo("information", "Please generate the estimation")


def send_mail():
    #if btnGenerate:
        send = SendEmail("nusransaleem@gmail.com")
        messagebox.showinfo("information", "email successfully sent")
    #else:
        #messagebox.showinfo("information", "Please generate the estimation")


root = tk.Tk()
# root.geometry("800x800")
label = tk.Label(root, text="Effort Estimation", font=("Arial", 30)).grid(row=0, columnspan=3)
# create Treeview with 2 columns
cols = ('Specification', 'Time (Minutes)')
listBox = ttk.Treeview(root, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)

btnUpload = tk.Button(root, text="Upload files", width=15, command=get_files).grid(row=4, column=0)
btnGenerate = tk.Button(root, text="Generate", width=15, command=generate_files).grid(row=4, column=1)
lblSpace = tk.Label(root, text=" ", width=15, height=2).grid(row=5, column=0, columnspan=2)
btnEmail = tk.Button(root, text="Send Email ", width=15, command=send_mail).grid(row=6, column=0)
btnExport = tk.Button(root, text="Export", width=15, command=export_file).grid(row=6, column=1)
root.mainloop()
