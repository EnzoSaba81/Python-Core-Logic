# Este código es un programa de conversión de moneda que utiliza una API para obtener las tasas de cambio actuales.

import requests

mi_url = "https://api.frankfurter.app/latest?from=EUR" # Definimos la URL de la API que queremos consultar
respuesta = requests.get(mi_url) # Usamos 'mi_url' que definimos arriba

datos = respuesta.json()["rates"]

historial = []


# Menu para poder elegir 3 opciones de conversion de euro a otras monedas. 
# El usuario ingresa la cantidad de euros que desea convertir y el programa muestra el resultado de la conversión.

while True:
    print("Bienvenido ingresa una de las siguientes opciones para convertir de Euro a las siguentes monedas : \n 1. Dólares (USD) \n 2. Libras Esterlinas (GBP) \n 3. Yen Japonés (JPY) \n 4. Historial  \n 5. Salir")
    opcion= input("Ingrese la opción deseada: ").strip()
# --- NUEVA LÓGICA DE SALIDA ---
    if opcion == "5":
        print("Gracias por usar el sistema. ¡Arrivederci!")
        break

    # --- NUEVA LÓGICA DE HISTORIAL ---
    if opcion == "4":
        print("--- TU HISTORIAL DE CONVERSIONES ---")
        if not historial:
            print("Aún no has realizado conversiones.")
        else:
            for operacion in historial:
                print (f" {operacion}")
        input("\nPresioná Enter para volver al menú...") # Pausa para que el usuario lea
        continue
    
    match opcion:
        case "1":moneda = "USD"
        case "2":moneda = "GBP"
        case "3":moneda = "JPY"
        case _:moneda = None 
        
    if moneda != None:
        try:
            cantidad = float(input(f"Ingresa la cantidad de Euros para convertir a {moneda}: "))  #Segun la opcion que elija el usuario, se le pedira ingresar la cantidad de euros a convertir a la moneda seleccionada.
            
            resultado = cantidad * datos[moneda] # Multiplacion entre cantidad de euros y la tasa de cambio de la moneda selec
            
            registro = f"Cantidad: {cantidad} EUR -> {resultado:.2f} {moneda}" # Cadena de texto que se guarda en historial, para poder mostrar al usuario que converisones ha realizado.
            
            # Guardamos la frase entera en la lista
            historial.append(registro) # Se manda a historial el registro que se hizo para mostrarlo luego.
            
            print(f"Resultado: {cantidad} EUR = {resultado:.2f} {moneda}")  # Finalmente, se muestra el resultado de la conversión al usuario.
        except ValueError:
            # Si el usuario ingresa texto, se ejecuta esto:
            print(" Error: Por favor, ingresa solo números.")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 3.")

