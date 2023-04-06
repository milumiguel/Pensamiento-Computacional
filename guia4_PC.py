#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:17:22 2022

@author: milimiguel
"""

# 1. ★☆☆ En papel, trate de predecir qué se verá en la consola al ejecutar este
#código, y luego compruebe su predicción:

contador = 1
while contador < 10:
    print(contador)
    contador = contador + 1

#a ¿Qué pasaría si eliminara la línea contador=contador+1?
#b ¿Qué ocurre si cambia la línea contador=contador+1 por contador += 1?
#c ¿Se puede afirmar que la variable contador se está usando para contar las 
# veces que se ejecuta el código dentro del while?

# a. si elimino esa línea se hace un ciclo infinito de unos
# b. es lo mismo
# c. si


#%%

#2. ★☆☆ En papel, trate de predecir qué se verá en la consola al ejecutar este 
#código, y luego compruebe su predicción:

suma = 0
contador = 1
while contador < 10:
    contador = contador + 1
    valor = input("Ingrese un número a sumar: ")
    suma = suma + valor
print(suma)

# ¿Se puede afirmar que la variable contador se está usando para contar las 
# veces que se ejecuta el código dentro del while?



# ¿Se puede afirmar que la variable suma se está usando para acumular 
#(ir sumando) cada uno de los valores que ingresa el usuario?

#¿Qué cambiaría en la ejecución del programa si la instrucción print(suma) 
#se coloca al mismo nivel de indentación que la instrucción suma=suma+valor?

#%%

#3. ★☆☆ En papel, trate de predecir qué se verá en la consola al ejecutar este 
#código, y luego compruebe su predicción:

indice = 0
stro = "72346"
while indice < len(stro):
    print(stro[indice])
    indice = indice + 1

#1 ¿Qué pasaría si se sustituye la expresión lógica del while con indice
# <= len(list)?
#2 ¿Qué ocurre si cambia la lista por la tupla tuple=(7,2,3,4,6), cambiando 
#también print(list[indice]) por print(tuple[indice])?
#3 ¿Qué ocurre si cambia la lista por la cadena string=’72346’, cambiando
#también print(list[indice]) por print(string[indice])?
#4 ¿Cuál es la diferencia entre los resultados al haber usado la lista, la 
#tupla y la cadena? Piense también en los tipos de datos que se imprimen en 
#pantalla.

# indice = 5
# list = [7, 2, 3, 4, 6]

#1
# si se sustituye por >= len(list) cuando se quiera hacer la ultima iteración
# (donde indice = 5), se va a entrar a while loop pero va a ocurrir un error.
# dentro del while se pide que se imprima el elemento "indice" es decir el 
# elemento 5 de la lista, y ese elemento no existe (hay de 0-4)
# la consola indicará un error del tipo "out of range"

#2
#lo mismo pero en tupla
# indice = 5
# tuple = (7, 2, 3, 4, 6)

#3
#lo mismo pero en str
# indice = 5
# str = 72346


#%%

#4. ★☆☆ Escriba un programa que imprima en pantalla (consola), en diferentes 
#líneas y secuencialmente cada uno de los caracteres de la cadena 
#string = “Federer” (para esto debe usar los índices de la secuencia)

strng = "Federer"

#• Luego, cambie su programa para que imprima por separado cada uno de los 
#elementos de la lista 

lista=["Hola","Chao","Hello","Bye"]

#• Cambie su programa para que imprima por separado cada uno de los elementos 
#de la tupla 

tupla=("Avion",3,4.7)


for letra in strng:
    print(letra)

for elem in lista:
    print(elem)

for x in tupla:
    print(x)


# 5. ★☆☆ Escriba un programa que sume los elementos de la lista ls, y muestre 
#el resultado en pantalla. No se permite usar sum(), para esto debe usar un 
#while.

ls = [3,4,3,9,10,5]

index = 0
suma = 0
while index < len(ls):
    suma += ls[index]
    index += 1
    
print(suma)


#6. ★☆☆ Escriba un programa que calcule el promedio de la tupla de números 
#my_tuple. No se permite usar sum(), para esto debe usar un while.

my_tuple = (12, 28, 29, 43, 3, 17)

index2 = 0
suma2 = 0
while index2 < len(my_tuple):
    suma2 += my_tuple[index2]
    index2 += 1
print(suma2/len(my_tuple))
    
#%%

#7. ★☆☆ Escriba un programa que le solicite al usuario ingresar varios números 
#naturales, e imprima en pantalla cada uno de los números en líneas diferentes 
#después de haberlos ingresado. La ejecución del programa se debe detener 
#cuando el usuario ingresa el número -1, para esto debe usar la cláusula break.


inp = input("Ingrese un número natural: ")

while True:
    print(inp)
    inp = input("Ingrese un número natural: ")
    if inp == -1:
        break
    
#%%

#8















    
    
#%%

#10. ★★☆ La tupla temp contiene temperaturas promedio medidas en grados celsius
#para 15 días. Escriba un programa que la utilice y, leyéndola elemento a 
#elemento, imprima por pantalla ‘Hace calor’ si la temperatura es mayor a 20∘,
#‘Está templado’ si está entre 10∘ y 20∘ y ‘Hace frío’ si es menor a 10∘

temp = (15,16,19,23,25,24,24,19,17,10,8,8,6,9,11)

i = 0
while  i < len(temp):
    if temp[i] > 20:
        print("Hace calor")
        
    elif temp[i] < 10:
        print("Hace frío")
        
    else:
        print("Está templado")
    i += 1


# en modo for sería:

for temp_hoy in temp:
    
    if temp_hoy > 20:
        print("Hace calor")
        
    elif temp_hoy < 10:
        print("Hace frío")
     
    else:
        print("Está templado")

#%%

#12

#★★☆ Escriba un programa que le pregunte al usuario un valor y luego busque ese 
#valor en la siguiente tupla:

tupla=(24,1,23,56,78,99,23,3,31,68,23)

# Si el número no está, debe imprimir en pantalla no se encuentra.
# Si el número está, debe imprimir en pantalla el número está en el índice <i> 
#donde i es el índice donde se encuentra en la tupla.
# Si el número buscado se repite en la tupla, debe imprimir el número está en el 
#índice <i> tantas veces como aparezca, sustituyendo la i por cada índice donde 
#se encuentre. Por ejemplo, si se busca el número 23, debe indicarse que está 
#en los índices 2, 6 y 10, de la siguiente forma:
    
#  el número está en el índice 2
#  el número está en el índice 6
#  el número está en el índice 10

numero_usuario = int(input("Ingrese un número: "))

if numero_usuario not in tupla:
    print( "El número no se encuentra")
else:
    i = 0

    while i < len(tupla):
        num = tupla[i]
        if num == numero_usuario:
            print("El número está en el índice", i)
        i += 1
    
    

























#%%

# 14

# ★★★ En el diccionario compras, se tienen registrados los montos de las compras
# que hicieron varias personas. Cada persona está identificada solamente por su
#DNI, este dato se usa como clave, y como valor, para cada DNI, se tiene una 
#lista con los montos de sus compras. Escriba un programa que muestre en pantalla 
#la cantidad de compras que hizo cada persona cuyo monto sea inferior a un valor
#que se le solicite al usuario. Para esto debe indicar en pantalla el usuario 
#<DNI> hizo <M> compras, donde DNI es el DNI correspondiente a cada usuario,
#y M es la cantidad de compras menores al valor ingresado 
#(ayuda: para esto puede usar keys()).

compras = {"12345678":[34,67,23,89,123,987,8,5], 
           "87654321":[300,2,100,56],
           "5678902":[456,234,67,12345,234,78,6,521,95,54,21,73],
           "1432126":[234,43], 
           "32145690":[543,7,1,2154,3542,654,789],
           "4567890":[1] }

monto_maximo = int(input("Ingrese un monto máximo: "))

# con while

i = 0
lista_dnis = list(compras.keys())

while i < len(lista_dnis):
    dni = lista_dnis[i]
    lista_compras = lista_dnis[i]
    contador_de_compras = 0
    j = 0
    while j < len(lista_compras):
        if lista_compras[j] < monto_maximo:
            contador_de_compras += 1
        j += 1
    print(lista_dnis[i], "hizo", contador_de_compras, "compras")
    
















# Modifique el programa anterior para que imprima en pantalla cuántos montos 
#son iguales al valor ingresado, esto considerando a todas las personas en 
#conjunto, y no de forma individual.

























