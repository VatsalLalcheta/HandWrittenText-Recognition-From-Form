import tkinter as tk
import cv2
from tkinter import filedialog
import numpy as np
import os
import try4
    
top = tk.Tk()  
top.geometry("400x250")  
e1 = tk.Entry(top)
e1.place(x = 150,y=50)

e2 = tk.Entry(top)
e2.place(x = 150,y=90)

e2 = tk.Entry(top)
e2.place(x = 150,y=90)

#e3 = tk.Entry(top,width=5)
#e3.place(x = 150,y=130)
#img_group = tk.Label(top,text="Enter form length:")
#img_group.place(x = 30 , y = 130)
main_folder_path = tk.Label(top, text = "Main Folder Path:").place(x = 30,y = 50)  
sub_folder_path = tk.Label(top, text = "Sub Folder Path:").place(x = 30, y = 90)  

f1=''

def select_folder1():
    global f1
    f1 = filedialog.askdirectory()
    e1.insert(0,f1)

def select_folder2():
    global f1
    f2 = filedialog.askdirectory()
    e2.insert(0,f2)
    
def fun():
    #n = e3.get()
    main_dir = e1.get()
    sec_dir = e2.get()
    cur_path= os.getcwd()
    fileiter = os.walk(main_dir)
    file_list=[]
    for cur_path,dir_name,file_name in fileiter:
        file_list.append(file_name)
    try4.box_extraction("hack.png")
'''
    for i in file_list[0]:
        print(i)
        q = i.split(".")
        if q[1]=="png" or q[1]=="jpg" or q[1] == "jpeg":
            try4.box_extraction(i)   
        else:
            print("pass")
'''    
br1 = tk.Button(top,text="Browse",command = select_folder1)
br1.place(x = 300, y = 50)

br2 = tk.Button(top,text="Browse",command = select_folder2)
br2.place(x = 300, y = 90)

br3 = tk.Button(top,text="Go",command = fun,width=10)
br3.place(x = 300, y = 200)
top.mainloop()  
