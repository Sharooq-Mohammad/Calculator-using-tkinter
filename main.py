from tkinter import *

win = Tk()
win.geometry("300x300")
win.resizable(0, 0)

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
  
expression = ""

input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# btns_frame = Frame(win)
# btns_frame.pack()

win.mainloop()
