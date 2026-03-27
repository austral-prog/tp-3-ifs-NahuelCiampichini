def calculator():
    """
    Ejercicio 7 - Calculadora Simple

    Leer dos números (pueden ser decimales) y una operación (+, -, *, /) mediante input().
    Realizar la operación correspondiente e imprimir el resultado.

    Validaciones:
    - Si la operación es inválida, imprimir "Operacion invalida"
    - Si es división y el divisor es cero, imprimir "Error: division por cero"

    Ejemplo:
        Para las entradas "10", "5" y "+", la salida esperada es:
        Resultado: 15.0

        Para las entradas "10", "2" y "/", la salida esperada es:
        Resultado: 5.0

        Para las entradas "10", "0" y "/", la salida esperada es:
        Error: division por cero

        Para las entradas "10", "5" y "x", la salida esperada es:
        Operacion invalida
    """
    num_1 = float(input())
    num_2 = float(input())
    op = input()

    inv = False

    if op == "*" or op == "/" or op == "+" or op == "-":
        inv = False
    else:
        inv = True
    
    if inv == False:
        if op == "+":
            print(f"Resultado: {num_1 + num_2}")
        elif op == "-":
            print(f"Resultado: {num_1 - num_2}")
        elif op == "*":
            print(f"Resultado: {num_1 * num_2}")
        elif op == "/" and num_2 != 0:
            print(f"Resultado: {num_1 /num_2}")
        else:
            print("Error: division por cero")
    else:
        print("Operacion invalida")