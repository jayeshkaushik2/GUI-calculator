# calculator number one
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
