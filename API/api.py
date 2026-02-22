import requests

mi_url = "https://api.frankfurter.app/latest?from=EUR&to=USD"
respuesta = requests.get(mi_url) # Usamos 'mi_url' que definimos arriba

datos = respuesta.json() 

valor_usd = datos["rates"]["USD"] 

print("Valor del USD (moneda base el euro):", valor_usd)

# Si queremos convertir la cantidad de euros a dólares que el usuario quiera, haecmos esto:

cantidad_euros = float(input("Ingrese la cantidad de euros que desea convertir a dólares: "))
cantidad_dolares = cantidad_euros * valor_usd
print(f"{cantidad_euros} euros equivalen a {cantidad_dolares} dólares.")