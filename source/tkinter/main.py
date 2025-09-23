import tkinter as tk
from tkinter import messagebox

numero = 0

def btnCounter():
    global numero
    numero += 1
    labelCount.config(text=f"Valor de número: {numero}")

def ShowMsg():
    messagebox.showwarning("ATENÇÃO", "Você pressionou o botão!")

root = tk.Tk()
root.title("Hello world from Python Tkinter")
root.geometry("400x200")

label = tk.Label(root, text="Clique no botão para incrementar")
label.pack()

button = tk.Button(root, text="Incrementar", command=btnCounter)
button.pack()

labelCount = tk.Label(root, text=f"Valor de número: {numero}")
labelCount.pack()

buttonMsg = tk.Button(root, text="Mostrar Msg", command=ShowMsg)
buttonMsg.pack()

root.mainloop()