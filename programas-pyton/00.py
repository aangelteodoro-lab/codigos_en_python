historial = []
while True:
    try:
        nombre = input("cual es el nombre de tu perro (o escribe 0 para cerrar):")
        if nombre == "0":
            print("bye suerte ;)")
            print("\n---RESUMENDE HOY ---")
            for perro in historial: 
                print(perro)
            break #esto rompe el bucle
        historial.append(f"{nombre} ({edad} años)")
        entrada = input(f"cuantos años tiene {nombre}?")
        edad = float(entrada)
        if edad == 1:
            print(nombre, "es un cachorro")
        elif edad in [2,3,4,5,6,7]:
            print (nombre, "es adulto")
        elif edad in [7,8,9,10,11,12,13,14,15]:
            print(nombre, "es un senior")
        else:
            print("pon la edad correcta -_-")
            continue
        print(f"dato curioso: {nombre} en años humanos tendria {edad * 7} años")
    except ValueError:
        print("oye si fue un error ok pero no juegues con el codigo de alguien no es educado")