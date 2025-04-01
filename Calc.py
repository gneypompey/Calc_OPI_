from tkinter import *
import math

win = Tk()
win.title("Калькулятор")
win.geometry('315x510')
win.configure(background='#D5B79B')  # Темно-бежевий фон для вікна

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

label = Label(win, font=('Helvetica', 20, 'bold'), text='Калькулятор', bg='#D5B79B', fg='#2E2A2A')
label.grid(columnspan=4, pady=10)

_input = StringVar()
operator = ""

display = Entry(win, font=('Helvetica', 20, 'bold'), textvariable=_input, insertwidth=7, bd=5, bg="#F4D7B8", fg="#2E2A2A", justify='right', relief='flat')
display.grid(columnspan=4, sticky='nsew', padx=20, pady=10)
display.bind("<Key>", key_press)

display.focus_set()

# Темно-бежеві кольори для кнопок
button_bg = '#F4D7B8'  # Світло-бежевий фон для кнопок
button_fg = '#2E2A2A'  # Темний текст для кнопок
button_active_bg = '#E1C29B'  # Легкий бежевий фон при натисканні
button_border = '1px solid #B18F6A'  # Легкий бордер для кнопок

def create_rounded_button(master, text, row, col, cmd, colspan=1):
    button = Button(master, text=text, font=('Helvetica', 20, 'bold'), padx=20, pady=20, bd=4, bg=button_bg, fg=button_fg, activebackground=button_active_bg, relief='solid', highlightthickness=0, command=cmd)
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5, columnspan=colspan)
    button.config(borderwidth=2, relief="solid", highlightthickness=0)
    button.config(width=4, height=2, font=("Helvetica", 18))
    return button

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

    create_rounded_button(win, text, row, col, cmd)

bequal = create_rounded_button(win, "=", 7, 2, answer, colspan=2)

for i in range(8):
    win.grid_rowconfigure(i, weight=1)
for j in range(4):
    win.grid_columnconfigure(j, weight=1)

win.mainloop()