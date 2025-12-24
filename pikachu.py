vida_pikachu = 100
ataque_enemigo = 15
while vida_pikachu > 0:
    print("Pikachu ha sido atacado")
    vida_pikachu -= ataque_enemigo
    if 0 <vida_pikachu < 20:
        print("¡Pikachu esta en peligro!")
    if vida_pikachu <= 0:
        print("¡Pikachu se ha debilitado")
    else:
        print(f"Vida restante :{vida_pikachu}")