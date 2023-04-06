#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:05:03 2022

@author: milimiguel
"""

# Ejercicio 1)

def read_file(ruta_archivo):
    """Esta función toma como único argumento la ruta de un archivo
    (dato de tipo str) y lee el archivo correspondiente y retorna un dict 
    con los nombres de columnas como llaves y los elementos de esa columna
    como valores."""
    diccionario = {}
    #abrimos el archivo en modo lectura
    archivo = open(ruta_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    #trabajamos con la linea que tiene los encabezados
    nombres_columnas = lineas[0].strip().split(",")
    #trabajamos con la linea que tienen los datos
    for linea in lineas[1:]:
        linea = linea.strip().split(",")
        for i, dato in enumerate(linea):
            clave = nombres_columnas[i] 
            if clave not in diccionario:
                diccionario[clave] = []
            diccionario[clave].append(dato)
    return diccionario

#definimos dicc como el return de esta función para usar en las demás funciones
dicc = read_file("/Users/milimiguel/Desktop/PYTHON/PENSAMIENTO COMP./TP 2/bolsa.csv")


# Ejercicio 2)

#definimos una funcion convertir_fecha para facilitar nuestro programa
def convertir_fecha(fecha_string):
    """Esta funcion devuelve año, mes, día. Hay que darle un dato tipo str
    con la fecha separada por guiones"""
    fecha_string = fecha_string.strip().split("-")
    return fecha_string[0], fecha_string[1], fecha_string[2]
      
   
def monthly_average(nombre_accion, diccionario):
    """Esta función recibe 2 argumentos: un dato str con el nombre de una 
    acción y un dato dict que provenga de la función read_file(). 
    Devuelve 2 elementos (secuencias con igual lenght): una con las fechas del 
    primer día de cada mes, y la segunda con los precios promedios mensuales.
    """
    fechas = diccionario["Date"]
    precios = diccionario[nombre_accion] #indexada igual que fechas
    dict_promedios = {}
    primeros_dias = []
    
    for fecha, precio in zip(fechas, precios):
        precio = float(precio)
        año, mes, dia = convertir_fecha(fecha)
        
        if mes not in dict_promedios:
            dict_promedios[mes] = [precio]
            primeros_dias.append(fecha)
            
        else:
            dict_promedios[mes].append(precio)
        lista_promedios = []
        for key in dict_promedios.keys():
            promedios_mes = sum(dict_promedios[key])/ len((dict_promedios[key]))
            lista_promedios.append(promedios_mes)
    
    return primeros_dias, lista_promedios

#prueba
monthly_average("SATL", dicc)

# Ejercicio 3)

#abrimos archivo “monthly_average_SATL.csv" en formato de escritura

archivo = open("/Users/milimiguel/Desktop/PYTHON/PENSAMIENTO COMP./TP 2/monthly_average_SATL.csv", "w")
primeros_dias, lista_promedios =  monthly_average("SATL", dicc)
#escribimos el encabezado una única vez (no cambia)
archivo.write("fecha, promedio\n")
#y ahora si iteramos ambas listas con zip (tienen mismos índices)
for dia, promedio in zip(primeros_dias, lista_promedios):
    archivo.write(f"{dia}, {promedio}\n")
    
archivo.close()


# Ejercicio 4)

# ganancia = (precio de venta - precio de compra) / precio de compra
# probar con fecha = 6 de junio de 2022.
    
fecha_venta_prueba = "2022-06-06"

def max_gain(nombre_accion, diccionario, fecha_venta):
    """Esta función recibe el nombre de una acción (str), el
    dict de datos y una fecha de venta (str). La función busca la
    fecha de compra (en el pasado) que hubiera generado la mayor
    ganancia y devuelve esta fecha y el retorno de la inversión."""
    retorno = 0
    precios_accion = diccionario[nombre_accion]
    fechas = diccionario["Date"]
    precio_venta = float(precios_accion[fechas.index(fecha_venta)])
    
    for precio in precios_accion:
        precio_compra = float(precio)
        ganancia = (precio_venta - precio_compra) / precio_compra
        if ganancia > retorno:
            retorno = ganancia
            precio_compra_max = precio
    fecha_compra = fechas[precios_accion.index(precio_compra_max)]
    
    return fecha_compra, retorno
    
#prueba
max_gain("SATL", dicc, fecha_venta_prueba)   

# Ejercicio 5)

def report_max_gains(diccionario, fecha_venta):
    """Esta función recibe un argumento tipo dict con datos de acciones y una 
    fecha de venta en tipo str. Genera un archivo de resumen en formato txt 
    que informa la mayor ganancia de todas las acciones.""" 
    archivo = open("resumen_mejor_compra.md", "w")
    diccionario_copy = diccionario.copy()
    diccionario_copy.pop("Date")
    nombres_acciones = list(diccionario_copy.keys())
    archivo.write("# Resumen mejor compra\n\n")
    for nombre_accion in nombres_acciones:
        fecha_compra, retorno = max_gain(nombre_accion, diccionario, fecha_venta)
        archivo.write(f"{nombre_accion} genera una ganancia de {round(retorno*100,4)}% habiendo comprando en {fecha_compra} y vendiendose en {fecha_venta}\n\n")
        if retorno < 0:
            archivo.writelines(f"La acción {nombre_accion} solo genera pérdidas\n\n")

    archivo.write("| Nombre Acción | Retorno | Fecha de compra | Fecha de venta |\n")
    archivo.write("|----------|---------|---------|---------|\n")
    for nombre_accion in nombres_acciones:
        fecha_compra, retorno = max_gain(nombre_accion, diccionario, fecha_venta)
        archivo.write(f"|{nombre_accion}|{round(retorno,4)}|{fecha_compra}|{fecha_venta}|\n")
    archivo.close()
    return

#prueba
report_max_gains(dicc, fecha_venta_prueba)
    

# Ejercicio 6)

import matplotlib.pyplot as plt

#Definimos la funcion. start y end tienen valor default
def plot_price(nombre_accion, diccionario, start="2021-10-04", end="2021-12-06"): 
    """Esta función recibe como argumento el nombre de una acción (dato tipo str) 
    y un argumento tipo dict con datos de acciones. La función también 
    puede recibir los parámetros opcionales start y end (tipo str) representando 
    las fechas que se quiere graficar (los valores default son start = 2022-01-01 
    y end = 2022-06-01). Luego genera un gráfico de líneas del precio, fecha por 
    fecha, de dicha acción.""" 

    index_start = diccionario["Date"].index(start)
    index_end = diccionario["Date"].index(end)
    
    from datetime import datetime
    fechas = diccionario["Date"][index_start:index_end + 1]
    fechas_nuevas = []
    for fecha in fechas:
        fecha_nueva = datetime.strptime(fecha, "%Y-%m-%d")
        fechas_nuevas.append(fecha_nueva)
    
    precios = diccionario[nombre_accion][index_start:index_end + 1]
    precios_nuevos = []
    for precio in precios:
        precio_nuevo = float(precio)
        precios_nuevos.append(precio_nuevo)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.grid("white")
    plt.plot(fechas_nuevas, precios_nuevos)
    plt.title(f"{nombre_accion} price")
    plt.ylabel("Price")
    plt.savefig(f"price_{nombre_accion}.png")
    plt.show()
    return f"price_{nombre_accion}.png"

plot_price("SATL", dicc)

# Ejercicio 7)

def monthly_average_bar_plot (nombre_accion, diccionario):
    """Esta función recibe el nombre de una acción y un diccionario de datos 
    y genera un gráfico de barras con el precio promedio de la acción, mes a mes. 
    El gráfico se guarda bajo el nombre 'monthly_average_bar_plot_XXX.png'. """
    
    # Usamos la funcion monthly_average para no repetir código
    primeros_dias, lista_promedios = monthly_average(nombre_accion, diccionario)
    
    from datetime import datetime
    primeros_dias_nuevos = []
    for fecha in primeros_dias:
        primer_dia_nuevo = datetime.strptime(fecha, "%Y-%m-%d")
        primeros_dias_nuevos.append(primer_dia_nuevo)

    plt.bar(primeros_dias_nuevos, lista_promedios, width = 22)
    plt.ylabel(nombre_accion)
    plt.title(nombre_accion)
    plt.savefig(f"monthly_average_bar_plot{nombre_accion}.png")
    plt.show()

#prueba
monthly_average_bar_plot("SATL", dicc)

def plot_max_gains(diccionario, fecha_venta):
    """Esta función recibe un diccionario de datos (dict )y una fecha de venta
    (str) y genera un gráfico de barras donde cada barra representa la ganancia 
    de la mejor inversión de cada acción. El gráfico se guarda bajo el nombre
    'max_gains.png'. """
    
    # Usamos la funcion max_gain para no repetir código
    fechas_y_retornos = []
    nombres_acciones = []
    
    for key in diccionario:
        #las llaves del dict son "Date" y los nombres de acciones
        #como el dict no tiene orden, tenemos que sacar "Date" manualmente
        if key != "Date":
            nombre_accion = key
            nombres_acciones.append(nombre_accion)
            #armamos lista de tuplas porque max_gain() retorna 2 elementos
            fechas_y_retornos.append(max_gain(nombre_accion, diccionario, fecha_venta))
                                     
    fechas = []
    retornos = []
           
    for k in range(len(fechas_y_retornos)):
        fechas.append(fechas_y_retornos[k][0])
        retornos.append(fechas_y_retornos[k][1])
                   
          
    plt.bar(nombres_acciones, retornos)
    plt.title("Max gain por acción")
    plt.savefig("max_gains.png")
    plt.show()
    return "max_gains.png"

#prueba
plot_max_gains(dicc, fecha_venta_prueba)

# Ejercicio 8)

def save_report(diccionario):
    """ Esta función recibe un diccionario con datos sobre acciones 
    (entiéndase por datos los precios de las acciones en distintas fechas).
    La función luego crea un reporte financiero en formato markdown"""
    
    from datetime import datetime   
    #Usamos la funcion today() para el nombre del archivo
    date, time = (str(datetime.today())).split(" ")
    #nos quedamos solo con date que es lo que nos interesa
    date = date.split("-")
    #desempaquetamos para llegar al formato que queremos
    YYYY, MM, DD = date
    archivo = open(f"/Users/milimiguel/Desktop/PYTHON/PENSAMIENTO COMP./TP 2/report_{DD}-{MM}-{YYYY}.md", "w")
    
    inicio_analisis = diccionario["Date"][0]
    final_analisis = diccionario["Date"][-1]
    
    diccionario_copy = diccionario.copy()
    diccionario_copy.pop("Date")
    nombres_acciones = list(diccionario_copy.keys())
    str_nombres_acciones = ", ".join(nombres_acciones)
    
    lineas = ["# Reporte Financiero\n\n", f"Fecha inicial del análisis bursátil: {inicio_analisis}\n\n", f"Fecha final del análisis bursátil: {final_analisis}\n\n", f"Acciones que se estudian en el reporte: {str_nombres_acciones}"]
    archivo.writelines(lineas)
 
    for nombre_accion in nombres_acciones:
        imagen_precio = plot_price(nombre_accion, diccionario, inicio_analisis, final_analisis)
        archivo.write(f"![{nombre_accion}]({imagen_precio})\n\n")
        archivo.write(f"El gráfico superior indica las variaciones de precio de {nombre_accion} entre las fechas de inicial y final del análisis.\n\n")
    
    archivo.write("| Nombre Acción | Retorno | Fecha de compra | Fecha de venta |\n")
    archivo.write("|----------|---------|---------|---------|\n")

    max_retorno = -100000
    for i, nombre_accion in enumerate(nombres_acciones):
        
        fecha_compra, retorno = max_gain(nombre_accion, diccionario, final_analisis)
        
        if retorno > max_retorno:
            max_retorno = retorno
            max_accion = nombre_accion
            max_index = i
        
    archivo.write(f"|**{max_accion}**|{round(max_retorno,4)}|{fecha_compra}|{final_analisis}|\n")
    nombres_acciones_copy = nombres_acciones.copy()
    nombres_acciones_copy.pop(max_index)
    
    for nombre_accion in nombres_acciones_copy:
        fecha_compra, retorno = max_gain(nombre_accion, diccionario, final_analisis)
        archivo.write(f"|{nombre_accion}|{round(retorno,4)}|{fecha_compra}|{final_analisis}|\n")
        
    imagen_max_gains = plot_max_gains(diccionario, final_analisis)
    archivo.write(f"\n\n![max_gains]({imagen_max_gains})\n\n")
    archivo.write("El gráfico superior indica los máximos rendimientos de cada acción.\n\n")
    
    imagen_graf_linea = plot_price(max_accion, diccionario)
    archivo.write(f"\n\n![max_accion_price]({imagen_graf_linea})\n\n")
    archivo.write(f" {max_accion} fue la acción de mayor retorno.\n\n")
    
    archivo.close()

#prueba
save_report(dicc)
    

    
#%%




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






    