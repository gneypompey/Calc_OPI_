from tkinter import *
import math

win = Tk()
win.title("Calculator")
win.geometry('315x510')
win.configure(background='grey')

def btnclick(num):
    global operator
    operator = operator + str(num)
    _input.set(operator)

def clear():
    global operator
    operator = ""
    _input.set("")

def answer():
    global operator
    try:
        ans = str(eval(operator))
        _input.set(ans)
        operator = ""
    except Exception as e:
        _input.set("Error")
        operator = ""

def power():
    global operator
    operator = str(operator) + "**"
    _input.set(operator)

def square_root():
    global operator
    try:
        ans = str(math.sqrt(float(operator)))
        _input.set(ans)
        operator = ""
    except ValueError:
        _input.set("Error")
        operator = ""

def sin_func():
    global operator
    try:
        ans = str(math.sin(math.radians(float(operator))))
        _input.set(ans)
        operator = ""
    except ValueError:
        _input.set("Error")
        operator = ""

def cos_func():
    global operator
    try:
        ans = str(math.cos(math.radians(float(operator))))
        _input.set(ans)
        operator = ""
    except ValueError:
        _input.set("Error")
        operator = ""

def tan_func():
    global operator
    try:
        ans = str(math.tan(math.radians(float(operator))))
        _input.set(ans)
        operator = ""
    except ValueError:
        _input.set("Error")
        operator = ""

def factorial():
    global operator
    try:
        ans = str(math.factorial(int(operator)))
        _input.set(ans)
        operator = ""
    except ValueError:
        _input.set("Error")
        operator = ""


label = Label(win, font=('ariel', 20, 'bold'), text='Калькулятор', bg='grey', fg='black')
label.grid(columnspan=4)

_input = StringVar()
operator = ""

display = Entry(win, font=('ariel', 20, 'bold'), textvariable=_input, insertwidth=7, bd=5, bg="white", justify='right')
display.grid(columnspan=4)

# Row 1
b7 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="7", bg="grey", command=lambda: btnclick(7))
b7.grid(row=2, column=0, sticky="nsew")

b8 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="8", bg="grey", command=lambda: btnclick(8))
b8.grid(row=2, column=1, sticky="nsew")

b9 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="9", bg="grey", command=lambda: btnclick(9))
b9.grid(row=2, column=2, sticky="nsew")

Add = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="+", bg="grey", command=lambda: btnclick("+"))
Add.grid(row=2, column=3, sticky="nsew")

# Row 2
b4 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="4", bg="grey", command=lambda: btnclick(4))
b4.grid(row=3, column=0, sticky="nsew")

b5 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="5", bg="grey", command=lambda: btnclick(5))
b5.grid(row=3, column=1, sticky="nsew")

b6 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="6", bg="grey", command=lambda: btnclick(6))
b6.grid(row=3, column=2, sticky="nsew")

Sub = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="-", bg="grey", command=lambda: btnclick("-"))
Sub.grid(row=3, column=3, sticky="nsew")

# Row 3
b1 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="1", bg="grey", command=lambda: btnclick(1))
b1.grid(row=4, column=0, sticky="nsew")

b2 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="2", bg="grey", command=lambda: btnclick(2))
b2.grid(row=4, column=1, sticky="nsew")

b3 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="3", bg="grey", command=lambda: btnclick(3))
b3.grid(row=4, column=2, sticky="nsew")

mul = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="*", bg="grey", command=lambda: btnclick("*"))
mul.grid(row=4, column=3, sticky="nsew")

# Row 4
b0 = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="0", bg="grey", command=lambda: btnclick(0))
b0.grid(row=5, column=0, sticky="nsew")

bc = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="c", bg="grey", command=clear)
bc.grid(row=5, column=1, sticky="nsew")

Decimal = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text=".", bg="grey", command=lambda: btnclick("."))
Decimal.grid(row=5, column=2, sticky="nsew")

Div = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="/", bg="grey", command=lambda: btnclick("/"))
Div.grid(row=5, column=3, sticky="nsew")

# Row 5 for additional operations
Power = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="^", bg="grey", command=power)
Power.grid(row=6, column=0, sticky="nsew")

Sqrt = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="√", bg="grey", command=square_root)
Sqrt.grid(row=6, column=1, sticky="nsew")

Sin = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="sin", bg="grey", command=sin_func)
Sin.grid(row=6, column=2, sticky="nsew")

Cos = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="cos", bg="grey", command=cos_func)
Cos.grid(row=6, column=3, sticky="nsew")

# Row 6 for additional operations
Tan = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="tan", bg="grey", command=tan_func)
Tan.grid(row=7, column=0, sticky="nsew")

Factorial = Button(win, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20, 'bold'), text="!", bg="grey", command=factorial)
Factorial.grid(row=7, column=1, sticky="nsew")

bequal = Button(win, padx=16, pady=16, bd=4, width=16, fg="black", font=('ariel', 20, 'bold'), text="=", bg="grey", command=answer)
bequal.grid(columnspan=4, sticky="nsew")

# Configure row and column weight to make buttons expand equally
for i in range(8):
    win.grid_rowconfigure(i, weight=1)
for j in range(4):
    win.grid_columnconfigure(j, weight=1)

win.mainloop()
