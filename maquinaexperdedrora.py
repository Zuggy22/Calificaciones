opcion = input("Elije un producto(A,B o C):")
match opcion:
    case "A":
        print ("Aqui tienes tu refresco")
    case "B":
        print ("Aqui tienes tus papas fritas")
    case "C":
        print ("Aqui tienes tus galletas")
    case _:
        print ("Opcion no reconocida")