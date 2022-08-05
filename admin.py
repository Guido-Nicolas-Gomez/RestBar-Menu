"""1.1) A lo largo de estos ejercicios vamos a crear un pequeño sistema para gestionar los platos del menú de un restaurante. Por ahora debes empezar creando un script llamado restaurante.py y dentro una función crear_bd() que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:

Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen. En caso contrario mostrará que se han creado correctamente.

CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)
CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
Nota: La línea FOREIGN KEY(categoria_id) REFERENCES categoria(id) indica un tipo de clave especial (foránea), por la cual se crea una relación entre la categoría de un plato con el registro de categorías.

Llama a la función y comprueba que la base de datos se crea correctamente."""

#   Modulos empleados
import sqlite3
from tkinter import messagebox as MessageBox

# conexion a la base de datos
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

#   Funcion que crea las tablas en a base de datos
def crear_bd():   
    # Intentar Crear las tablas
    try:
        cursor.execute("""
                  CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)  
        """)
        cursor.execute("""
                  CREATE TABLE plato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL, 
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))  
        """)
    except:
        MessageBox.showwarning(message="Las tablas ya se encuentran creadas", title="Alerta!!")
        print("Las tablas ya se encuentran creadas")
    else:
        print("\nLas Tablas fueron creadas con exito4\n")


#1.2) Crea una función llamada agregar_categoria() que pida al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos (ten en cuenta que si ya existe dará un error, por que el nombre es UNIQUE).
def agregar_categoria():
    # Solicitar al usuario el nombre de la nueva categoria
    nueva_categoria = input("\nPor favor ingrese el nombre de la categoría:\n>")

    # Intentar cargar en la base de datos
    try:
        cursor.execute(f"INSERT INTO categoria (nombre) VALUES ('{nueva_categoria}')") # Se debe colocar comillas
    except:
        MessageBox.showerror(title="Error", message="La categoria ya se encuentra creada o la base de datos se encuentra en uso")
    else:
        print(f"\nLa categoría {nueva_categoria} fue creada con exito\n")


#1.3) Crea una función llamada agregar_plato() que muestre al usuario las cat1egorías disponibles y le permita escoger una (escribiendo un número).
#Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, teniendo en cuenta que la categoria del plato concuerde con el id de la categoría y que el nombre del plato no puede repetirse (no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).
def agregar_plato():
    # Consultando la base de datos:
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()

    # Eligiendo la categoria
    print("\nLas categorias disponibes son las siguientes, elija una:\n>")
    for i,v in enumerate(categorias):
        print(f"[{i+1}] {v[1]}")
    categoria = input("")
    id_categoria = categorias[int(categoria)-1][0]

    # Solicitando el nombre del plato
    plato = input("\nIngrese el nombre del plato a agregar: ")

    # Intentando cargar el nuevo plato
    try:
        cursor.execute(f"INSERT INTO plato (nombre, categoria_id) VALUES ('{plato}','{id_categoria}')")
    except:
        MessageBox.showerror(title="Error", message="La categoria ya se encuentra creada o la base de datos se encuentra en uso")
    else:
        print(f"\nEl plato {plato} fue creado con exito\n")
        

#1.4) Crea una función llamada mostrar_menu() que muestre el menú con todos los platos de forma ordenada: los primeros, los segundos y los postres. Optativamente puedes adornar la forma en que muestras el menú por pantalla.
def mostrar_menu():
    print("\n===============  MENU  ===============")

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(f"\n{categoria[1].upper()}:")

        platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id = '{categoria[0]}'").fetchall()
        for plato in platos:
                print(f"{plato[1]}")


#Ahora, crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te permita Crear una categoría o Salir. Añade las siguientes tres categorías utilizando este menú de opciones:
#Primeros
#Segundos
#Postres"""
def menu():

    while True:

        eleccion = input("""
    Bienvenidos a esta seccion.
    Que desea hacer??

    [1] Crear una Categoria
    [2] Crear un plato
    [3] Mostrar Menu
    [4] Salir

    >""")

        if eleccion == "1":
            agregar_categoria()

        elif eleccion == "2":
            agregar_plato()

        elif eleccion == "3":
            mostrar_menu()

        elif eleccion == "4":
            print("\nGracias por su visita!!\n")
            conexion.commit()
            conexion.close()
            break

        else:
            print("\nClave incorrecta, intentar nuevamente\n")


menu()








