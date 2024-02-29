import tkinter as tk
from tkinter import font

terminales = {'automata', 'aceptacion', 'alfabeto', 'fin', ',', ':', ';'}
no_terminales = {'S', 'A', 'V', 'B', 'AL', 'G', 'SM', 'RA', 'F', 'C', 'D'}

tabla = {
    'S': {'automata': ['A', 'B', 'V']},
    'A': {'automata': ['automata']},
    'V': {'fin': ['fin']},
    'B': {'alfabeto': ['AL', 'F']},
    'AL': {'alfabeto': ['G', ':', 'SM', 'RA', ';']},
    'G': {'alfabeto': ['alfabeto']},
    'SM': {'a...z': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
           '0...9': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']},
    'RA': {',': [',', 'SM', 'RA']},
    'F': {'aceptacion': ['C', ':', 'D', ';']},
    'C': {'aceptacion': ['aceptacion']},
    'D': {'0-9': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}
}

def a_pila_predictivo_no_recursivo(cadena):
    pila = ['$', 'S']
    cadena = cadena.split()
   
    while True:
        if pila[-1] == '$':
            return 'Cadena aceptada'
        elif pila[-1] in terminales:
            if pila[-1] == cadena[0]:
                pila.pop()
                cadena.pop(0)
            else:
                return 'Cadena no aceptada'
        else:
            if cadena[0].isalpha() and cadena[0] not in terminales:
                pila.pop()
                cadena.pop(0)
            
            if cadena[0].isdigit() and cadena[0] not in terminales:
                pila.pop()
                cadena.pop(0)
                if cadena[0] == ';':
                    continue

            if cadena[0] == ';' and pila[-1] == 'RA':
                pila.pop()
                continue
            
            produccion = tabla[pila[-1]].get(cadena[0])

            if produccion != None:
                pila.pop()
                for simbolo in produccion[::-1]:
                    pila.append(simbolo)
            else:
                return 'Cadena no aceptada'

def verificar_cadena():
    cadena = entry.get()
    resultado = a_pila_predictivo_no_recursivo(cadena)
    result_label.config(text=resultado)

# Crear ventana
root = tk.Tk()
root.title('Verificador de Cadenas')
root.geometry('430x250') 
font_size = font.Font(size=12)

# etiqueta y entrada
label = tk.Label(root, text='Introduce una cadena:', font=font_size)
label.pack(pady=5)  
entry = tk.Entry(root, width=40, font=font_size)  
entry.pack(pady=5) 

#  botón
button = tk.Button(root, text='Verificar', command=verificar_cadena, font=font_size)
button.pack(pady=5) 

# mostrar el resultado
result_label = tk.Label(root, text='', font=font_size)
result_label.pack(pady=5) 

root.mainloop()

