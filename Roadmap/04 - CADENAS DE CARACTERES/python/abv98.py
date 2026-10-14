# En este caso hacemos directamente el ejercicio extra

'''
EJERCICIO EXTRA:
Pedir al usuario 2 palabras por teclado y realizar lo siguiente:
- Comprobar si cada una de las palabras es un palíndromo (se lee igual en ambas direcciones)
- Comprobar si entre ellas son anagramas (una se forma reordenando las letras de la otra)
- Comprobar si cada una de las palabras es un isograma (ninguna de sus letras se repite)
'''
# Definición de funciones

def pedir_palabras():
    while True:
        lista_palabras = input("Introduzca dos palabras distintas separadas por un espacio en minúsculas: ")
        palabras_separadas = lista_palabras.split(" ")
        print()
        lista_palabras_sin_espacio = lista_palabras.replace(" ","")
        if " " not in lista_palabras:
            print("No se ha introducido un espacio entre palabras " 
                  "o sólo se ha introducido una palabra. Vuelva a introducir las palabras\n")
        elif not lista_palabras_sin_espacio.isalpha():
            print("Solo se pueden introducir letras. Vuelva a introducir las palabras\n")
        elif not lista_palabras_sin_espacio.islower():
            print("Las palabras se deben introducir en minúscula. Vuelva a introducir las palabras\n")
        elif palabras_separadas[0] == palabras_separadas[1]:
            print("Las palabras deben ser diferentes. Vuelva a introducir las palabras\n")
        else:
            break
    
    return palabras_separadas[0], palabras_separadas[1]

def palindromo(palabra):

    lista_palabra = list(palabra) # Convierto la palabra en una lista de caracteres
    coincidencias = 0
    for indice, letra in enumerate(lista_palabra):
        if lista_palabra[indice] == lista_palabra[len(lista_palabra)-indice-1]:
            coincidencias +=1
    if coincidencias == len(lista_palabra):
        print(f"{palabra} es un palíndromo\n")
    else:
        print(f"{palabra} no es un palíndromo\n")

def isograma(palabra):

    coincidencias = 0
    for letra in palabra:
        if palabra.count(letra) > 1:
            coincidencias += 1

    if coincidencias == 0:
        print(f"{palabra} es un isograma\n")
    else:
        print(f"{palabra} no es un isograma\n")

def anagramas(palabra1, palabra2):

    coincidencias = 0
    if len(palabra1) != len(palabra2):
        print(f"{palabra1} y {palabra2} no son anagramas")
    else:
        for indice, letra in enumerate(palabra1):
            if palabra1.count(letra) == palabra2.count(letra):
                coincidencias += 1
        if coincidencias == len(palabra1):
            print(f"{palabra1} y {palabra2} son anagramas")
        else:
            print(f"{palabra1} y {palabra2} no son anagramas")
            

# Programa principal

palabra1, palabra2 = pedir_palabras()
print("Se comprueba si cada una de las palabras es un palíndromo:\n")
palindromo(palabra1)
palindromo(palabra2)
print("Se comprueba si cada una de las palabras es un isograma:\n")
isograma(palabra1)
isograma(palabra2)
print("Se comprueba si las palabras son anagramas entre si:\n")
anagramas(palabra1,palabra2)