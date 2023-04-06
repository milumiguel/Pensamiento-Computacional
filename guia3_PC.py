#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:32:09 2022

@author: milimiguel
"""

#GUIA 3 ejs recomendados:
# 10
# 18, 19, 20
# !!! 21, 22, 23

#15-23

#%% 
# no entendi:
#    - 22

#%%

#EJ 10

#10. ★★☆ Escriba un programa que le pida al usuario un número (para esto le puede servir 
#la función built-in input()) e imprima en pantalla si es par o impar.
# • Pista: Un número par es múltiplo de 2, su división entre 2 es exacta.


numero = float(input("Inserte un numero: "))
if numero % 2 == 0:
    print("El número ingresado es par.")

else:
    print("El número ingresado es impar.")


#%%

#EJ 15

#15. ★★☆ arboles_por_km2 es un diccionario que contiene como claves los nombres de 
#distintos países y como valores asociados, la cantidad de árboles por kilómetro cuadrado 
#que posee dicho país:
    
    
arboles_por_km2 = {"Brasil": 39542, "Finlandia": 90652, "Estados Unidos": 23513,
"Dinamarca": 6129, "Siria": 534, "Arabia Saudita": 1}


#Escriba un programa que evalúe cada clave del diccionario e imprima ‘pais tiene más 
#de 20000 árboles por kilómetro cuadrado’ si el país en cuestión tiene más de 20000 árboles
#por metro cuadrado, y ‘pais tiene menos de 20000 árboles por kilómetro cuadrado’ en el 
#caso contrario.
#Por ejemplo, al evaluar la clave ‘Finlandia’ el programa debería imprimir ‘Finlandia tiene
# más de 20000 árboles por kilómetro cuadrado’, mientras que en el caso de ‘Siria’ se 
#debería mostrar ‘Siria tiene menos de 20000 árboles por kilómetro cuadrado’.

if arboles_por_km2["Brasil"] >= 20000:
    print("Brasil tiene más de 20000 árboles por kilómetro cuadrado")
else:
    print("Brasil tiene menos de 20000 árboles por kilómetro cuadrado")


if arboles_por_km2["Finlandia"] >= 20000:
    print("Finlandia tiene más de 20000 árboles por kilómetro cuadrado")
else:
    print("Finlandia tiene menos de 20000 árboles por kilómetro cuadrado")
    
    
if arboles_por_km2["Estados Unidos"] >= 20000:
    print("Estados Unidos tiene más de 20000 árboles por kilómetro cuadrado")
else:
    print("Estados Unidos tiene menos de 20000 árboles por kilómetro cuadrado")
    
    
if arboles_por_km2["Dinamarca"] >= 20000:
    print("Dinamarca tiene más de 20000 árboles por kilómetro cuadrado")
else:
    print("Dinamarca tiene menos de 20000 árboles por kilómetro cuadrado")
    
    
if arboles_por_km2["Siria"] >= 20000:
    print("Siria tiene más de 20000 árboles por kilómetro cuadrado")
else:
    print("Siria tiene menos de 20000 árboles por kilómetro cuadrado")
    
    
if arboles_por_km2["Arabia Saudita"] >= 20000:
    print("Arabia Saudita tiene más de 20000 árboles por kilómetro cuadrado")
else:
    print("Arabia Saudita tiene menos de 20000 árboles por kilómetro cuadrado")

#%%

# EJ 16

#16. ★★☆ Escriba un programa que le pida al usuario ingresar los largos de los tres lados 
#de un triángulo, y determine si es equilátero (los tres lados iguales), 
#isósceles (dos lados iguales y uno distinto) o escaleno (los tres lados distintos). 
#Imprima por pantalla el tipo de triángulo.

lado_1 = float(input("Ingrese el largo del primer lado del triangulo: "))
lado_2 = float(input("Ingrese el largo del segundo lado del triangulo: "))
lado_3 = float(input("Ingrese el largo del tercer lado del triangulo: "))

if lado_1 == lado_2 and lado_1 == lado_3:
    print("El triangulo es equilatero.")
elif (lado_1 == lado_2 and lado_1 != lado_3) or (lado_1 == lado_3 and lado_1 != lado_2) or (lado_2 == lado_3 and lado_2 != lado_1):
    print("El triangulo es isóceles.")
else:
    print("El triangulo es escaleno.")
    
# mas facil

if lado_1 == lado_2 and lado_1 == lado_3:
    print("El triangulo es equilatero.")

elif (lado_1 != lado_2) and (lado_1 != lado_3) and (lado_2 != lado_3):
    print("El triangulo es escaleno.")

else:
    print("El triangulo es isóceles.")
    



#%%

# EJ 17

#17. ★★☆ Crear un programa que permita al usuario elegir un candidato por quien quiere 
#votar. Las posibilidades son: candidato A por el partido sur, candidato B por el partido 
#este, candidato C por el partido oeste, y candidato D por el partido norte. 
#Según el candidato elegido (A, B, C ó D) se debe imprimir el mensaje “Usted ha votado
#por el partido [punto cardinal que corresponda al candidato elegido]”. Si el usuario 
#ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar 
#“Opción errónea”.

eleccion = input("Elija un candidato (las opciones son A, B, C ó D): ").upper()

if eleccion == "A":
    print("Usted ha votado por el partido sur.")
elif eleccion == "B":
    print("Usted ha votado al partido este.")
elif eleccion == "C":
    print("Usted ha votado por el partido oeste.")
elif eleccion == "D":
    print("Usted ha votado por el partido norte.")
else:
    print("Opción errónea.")

#%%

# EJ 18

#18. ★★☆ Escriba un programa que permita jugar al piedra, papel o tijera. Para hacerlo, 
#pídale al usuario que indique la elección del jugador 1 (piedra, papel o tijera), 
#para luego pedir la elección del jugador 2. En base a los datos ingresados, imprimir por 
#pantalla ‘Ganó el jugador 1’ o ‘Ganó el jugador 2’. Si el usuario ingresa una opción
#incorrecta para alguno de los dos jugadores, avisar por pantalla imprimiendo 
#‘Error en los datos ingresados’.


jugador_1 = input("Indique la eleccion del jugador 1 (piedra, papel o tijera): ").lower()
jugador_2 = input("Indique la eleccion del jugador 2 (piedra, papel o tijera): ").lower()

if (jugador_1 == "piedra" and jugador_2 == "tijera") or (jugador_1 == "papel" and jugador_2 == "piedra") or (jugador_1 == "tijera" and jugador_2 == "papel"):
    print("Ganó el jugador 1.")
elif (jugador_2 == "piedra" and jugador_1 == "tijera") or (jugador_2 == "papel" and jugador_1 == "piedra") or (jugador_2 == "tijera" and jugador_1 == "papel"):
    print( "Ganó el jugador 2.")
elif jugador_1 == jugador_2:
    print("Empate.")
else:
    print("Error en los datos ingresados.")

#%%

# EJ 19

#19. ★★☆ Escriba un programa que le pida al usuario ingresar dos números enteros que 
#representan un día y un mes, respectivamente, y que en base a eso imprima en pantalla 
#la estación del año correspondiente.


dia = int(input("Inserte un día (en forma de número entero): "))
mes = int(input("Inserte un mes (en forma de número entero): "))

#Verano (21 de diciembre a 20 de marzo).
#Otoño (21 de marzo a 20 de junio).
#Invierno (21 de junio a 20 de septiembre).
#Primavera (21 de septiembre a 20 de diciembre).

if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <=20):
    print("La estación del año es Otoño.")

elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
    print("La estación del año es Invierno.")

elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    print("La estación es Primavera.")
elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    print("La estación es Verano.")
else:
    print("Error.")

#%%

# EJ 20

#20. ★★☆ Escriba un programa que, dados un mes y un día almacenados en una lista como las 
#que se proveen de ejemplos, imprima en pantalla a que estación del año corresponde.


#fecha_uno = ['enero', 14] # verano
#fecha_uno = ['agosto', 15] # invierno
fecha_uno = ['septiembre', 21] # primavera


dict_meses = {"enero": 1, 
             "febrero": 2,
             "marzo": 3, 
             "abril": 4,
             "mayo": 5,
             "junio": 6,
             "julio": 7, 
             "agosto": 8, 
             "septiembre": 9, 
             "octubre": 10, 
             "noviembre": 11, 
             "diciembre": 12           
}

mes = dict_meses[fecha_uno[0]]
dia = fecha_uno[1]

if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <=20):
    print("La estación del año es Otoño.")

elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
    print("La estación del año es Invierno.")

elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    print("La estación es Primavera.")
elif (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    print("La estación es Verano.")
else:
    print("Error.")

#%%

# EJ 21

#21. ★★★ Escriba un programa que le pida al usuario ingresar un día, un mes y un año, 
#y que le devuelva la fecha del día siguiente. El programa debe tener en cuenta las fechas 
#inválidas y dar aviso al respecto. Considere también los años bisiestos 
#(para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, 
#excepto que también sea divisible por 400). Algunos ejemplos podrían ser:
    
#• El usuario ingresa 8, 12 y 2018, que corresponde al 8 de diciembre del 2018. 
    #El programa debe imprimir por pantalla ‘El día siguiente es el 9/12/2018’.
#• El usuario ingresa 28, 2 y 2014, que corresponde al 28 de febrero del 2014. 
    #El programa debe imprimir por pantalla ‘El día siguiente es el 1/3/2014’.
#• El usuario ingresa 40, 5 y 1987, que corresponde al 40 de mayo del 1987, una fecha inexistente. 
    #El programa debe imprimir por pantalla ‘La fecha ingresada no es válida’.
#• El usuario ingresa 31, 12 y 1405, que corresponde al 31 de diciembre del 1405. 
    #El programa debe imprimir por pantalla ‘El día siguiente es el 1/1/1406’.
#• El usuario ingresa 28, 2 y 2024, que corresponde al 28 de febrero del 2024, un año bisiesto. 
    #El programa debe imprimir por pantalla ‘El día siguiente es el 29/2/2024’.

#Al resolver este problema debe indicar:
#• Cuáles y qué tipo de variables usará. Justifique.
#• Cuáles son los datos de entrada y de salida.
#• Una solución paso a paso en castellano que permita resolver el problema.
#• La solución en Python.



dia = int(input("Ingresar un día: "))


if 0 < dia <= 27:
    mes = int(input("Ingresar un mes: "))
    if 0 < mes <= 12:
        año = int(input("Ingresar un año: "))
        if 0 < año:
            print("El día siguente es el ", dia + 1, "/", mes, "/", año, ".")
        else:
            ("Error. Conteste con un valor positivo.")
    else:
        print ("Error. Conteste con un valor entre 0 y 12.")

elif dia == 28:
    mes = int(input("Ingresar un mes: "))
    if mes == 2:
        año = int(input("Ingresar un año: "))
        if 0 < año and ((año % 4 == 0) and ((año % 100 != 0) and (año % 400 != 0))):
            print("El día siguente es el ", dia + 1, "/", mes, "/", año, ".")
        elif 0 < año:
            print("El día siguente es el ", 1, "/", mes + 1, "/", año, ".")            
            
elif dia == 29:
    mes = int(input("Ingresar un mes: "))
    if (0 < mes <= 12 and mes != 2):
        año = int(input("Ingresar un año: "))
        if 0 < año:
            print("El día siguente es el ", dia + 1, "/", mes, "/", año, ".")
    elif mes == 2:
        año = int(input("Ingresar un año: "))
        if 0 < año and ((año % 4 == 0) and ((año % 100 != 0) and (año % 400 != 0))):
            print("El día siguente es el ", 1, "/", mes + 1, "/", año, ".")
        elif 0 < año and ((año % 4 != 0) or ((año % 100 == 0) or (año % 400 == 0))):
            print("Error. El mes no cuenta con la fecha indicada.")
            
    else:
        print ("Error. Conteste con un valor entre 0 y 12.")
        
elif dia == 30:
     mes = int(input("Ingresar un mes: "))   
     if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
          año = int(input("Ingresar un año: "))
          if 0 < año:
              print("El día siguente es el ", dia + 1, "/", mes, "/", año, ".")
     elif  mes == 4 or mes == 6 or mes == 9 or mes == 11:
        año = int(input("Ingresar un año: "))
        if 0 < año:
            print("El día siguente es el ", 1, "/", mes + 1, "/", año, ".")
     elif mes == 2:
        print("Error. El mes no cuenta con la fecha indicada.")
     else:
         print("Error. Conteste con un valor entre 1 y 12.")
       
    
elif dia == 31:
    mes = int(input("Ingresar un mes: "))
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
        año = int(input("Ingresar un año: "))
        if 0 < año:
            print("El día siguente es el ", 1, "/", mes + 1, "/", año, ".")
    elif mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print("Error. El mes no cuenta con la fecha indicada.")
    elif mes == 12:
        año = int(input("Ingresar un año: "))
        if 0 < año:
            print("El día siguente es el ", 1, "/", mes + 1, "/", año + 1, ".")   
else:
    print ("Error. Conteste con un valor entre 0 y 31.")
  #  dia = int(input("Ingresar un día: "))
  # hago while loop???
  

  
#%%

# EJ 22

# 22. ★★★ Escriba un programa que, según los síntomas que posee una persona, determine si 
# es posible que tenga COVID. Para determinar esto, debe tener al menos tres de los 
# siguientes síntomas:
    
#• Fiebre o escalofríos
#• Tos
#• Dificultad para respirar (sentir que le falta el aire)
#• Fatiga
#• Dolores musculares y corporales
#• Dolor de cabeza
#• Pérdida reciente del olfato o el gusto
#• Dolor de garganta
#• Congestión o moqueo
#• Náuseas o vómitos
#• Diarrea
#Para resolver este problema debe elegir cuáles y qué tipos variables va a usar, y qué 
#datos debe solicitarle al usuario. Al finalizar el programa debe imprimir “No tiene COVID”
#o “Es posible que tenga”.

#Al resolver este problema debe indicar:
#• Cuáles y qué tipo de variables usará. Justifique.
#• Cuáles son los datos de entrada y de salida.
#• Una solución paso a paso en castellano que permita resolver el problema.
#• La solución en Python.


# tengo que frenar cuando ya me dijo que si a 3??

i = 0


sin_1 = input("Experimentaste fiebre o escalofríos?(responder si/no): ").lower()
if sin_1 == "si":
    i = i + 1
sin_2 = input("Experimentaste tos?(responder si/no): ").lower()
if sin_2 == "si":
    i = i + 1
sin_3 = input("Experimentaste dificultad para respirar (sentir que le falta el aire)?(responder si/no): ").lower()
if sin_3== "si":
    i = i + 1
    


    sin_4 = input("Experimentaste fatiga?(responder si/no): ").lower()
sin_5 = input("Experimentaste dolores musculares y corporales?(responder si/no): ").lower()
sin_6 = input("Experimentaste dolor de cabeza?(responder si/no): ").lower()
sin_7 = input("Experimentaste pérdida reciente del olfato o el gusto?(responder si/no): ").lower()
sin_8 = input("Experimentaste dolor de garganta?(responder si/no): ").lower()
sin_9 = input("Experimentaste congestión o moqueo?(responder si/no): ").lower()
sin_10 = input("Experimentaste diarrea?(responder si/no): ").lower()



# uso contador i



#%%

# EJ 23

# 23. ★★★ En la Universidad de San Andrés, en donde se dictan clases de Introducción al 
#Pensamiento Computacional, se necesita un programa que les permita, cada día, procesar 
#observaciones sobre las clases de ese día. La universidad dicta clases a estudiantes de 
#distintos niveles y cada nivel tiene clases en un día de la semana diferente: 

#los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel 
#avanzado, mientras que los jueves son para tutorías y los viernes se resuelven problemas.
#Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato 
#“día, DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el número 
#de mes. 

# 1era tarea : Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere 
#el número de días del mes o el mes supere el número 12, el programa debe finalizar 
#indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en 
#minúsculas o mayúsculas indistintamente (ayuda: las funciones upper() o lower() puede ser 
#útiles). Como condición previa se tiene que lo ingresado por el usuario tendrá el formato 
#<[alfanumérico], [numérico]/[numérico]>. 
#Una vez indicada la fecha, el usuario debe poder indicar si ese día se tomó un examen, 
#pero sólo si se trata de días en los que se dicten clases a los niveles inicial, 
#intermedio o avanzado, ya que las tutorías y la resolución de problemas no tienen exámenes.
# Si hubo examen, el usuario debe poder ingresar cuántos alumnos aprobaron y cuántos no, 
#y el programa le mostrará el porcentaje de aprobados.

#Si el día fue el correspondiente a una tutoría, el usuario deberá ingresar el porcentaje 
#de asistencia a clase y el programa le indicará “asistió la mayoría” en caso de que la 
#asistencia sea mayor al 50% o “no asistió la mayoría” si no es así.
#Si se trata de la clase de resolución de problemas y la fecha corresponde al día 1 de los 
#meses 3 u 8, se deberá imprimir “Les damos la bienvenida” y solicitar al usuario que 
#ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para 
#luego imprimir el ingreso total en $.

#Al resolver este problema debe indicar:
#• Cuáles y qué tipo de variables usará. Justifique.
#• Cuáles son los datos de entrada y de salida.
#• Una solución paso a paso en castellano que permita resolver el problema.
# La solución en Python.


pregunta = input("Ingrese la fecha actual en formato 'día, DD/MM': ").lower()

dia_semana = pregunta.split(", ")[0]
dia_mes = int((pregunta.split(", ")[1]).split("/")[0])
mes = int((pregunta.split(", ")[1]).split("/")[1])

# otra forma
dia_semana_2 = pregunta[:-7]
dia_mes_2 = pregunta[-5:-3]
mes_2 = pregunta[-2:]



dict_meses = {1: 31, 
             2: 28,
             3: 31, 
             4: 30,
             5: 31,
             6: 30,
             7: 31, 
             8: 31, 
             9: 30, 
             10: 31, 
             11: 30, 
             12: 31           
}

if dia < 1 or dia > 31:
    print("Se produjo un error.")
    
elif dia_semana not in  ["lunes", "martes" , "miercoles",  "miércoles",  "jueves" ,"viernes"]:
   print("Se produjo un error.")

elif mes not in dict_meses: # estoy preguntando si está como key
    print("Se produjo un error.")

elif dict_meses[mes] < dia_mes: # si el dia maximo del mes es < al ingresado
    print("Se produjo un error.")

elif dia_semana in  ["lunes", "martes" , "miercoles"]:
    examen = input("¿Se tomó un examen hoy?(conteste si/no): ").lower()
    if examen == "si" or examen == "si":
        aprobados = int(input("¿Cuántos aprobaron? (formato numérico): "))
        desaprobados = int(input("¿Cuántos desaprobaron? (formato numérico): "))
        porcentaje_examen = int((aprobados / (aprobados + desaprobados)) * 100) #pongo int?
        print("Aprobó el", porcentaje_examen,  "%" )
    #else:
        # pongo algun fin?
        
elif dia_semana == "jueves":
    # me dice que el usuario debe ingresar el "porcentaje" de asistencia
    porcentaje_asistencia = (input("Ingrese el porcentaje de asistencia (solo el número): ")) 
    if porcentaje_asistencia > 50:
        print("Asistió la mayoria.")
    else:
        print("No asistió la mayoria.")
        #quizas seria mejor preguntar cuantos fueron y cuantos son y sacar el %

elif dia_mes == 1 and (mes == 3 or mes == 8):
    #(viernes implicito) 
    print("Les damos la bienvenida")
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo (formato numérico): "))
    arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
    ingreso_total = cantidad_alumnos * arancel #float
    print("El ingreso total es: $", ingreso_total)
    

#%%



















