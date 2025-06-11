from Funciones import turistas_por_mes, turistas_por_pais, eliminar_turista


print("\n*** MENU PRINCIPAL ***")
while True:
    print("\n1.- Turistas por país.")
    print("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir.\n")

    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion < 1 or opcion > 4:
            print("Por favor, ingrese un número del 1 al 4.")
            continue
    except ValueError:
        print("Solo están permitidos los numeros.")
        continue

    if opcion == 1:
        pais_selec = input("\n¿Que pais quiere buscar?: ")
        turistas_por_pais(pais_selec)
    elif opcion == 2:
        while True:
            try:
                mes_selec = int(input("Ingrese el numero del mes (1-12): "))
                if mes_selec < 1 or mes_selec > 12:
                    print("\nPor favor ingrese un número del 1 al 12.")
                    continue
                break
            except ValueError:
                print("\nSolo están permitidos los numeros.")

        porcentaje = turistas_por_mes(mes_selec)
        print(f"\n{porcentaje}% de los turistas visitó Chile en ese mes.")
    elif opcion == 3:
        eliminar_turista()
    elif opcion == 4:
        print("----- PROGRAMA TERMINADO -----")
        break