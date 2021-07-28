# ---------------INTRO PROG UNLU: EJEMPLO PARCIALITO ENUNCIADO------------------
# Completar con tus datos:
# Nombre:
# DNI:
# Entrega: por GitHub (preferentemente) o por mail a: introprog.unlu@gmail.com

# A) Suponé que es necesario escribir un programa que procese la edad de los
# docentes de una universidad, y el programa debe terminar cuando el usuario
# ingresa -99 como edad. ¿Qué estructura repetitiva utilizarías para implementar
# el algoritmo? ¿Por qué?.
# Puntaje: 1/10

# RESPUESTA: La estructura es CICLO INDEFINIDO CON CENTINELA (que se implementa
# con while en Python, pero while es una palabra reservada de Python para hacer
# ciclos indefinidos, no es una estructura, y en otros lenguajes de programación
# podría no llamarse while). Con respecto a la justificación, es ciclo indefinido,
# porque se desconoce cuántos datos se ingresarán, y el ciclo es con centinela,
# porque termina cuando se ingresa como dato -99 (el valor centinela).


# B1) Programar la función suma_primeros_impares que recibe un número natural n
# como parámetro, y retorna la suma los primeros n números impares.
# Ejemplo: si n=3, la función debe retornar 9 (ya que 1+3+5=9)
# Puntaje: 3/10

# Para que sea más útil la resolución, les ponemos distintas formas de resolver
# el problema de la suma de los primeros n impares. Ustedes sólo debían entregar
# una versión.


def suma_primeros_impares_v1(n):
    numero = 1
    impares = 0
    suma = 0

    while impares < n:
        suma = suma + numero
        numero = numero + 2
        impares = impares + 1

    return suma


def suma_primeros_impares_v2(n):
    suma = 0
    for i in range(1, n * 2, 2):
        suma += i

    return suma


def suma_primeros_impares_v3(n):
    suma = 0
    for i in range(1, n * 2):
        if (i % 2) == 1:
            suma += i

    return suma


def suma_primeros_impares_v4(n):
    suma = 0
    for i in range(n):
        suma += 2 * i + 1

    return suma


# B2) Programar la función test_suma_primeros_impares que testea la función
# suma_primeros_impares, con al menos 2 casos de test. Justifique por qué
# considera que esos casos de tests son relevantes para testear el programa.
# Puntaje: 0.5/10

# JUSTIFICACION: Los casos de tests n=1 y n=3 son convenientes, porque siempre
# se testea el caso extremo (ya que ahí suelen estar los errores), y algún otro
# caso, no muy complejo, para que haga varias iteraciones del ciclo.
# El caso extremo es n=1 y un caso simple que hace varias iteraciones es n=3.


def test_suma_primeros_impares():
    print("Testeando suma_primeros_impares_v1... ", end="")
    assert suma_primeros_impares_v1(1) == 1
    assert suma_primeros_impares_v1(3) == 9
    print("Pasó!")
    print("Testeando suma_primeros_impares_v2... ", end="")
    assert suma_primeros_impares_v2(1) == 1
    assert suma_primeros_impares_v2(3) == 9
    print("Pasó!")
    print("Testeando suma_primeros_impares_v3... ", end="")
    assert suma_primeros_impares_v3(1) == 1
    assert suma_primeros_impares_v3(3) == 9
    print("Pasó!")
    print("Testeando suma_primeros_impares_v4... ", end="")
    assert suma_primeros_impares_v4(1) == 1
    assert suma_primeros_impares_v4(3) == 9
    print("Pasó!")


test_suma_primeros_impares()

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

    # Iniciamos el procesamiento de los encuestados
    for i in range(cantidad_encuestas):
        # Ingreso los datos
        encuestado_edad = int(input("Ingrese la edad del encuestado: "))
        encuestado_emails = int(input("Ingrese la cantidad de emails diarios del encuestado: "))

        # Busco el mayor
        if encuestado_emails > max_emails:
            max_emails = encuestado_emails
            max_edad = encuestado_edad

        # Si es el primer encuestado me guardo la cantidad, sino me fijo si se repite
        if i == 0:
            primer_encuestado_emails = encuestado_emails
        elif primer_encuestado_emails == encuestado_emails:
            repite_primer_encuestado = True

        # Acumulo los correos diarios para el promedio
        suma_emails_diarios = suma_emails_diarios + encuestado_emails

    # Calculo el promedio
    promedio = suma_emails_diarios / cantidad_encuestas

    # Informo los resultados del procesamiento
    print("\n############## RESULTADO DEL CENSO DE CORREOS ##############")
    print(f"La edad de la persona que mas correos envía es {max_edad}")

    if repite_primer_encuestado:
        print("La cantidad de emails del primer encuestado se repite al menos una vez.")
    else:
        print("La cantidad de emails del primer encuestado NO se repite.")

    print(f"El promedio total de emails diarios enviados es {promedio}")


# Testeo para 3 encuestas
# censo_mails(3)
# Entrego para 10 encuestas
censo_mails(10)

# C2) ¿Es posible testear que su programa funciona correctamente ingresando
# menos de 10 encuestas? Justifique su respuesta.
# Puntaje: 0.5/10
#
# RESPUESTA: Sí es posible, porque lo importante es probar la lógica del programa
# y eso se puede hacer con muchas menos encuestas (por ejemplo con sólo 3 encuestas).
# Y eso es lo que se hace para probar, ya que podríamos haber pedido ingresar
# 5000 encuestas, y es imposible que alcance el tiempo del examen para ingresar
# tantas encuestas. Además, que con sólo 3 encuestas, es más fácil encontrar
# los errores del programa.
