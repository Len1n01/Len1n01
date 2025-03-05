from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Основные цвета
BG_COLOR = "#2c3e50"
BTN_COLOR = "#27ae60"
TEXT_COLOR = "#ecf0f1"
ENTRY_BG = "#34495e"
ENTRY_FG = "#ecf0f1"
BTN_HOVER = "#2ecc71"

def calculate_discriminant():
    """Вычисляет дискриминант и отображает его с формулой"""
    try:
        global d, a, b, c
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        if a == 0:
            result_label.config(text="Ошибка! a не может быть 0.", foreground="red")
            btn_roots.config(state=DISABLED)
            btn_graph.config(state=DISABLED)
            btn_viete.config(state=DISABLED)
            return

        d = (b**2) - (4 * a * c)
        formula_text = f"D = b² - 4ac = {b}² - 4×{a}×{c} = {d}"
        result_label.config(text=formula_text, foreground="blue")

        btn_roots.config(state=NORMAL if d >= 0 else DISABLED)
        btn_graph.config(state=NORMAL)
        btn_viete.config(state=NORMAL)

    except ValueError:
        result_label.config(text="Ошибка! Введите числа.", foreground="red")
        btn_roots.config(state=DISABLED)
        btn_graph.config(state=DISABLED)
        btn_viete.config(state=DISABLED)

def calculate_roots():
    """Вычисляет и отображает корни уравнения"""
    if d < 0:
        result_label.config(text="Нет корней (D < 0)", foreground="red")
    elif d == 0:
        x = -b / (2 * a)
        result_label.config(text=f"x = {-b} / (2×{a}) = {x:.2f}", foreground="green")
    else:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        result_label.config(text=f"x₁ = {x1:.2f}, x₂ = {x2:.2f}", foreground="green")

def calculate_viete():
    """Находит целые корни с использованием формул Виета"""
    try:
        sum_x = -b / a
        prod_x = c / a
        
        for x1 in range(-1000, 1001):
            x2 = sum_x - x1
            if x1 * x2 == prod_x and x2.is_integer():
                result_label.config(text=f"Корни Виета: x₁ = {x1}, x₂ = {int(x2)}", foreground="purple")
                return
        
        result_label.config(text="Целых корней нет (по Виету)", foreground="red")
    except ZeroDivisionError:
        result_label.config(text="Ошибка! a не может быть 0.", foreground="red")

def plot_graph():
    """Построение графика квадратного уравнения"""
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label=f"{a}x² + {b}x + {c}", color="blue")
    
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.scatter(vertex_x, vertex_y, color="purple", label="Вершина", zorder=3)
    
    if d >= 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        plt.scatter([x1, x2], [0, 0], color="red", label="Корни", zorder=3)
    
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.title("График функции")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def show_about():
    tk.messagebox.showinfo("О программе", "Калькулятор квадратных уравнений\nАвтор: Len_in\nTg: NONAME2030")

def show_help():
    tk.messagebox.showinfo("Помощь", "Введите коэффициенты a, b, c и нажмите 'Вычислить D'.\n"
                                     "Если D ≥ 0, станет доступной кнопка для нахождения корней.\n"
                                     "Кнопка Виета ищет целые корни без дискриминанта.")


# Создание окна
root = tk.Tk()
root.geometry('420x450')
root.title('Квадратное уравнение')
root.configure(bg=BG_COLOR)
root.resizable(False,False)

# Стили
style = ttk.Style()
style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR, font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"), padding=5)
style.map("TButton", background=[("active", BTN_HOVER)], foreground=[("active", "white")])

# Фрейм для кнопок
frame_top = ttk.Frame(root, style="TFrame")
frame_top.pack(anchor='nw', padx=10, pady=10)

btn_about = ttk.Button(frame_top, text="ABOUT US", command=show_about)
btn_about.grid(row=0, column=0, padx=5, pady=5)

btn_help = ttk.Button(frame_top, text="HELP", command=show_help)
btn_help.grid(row=0, column=1, padx=5, pady=5)

# Заголовок
title_label = ttk.Label(root, text="Решение квадратного уравнения", font=("Arial", 14, "bold"), background=BG_COLOR)
title_label.pack(pady=10)

#Фрейм для ввода коэффициентов
frame_input = ttk.Frame(root, padding=10)
frame_input.pack()

ttk.Label(frame_input, text="a =", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
entry_a = ttk.Entry(frame_input, width=7, font=("Arial", 12))
entry_a.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="b =", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=5)
entry_b = ttk.Entry(frame_input, width=7, font=("Arial", 12))
entry_b.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame_input, text="c =", font=("Arial", 12)).grid(row=0, column=4, padx=5, pady=5)
entry_c = ttk.Entry(frame_input, width=7, font=("Arial", 12))
entry_c.grid(row=0, column=5, padx=5, pady=5)

## Кнопки
btn_discriminant = tk.Button(root, text="Вычислить D", command=calculate_discriminant, font=("Arial", 12, "bold"), bg=BTN_COLOR, fg="white")
btn_discriminant.pack(pady=10)

btn_roots = tk.Button(root, text="Найти X1, X2", command=calculate_roots, state=DISABLED, font=("Arial", 12, "bold"), bg=BTN_COLOR, fg="white")
btn_roots.pack(pady=5)

btn_viete = tk.Button(root, text="Метод Виета", command=calculate_viete, state=DISABLED, font=("Arial", 12, "bold"), bg=BTN_COLOR, fg="white")
btn_viete.pack(pady=5)

btn_graph = tk.Button(root, text="Построить график", command=plot_graph, state=DISABLED, font=("Arial", 12, "bold"), bg="#2196F3", fg="white")
btn_graph.pack(pady=5)

##Панель для вывода результата
result_label = ttk.Label(root, font=("Arial", 12, "bold"), background=BG_COLOR)
result_label.pack(pady=20)

root.mainloop()
