import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def create_button(text, row, column, colspan=1):
    button = tk.Button(root, text=text, padx=20, pady=20, bg="light grey", command=lambda: button_click(text))
    button.grid(row=row, column=column, columnspan=colspan, sticky="nsew")

root = tk.Tk()
root.title("Calculadora Casio-like")

# Estilo e Layout
root.configure(bg="black")
root.geometry("300x400")

entry = tk.Entry(root, width=16, borderwidth=5, font=("Arial", 24), bg="black", fg="lime", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Botões
create_button("7", 1, 0)
create_button("8", 1, 1)
create_button("9", 1, 2)
create_button("/", 1, 3)

create_button("4", 2, 0)
create_button("5", 2, 1)
create_button("6", 2, 2)
create_button("*", 2, 3)

create_button("1", 3, 0)
create_button("2", 3, 1)
create_button("3", 3, 2)
create_button("-", 3, 3)

create_button("0", 4, 0, 2)
create_button(".", 4, 2)
create_button("+", 4, 3)

button_clear = tk.Button(root, text="C", padx=20, pady=20, bg="red", command=button_clear)
button_clear.grid(row=5, column=0, columnspan=2, sticky="nsew")

button_equal = tk.Button(root, text="=", padx=20, pady=20, bg="light blue", command=button_equal)
button_equal.grid(row=5, column=2, columnspan=2, sticky="nsew")

# Configuração das linhas e colunas
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
