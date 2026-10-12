## ESTRUCTURAS EN PYTHON ##

# Listas
lista = ["Hola", "Hello", 10, 20, 30]
print(lista)
lista.append(True)
print(lista)
lista.remove("Hola")
print(lista)
print(lista[0],lista[3])
print(lista[0:2])
print(lista.count(10))
lista[0] = "Adiós"
print(lista)
lista_2 = ["Pablo", "Angel","Luis","Ferran"]
lista_2.sort()
print(lista_2)
print(len(lista_2))

# Tupla (es inmutable)
tupla = ("Angel", "Bellver", 1998)
print(tupla)
for elemento in tupla:
    print(elemento)
for indice,valor in enumerate(tupla):
    print(tupla[indice])

# Sets (listas desordenadas que no adminten duplicados)
my_set = {"Manzana", "Pera", "Melón","Sandía"}
print(my_set)
my_set.add("Melocotón")
my_set.add("Manzana")
print(my_set,len(my_set))
my_set.remove("Pera")
print(my_set)
my_set.update({"Plátano","Uva","Piña"})
print(my_set)
print(sorted(my_set))

# Diccionario
diccionario = {"nombre": "Ángel",
               "edad": 28,
               "profesion": "Ingeniero"}
print(diccionario)
diccionario = dict(nombre = "Angel", edad = 28, profesion = "Ingeniero")
print(diccionario)
diccionario["edad"] = 29
print(diccionario)
print(diccionario.items())
diccionario["ciudad"] = "Valencia"
print(diccionario)
del diccionario["edad"]
print(diccionario)
diccionario_ordenado = dict(sorted(diccionario.items()))
print(diccionario_ordenado)
print()

## EJERCICIO EXTRA: AGENDA TELEFÓNICA ##

agenda = dict() # Se crea diccionario vacio

while True:
    print("Su agenda actual:")
    print(agenda)
    print()

    # Pedir acción al usuario
    print("1. Buscar Contacto\n"
          "2. Añadir Contacto\n"
          "3. Actualizar Contacto\n"
          "4. Eliminar Contacto\n"
          "5. Salir")
    opcion = input("Seleccione una opción: ")
    print()

    match opcion:
        case '1': 
            nombre_contacto_buscar = input("Introduzca el nombre del contacto que desea buscar: ")

            if nombre_contacto_buscar in agenda:
                print(f"{nombre_contacto_buscar}:{agenda[nombre_contacto_buscar]}")
                print()
            else:
                print("El contacto no existe")
                print()

        case '2':
            nombre_contacto_nuevo = input("Introduzca el nombre del nuevo contacto: ")
            numero_contacto_nuevo = input("Introduzca el número del nuevo contacto: ")

            if numero_contacto_nuevo.isdigit() and len(numero_contacto_nuevo) <= 9 and\
                nombre_contacto_nuevo not in agenda and numero_contacto_nuevo not in agenda.values():
                agenda[nombre_contacto_nuevo] = numero_contacto_nuevo
                print("Contacto añadido a su agenda:")
                print(f"{nombre_contacto_nuevo}:{agenda[nombre_contacto_nuevo]}")
                print()

            elif not numero_contacto_nuevo.isdigit() or len(numero_contacto_nuevo) > 9:
                print("El número introducido no es correcto")
                print()

            elif numero_contacto_nuevo in agenda.values():
                print("El número de teléfono introducido ya existe")

            elif nombre_contacto_nuevo in agenda:
                print("El nombre del contacto introducido ya existe")
                print()

        case '3':
            nombre_contacto_actualizar = input("Introduzca el nombre del contacto a actualizar: ")
            numero_contacto_actualizar = input("Introduzca el nuevo número del contacto a actualizar: ")

            if nombre_contacto_actualizar in agenda and numero_contacto_actualizar.isdigit()\
            and len(numero_contacto_actualizar) <= 9 and\
            numero_contacto_actualizar not in agenda.values():
                agenda[nombre_contacto_actualizar] = numero_contacto_actualizar
                print("Contacto actualizado:")
                print(f"{nombre_contacto_actualizar}:{agenda[nombre_contacto_actualizar]}")
                print()

            elif nombre_contacto_actualizar not in agenda:
                print("El nombre introducido no se encuentra en la agenda")
                print()

            elif not numero_contacto_actualizar.isdigit() or len(numero_contacto_actualizar) > 9:
                print("El número introducido no es correcto")
                print()

            elif numero_contacto_actualizar in agenda.values():
                print("El número de teléfono introducido ya existe")
                print()

        case '4':
            nombre_contacto_eliminar = input("Introduzca el nombre del contacto a eliminar: ")

            if nombre_contacto_eliminar in agenda:
                del agenda[nombre_contacto_eliminar]
                print("Contacto eliminado")
                print()
            else:
                print("El contacto que desea eliminar no se encuentra en la agenda")
                print()

        case '5':
            print("¡Hasta luego!")
            break

        case _:
            print("Opción no válida")
            print()