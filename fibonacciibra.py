print("Hecho por Ibrahim Hernandez Guillen")
def serie_fibonacci(n):
    a, b = 0, 1
    serie = [a] 
    if n > 1:
        serie.append(b)
    for contador in range(2, n):
        a, b = b, a + b
        serie.append(b)
    return serie
n = int(input("Ingresa un numero: "))
serie_fibonacci = serie_fibonacci(n)
print(f"La serie {n} es: {serie_fibonacci}")
