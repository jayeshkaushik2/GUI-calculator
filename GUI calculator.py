# calculator number one
'''
from tkinter import *
root_calculator = Tk()
root_calculator.geometry("175x210")
root_calculator.title("GUI calculator")
root_calculator.configure(bg="black")

def click(event):
    text = event.widget.cget("text")
    if(text == "="):
        if(scvalue.get().isdigit()):
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif(text == "clear"):
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root_calculator, textvar=scvalue, font=("lucida 11 bold"))
screen.pack()
#-------------Numbers 1 to 9 and 0 ----------------------#
f = Frame(root_calculator)
button1 = Button(root_calculator, text="1", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button1.place(x=1, y=25)
button1.bind("<Button-1>", click)

button2 = Button(root_calculator, text="2", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button2.place(x=44, y=25)
button2.bind("<Button-1>", click)

button3 = Button(root_calculator, text="3", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button3.place(x=87, y=25)
button3.bind("<Button-1>", click)

button4 = Button(root_calculator, text="4", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button4.place(x=1, y=70)
button4.bind("<Button-1>", click)

button5 = Button(root_calculator, text="5", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button5.place(x=44, y=70)
button5.bind("<Button-1>", click)

button6 = Button(root_calculator, text="6", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button6.place(x=87, y=70)
button6.bind("<Button-1>", click)

button7 = Button(root_calculator, text="7", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button7.place(x=1, y=115)
button7.bind("<Button-1>", click)

button8 = Button(root_calculator, text="8", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button8.place(x=44, y=115)
button8.bind("<Button-1>", click)

button9 = Button(root_calculator, text="9", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button9.place(x=87, y=115)
button9.bind("<Button-1>", click)

button18 = Button(root_calculator, text=".", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button18.place(x=1, y=160)
button18.bind("<Button-1>", click)

button17 = Button(root_calculator, text="0", width=4, height=2,bg="lightblue", fg="black", font=("lucida", 10, "bold"))
button17.place(x=44, y=160)
button17.bind("<Button-1>", click)
#-------------- + , - , x , / --------------------------#

button11 = Button(root_calculator, text="+", width=4, height=2,bg="yellow", fg="black", font=("lucida", 10, "bold"))
button11.place(x=130, y=25)
button11.bind("<Button-1>", click)

button12 = Button(root_calculator, text="-", width=4, height=2,bg="yellow", fg="black", font=("lucida", 10, "bold"))
button12.place(x=130, y=70)
button12.bind("<Button-1>", click)

button13 = Button(root_calculator, text="*", width=4, height=2,bg="yellow", fg="black", font=("lucida", 10, "bold"))
button13.place(x=130, y=115)
button13.bind("<Button-1>", click)

button14 = Button(root_calculator, text="/", width=4, height=2,bg="yellow", fg="black", font=("lucida", 10, "bold"))
button14.place(x=130, y=160)
button14.bind("<Button-1>", click)

#----------------   = and clear   ---------------------------------#

button16 = Button(root_calculator, text="=", width=4, height=2,bg="green", fg="black", font=("lucida", 10, "bold"))
button16.place(x=87, y=160)
button16.bind("<Button-1>", click)

button10 = Button(root_calculator, text="clear", width=4, height=2,bg="green", fg="black", font=("lucida", 10, "bold"))
button10.place(x=1, y=160)
button10.bind("<Button-1>", click)
f.pack()


root_calculator.mainloop()
'''










from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if display_value.get().isdigit():
            value = int(display_value.get())
        else:
            value = eval(display_value.get())
        
        display_value.set(value)
        display_numbers.update()
    
    elif text == "!" and display_value.get().isdigit():
        new_value = int(display_value.get()) + 1
        fact = 1
        for i in range(1, new_value):
            fact = fact*i
        
        display_value.set(fact)
        display_numbers.update()
    
    elif text == "DEL":
        display_value.set("")
        display_numbers.update()
    
    else:
        display_value.set(display_value.get() + text)
        display_numbers.update()
    

root = Tk()
root.title("Calculator")
root.geometry("400x500")


# making the entry widget for display the numberss
display_value = StringVar()
display_value.set("")
display_numbers = Entry(root, textvar=display_value, bg="grey", font="lucida 20 bold", borderwidth=1)
display_numbers.grid(row=1, column=0)

