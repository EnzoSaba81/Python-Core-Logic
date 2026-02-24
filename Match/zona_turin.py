status_code =input("ingresar zona en la que reside (ej: Centro, Crocetta, San Donato, Parella,Cenisia): ") .strip().capitalize()

match status_code:
    case "Centro" | "Crocetta":
        print ("el costo de esa zona es alto")
    case "San Donato" | "Vanchiglia":
        print("el costo de esa zona es medio")
    case "Parella" | "Cenisia":
        print("el costo de esa zona es bajo")
    case _:
        print("Zona desconocida.")