base_de_datos = []
while True:
    entrada = input("escribe x para salir (o su nombre si quiere seguir):")
    nombre = entrada
    if entrada == "x":
        break
    edad = input("escribe tu edad:")
    hobby = input("escibe tu hobby favorito:")

    perfil_1 = {"nombre": nombre,
                "edad": edad, 
                "hobby": hobby}
    base_de_datos.append(perfil_1)
    print(base_de_datos)
busqueda = input("\n a quien buscas")
encontrado = False
for perfil in base_de_datos:
    if  perfil ["nombre"] == busqueda:
     print(f"\nUsuario encontrado")
     print(f"nombre: {perfil["nombre"]}")
     print(f"edad : {perfil["edad"]}")
     print(f"hobby {"hobby"}")
     encontrado = True
    break
if not encontrado:
     print("lo siento ese usuario no existe en la base de datos") 