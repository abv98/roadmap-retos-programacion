## EJERCICIOS

def factorial(numero: int) -> int:
    if numero < 0:
        print("No existe el factorial de números negativos")
        return 0
    elif numero == 0:
        return 1
    else:
        return numero*factorial(numero - 1)

def fibonacci(posicion: int) -> int:
    if posicion <= 0:
        return 0
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)


print(factorial(5))
print(fibonacci(10))
