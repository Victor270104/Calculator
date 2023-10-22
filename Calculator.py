import tkinter as tk

# Definirea functiei de afisare a butoanelor
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Definirea functiei de calcul
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Definirea functiei de stergere
def clear():
    global expression
    expression = ""
    equation.set("")

# Crearea ferestrei principale
root = tk.Tk()
root.title("Calculator")

# Initializarea variabilelor
expression = ""
equation = tk.StringVar()

# Crearea casetei de text pentru afisarea expresiei
expression_field = tk.Entry(root, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

# Crearea butoanelor
button1 = tk.Button(root, text=' 1 ', command=lambda: press(1), height=2, width=7)
button1.grid(row=2, column=0)
button2 = tk.Button(root, text=' 2 ', command=lambda: press(2), height=2, width=7)
button2.grid(row=2, column=1)
button3 = tk.Button(root, text=' 3 ', command=lambda: press(3), height=2, width=7)
button3.grid(row=2, column=2)
button4 = tk.Button(root, text=' 4 ', command=lambda: press(4), height=2, width=7)
button4.grid(row=3, column=0)
button5 = tk.Button(root, text=' 5 ', command=lambda: press(5), height=2, width=7)
button5.grid(row=3, column=1)
button6 = tk.Button(root, text=' 6 ', command=lambda: press(6), height=2, width=7)
button6.grid(row=3, column=2)
button7 = tk.Button(root, text=' 7 ', command=lambda: press(7), height=2, width=7)
button7.grid(row=4, column=0)
button8 = tk.Button(root, text=' 8 ', command=lambda: press(8), height=2, width=7)
button8.grid(row=4, column=1)
button9 = tk.Button(root, text=' 9 ', command=lambda: press(9), height=2, width=7)
button9.grid(row=4, column=2)
button0 = tk.Button(root, text=' 0 ', command=lambda: press(0), height=2, width=7)
button0.grid(row=5, column=1)

plus = tk.Button(root, text=' + ', command=lambda: press("+"), height=2, width=7)
plus.grid(row=2, column=3)
minus = tk.Button(root, text=' - ', command=lambda: press("-"), height=2, width=7)
minus.grid(row=3, column=3)
multiply = tk.Button(root, text=' * ', command=lambda: press("*"), height=2, width=7)
multiply.grid(row=4, column=3)
divide = tk.Button(root, text=' / ', command=lambda: press("/"), height=2, width=7)
divide.grid(row=5, column=3)

equal = tk.Button(root, text=' = ', command=equalpress, height=2, width=7)
equal.grid(row=5, column=2)
clear = tk.Button(root, text='Clear', command=clear, height=2, width=7)
clear.grid(row=5, column='0')

# Pornirea aplicatiei
root.mainloop()
