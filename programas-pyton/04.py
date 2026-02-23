gastos = []
while True:
    try:
        nombre = input("dime el nombre de tu gasto:) (o escribe salir para salir:")
        if nombre == "salir":
            total= sum(gasto["precio"] for gasto in gastos)
            print(f"gracias por probar :) el precio de todos los gastos es {total} ")
            break
        categoria = input("""el gasto que categoria es
                        comida
                        estudio
                        social
                        personal""")
        costo = float(input("cuanto cuesta el gasto"))
        diccionario = {"item": nombre,
                    "categoria": categoria,
                    "precio": costo}
        gastos.append(diccionario)
    except ValueError:
        print("nose que hiciste pero no lo hagas")