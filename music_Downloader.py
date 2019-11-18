import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import os
import threading

window = tk.Tk()
window.title('my window')
window.geometry('400x200')


l = tk.Label(window, 
    text='Youtube music download',
    font=('Arial', 12),
    )
l.pack()

statue = 0
downloading = False

def start_download():
    t1 = threading.Thread(target=download)
    t1.start()
    global statue
    global downloading
    statue = 0
    var.set('downloading')
    tk.messagebox.showinfo(title='download start', message='Please waitting')
    
    t2 = threading.Thread(target=check)
    t2.start()
    
def download():
    URL = var_URL.get()
    realpath = path.get()
    fullURL='youtube-dl -x --audio-format mp3 -o "'
    aaa='/%(title)s.%(ext)s"'
    bbb='--embed-thumbnail --add-metadata '
    ccc=fullURL+realpath+aaa+bbb+URL
    os.system(ccc)
    global statue
    statue = 1
    
def check():
    while True:
        if statue == 1:
            tk.messagebox.showinfo(title='download end', message='done')
            var.set('Finishing')
            break

def selectPath():
    path_ = askdirectory()
    path.set(path_)

tk.Label(window, text='URL').place(x=20, y= 50)

var_URL = tk.StringVar()
var_URL.set('http...')
entry_URL = tk.Entry(window, textvariable=var_URL)
entry_URL.place(x=100, y=50)

btn_login = tk.Button(window, text='download', command= start_download)
btn_login.place(x=170, y=100)

path = tk.StringVar()
tk.Label(window, text = "儲存路徑").place(x=20, y= 130)
entry_path = tk.Entry(window, textvariable = path).place(x=100, y=130)
btn_path = tk.Button(window, text='選擇', command= selectPath).place(x=300, y=130)


var = tk.StringVar()
tk.Label(window, textvariable=var).place(x=20, y= 150)

window.mainloop()