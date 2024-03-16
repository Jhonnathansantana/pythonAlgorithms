# Pedir al usuario que ingrese los elementos de la lista separados por espacios
entrada = input("Ingresa los elementos de la lista separados por espacios: ")

# Dividir la entrada en una lista de cadenas usando el espacio como separador
elementos = entrada.split()

# Convertir cada cadena a un número entero
mi_lista = [int(elemento) for elemento in elementos]

# Iterar sobre los elementos de la lista e imprimirlos
print("Los elementos de la lista son:")
for elemento in mi_lista:
    print(elemento)
