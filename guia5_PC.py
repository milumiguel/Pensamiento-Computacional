#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:31:32 2022

@author: milimiguel
"""


#PREGUNTAS

#1

#★☆☆ Dado el diccionario dic1 = {}, vacío. Escriba un programa que agregue dos 
#nuevas claves, ‘a’ y ‘b’, cuyos valores son 1 y 2 respectivamente.

dic1 = {}

dic1["a"] = 1
dic1["b"] = 2

print(dic1)


#%%
# 2

#★☆☆ Dado el diccionario dic2 = {‘uno’:[3,2,7],’dos’:[3,9,1]}. Escriba un 
#programa que modifique el valor de la clave ‘dos’ para que ahora su lista 
#también contenga el número 8.

dic2 = {"uno":[3,2,7],"dos":[3,9,1]}

dic2["dos"].append(8)

print(dic2)


#%%
# 3

# ★☆☆ Dada la tupla t = (1,2,3,1,2,3,4,3,2,7). Escriba un programa que imprima 
#en pantalla cuántos números 3 hay a partir del índice 4 de la tupla. 
#Recomendación: Lea la documentación de la función count

t = (1,2,3,1,2,3,4,3,2,7)

t_2 = t[4:]

print(t_2.count(3))

#%%

# 4

#★☆☆ Dada la siguiente tupla t = (1,2,3,1,2,3,4,3,2,7), escriba en una línea de 
#código Python, la forma de crear una lista con los elementos que están en los 
#índices impares de la tupla.

t = (1,2,3,1,2,3,4,3,2,7)
t2 = t[1::2]
print(t2)

#%%

# 5

#★☆☆ Escriba un programa que dado un diccionario:

d = {"a":1,"b":2,"c":3,"z":26}

#muestre en pantalla cada clave y su valor correspondiente (el método items 
#puede ser de ayuda, junto con la descomposición). 
#Para su solución utilice ciclos for.


for x, y in d.items():
    print(x, y)

#%%

# 6
# ★☆☆ Escriba un programa que dado un diccionario 

d = {"a":1,"b":2,"c":3,"z":26}

#muestre en pantalla la posición que tiene cada clave en el diccionario 
#(utilizando ciclos for), empezando desde 0, también debe mostrar la clave y 
#su valor correspondiente. Genere dos soluciones, una usando la función 
#enumerate(), y la otra sin usarla (la descomposición puede ayudar).

for x, (y, z)  in enumerate(d.items()):
    print(x, y, z)

#

for x, tup in enumerate(d.items()):
    key = tup[0]
    val = tup[1]
    print(x, key, val)

#

i = 0

for key, value in d.items():
    print(i, key, value)
    i +=1
    
    

#%%

# 7
#★☆☆ ¿Qué imprime el siguiente programa?

for n in range(5):
    print(n)
#Recomendación: leer sobre la función range()

# imprime:
# 0
# 1
# 2
# 3
# 4

#%%

#8
#★☆☆ Reemplazar X, Y en el siguiente programa para que se impriman los números 
#del 4 al 10, incluyendo al 10.

for n in range(4, 11):
    print(n)

#%%

# 9
#★☆☆ Reemplazar X, Y, Z en el siguiente programa para que se impriman los 
#números del 4 al 10, incluyendo al 10, de 2 en 2. Es decir: 4,6,8,10

for n in range(4, 11, 2):
    print(n)

#%%

# 10
#★☆☆ ¿Los siguientes 3 programas hacen lo mismo?

for n in range(1, 10):
    print(n)

for numero in range(1, 10):
    print(numero)

for avion in range(1, 10):
    print(avion)

# si, el nombre del valor que extraemos del random queda a eleccion del 
# programador, no cambia el resultado porque el start/stop/step es el mismo
# y la acción a ejecutar es la misma (print)

#%%

# 11
#★☆☆ Completar el siguiente programa para que recorra los números del 1 al 15 
#e imprima "el número X es par" cuando lo es e imprima "el número X es impar" 
#cuando el número es impar


for numero in range(1, 16):
    if numero % 2 == 0 :
        print("El número", numero, "es par")
    else:
        print("El número", numero, "es impar")
            
#Recordar el uso del operador %

#%%

# 12
#★★☆ ¿Qué imprime el siguiente código? Explique el porqué de este resultado.

lista1 = [1,2,3]
lista2 = lista1
lista1.append(4)
print(lista2)
print(lista1)

# como iguala las listas, al editar una usando la función .append se están
# modificando ambas. Si hubiera appendeado la lista 2 también pasaría esto
# (son la misma lista). Si quisiera editar solo lista 2 y mantener la 1 
#original, la segunda linea deberia ser lista2 = lista1.copy()

#Esto ocurre oirque las listas son mutables, y la función la está modificando
# como si se modificara su "adn"

#%%

# 13
#★★☆ ¿Qué imprime el siguiente código? Explique el porqué de este resultado.

lista1 = [1,2,3]
lista2 = lista1
lista1 = lista1 + [4]

print(lista2)
print(lista1)

# En este ejemplo, a != del anterior, la tercer linea no está modificando
# la lista en si misma con una funcion, por ende a la lista 2 no se le "agrega"
#el elemento [4] (una concatenación no modifica el "adn" mencionado)

#%%

# 14
#★★☆ Completar el siguiente programa para que imprima una lista nueva con los 
#números pares del 1 al 15.

lista_nueva = []
for numero in range(1, 16):
    if numero % 2 ==0 :
        lista_nueva.append(numero)
print(lista_nueva)

#Recordar el uso del operador % 
#Resuelva este mismo ejercicio pero sustituya 
#el uso del método append por el método extend.

lista_nueva_2 = []
lista_final = []
for numero_2 in range(1, 16):
    if numero_2 % 2 ==0 :
        lista_nueva_2 += [numero]
        lista_final.extend(lista_nueva_2)
print(lista_nueva)

#%%

# 15
#★★☆ Completar el siguiente programa para que imprima los nombres que comienzan
#con la letra "a" ó "A".
#Resuelva el ejercicio usando upper o lower, y también sin usarlos.

nombres = ["Ambrosia", "Humberto", "antonio", "Diógenes"]
for nombre in nombres:
    if nombre.lower()[0] == "a" :
        print(nombre)

for nombre in nombres:
    if nombre[0] == "a" or nombre[0] == "A":
        print(nombre)

#%%

# 16
#★★☆ Escribir un programa que imprima los nombres de longitud menor a 6.
#Por ejemplo, dada la siguiente lista:

nombres = ["John", "Polly", "Thomas", "Arthur", "Michael", "Finn", "Ada"]

for nombre in nombres:
    if len(nombre) < 6:
        print(nombre)

#%%

# 17
#★★☆ Escribir un programa que cuente la cantidad de nombres de longitud menor 
#a 6 e imprima el resultado.
#Por ejemplo, dada la siguiente lista:
nombres = ["John", "Polly", "Thomas", "Arthur", "Michael", "Finn", "Ada"]
#Se debería imprimir 4

suma = 0
for nombre in nombres:
    if len(nombre) < 6:
        suma += 1
print(suma)

#%%

# 18
#★★☆ Escribir un programa que imprima una lista nueva con nombres de longitud 
#menor a 6.
#Por ejemplo, dada la siguiente lista:
nombres = ["John", "Polly", "Thomas", "Arthur", "Michael", "Finn", "Ada"]

#Se deberían imprimir ["John", "Polly", "Finn", "Ada"]
#Recordar el uso de la función append()

lista_nombres = []
for nombre in nombres:
    if len(nombre) < 6:
        lista_nombres.append(nombre)
print(lista_nombres)


#%%

#19
#★☆☆ Escribir un programa que imprima una lista en orden invertido.
#Por ejemplo, dada la siguiente lista:

nombres = ["John", "Polly", "Thomas", "Arthur", "Michael", "Finn", "Ada"]

#Se debería imprimir
#Ada
#Finn
#...
#...
#Polly
#John

#Recomendación: leer sobre la función reversed()

#print(list(reversed(nombres)))  #lista

lista_reversa = list(reversed(nombres))
    
for nombre in lista_reversa:
    print(nombre)


#%%

#20
#★★☆ Escribir un programa que replique el comportamiento de la función sum() 
#e imprima su resultado. Es decir: dada una lista de números, calcular la suma 
#de todos ellos e imprimirla.

lista_de_numeros = [1, 2, 3, 44, 5, 1, 23, 3.5, 6, 6, 2]

suma = 0

for numero in lista_de_numeros:
    suma += numero
    
print(suma)  
    

#%%

# 21
#★★☆ Escribir un programa que cuenta la cantidad de apariciones de una letra 
#en un string. Por ejemplo, si buscamos la letra y en el string "yo no manejo 
#el rating, yo manejo un rolls royce" el programa debería imprimir 3.

frase = "yo no manejo el rating, yo manejo un rolls royce"
letra_buscada = input("Ingrese una letra: ")

print(frase.count(letra_buscada))


#%%

#22
#★★☆ Completar el siguiente programa para que dada una lista de strings 
#(palabras_a_buscar) y una frase (variable de tipo string) , se imprima la 
#cantidad de veces que cada string de la lista aparece en la frase.

palabras_a_buscar = ["yo", "manejo", ",", "rolls royce"]
frase = "yo no manejo el rating, yo manejo un rolls royce"

for palabra in palabras_a_buscar:
    print("La palabra", palabra, "aparece", frase.count(palabra), "veces en la frase")

#Recomendación: leer sobre el uso de la función count()

#%%

#23
#★★☆ Escriba un programa que le solicite al usuario una frase, y el programa 
#imprima una cadena que contenga las palabras de esa frase ordenadas 
#alfabéticamente.

string = ""
frase_usuario = input("Ingrese una frase: ").lower()


lista_de_palabras = frase_usuario.split(" ")
lista_de_palabras.sort()
print(lista_de_palabras)


#%%
# 24

#24. ★★☆ Escriba un programa que dada una lista de números arbitraria y un 
#número solicitado al usuario, agregue el doble de ese número en la posición 
#anterior a la que aparece en la lista. Por ejemplo, si el usuario ingresara el
#número 6 y la lista fuera: l = [1,3,5,6,7,6] Se debería imprimir: [1,3,5,12,6,7,12,6]

lista_1 = [1,3,5,6,7,6]
lista_2 =[]

num_usuario = int(input("Ingrese un número: "))

for index, num in enumerate(lista_1): # desempaquetado
    if num == num_usuario:
        lista_2.insert(index-1, num*2)
        lista_2.insert(index, num)
    else:
        lista_2.insert(index, num)
    
print(lista_2)

for num in lista_1: # desempaquetado
    if num == num_usuario:
        lista_2.append(num*2)
        lista_2.append(num)
    else:
        lista_2.append(num)
    
print(lista_2)


#%%

# 25
#★★★ Escriba un programa que dada una lista de números cualquiera, por cada 
#ocurrencia de un número en particular debe reemplazarse en la lista por el 
#triple de su valor. Este número se le solicita al usuario. Al final debe 
#imprimir la lista resultante.

lista_num = [1, 2, 4, 5, 66, 2, 2, 7, 89, 1.2, 2]

numero_del_usuario = int(input("Ingrese un número: "))

for i, num in enumerate(lista_num):
    if num == numero_del_usuario:
        lista_num[i] = num * 3
print(lista_num)


#%%

#26
#★★★ Escriba un programa que implemente un traductor, para esto cuenta con un 
#diccionario que tiene como claves las palabras escritas en inglés, y como 
#valores su correspondiente traducción al español. El programa le debe solicitar 
#al usuario que ingrese una frase escrita en inglés, y debe imprimir la frase 
#traducida al español (para probar solo utilice pocas palabras en el 
#diccionario). Si la palabra en inglés no está en el diccionario, se debe dejar 
#escrita en inglés en el resultado final.


traductor = {
     "how": "como",
     "i": "yo",
     "met": "conocí"
     
     }

frase = input(("Ingrese una frase: ")).lower()

frase_traducida = ""

lista_frase = frase.split(" ")

for palabra in lista_frase:
    if palabra in traductor:
        frase_traducida += traductor[palabra] + " "  #esto traduce
    else:
        frase_traducida += palabra + " " #esto la mantiene

print(frase_traducida)

#%%

#27

#★★★ Se tienen tres listas de datos, una denominada “dni” que contiene los DNI 
#de 20 personas, la otra, denominada “nombres”, contiene sus nombres, la 
#tercera, “apellidos”, contiene sus apellidos. Se necesita crear en una
#única línea de código un diccionario que como clave tenga los DNI de cada 
#persona, y como valor su nombre y apellido.
# !!! Ayuda: la función zip es capaz de unir dos secuencias, apareando sus elementos.


dni = [44513560, 20597685, 23324357, 44713671]
nombres = ["Milagros", "Rodrigo", "Cynthia", "Rosario"]
apellidos = ["Miguel", "Miguel", "Remudo", "Podestá", "Gonzales"]

dictio_milu = {}

#for i, DNI in enumerate(dni):
#    dictio_milu[DNI] = nombres[i] + " " + apellidos[i]
#print(dictio_milu)

# con zip
#dictio_milu = dict(list(zip(dni, (zip(nombres,apellidos)))))

#print(dictio_milu)

print(dict(list(zip(dni, zip(nombres, apellidos)))))

        
#%%

#28. ★★★ Escriba un programa que le solicite al usuario una clave, la cual debe
#estar compuesta por al menos una mayúscula, al menos una minúscula, al menos 
#un número, al menos un caracter especial (%, &, $, etc.) y debe tener entre 
#8 y 20 caracteres. Si no cumple estas condiciones, debe solicitarle nuevamente 
#al usuario que ingrese la clave.

mayuscula = False
minuscula = False
caracter_especial = False
numero = False
cantidad = False


while True:
   clave = input( "Ingrese una clave: ")
    
    
   for letra in clave:
        if letra.isupper():
            mayuscula = True
        if letra.islower():
            minuscula = True
        if letra.isnumeric():
            numero = True
        if letra.isalnum() == False:
            caracter_especial = True
        if 8 <= len(clave) <= 20:
            cantidad = True
    
   if mayuscula and minuscula and caracter_especial and numero and cantidad:
         break
        
#%%

#29 
#★★★ Escribir un programa que dada una lista de strings que son palabras a 
#buscar (palabras_a_buscar) y un string largo (una frase), genere un 
#diccionario donde las claves son cada una de las palabras a buscar y el valor 
#es la cantidad de veces que la palabra aparece en el string largo (frase).

#Por ejemplo, dada la lista:

palabras_a_buscar = ["yo", "manejo", ",", "rolls-royce", "hola"]

#y la frase:
    
frase = "yo no manejo el rating, yo manejo un rolls-royce"

#El programa debe imprimir el diccionario:
#{"yo": 2, "manejo": 2, ",":1, "rolls royce": 1}


dictio_m = {}

for palabra in palabras_a_buscar:
        dictio_m[palabra] = frase.count(palabra)
        
print(dictio_m)
        

#%%

#30

# ★★★ Escribir un programa que dados un diccionario con el listado de un carrito 
#de supermercado y otro con los precios de los productos de un supermercado, 
#imprima el costo total del carrito.
#Aclaración: el programa debe poder correr para cualquier carrito de supermercado. 
#Es decir, que si un producto del carrito no existe dentro del listado de precios, 
#el programa debe imprimir el mensaje de error “El producto X no existe en el 
#supermercado” y este no debe ser incluido al costo total del carrito.

#Por ejemplo, dado el carrito:
    
carrito = {
    "topline 7": 2,
    "fanta": 1,
    "lata de atun": 6,
    "esparragos": 100,
}

# y los precios

precios = {
    "topline 7": 50,
    "beldent": 25,
    "fanta": 200,
    "coca light": 140,
    "coca comun": 140,
    "lata de atun": 150,
}

#El programa debe imprimir:
#El producto esparragos no existe en el supermercado
#El costo total del carrito es: $1200
#La cuenta que se realiza es: 2 latas de atún * $50 + 1 botella de fanta * $200 +
#6 latas de atún * $150 = $1200

costo_total = 0

for producto in carrito:
    if producto in precios:
        cantidad_producto = carrito[producto]
        precio_producto = precios[producto]
        costo_total += cantidad_producto * precio_producto
    else:
        print("el producto", producto, "no existe en el supermercado")
    
print("El costo total del carrito es: ", costo_total)
    
#%%

#31
#★★★ Escribir un programa que dados un diccionario con el listado de un carrito 
#de supermercado y otro con los precios de los productos de un supermercado, 
#imprima una lista con los productos del carrito, que NO existan en el listado de precios.


#Por ejemplo, dado el carrito:
    
carrito = {
    "arándanos": 1,
    "topline 7": 2,
    "fanta": 1,
    "lata de atun": 6,
    "esparragos": 100,
    "anchoas": 100,
}

#y los precios:
    
precios = {
    "topline 7": 50,
    "beldent": 25,
    "fanta": 200,
    "coca light": 140,
    "coca comun": 140,
    "lata de atun": 150,
}

#El programa debe imprimir: ["esparragos", "anchoas", "arándanos"]

no_estan = []

for producto in carrito:
    if producto not in precios:
        no_estan.append(producto)
        
print(no_estan)
    
    
#%%

#32
#★★★ Escribir un programa que dados un diccionario con el listado de un carrito 
#de supermercado y otro con los precios de los productos de un supermercado, 
#genere una lista con los productos del carrito, que NO existan en el listado 
#de precios. Y luego los elimine del carrito e imprima el carrito actualizado.

#Por ejemplo, dado el carrito:
    
carrito = {
    "arándanos": 1,
    "topline 7": 2,
    "fanta": 1,
    "lata de atun": 6,
    "esparragos": 100,
    "anchoas": 100,
}

#y los precios

precios = {
    "topline 7": 50,
    "beldent": 25,
    "fanta": 200,
    "coca light": 140,
    "coca comun": 140,
    "lata de atun": 150,
}

#El programa debe imprimir: {"topline 7": 2, "fanta": 1, "lata de atun": 6}
# !!! Recomendación: leer sobre el uso de la función pop()

no_estan = []
carrito_nuevo = carrito.copy()

for producto in carrito:
    if producto not in precios:
        carrito_nuevo.pop(producto)
        no_estan.append(producto)
print(no_estan)
print(carrito_nuevo)


    
    
    
    
    
    
    
    
    
    
    