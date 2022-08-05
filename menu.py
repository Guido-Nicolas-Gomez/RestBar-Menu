# #2) En este ejercicios debes crear una interfaz gráfica con tkinter (menu.py) que muestre de forma elegante el menú del restaurante.

# Tú eliges el nombre del restaurante y el precio del menú, así como las tipografías, colores, adornos y tamaño de la ventana.
# El único requisito es que el programa se conectará a la base de datos para buscar la lista categorías y platos.

#   modulos utilizados
from tkinter import *
import sqlite3

#   Definiciones
root = Tk()
root.iconbitmap("cafe_icon.ico")
root.title("Menú")
root.resizable(0,0)
root.config(
    padx=10,
    pady=10,
    bg = "#444444"
    )

# Titulo
titulo1 = Label(root) 
titulo1.config(
    text="RestoBar Pelli",
    bg="#444444",
    font=("console",15,"italic"),
    foreground="White", 
)
titulo2 = Label(root)
titulo2.config(
    text="OUR MENU",
    bg="#444444",
    font=("console",30),
    foreground="#ffd000", 
)


# Cuerpo
frame = Frame(root, bg="#444444", pady=10, padx=10)
# Conectando con la Base de Datos
coneccion = sqlite3.connect("restaurante.db")
cursor = coneccion.cursor()
# Cargarndo los valores de interes
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
platos = cursor.execute("SELECT * FROM plato").fetchall()

for categoria in categorias:
    Label(frame, bg="#444444").pack()
    Label(frame, text = categoria[1].upper(), bg="#ffd000", font=("",15)).pack() # Categorias
    for plato in platos:
        if plato[2] == categoria[0]:
            Label(frame,text=plato[1], bg="#444444", font=("",12,"italic"), foreground="white").pack() #platos

# Pie
pie = Label(root)
pie.config(
    text="$1.200",
    bg="#444444",
    font=("",20,"italic"),
    width=10,
    anchor="e",
    pady=10,
    foreground="#ffd000"
)


#   Instancias
titulo1.pack()
titulo2.pack()
frame.pack()
pie.pack()
root.mainloop()