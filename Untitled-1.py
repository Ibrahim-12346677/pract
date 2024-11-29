def gestion_de_tenis():
    print("Hecho por Ibrahim Hernandez Guillen e Ilse Guadalupe Rodriguez Molina ")
    
    
    CONTRASENA_CORRECTA = "973412"
    intentos = 0
    while True:
        contrasena = input("Introduce la contraseña: ")
        if contrasena == CONTRASENA_CORRECTA:
            print("¡Contraseña correcta! Bienvenido al sistema.")
            break
        else:
            print("¡Contraseña incorrecta! vuelve a intentarlo.")
            intentos += 1
            if intentos >= 3:
                print("Demasiados intentos fallidos. Saliendo del programa.")
                return

    
    tenis = []
    
    while True:
        print("\nMenu de Gestion de Tenis")
        print("1. Agregar")
        print("2. Consultar")
        print("3. Modificar ")
        print("4. Eliminar")
        print("5. Salir del programa")
        opcion = input("Elige una opción (1/2/3/4/5): ")

        if opcion == "1":  
            if len(tenis) < 100:
                print("\nAgrega los datos del par de tenis:")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                talla = input("Talla: ")
                color = input("Color: ")
                material = input("Material: ")
                precio = input("Precio: ")
                genero = input("Género: ")
                deporte = input("Deporte: ")
                disponibilidad = input("Disponibilidad: ")
                
                tenis.append([marca, modelo, talla, color, material, precio, genero, deporte, disponibilidad])
                print("Par de tenis agregado exitosamente.")
            else:
                print("No se pueden agregar mas tenis, la lista se.encuentra llena.")
        
        elif opcion == "2":  
            if tenis:
                print("\nLista de Tenis:")
                for i, t in enumerate(tenis, start=1):
                    print(f"Tenis {i}: Marca={t[0]}, Modelo={t[1]}, Talla={t[2]}, Color={t[3]}, "
                          f"Material={t[4]}, Precio={t[5]}, Género={t[6]}, Deporte={t[7]}, Disponibilidad={t[8]}")
            else:
                print("No hay tenis en la lista.")
        
        elif opcion == "3":
            if tenis:
                print("\nModificar un par de tenis")
                indice = int(input("Introduce el numero del par de tenis que deseas modificar: ")) - 1
                if 0 <= indice < len(tenis):
                    print("Ingresa los datos a modificar:")
                    tenis[indice][0] = input(f"Marca [{tenis[indice][0]}]: ") or tenis[indice][0]
                    tenis[indice][1] = input(f"Modelo [{tenis[indice][1]}]: ") or tenis[indice][1]
                    tenis[indice][2] = input(f"Talla [{tenis[indice][2]}]: ") or tenis[indice][2]
                    tenis[indice][3] = input(f"Color [{tenis[indice][3]}]: ") or tenis[indice][3]
                    tenis[indice][4] = input(f"Material [{tenis[indice][4]}]: ") or tenis[indice][4]
                    tenis[indice][5] = input(f"Precio [{tenis[indice][5]}]: ") or tenis[indice][5]
                    tenis[indice][6] = input(f"Genero [{tenis[indice][6]}]: ") or tenis[indice][6]
                    tenis[indice][7] = input(f"Deporte [{tenis[indice][7]}]: ") or tenis[indice][7]
                    tenis[indice][8] = input(f"Disponibilidad [{tenis[indice][8]}]: ") or tenis[indice][8]
                    print("Par de tenis modificado exitosamente.")
                else:
                    print("El numero de tenis no se encuentra en la lista")
            else:
                print("No hay tenis para modificar.")
        
        elif opcion == "4":  
            if tenis:
                print("\nEliminar un par de tenis")
                indice = int(input("ingresa el numero del tenis que deseas eliminar: ")) - 1
                if 0 <= indice < len(tenis):
                    tenis.pop(indice)
                    print("Par de tenis eliminado exitosamente.")
                else:
                    print("Numero de tenis no invalido.")
            else:
                print("No hay tenis para eliminar.")
        
        elif opcion == "5": 
            print("Gracias por elegirnos, que tenga un excelente dia ")
            break
        
        else:
            print("Opción inválida. Inténtalo de nuevo.")
gestion_de_tenis()