#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:51:30 2022

@author: milimiguel
"""

from random import randint
    
contador_partidas = 1
plata_jugador = 500

inicio = input("Bienvenido a Easy 21. Presione enter para comenzar a jugar: ")

while inicio == "" :
    suma_jugador = 0
    lista_cartas = []
    cantidad_apostada = 0
    carta_1_crupier = randint(1,10)
    lista_cartas_crupier = [carta_1_crupier]
    print("La carta 1 del crupier es: ", carta_1_crupier)

    apuesta = input("Queres apostar? (contestar si/no): ").lower()
    while apuesta != "si" and apuesta != "sí" and apuesta != "no":
        print("Error.")
        apuesta = input("Queres apostar? (contestar si/no): ").lower()
    
    
    if apuesta == "si" or apuesta == "sí":
        cantidad_apostada = int(input("Cuanto queres apostar? (contestar con valor numérico): "))
        
        while cantidad_apostada > plata_jugador or cantidad_apostada < 0:
            print("Error. Fondos insuficientes.")
            cantidad_apostada = int(input("Cuanto queres apostar? (contestar con valor numérico): "))
        plata_jugador -= cantidad_apostada
            
    while suma_jugador < 21:
        sacar_carta = input("Para sacar una carta presione enter, para terminar su turno escriba 'terminar' y luego presione enter: ").lower()
        if sacar_carta != "" and sacar_carta != "terminar":
            print("Error.")
            continue
  
        elif sacar_carta == "terminar":
            print("Terminaste tu turno.")
            break
        
        else:
            carta_jugador = randint(1,10)
            print("Tu carta es: ", carta_jugador)
            lista_cartas += [carta_jugador]
            print("Tu lista de cartas:  ", lista_cartas)
    

        suma_jugador += carta_jugador
    
        if suma_jugador < 21:
            print("LLevas acumulando: ",suma_jugador, "puntos.")
        
        
        elif suma_jugador == 21:
                break
            

    if suma_jugador > 21:
        print("Perdiste el juego. Acumulaste ",suma_jugador," puntos.")
        
            
    else: 
        k = 2
        suma_crupier = carta_1_crupier
        print("LLevas acumulando: ",suma_jugador, "puntos.")
        while suma_crupier < 21:
    
            if k == 2:
                print("Es el turno del crupier.")
            cartas_crupier = randint(1,10)
    
            print("La carta número", k, " del crupier es: ", cartas_crupier)
            lista_cartas_crupier += [cartas_crupier]
            print("Lista de cartas del crupier:  ", lista_cartas_crupier)
            
            k += 1
            suma_crupier += cartas_crupier
            lista_cartas_crupier =lista_cartas_crupier
            if suma_crupier >= 16:
                break
    
            print("Lleva acumulando: ",suma_crupier, "puntos.")
    
    
        premio = 2*cantidad_apostada
        plata_jugador += premio
        
        if suma_crupier > 21:
            print("Ganaste el juego! El crupier acumuló", suma_crupier, "puntos.")
            
        elif suma_crupier >= suma_jugador:
            print("El crupier sumó", suma_crupier, "puntos.")
            print("Vos sumaste", suma_jugador, "puntos.")
            print("Perdiste! Gana el crupier.")

        else:
            print("El crupier sumó", suma_crupier, "puntos.")
            print("Vos sumaste", suma_jugador, "puntos.")
            print("Ganaste el juego!")
        
    print("Tu saldo es de $ " + str(plata_jugador))
    

    inicio = input("Fin de la partida, querés jugar de nuevo? (conteste si/no): ").lower()

    while inicio != "si" and inicio != "sí" and inicio != "no":
        print("Error.")
        inicio = input("Fin de la partida, querés jugar de nuevo? (conteste si/no): ").lower()

    if inicio == "no":
        inicio = 0
        break
    
    contador_partidas += 1
    inicio = input("Presione enter para comenzar a jugar su partida "+ str(contador_partidas) + ":")
    if inicio == "":
        continue
        
print("Terminó el juego.")






