primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

suma = primer_numero + segundo_numero
multiplicacion = primer_numero * segundo_numero
division = primer_numero / segundo_numero

print ("la suma de los dos numeros es:", suma)
print ("la multiplicacion de los dos numeros es:" , multiplicacion)
print ("la division de los dos numeros es:" , division)

#se pued poner // para que el resultado de la division sea un numero entero, sin decimales.
#es mejor poner float en vez de int para poder ingresar cualquier numero para ahorrarnos el error de ingresar un numero con decimales.
