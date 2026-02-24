status_code = int(input("ingresar estado de la api (ej: 200, 404, 500): "))

match status_code:
    case 200:
        print("Todo OK. Los datos llegaron perfecto.")
    case 404:
        print("No se encuentra la pagina.")
    case 500:
        print("el servidor encontró una condición inesperada que le impidió cumplir con la solicitud.")
    case _:
        print("Código desconocido.")