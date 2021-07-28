# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:44:46 2021

@author: Juan
"""

def suma_primeros_impares(n):
    numero = 1
    impares = 0
    suma = 0
    
    while impares < n:
        suma = suma + numero
        numero = numero + 2
        impares = impares + 1

    return suma

# C1) Programar la función censo_mails que permita realizar una encuesta sobre
# cuántos emails diarios envían las personas. La función debe permitir hacer la
# encuesta para diez (10) personas, solicitando al usuario ingresar los datos
# por teclado. Además de la cantidad de emails diarios, se debe solicitar la
# edad del encuestado.
# Por ejemplo, una entrada válida del programa sería el valor 15 para la
# cantidad de emails diarios enviados, y 23 para la edad.
# Una vez procesadas las diez personas, la función debe informar por pantalla:
# 1) La edad de la persona que más emails envía por día.
# 2) Si la cantidad de emails del primer encuestado se repite al menos una vez.
# 3) El promedio total de emails diarios enviados entre todos los encuestados.
# Puntaje: 5/10

def censo_mails(cantidad_encuestas):
    
    # Inicializamos las variables
    max_emails = 0    
    max_edad = 0
    repite_primer_encuestado = False
    suma_emails_diarios = 0
    
    # Iniciamos el procesamiento de los 10 encuestados
    for i in range(1, cantidad_encuestas+1):
        # Ingreso los datos
        encuestado_edad = int(input("Ingrese la edad del encuestado: "))
        encuestado_emails = int(input("Ingrese la cantidad de emails diarios del encuestado: "))

        # Busco el mayor
        if encuestado_emails > max_emails:
            max_emails = encuestado_emails
            max_edad = encuestado_edad

        # Si es el primer encuestado me guardo la cantidad, sino me fijo si se repite
        if i==1:
            primer_encuestado_emails = encuestado_emails
        elif primer_encuestado_emails==encuestado_emails:
            repite_primer_encuestado = True
            
        # Acumulo los correos diarios para el promedio
        suma_emails_diarios = suma_emails_diarios + encuestado_emails
    
    # Calculo el promedio
    promedio = suma_emails_diarios/cantidad_encuestas
    
    # Informo los resultados del procesamiento
    print('\n############## RESULTADO DEL CENSO DE CORREOS ##############')
    print(f'La edad de la persona que mas correos envía es {max_edad}')
    
    if repite_primer_encuestado:
        print('La cantidad de emails del primer encuestado se repite al menos una vez.')
    else:
        print('La cantidad de emails del primer encuestado NO se repite.')
        
    print(f'El promedio total de emails diarios enviados es {promedio}')
    
censo_mails(3)