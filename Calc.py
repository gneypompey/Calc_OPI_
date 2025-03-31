from tkinter import *
import math

win = Tk()
win.title("Калькулятор")
win.geometry('315x510')
win.configure(background='grey')

def btnclick(num):
    global operator
    operator += str(num)
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
        operator = ans  # Позволяет продолжить вычисления с полученным результатом
    except Exception:
        _input.set("Error")
        operator = ""

def power():
    global operator
    operator += "**"
    _input.set(operator)

def square_root():
    global operator
    try:
        ans = str(math.sqrt(float(operator)))
        _input.set(ans)
        operator = ans
    except ValueError:
        _input.set("Error")
        operator = ""

def sin_func():
    global operator
    try:
        ans = str(math.sin(math.radians(float(operator))))
        _input.set(ans)
        operator = ans
    except ValueError:
        _input.set("Error")
        operator = ""

def cos_func():
    global operator
    try:
        ans = str(math.cos(math.radians(float(operator))))
        _input.set(ans)
        operator = ans
    except ValueError:
        _input.set("Error")
        operator = ""

def tan_func():
    global operator
    try:
        ans = str(math.tan(math.radians(float(operator))))
        _input.set(ans)
        operator = ans
    except ValueError:
        _input.set("Error")
        operator = ""

def factorial():
    global operator
    try:
        num = int(float(operator))
        if num < 0:
            raise ValueError
        ans = str(math.factorial(num))
        _input.set(ans)
        operator = ans
    except (ValueError, OverflowError):
        _input.set("Error")
        operator = ""

def key_press(event):
    global operator
    if event.char.isdigit() or event.char in ".+-*/()":
        operator += event.char
        _input.set(operator)
        return "break"  # Запобігає подвійному введенню
    elif event.keysym == "Return":
        answer()
        return "break"
    elif event.keysym == "BackSpace":
        operator = operator[:-1]
        _input.set(operator)
        return "break"
    elif event.keysym == "Escape":
        clear()
        return "break"

label = Label(win, font=('ariel', 20, 'bold'), text='Калькулятор', bg='grey', fg='black')
label.grid(columnspan=4)

_input = StringVar()
operator = ""

display = Entry(win, font=('ariel', 20, 'bold'), textvariable=_input, insertwidth=7, bd=5, bg="white", justify='right')
display.grid(columnspan=4, sticky='nsew')
display.bind("<Key>", key_press)

display.focus_set()

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('C', 5, 1), ('.', 5, 2), ('/', 5, 3),
    ('^', 6, 0), ('√', 6, 1), ('sin', 6, 2), ('cos', 6, 3),
    ('tan', 7, 0), ('!', 7, 1)
]

for (text, row, col) in buttons:
    action = lambda x=text: btnclick(x) if x not in ('C', '√', 'sin', 'cos', 'tan', '!', '^') else None
    cmd = {
        'C': clear,
        '√': square_root,
        'sin': sin_func,
        'cos': cos_func,
        'tan': tan_func,
        '!': factorial,
        '^': power
    }.get(text, action)
    Button(win, text=text, font=('ariel', 20, 'bold'), padx=16, pady=16, bd=4, bg='grey', command=cmd).grid(row=row, column=col, sticky='nsew')

bequal = Button(win, text="=", font=('ariel', 20, 'bold'), padx=16, pady=16, bd=4, bg="grey", command=answer)
bequal.grid(row=7, column=2, columnspan=2, sticky="nsew")

for i in range(8):
    win.grid_rowconfigure(i, weight=1)
for j in range(4):
    win.grid_columnconfigure(j, weight=1)

win.mainloop()