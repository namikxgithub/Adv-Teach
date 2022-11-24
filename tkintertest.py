from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")

import os
def takess():
    ss="python3 SS.py"
    os.system('%s'%ss)
def track():
    ss="python3 main_video.py"
    os.system('%s'%ss)
def summary():
    ss="python3 audioText.py"
    os.system('%s'%ss)
def display_text():
   global entry
   string= entry.get()

root=customtkinter.CTk()
root.title('Advance Meet')
root.geometry("1920x1080")
bg = PhotoImage(file = "bg2.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

ssbut=Button(root,text="ScreenShot",command=takess,width=20,borderwidth=0)
ssbut.place(x=100,y=100)

vidtrace=Button(root,text="Track me",command=track,width=20,borderwidth=0)
vidtrace.place(x=400,y=100)

txt=Button(root,text="Summarize",command=summary,width=20,borderwidth=0)
txt.place(x=700,y=100)

entry= Entry(root, width= 40,borderwidth=0)
entry.focus_set()
entry.place(x=100,y=703)

Button(root, text= "Store mail", command= display_text,borderwidth=0).place(x=450,y=700)

root.mainloop()