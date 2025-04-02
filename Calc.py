from tkinter import *
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Створення головного вікна
win = Tk()
win.title("Калькулятор")
win.geometry('500x700')  # Збільшено висоту вікна
win.configure(background='#2C3E50')  # Фон вікна

# Функція для додавання числа до виразу
def btnclick(num):
    global operator
    operator += str(num)
    _input.set(operator)

# Функція для очищення дисплею
def clear():
    global operator
    operator = ""
    _input.set("")

# Функція для обчислення результату виразу
def answer():
    global operator
    try:
        # Замінюємо ^ на  для правильного обчислення степеня
        operator = operator.replace("^", "").replace("x", "x")
        # Обчислюємо вираз та оновлюємо дисплей
        ans = str(eval(operator, {"builtins": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt}))
        _input.set(ans)
        operator = ans
    except Exception as e:
        # Виводимо помилку на дисплей, якщо вона виникла
        _input.set(f"Error: {e}")
        operator = ""

# Функція для додавання символу степеня
def power():
    global operator
    operator += "^"
    _input.set(operator)

# Функція для обчислення квадратного кореня
def square_root():
    global operator
    try:
        # Обчислюємо квадратний корінь
        ans = str(math.sqrt(float(operator)))
        _input.set(ans)
        operator = ans
    except ValueError:
        # Якщо введене значення неправильне
        _input.set("Error")
        operator = ""

# Функція для додавання функції синуса
def sin_func():
    global operator
    operator += "sin("
    _input.set(operator)

# Функція для додавання функції косинуса
def cos_func():
    global operator
    operator += "cos("
    _input.set(operator)

# Функція для додавання функції тангенса
def tan_func():
    global operator
    operator += "tan("
    _input.set(operator)

# Функція для обчислення факторіалу
def factorial():
    global operator
    try:
        # Перевіряємо, чи є введене число цілим
        num = int(float(operator))
        if num < 0:
            raise ValueError
        ans = str(math.factorial(num))
        _input.set(ans)
        operator = ans
    except (ValueError, OverflowError):
        # Якщо сталося помилку, виводимо її
        _input.set("Error")
        operator = ""

# Функція для обробки натискання клавіш з клавіатури
def key_press(event):
    global operator
    if event.char.isdigit() or event.char in ".+-*/()x^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        operator += event.char
        _input.set(operator)
        return "break"
    elif event.keysym == "Return":
        # Якщо натиснуто Enter, обчислюємо результат
        answer()
        return "break"
    elif event.keysym == "BackSpace":
        # Якщо натиснуто BackSpace, видаляємо останній символ
        operator = operator[:-1]
        _input.set(operator)
        return "break"
    elif event.keysym == "Escape":
        # Якщо натиснуто Escape, очищуємо дисплей
        clear()
        return "break"

# Функція для побудови графіка функції
def plot_function():
    global operator, graph_canvas
    try:
        # Замінюємо ^ на  для правильного обчислення степеня
        func = operator.replace("^", "")
        # Створюємо масив значень x від 0 до 10
        x_vals = np.linspace(0, 10, 400)
        # Обчислюємо відповідні значення y для кожного x
        y_vals = np.array([eval(func.replace('x', str(x)), {"builtins": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt}) for x in x_vals])

        # Створюємо графік
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=func)
        ax.set_title("Графік функції", color='white')
        ax.set_xlabel("x", color='white')
        ax.set_ylabel("f(x)", color='white')
        ax.legend()
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
# Якщо графік вже є на екрані, видаляємо його
        if graph_canvas:
            graph_canvas.get_tk_widget().destroy()

        # Створюємо новий графік на основі функції
        graph_canvas = FigureCanvasTkAgg(fig, master=win)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().grid(row=8, column=0, columnspan=4)

        # Додаємо кнопку для приховування графіка
        hide_button.grid(row=9, column=0, columnspan=4)

    except Exception as e:
        # Якщо сталася помилка під час побудови графіка
        _input.set(f"Error: {e}")

# Функція для приховування графіка
def hide_graph():
    global graph_canvas
    if graph_canvas:
        graph_canvas.get_tk_widget().destroy()
        hide_button.grid_forget()

graph_canvas = None

# Заголовок калькулятора
label = Label(win, font=('Poppins', 24, 'bold'), text='Калькулятор', bg='#2C3E50', fg='#FFFFFF')
label.grid(columnspan=4, pady=20)

# Змінна для введення
_input = StringVar()
operator = ""

# Дисплей калькулятора
display = Entry(win, font=('Poppins', 20, 'bold'), textvariable=_input, insertwidth=7, bd=5, bg="#34495E", fg="#FFFFFF", justify='right', relief='flat')
display.grid(columnspan=4, sticky='nsew', padx=20, pady=10)
display.bind("<Key>", key_press)

display.focus_set()

# Кольори кнопок
button_bg = '#34495E'
button_fg = '#FFFFFF'
button_active_bg = '#3A5A8D'
button_border = 'none'  # Забираємо рамки

# Функція для створення кнопок калькулятора
def create_rounded_button(master, text, row, col, cmd, colspan=1, width=4):
    button = Button(master, text=text, font=('Poppins', 18, 'bold'), padx=20, pady=20, bd=4, bg=button_bg, fg=button_fg, activebackground=button_active_bg, relief='flat', highlightthickness=0, command=cmd, width=width)
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5, columnspan=colspan)
    button.config(width=width, height=2, font=("Poppins", 18))
    return button

# Список кнопок для калькулятора
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('C', 5, 1), ('.', 5, 2), ('/', 5, 3),
    ('^', 6, 0), ('√', 6, 1), ('sin', 6, 2), ('cos', 6, 3),
    ('tan', 7, 0), ('!', 7, 1), ('Plot', 7, 2)
]

# Створення кнопок
for (text, row, col) in buttons:
    action = lambda x=text: btnclick(x) if x not in ('C', '√', 'sin', 'cos', 'tan', '!', '^', 'Plot') else None
    cmd = {
        'C': clear,
        '√': lambda: btnclick('sqrt('),
        'sin': sin_func,
        'cos': cos_func,
        'tan': tan_func,
        '!': factorial,
        '^': power,
        'Plot': plot_function
    }.get(text, action)

    create_rounded_button(win, text, row, col, cmd)

# Кнопка для обчислення результату
bequal = create_rounded_button(win, "=", 7, 3, answer, colspan=2)

# Кнопка для приховування графіка
hide_button = create_rounded_button(win, "Сховати графік", 9, 0, hide_graph, colspan=4, width=10)
hide_button.grid_forget()

# Налаштування ваги рядків та стовпців для адаптивності
for i in range(8):
    win.grid_rowconfigure(i, weight=1)
for j in range(4):
    win.grid_columnconfigure(j, weight=1)

# Запуск основного циклу програми
win.mainloop()