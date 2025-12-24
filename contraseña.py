secreto = "Python123"
while True:
    intento = input("Introduce la contraseña: ")
    if intento == secreto:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta, intentalo de nuevo")

