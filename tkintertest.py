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
def summary2():
    ss="python3 audioText.py"
    os.system('%s'%ss)
def summary():
    ss="python3 audioText2.py"
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

ssbut=customtkinter.CTkButton(root,text="ScreenShot",text_font="Roboto 20",command=takess,height=60,borderwidth=0)
ssbut.place(x=100,y=100)

vidtrace=customtkinter.CTkButton(root,text="Track me",text_font="Roboto 20",command=track,height=60,borderwidth=0)
vidtrace.place(x=300,y=100)

txt=customtkinter.CTkButton(root,text="Record Live",text_font="Roboto 20",command=summary,height=60,borderwidth=0)
txt.place(x=500,y=100)

txt=customtkinter.CTkButton(root,text="Summarize recording",text_font="Roboto 20",command=summary2,height=60,borderwidth=0)
txt.place(x=700,y=100)

entry= Entry(root,width=40,borderwidth=0,justify=CENTER)
entry.focus_set()
entry.pack(pady=20)
entry.place(x=100,y=800)
entry.insert(0,"Email Address")

entry2= Entry(root,width=40,borderwidth=0,justify=CENTER)
entry2.focus_set()
entry2.pack(pady=20)
entry2.place(x=100,y=850)
entry2.insert(0,"File Name")

customtkinter.CTkButton(root, text= "Set Email",text_font="Roboto 20",command= display_text,borderwidth=0,height=60).place(x=450,y=800)

root.mainloop()