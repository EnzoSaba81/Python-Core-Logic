#Contexto: Un usuario quiere comprar un producto, pero no sabe si tiene suficiente dinero para comprarlo. 
# El programa le pedirá al usuario el precio del producto y la cantidad de dinero que tiene, y luego le dirá si puede comprar el producto o no. Si puede comprarlo, también le dirá cuánto dinero le quedará después de la compra. 
# Si no puede comprarlo, le dirá cuánto dinero le falta para poder comprarlo.

precio_producto = int(input("¿Cuánto cuesta el producto? "))
dinero_usuario = int(input("¿Cuánto dinero tenés? "))
if dinero_usuario >= precio_producto:
    vuelto = dinero_usuario - precio_producto
    print("Podés comprar el producto, tu vuelto es:", vuelto)
else:
    dinero_faltante = precio_producto - dinero_usuario
    print("No podés comprar el producto, te falta la siguente cantidad de dinero:", dinero_faltante)