frame_numbers = Frame(root, bg="black")
b1 = Button(frame_numbers, text='1', font="lucida 10 bold", padx=10, pady=10)
b1.grid(row=2, column=0, padx=10, pady=5, ipadx=4)
b1.bind("<Button-1>", click)

b2 = Button(frame_numbers, text='2', font="lucida 10 bold", padx=10, pady=10)
b2.grid(row=2, column=1, padx=10, pady=5, ipadx=4)
b2.bind("<Button-1>", click)

b3 = Button(frame_numbers, text='3', font="lucida 10 bold", padx=10, pady=10)
b3.grid(row=2, column=2, padx=10, pady=5, ipadx=4)
b3.bind("<Button-1>", click)

b4 = Button(frame_numbers, text='4', font="lucida 10 bold", padx=10, pady=10)
b4.grid(row=3, column=0, padx=10, pady=5, ipadx=4)
b4.bind("<Button-1>", click)

b5 = Button(frame_numbers, text='5', font="lucida 10 bold", padx=10, pady=10)
b5.grid(row=3, column=1, padx=10, pady=5, ipadx=4)
b5.bind("<Button-1>", click)

b6 = Button(frame_numbers, text='6', font="lucida 10 bold", padx=10, pady=10)
b6.grid(row=3, column=2, padx=10, pady=5, ipadx=4)
b6.bind("<Button-1>", click)

b7 = Button(frame_numbers, text='7', font="lucida 10 bold", padx=10, pady=10)
b7.grid(row=4, column=0, padx=10, pady=5, ipadx=4)
b7.bind("<Button-1>", click)

b8 = Button(frame_numbers, text='8', font="lucida 10 bold", padx=10, pady=10)
b8.grid(row=4, column=1, padx=10, pady=5, ipadx=4)
b8.bind("<Button-1>", click)

b9 = Button(frame_numbers, text='9', font="lucida 10 bold", padx=10, pady=10)
b9.grid(row=4, column=2, padx=10, pady=5, ipadx=4)
b9.bind("<Button-1>", click)

b_point = Button(frame_numbers, text='.', font="arial 10 bold", padx=10, pady=10)
b_point.grid(row=5, column=0, ipadx=4)
b_point.bind("<Button-1>", click)

b0 = Button(frame_numbers, text='0', font="lucida 10 bold", padx=10, pady=10)
b0.grid(row=5, column=1, ipadx=4)
b0.bind("<Button-1>", click)

b_equal = Button(frame_numbers, text='=', font="arial 10 bold", padx=10, pady=10)
b_equal.grid(row=5, column=2, ipadx=4)
b_equal.bind("<Button-1>", click)

# starting of the operator delete
b_del = Button(frame_numbers, text="DEL", font="arial 10 bold", padx=4, pady=10)
b_del.grid(row=2, column=3)
b_del.bind("<Button-1>", click)

# starting of the operator plus
b_plus = Button(frame_numbers, text="+", font="arial 10 bold", padx=12, pady=10)
b_plus.grid(row=3, column=3)
b_plus.bind("<Button-1>", click)

# starting of the operator minus
b_minus = Button(frame_numbers, text="-", font="arial 10 bold", padx=14, pady=10)
b_minus.grid(row=4, column=3)
b_minus.bind("<Button-1>", click)

# starting of the operator multiply
b_multi = Button(frame_numbers, text="*", font="arial 10 bold", padx=12, pady=10)
b_multi.grid(row=5, column=3)
b_multi.bind("<Button-1>", click)

# starting of the operator divide(quotient)
b_divide = Button(frame_numbers, text="/", font="arial 10 bold", padx=10, pady=10)
b_divide.grid(row=6, column=3)
b_divide.bind("<Button-1>", click)

# starting of sin
b_sin = Button(frame_numbers, text="Sin", font="arial 10 bold", padx=10, pady=10)
b_sin.grid(row=6, column=0, pady=4)
b_sin.bind("<Button-1>", click)

# starting of iota(!)
b_fact = Button(frame_numbers, text="!", font="arial 10 bold", padx=10, pady=10)
b_fact.grid(row=6, column=1)
b_fact.bind("<Button-1>", click)

# starting of reminder
b_remi = Button(frame_numbers, text="%", font="arial 10 bold", padx=10, pady=10)
b_remi.grid(row=6, column=2)
b_remi.bind("<Button-1>", click)

frame_numbers.grid()

root.mainloop()