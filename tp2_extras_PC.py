#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:00:39 2022

@author: milimiguel
"""

#import numpy as np
#import matplotlib as plt

def func_dict(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    dic = {}
    funciones = lineas[0].strip().split(",")
    lista_valores = []
    
    for linea in lineas[1:]:
        linea = linea.strip().split(",")
        
        for funcion in funciones:
            lista_valores.append([linea[funciones.index(funcion)]])
            dic[funcion] = lista_valores[funciones.index(funcion)]

    return print(dic)
    
#def func_data(nombre_archivo, funcion):

    

#def func_plot():
    
    
    
func_dict("/Users/milimiguel/Desktop/PYTHON/PENSAMIENTO COMP./TP 2/math_func.csv")
    

#%%



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













































