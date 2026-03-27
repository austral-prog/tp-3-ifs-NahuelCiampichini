def compare():
    """
    Ejercicio 4 - Comparar Dos Números

    Leer dos números enteros mediante input(). Compararlos e imprimir si el primero
    es mayor, menor o igual al segundo.

    Ejemplo:
        Para las entradas "10" y "5", la salida esperada es:
        10 es mayor que 5

        Para las entradas "3" y "8", la salida esperada es:
        3 es menor que 8

        Para las entradas "7" y "7", la salida esperada es:
        7 es igual a 7
    """
    num_1 = int(input())
    num_2 = int(input())
    if num_1 > num_2:
        print(f"{num_1} es mayor que {num_2}")
    elif num_1 < num_2:
        print(f"{num_1} es menor que {num_2}")
    else:
        print(f"{num_1} es igual a {num_2}")

