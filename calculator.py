from tkinter import *
root=Tk()
#title of the application
root.title("Calculator")
e=Entry(root,width=50,borderwidth=20,fg="blue")
e.grid(row=0,column=0,columnspan=20,padx=20,pady=30)

#declaring functions
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def buttonadd():
    firstnum=e.get()
    global f_num
    global math
    math="add"
    f_num=int(firstnum)
    e.delete(0,END)
def equal():
    secondnum=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num+int(secondnum))
    elif math=="sub":
        e.insert(0,f_num-int(secondnum))
    elif math=="mul":
        e.insert(0,f_num*int(secondnum))
    elif math=="div":
        e.insert(0,f_num/int(secondnum))
    elif math=="pow":
        e.insert(0,f_num**int(secondnum))
def sub():
    firstnum=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(firstnum)
    e.delete(0,END)
    return
def mul():
    firstnum=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(firstnum)
    e.delete(0,END)
    return
def div():
    firstnum=e.get()
    global f_num
    global math
    math="div"
    f_num=int(firstnum)
    e.delete(0,END)
    return
def pow():
    firstnum=e.get()
    global f_num
    global math
    math="pow"
    f_num=int(firstnum)
    e.delete(0,END)
    return


#creating buttons

button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_add=Button(root,text="+",padx=40,pady=20,command=buttonadd)
button_equal=Button(root,text="=",padx=50,pady=20,command=equal)
button_clear=Button(root,text="clear",padx=50,pady=20,command=clear)
button_sub=Button(root,text="-",padx=40,pady=20,command=sub)
button_mul=Button(root,text="*",padx=40,pady=20,command=mul)
button_div=Button(root,text="/",padx=40,pady=20,command=div)
button_pow=Button(root,text="**",padx=40,pady=20,command=pow)
buttonquit=Button(root,text="quit",padx=50,pady=20,command=root.quit)

#putting buttons on screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_mul.grid(row=5,column=0)
button_div.grid(row=5,column=1)
button_clear.grid(row=6,column=0)
button_equal.grid(row=5,column=2)
button_pow.grid(row=6,column=1)
buttonquit.grid(row=6,column=2)

#without this the application could not run
root.mainloop()
    

