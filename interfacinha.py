import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Conversor e Verificador de Cotações')

frame = Frame(root)

Label(frame, text="Insira a Moeda" ).pack()
Button(frame, text="A1").pack(side=LEFT, fill=Y)

frame.pack()
root.mainloop()