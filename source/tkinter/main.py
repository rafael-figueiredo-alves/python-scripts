import tkinter as tk
from tkinter import messagebox

def Button_click():
    messagebox.showwarning("ATENÇÃO", "Você pressionou o botão!")

root = tk.Tk()
root.title("Hello world from Python Tkinter")

label = tk.Label(root, text="Teste")
label.pack()

button = tk.Button(root, text="Ok", command=Button_click)
button.pack()

root.mainloop()