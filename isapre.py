afiliado={}

def registro():
    while True:
        try:
            nombre=str(input("\nIngrese nombre: ")).strip().upper()
            apellido=str(input("Ingrese apellido paterno: ")).strip().upper()
            genero=str(input("Ingrese Genero: ")).strip()
            estado_civil=str(input("Seleccione estado civil:  C = casado | S = soltero | V = viud@:  ")).strip().upper()
            if estado_civil=="C":
                estado_civil="casado"
            elif estado_civil=="V":
                estado_civil="viud@"
            elif estado_civil=="S":
                estado_civil="soltero"
            break
        except ValueError:
            print("\nError....asegurese de escribir de manera correcta los datos ingresados !!\n")

    while True:
        try:
            edad=int(input("Ingrese Edad: "))
            rut=input("Ingrese rut (11111111-1): ")
            fecha=input("Ingrese fecha de afiliacion (dd/mm/aaaa): ")
            break
        except ValueError:
            print("\nError...debe ingresar valor numerico !!\n")
    
    afiliado[rut]={"Nombre":nombre,"Apellido":apellido,"Edad":edad,"Estado civil":estado_civil,"Genero":genero,"Fecha":fecha}
    
    
    print(f"\nSe a registrado con exito a {afiliado[rut]["Nombre"]} {afiliado[rut]["Apellido"]}\n")
    input("Presiona cualquier tecla para continuar.....")
    menu()

def buscar():
        rut=input("Ingresa rut del afiliado para su busqueda: ")
        if rut in afiliado:
            print(f"\nEl afiliado de rut: {rut} sus datos son: {afiliado[rut]}")
            input("Presiona cualquier tecla para continuar.....")
            menu()   
        else:
            print("El rut ingresado no figura como afiliado !!\n")
            input("Presiona cualquier tecla para continuar.....")
            menu()

def certificaco():
    rut=input("\nIngrese el rut para imprimir certificado: ")
    if rut in afiliado:
        print("\tCERTIFICADO DE AFILIACION\n")
        print(f"Nombre:\t\t\t{afiliado[rut]['Nombre']} {afiliado[rut]['Apellido']}")
        print(f"Edad:\t\t\t{afiliado[rut]['Edad']}")
        print("Rut:\t\t\t",rut)
        print(f"Estado Civil:\t\t{afiliado[rut]['Estado civil']}")
        print(f"Genero:\t\t\t{afiliado[rut]['Genero']}")
        print(f"Fecha de afiliacion:\t{afiliado[rut]['Fecha']}\n")
        input("Presiona una tecla para continuar....")
        menu()
    else:
        print("\nNo se han encontrado registro del Rut !!\n")
        menu()

def salir():
    print("\nCERRANDO PROGRAMA.........\n")

def menu():
    print("\n\t***** isapre mas vida *****\n")
    print("1) Registrar Afiliado\n2) Buscar Afiliado\n3) Imprimir Certificado\n4) Salir\n")
    while True:
        try:
            op=int(input("Ingrese una opcion: "))
            if(op==1 or op==2 or op==3 or op==4):
                break
            else:
                print("\nDebe ingresar opcion enre 1 y 4 !!\n")
        except ValueError:
            print("\nError.......ingrese una opcion valida !!\n")
    if op==1:
        registro()
    elif op==2:
        buscar()
    elif op==3:
        certificaco()
    elif op==4:
        salir()

menu()