from tkinter import *
import time
app_window=Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font=("Boulder",68,"bold")
background="#16f2ef"
foreground="#78e3af"
border_width=25
label=Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def digital():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital)

digital()
app_window.mainloop()