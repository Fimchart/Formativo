turistas = {
        "001": {"Nombre": "John Doe", "Pais": "Estados Unidos", "Fecha": "12-01-2024"},
        "002": {"Nombre": "Emily Smith", "Pais": "Estados Unidos", "Fecha": "23-03-2024"},
        "012": {"Nombre": "Julian Martinez", "Pais": "Argentina", "Fecha": "19-09-2023"},
        "014": {"Nombre": "Agustin Morales", "Pais": "Argentina", "Fecha": "28-03-2024"},
        "005": {"Nombre": "Carlos Garcia", "Pais": "Mexico", "Fecha": "10-05-2024"},
        "006": {"Nombre": "Maria Lopez", "Pais": "Mexico", "Fecha": "08-12-2023"},
        "007": {"Nombre": "Joao Silva", "Pais": "Brasil", "Fecha": "20-06-2024"},
        "003": {"Nombre": "Michael Brown", "Pais": "Estados Unidos", "Fecha": "05-07-2023"},
        "004": {"Nombre": "Jessica Davis", "Pais": "Estados Unidos", "Fecha": "15-11-2024"},
        "008": {"Nombre": "Ana Santos", "Pais": "Brasil", "Fecha": "03-10-2023"},
        "010": {"Nombre": "Martin Fernandez", "Pais": "Argentina", "Fecha": "13-02-2023"},
        "011": {"Nombre": "Sofia Gomez", "Pais": "Argentina", "Fecha": "07-04-2024"},
    }


def turistas_por_pais(pais):
    encontrados = False
    for t in turistas.values():
        if t["Pais"].lower() == pais.lower():
            print(t["Nombre"]) 
            encontrados = True
    if not encontrados:
        print("\nNo hay turistas de este país.")
    return


def turistas_por_mes(mes):
    total = len(turistas)
    contador = 0
    for t in turistas.values():
        fecha = t["Fecha"]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            contador += 1
    if total == 0:
        return 0.0
    porcentaje = (contador / total) * 100
    return round(porcentaje,1)


def eliminar_turista():
    global turistas
    nombre_eliminar = input("\nIngrese el nombre completo del turista a eliminar: ").strip().lower()
    eliminado = False
    for clave, datos in list(turistas.items()):
        if datos["Nombre"].lower() == nombre_eliminar:
            del turistas[clave]
            print("\nTurista eliminado.")
            eliminado = True
            break
    if not eliminado:
        print("\nTurista no encontrado. No se pudo eliminar.")