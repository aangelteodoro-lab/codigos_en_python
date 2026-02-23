inventario = []
while True:
    try:
        entrada = input("escribe el nombre de un dispositivo (o envia salir al acabar):")
        dispositivo = entrada
        if entrada == "salir":
            print("gracias por la ayuda esperamos que sean todos")
            break
        numero_serie = input("escribe el numero de serie de el dispositivo:")
        estado = input("escribe el estado de el dispositivo:")
        equipo = {"dispositivo": dispositivo,
                "numero_serie": numero_serie,
                "estado": estado}
        inventario.append(equipo)
    except ValueError:
        print("un dato esta mal")
busqueda = input("\n escribe numero de serie para buscar y ver detalles")
encontrado = False
for aparatos in inventario:
    if aparatos ["numero_serie"] == busqueda:
        print(f"\nDispositivo encontrado")
    print(f"dispositivo: {aparatos["dispositivo"]}")
    print(f"numero_serie : {aparatos["numero_serie"]}")
    print(f"estado {"estado"}")
    encontrado = True
    break
if not encontrado:
      print("lo sentimos el dispositivo no esta registrado")