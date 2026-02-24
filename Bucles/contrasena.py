# Programa para verificar el PIN de un usuario utilizando un bucle while
pin_correcto = "1234"
intento = ""

print("BIENVENIDO AL BANCO ")

# Pide al usuario que introduzca su PIN hasta que sea correcto
while intento != pin_correcto:
    intento = input("Introduce tu PIN para continuar: ")
    
    if intento != pin_correcto:
        print("PIN incorrecto. Inténtalo de nuevo.")

print("Acceso concedido. ¡Bienvenido!")