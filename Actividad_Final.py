cliente = {"rutes",
           "nombres",
           "apellidospaternos",
           "edades",
           "estadosciviles",
           "generos",
        "fechasdeafiliaciones"}

rut = input("Ingrese su rut: ")
nombre = input("Ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
edad = int(input)("Ingrese su edad: ")
estado_civil = str(input("Ingrese el estado civil: (c = casado), (s = soltero), (v = viudo)"))
genero = input("Ingrese su genero: ")
fecha_de_afiliacion = int(input("Ingrese la fecha de afiliación: "))

if opcion == 1:
    rutes.append(rut)
    nombres.append(nombre)
    apellidospaternos.append(apellido_paterno)
    edades.append(edad)
    estadosciviles.append(estado_civil)
    generos.append(genero)
    fechasdeafiliaciones.append(fecha_afiliacion)
           
if opcion==2:
    if afiliados==0:
        print("\nNO se han registrados afiliados !!\n")
    else:
        rut=input("\nIngresa RUT del afiliado")
        for rut in cliente.items():
            print(f"{cliente}")
