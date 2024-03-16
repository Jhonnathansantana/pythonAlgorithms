# Crear una lista vacía para almacenar los elementos
mi_lista = []

# Pedir al usuario que ingrese los elementos uno por uno
print("Ingresa los elementos de la lista (escribe 'fin' para terminar):")
while True:
    elemento = input("Elemento (o escribe 'fin' para terminar): ")
    if elemento.lower() == 'fin':
        break  # Salir del bucle si se ingresa 'fin'
    mi_lista.append(elemento)  # Agregar el elemento a la lista

# Imprimir la lista ingresada por el usuario
print("Los elementos de la lista son:")
for elemento in mi_lista:
    print(elemento)
