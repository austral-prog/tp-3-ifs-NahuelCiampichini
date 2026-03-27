def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """
    precio_unitario = float(input())
    cant_unid = int(input())

    if cant_unid >= 10:
        print(f"Subtotal: {precio_unitario * cant_unid}")
        print("Descuento aplicado: 20%")
        print(f"Monto de descuento: {(precio_unitario * cant_unid) * 0.20}")
        print(f"Total final: {(precio_unitario * cant_unid) * 0.80}")
    
    elif cant_unid >=5 and cant_unid <= 9:
        print(f"Subtotal: {precio_unitario * cant_unid}")
        print("Descuento aplicado: 10%")
        print(f"Monto de descuento: {(precio_unitario * cant_unid) * 0.10}")
        print(f"Total final: {(precio_unitario * cant_unid) * 0.90}")
    else: 
        print(f"Subtotal: {precio_unitario * cant_unid}")
        print("Descuento aplicado: 0%")
        print(f"Monto de descuento: {(precio_unitario * cant_unid) * 0}")
        print(f"Total final: {(precio_unitario * cant_unid)}")
        
