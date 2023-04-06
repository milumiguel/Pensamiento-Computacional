#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 19:45:07 2022

@author: milimiguel
"""

#1. ★☆☆ Determine de forma manual y luego corrobore en Python el tipo 
#y valor de cada una de las siguientes variables.

a = (5/2)+15
b = (((1*3)+5)+6-3*3**2)
c = (5+15-3)>(10/10*5+2)
d = True and True
e = True or False and True
f = 'Hola' + 'mundo'
g = (12 * 2 + 22 ** 2) > 45 and False

# a = float
# b = int
# c = bool (True)
# d = bool (True)
# e = bool (True)
# f = str "Holamundo"
# g = bool (False)

print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))

#%%

#2. ★☆☆ Pruebe correr el siguiente código y analice el resultado

lyric = 'My name is '
print(lyric * 3)
primera_letra = 'H'
segunda_letra = 'i'
print(primera_letra + segunda_letra)

# Análisis: Los strings pueden "multiplicarse" pero al no ser valores numericos
# lo que hace la multiplicacion es concatenar un mismo str el numero de veces
# que se lo esté multiplicando
# Luego vemos que se puede expresar variables como strings y concatenarlos (+)
# llegando a un único str


#%%

#3. ★☆☆ Realiza un programa que lea 2 números por teclado y determine los 
#siguientes aspectos (es suficiente con mostrar True o False):

   # 1. Si los dos números son iguales
   # 2. Si los dos números son diferentes
   # 3. Si el primero es mayor que el segundo
   # 4. Si el segundo es mayor o igual que el primero
   
x = 2
y = 4 

print(x == y)
print (x!= y)
print(x > y)
print(x <= y)


#%%

#4. ★☆☆ Utilizando operadores lógicos, determine si una cadena de texto 
#introducida por el usuario tiene una longitud mayor o igual que 3 y 
#a su vez es menor que 10 (es suficiente con mostrar True o False).

mensaje = str(input("Dejá tu mensaje acá: "))

longitud = len(mensaje)

x = longitud >= 3 and longitud < 10

print(x)

#%%

# 5. ★★☆ Realiza un programa que cumpla el siguiente algoritmo utilizando
# siempre que sea posible operadores en asignación:

    # 1. Guarda en una variable numero_magico el valor 12345679 (sin el 8)
    # 2. Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
    # 3. Multiplica el numero_usuario por 9, y almacene el resultado en la misma variable numero_usuario
    # 4. Multiplica el numero_magico por el numero_usuario, y almacene el resultado en la misma variable numero_magico
    # 5. Finalmente muestra el valor final del numero_magico por pantalla




#numero_usuario = (input("inserte su numero entre 1-9: ")) 
#numero_usuario =  numero_usuario * 9
#numero_magico = 12345679 
#numero_magico = numero_magico * numero_usuario

#print(numero_magico)


#numero_usuario = (input("inserte su numero entre 1-9: ")) * 9
#numero_magico = 12345679 * numero_usuario
#print(numero_magico)

#%%

#6. ★☆☆ Las cadenas (o strings) son un tipo de datos compuestos por secuencias 
#de caracteres que representan texto. Estas cadenas de texto son de tipo str
# y se delimitan mediante el uso de comillas simples o dobles. 
#Dadas las siguientes variables tipo cadena, imprima en pantalla el nombre 
#completo de la persona sin modificar las variables.

#Pista: capaz tengas que agregar un espacio entre nombre y apellido

nombre = 'Roger'
apellido = 'Federer'

#Imprima en pantalla también el nombre completo de la persona, 
#pero dado vuelta ("reredeF regoR").
#Pista: la función reverse podría ayudar.

nombre_completo = nombre + " " + apellido

print(nombre_completo)

reversa = nombre_completo[::-1]     
# el -1 marca de a cuantos te lo devuelve
# si pongo [::2] me va a devolver el string de principio a fin pero solo de 2 en 2
# acá puse -1 para que me lo devuelva en reversa

print(reversa)

# la funcion .reverse no funciona para strings, pero puedo transformarlo en lista y 
# despues usar "".join para que junte los elementos en un str

# reversa2 = "".join (list[nombre_completo].reverse)
# print(reversa2)


#%%


# 7. ★★☆ Escribir un programa que pregunte el nombre completo del usuario en la consola 
# y después muestre por pantalla el nombre completo del usuario tres veces, una con todas
# las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera 
# letra del nombre y de los apellidos en mayúscula. 
#El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.


nombre_completo= input("Insertar su nombre completo: ")

nombre_completo = nombre_completo.split(" ")

nom = nombre_completo[0]
ap = nombre_completo[1]

nom_min = nom.lower()
nom_mayus = nom.upper() 
ap_min = ap.lower()
ap_mayus = ap.upper()

completo_min = nom_min + " " + ap_min
completo_mayus = nom_mayus + " " + ap_mayus
siglas = nom_mayus[0] + "." + ap_mayus[0]


print(completo_min, completo_mayus, siglas)

# otra manera de hacerlo:
    
nombre_completo_2 = input("Insertar su nombre completo: ")

index = nombre_completo_2.index(" ")

completo_min_2 = nombre_completo_2.lower()
completo_mayus_2 = nombre_completo_2.upper()

siglas = (nombre_completo_2[0] + "." + nombre_completo_2[index + 1]).upper()

print(completo_min_2, completo_mayus_2, siglas)

#%%

#EJS RECOMENDADOS

#GUIA 2 teoricos
# 20-24


#%%

#EJ 20

#20. ★☆☆ Dada la siguiente tupla, imprima en pantalla el número que está en el medio. 
# Para esto deberá aportar dos soluciones, una usando índices positivos, y otra solución 
# usando solamente índices negativos.


mi_tupla_tres = (17, 12, 4, 29, 13,)

print(mi_tupla_tres [2])
print(mi_tupla_tres[-3])

#%%

# EJ 21

#21. ★★☆ Dada la siguiente tupla, imprima en pantalla el elemento “Messi”

mi_secuencia = (0, ("Roger", 2, "Nadal"), (17, 12), ("Palermo", "Messi"), 29)


print(mi_secuencia[3][1])


#%%

# EJ 22

#22. ★★☆ También es común usar estructuras combinadas o anidadas. Dada la siguiente lista,
# ¿qué tipo de elementos contiene? Imprima en pantalla el elemento 3.

numeros = [(1, 2, 3), 4, 6, 7]

# la lista contiene adentro una tupla (1,2,3) con ints adentro y luego 3 ints individuales 

print(numeros[0][2])

#%%

# EJ 23

#23. ★★☆ Los diccionarios en python nos permiten almacenar una serie de mapeos entre dos 
#conjuntos de elementos,llamados keys and values (Claves y Valores). En lugar de acceder 
#a un elemento por su “index”, podemos acceder a el por su clave.
#Corra el siguiente código y analice el resultado


mi_diccionario = {'Roger': 20, 'Novak': 21, 'Rafa': 22}
print(mi_diccionario['Roger'])

# analisis: al llamar a la llave "roger" el programa devuelve su valor 20, justamente
# funciona como un diccionario donde la palabra es la llave y la definicion es el valor

#%%

# EJ 24

#24. ★★☆ Dado el siguiente diccionario, imprima en pantalla solo las claves utilizando 
#una sola línea de código.

mi_diccionario = {'Roger': 20, 'Novak': 21, 'Rafa': 22}

print(mi_diccionario.keys())

# el .keys() me devuelve una lista con las llaves como elementos



#%%

i = 1
lista = []

while i > 0:
    if i % 7 == 0:
        suma = str(i)[0::1]
        if suma == 49:
            lista += [i]
    i += 1
    
print(lista)


#%%

print(7* 599998)

print(sum([4,1,9,9,9,8,6)


