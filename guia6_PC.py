#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:54:48 2022

@author: milimiguel
"""

# DUDAS

# 8. 

# 13.

# 14.

# 15. no me deja fstring con {} vacío, no se que imprime

# 16.

# 18.???

# 19.

# 20. importo exp() from math?? 

# 22. y 23. ayuda

#%%

#1. ★☆☆ Defina una función llamada greet que imprima "hola mundo".

def greet():
    mensaje = "hola mundo"
    print(mensaje)
    return

#%%

#2. ★☆☆ Defina una función llamada greet_person que tome como argumento una 
#cadena y que imprima Hola <Nombre>! donde <Nombre> es la cadena pasada como 
#argumento.

def greet_person(nombre):
    # toma str como argumento
    print("Hola", nombre, "!")
    return

#%%

#3. ★☆☆ Defina una función llamada get_number que le solicite al usuario un 
#número entero y devuelva ese número.

def get_number(num_entero):
    # toma int como argumento
    return num_entero

#%%

#4. ★☆☆ Defina una función add que tome como argumento dos números y que 
#imprima la suma de los dos números.

def add(num_1, num_2):
    suma = num_1 + num_2
    print(suma)
    return

#%%

# 5. ★☆☆ Defina una función square que devuelva el cuadrado de un número. 
# Si la función toma como argumento un número de tipo float o de tipo int y 
# debe devolver el mismo tipo.


def square(num):
    # toma float o int como argumento
    cuadrado = num ** 2
    return cuadrado

#%%
    
# 6. ★☆☆ Defina una función llamada es_alto que tome como argumento un número 
# y que imprima es altisimo si el número es mayor a 39.


def es_alto(num):
    if num > 39:
        print("es altísimo")
    return

#%%

# 7. ★☆☆ Defina una función llamada estare_gritando que tome como argumento 
# una cadena y que imprima Deja de gritar si todas las letras son mayúsculas.

def estare_gritando(string):
    # toma str como argumento
    if str.isupper():
        print("Deja de gritar")
    return

#%%

# 8. ★☆☆ Defina una función llamada greet_user que tome como argumento una 
# cadena y que imprima: Bienvenida/o de vuelta, seguido por la cadena. 
# Si la función no recibe ningún argumento debería imprimir Bienvenida/o de 
# vuelta, Usuaria/o.


def greet_user(nombre):
    # toma str como argumento
    if nombre == None:
        print("Bienvenida/o de vuelta, Usuaria/o")
    else:
        print("Bienvenida/o de vuelta, ",nombre)

greet_user()


# no se como hacer que no me pida 1 argumento

#%%

# 9. ★☆☆ Defina una función "add" que tome como argumento dos números y que 
# devuelva la suma de los dos números.(Este ejercicio es distinto al 4)

def add_2(num_1, num_2):
    suma = num_1 + num_2
    return suma

#%%

# 10. ★☆☆ Defina una función susurro_grito que tome como argumento una cadena 
# y que devuelva dos cadenas: La cadena en minúsculas y la misma cadena en 
# mayúsculas.

def susurro_grito(string):
    mayus = string.upper()
    minusc = string.lower()
    return mayus, minusc

#%%

# 11. ★☆☆ Defina una función division_entera que tome dos números enteros como 
# argumentos y que devuelva dos números enteros: el primer número entero 
# devuelto debe ser el resultado de la division entera y el segundo número 
# devuelto es el resto (módulo) de la división.
    

def division_entera(num_1_entero, num_2_entero):
    resultado = num_1_entero // num_2_entero
    resto = int(num_1_entero % num_2_entero)
    return resultado, resto

#%%

# 12. ★☆☆ Dado el siguiente programa modifíquelo para que imprima el resultado 
# de la función simple. 
# Explique porqué razón falla el programa tal como se presenta:
    
# resultado = simple()
# print(resultado)
# def simple():
# return "buenisimo"

def simple():
    return "buenisimo"

resultado = simple()
print(resultado)

#El programa falla porque la funcion no esta definida al momento de "invocarla"

#%%

# 13. ★★☆ En el siguiente programa la función igualar_a_cero recibe un número 
# y lo iguala a cero. Luego se invoca dicha función con la variable frutas que 
# vale 99, como argumento. Esto significa que corre la función y adentro de 
# igualar_a_cero se iguala el argumento (en este caso, frutas) a cero. 
# ¿Que imprime el siguiente código? ¿Por qué el valor de frutas no es 0 una
# vez terminado el programa? ¿Se le puede cambiar el valor 99 asignado a la 
# variable frutas dentro de la función?

def igualar_a_cero(numero):
    numero = 0

frutas = 99
igualar_a_cero(frutas)
print(frutas)


# El codigo imprime 99.
# No cambiaste el valor de la variable frutas! 


#%%

# 14.
# ★★☆ Se define la variable frutas en el siguiente código y se la iguala a 99.
# ¿Será que se puede igualar frutas a 0 desde adentro de una función?
# ¿Que imprime el siguiente código?:
    
frutas = 99

def descartar_frutas():
    frutas = 0

igualar_a_cero(frutas)
print(frutas)

#%%

# 15.
# ★☆☆ Del ejercicio anterior sabemos que podemos crear variables nuevas 
# adentro de una función que comparten el mismo nombre con variables globales 
# afuera de la función.A pesar que las funciones tienen un espacio de trabajo 
# aparte para variables locales, no todo es tan "local". 
# ¿Qué imprime el siguiente código? ¿Es válido?

frutas = 99

def imprimir_frutas():
    print(f"Tengo { } frutas!", frutas)
    
imprimir_frutas()

#%%

# 16.
# ★★☆ Es importante reconocer la diferencia entre una variable local a una 
# función y una variable global.
# ¿Por qué el siguiente programa resulta en un error? ¿Cómo se puede corregir?

frutas = 99

def imprimir_frutas():
    print(f"Tengo", frutas, "frutas!")
    frutas = 0
    
imprimir_frutas()

# UnboundLocalError: local variable 'frutas' referenced before assignment

#%%

# 17.
# ★☆☆ Defina una función esta_presente que reciba una lista de cadenas y que 
# devuelva un bool. La función deberá devolver verdadero si alguno de los 
# siguientes nombres está en la lista:
    
invitados = ["Cristina", "Mauricio", "Alfonsin", "Alberto"]

# Utilice la variable invitados como variable global.

def esta_presente(lista):
    # recibe lista de cadenas
    if lista in invitados:
        return True
    
#%%

# 18.
# ★☆☆ A continuación se tiene una función con un docstring. Los docstrings 
# ayudan a documentar lo que hace una función, esta documentación se muestra 
# cuando se usa la función help.

def suma(a, b):
"""
Esta función calcua la suma de dos números.
Recibe 2 núemros que pueden ser float o int.
Retoran la suma de ellos en tipo float
"""
return a + b

# Reescriba la función para que el docstring ocupe múltiples líneas
# (Ayuda: consulte PEP 257).

#%%

# 19.
# ★☆☆ Considerando el objetivo o meta que cumpla una función, en ocasiones es 
# necesario crear docstrings apropiados para cada caso. Por ejemplo, consulte 
# el siguiente enlace mathworld y cree los docstrings apropiados para el 
# siguiente programa:
    
def approx_e():
    exp = 3**(2**85)
    return (1+9**(-4**(7-6)))**exp



#%%

# 20. ★☆☆ Defina una función expv que tome dos argumentos:
# • El exponente como argumento mandatorio.
# • La base como argumento opcional. Por defecto es el número e.
# El resultado de la función debería ser el resultado de la base elevado 
# al exponente (float).

from math import exp

def expv(exponente, base = exp(1)):
    return base ** exponente
    
#%%

# 21.
# ★☆☆ Sin copiarlo y pegarlo en su editor de código, piense, 
# ¿Qué imprime el siguiente programa?

def concat(lista_de_cadenas, sep="/"):
    return sep.join(lista_de_cadenas)

juego = concat(["Disco", "Elysium"])
frase = concat(["saludos","al","gran","rey"], sep=",")
print(juego)
print(frase)

#%%

# 22. 
# ★★☆ Defina una función local_avg que tome los siguientes argumentos:
# • numbers: Una lista de números
# • index: Un índice que no debe superar la longitud de la lista
# • window (Opcional): Cantidad impar de elementos a tomar en el promedio. 
# Por defecto 3.
# La función debería calcular la media móvil central de la lista de números en 
# la ventana (window) alrededor del indice. Idealmente se toman window cantidad 
# de elementos para el cálculo. En el caso en donde la ventana excede los 
# límites de la lista se debe calcular el promedio correctamente
# dividiendo la suma de los números adentro de la ventana por la cantidad de 
# números adentro de la ventana.

# La salida de la función debería ser:
# • La media movil en el índice. Si hay un argumento inválido debería devolver 
# 0 (float).
# • Una cadena que indica si algún argumento era inválido. Si no hay argumentos 
# inválidos se devuelve una cadena vacía.


# Ejemplo:
# Se promedian los 3 valores centrados en el índice 2:
> local_avg([1, 2, 3, 4, 3], 2) # == (2+3+4)/3
> (3.0, '')
# Se promedian los 3 valores centrados en el índice 0.
# Como el índice -1 cae afuera de la lista no se incluye en el promedio:
> local_avg([1, 2, 3, 4, 3], 0) # == (1+2)/2
> (1.5, '')
# Se promedian los 5 valores centrados en 5, que incluye toda la lista:
> local_avg([1, 2, 3, 4, 3], 2, window=5) # ==(1+2+3+4+3)/5
> (2.6, '')

def local_avg(numbers, index, window = 3):
    if window > len(numbers):
        return (sum(numbers)/len(numbers), "")


#%%

# 23.

# ★★☆ Defina una función moving_avg que tome los siguientes argumentos:
# • numbers: Una lista de números
# • window (Opcional): Cantidad impar de elementos a tomar en el promedio. 
# Por defecto 3.

# Calcule la media móvil central de la lista de números.
# • La media movil. Es una lista de los promedios de la lista números.
# • Una cadena que indica si algún argumento era inválido. Si no hay argumentos 
# inválidos se devuelve una cadena vacía.


def moving_avg(numbers, window = 3):
    
#%%

# 24.
# ★★☆ Defina una función llamada lista_fibonacci que tome un número entero n 
# como argumento y devuelva una lista que contenga los números de Fibonacci 
# desde 0 hasta n inclusive.

def lista_fibonacci(n):
    contador = 0
    primer_numero = 0
    segundo_numero = 1
    suma = 0
    
    while contador <= n:
        print(suma)
        contador += 1
        primer_numero = segundo_numero
        segundo_numero = suma
        suma = primer_numero + segundo_numero
       
lista_fibonacci(5)
        
        
#%%

# 25.
# ★★★ Examine la función convertir_a_float y el uso de la misma. Considerando 
# el nombre de la función y sin copiar y pegar en su editor, piense, 
# ¿Qué debería imprimir el programa cuando se ejecute? ¿Qué es lo que realmente 
# imprime el programa? Cambie la función convertir_a_float para que haga lo 
# esperado según el nombre.

def convertir_a_float(cadena):
    separado = cadena.split(".")
    hay_punto = len(separado) == 2
    es_real = hay_punto and separado[0].isnumeric() and separado[1].isnumeric()
    if es_real:
            return float(cadena)
        else:
            return 0.0
        
a = convertir_a_float("2.5")
b = convertir_a_float("2")
c = convertir_a_float("1.")
d = convertir_a_float("no soy float")
print(a+b+c+d)

# Una vez resuelta el ejercicio: ¿En qué casos sería útil esta función? 
# ¿Por qué no querríamos reemplazar la función convertir_a_float con float?
        
        
        
#%%

# 27

def duracion_a_tiempo(duracion):
    spliteado = duracion.split(":")
    if len(spliteado) == 1:
        return int(spliteado[0])
     elif len(spliteado) == 2:
         return int(spliteado[0]) * 60 +  int(spliteado[1]) 
      else:
          return int(spliteado[0]) * 60 * 60 +  int(spliteado[1]) * 60 +  int(spliteado[2]) 
        
        
def info(datos):
    # "{2332, 11:32:09}"
    spliteados = datos.split(",")
    return int(spliteados[0][1:]), duracion_a_tiempo(spliteados[1][:-1])


def procesar_tema(tema: str):
    # Every Time the Sun Comes Up - Sharon Van Etten {1024,4:23}
    # Don't Look Up - Nicholas Britell {128,52} {456,4:08}
    
    spliteados = tema.split("{")
    nombre = spliteados[0].split()
    
    if len(spliteados) == 2:
        rep, duracion = info("{" + spliteados[1])        
        return rep, duracion_a_tiempo, nombre
    
    elif len(spliteados) == 3:
        rep1, dur1 = info("{" + spliteados[1])
        rep2, dur2 = info("{" + spliteados[2])
        if dur1 > dur2:
            duracion = dur1
        else:
            duracion = dur2
        rep = rep1 + rep2
        return rep, duracion_a_tiempo, nombre
    
    
#%%

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    













