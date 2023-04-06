#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:41:39 2022

@author: milimiguel
"""

# 8.
# ★☆☆ Escribir una función, llamada wc, que reciba un archivo de texto, e 
# imprima por pantalla cuántas líneas, cuántas palabras, cuántos caracteres 
# contiene el archivo, y el nombre del archivo.

#Ejemplo:

#   wc('file.txt')
#   > 9 21 243 file.txt

def wc(nom_archivo: str):
    archivo = open(nom_archivo, "r")
    lineas = archivo.readlines() # ["sbdsbjb,;sldk,djshdjs\n","sblabla\n"]
    archivo.close()
    c_lineas = len(lineas)
    c_palabras = 0
    c_caracteres = 0
    
    for linea in lineas:
        c_caracteres += len(linea)
        for palabra in linea.split(" "):
            if palabra != "":
                c_palabras += 1
    return print(c_lineas, c_palabras, c_caracteres)

# prueba:
wc("/Users/milimiguel/Desktop/PYTHON/PENSAMIENTO COMP./group_chat_history.whatsapp.txt")

#%%

# 13. 
# ★★☆ Escribir una función load_data que reciba un nombre de archivo, cuyo 
# contenido tiene el formato:

#   key1:value1
#   key2:value2
#   key3:value3

# La funcion debe devolver un diccionario con el primer campo como clave y el 
# segundo como diccionario. En este caso:
    
#   {'key1':'value1', 'key2':'value2', 'key3':'value3'}
    
def load_data(nom_archivo):
    archivo = open(nom_archivo, "r")
    lineas = archivo.readlines() # [key1: value1, key2:value2, ...]
    archivo.close()
    
    dic = {}
    for linea in lineas:
        # linea = "key1:value1"
        spliteada = linea.split(":")
        dic[spliteada[0]] = spliteada[1]
        
#%%

def esBisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return 1
    else:
        return 0
        
    
esBisiesto(4)

#es divisible entre cuatro y (no es divisible entre 100 o es divisible entre 400).
        
    #%%
    
def factorial(n):
    if 0 <= n <= 10:
        if n == 0:
            return 1
        elif n == 1:
            return n
        else:
            return n * factorial(n-1)
                
                
        
    

factorial(7)  
    
#%%

def fibonacci(n):
   # f(n) = f(n-1) + f(n-2)
   if 0 <= n <= 20:
       if n == 0 or n ==1:
           return n
       else:
           return fibonacci(n-1) + fibonacci(n-2)
    
    
print(fibonacci(3))
    
    
    
    
    
    
    