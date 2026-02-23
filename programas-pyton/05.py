lista = []
contador = 0
contador_2 = 0
suma = 0
mayor_nom = None
mayor_num = -999999999
while True:
       try: 
        empleados = input("ingresa el nombre de el empleado (o escribe FIN para salir)")
        contador +=1
        if empleados == "FIN":
            if contador_2 > 0:
                print("no se puede dividir por cero listo -_-")
                break
            print(f"gracias por hacer el trabajo la nomina total es {suma} de {contador_2} empleados el promedio es {promedio}")
            print(f"el empleado con mayor sueldo fue {mayor_nom} con un sueldo de {mayor_num} pesos")
        else:
            print("no registraste a nadie -_-")
            break
        nombre = empleados
        puesto = input("menciona el puesto")
        sueldo = float(input("menciona el sueldo de el empleado"))
        suma += sueldo
        contador_2 += 1
        if sueldo > mayor_num: mayor_num = sueldo 
        mayor_nom = nombre
        promedio = suma / contador_2
        datos = {"nombre": nombre,
                 "puesto": puesto,
                 "sueldo": sueldo}
        lista.append(datos)
       except ValueError:
           print("cometiste un error vuelve a intentarlo")