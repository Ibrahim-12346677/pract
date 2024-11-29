print("Hecho por Ibrahim Hernandez Guillen e Ilse Guadalupe Rodriguez Molina")
def triangulo_de_pascal(n):
    triangulo = []
    for i in range(n):
        fila = [1]
        if triangulo:
            ultima_fila = triangulo[-1]
            for j in range(len(ultima_fila) - 1):
                fila.append(ultima_fila[j] + ultima_fila[j + 1])
            fila.append(1)
        triangulo.append(fila)
    for fila in triangulo:
        print(' '.join(map(str, fila)).center(n * 2))
while True:
    filas = int(input("¿Cuántas filas del Triángulo de Pascal deseas? "))
    triangulo_de_pascal(filas)
    repetir = input("¿Deseas generar otro Triángulo de Pascal? (s/n): ").strip().lower()
    if repetir != 's':
        print("¡Hasta luego!")
        break