while True:
    try:
        entrada = float(input("bienvenido a la calculadora, escribe un numero, o escribe 0.1 para salir"))
        num1 = entrada
        if entrada == 0.1:
            print("bye")
            break
        num2 = float(input("escribe otro numero"))
        operacion = input("""elige una operacion
        1, suma
        2, resta
        3, divicion
        4, multiplicacion""")
        if operacion == "1":
            print(f"{num1 + num2}")
        elif operacion == "2":
            print(f"{num1 - num2}")
        elif operacion == "3":
            print(f"{num1 / num2}")
        elif operacion == "4":
            print(f"{num1 * num2}")
        else:
            print("error")
    except ValueError:
        print("escribe un dijito correcto")