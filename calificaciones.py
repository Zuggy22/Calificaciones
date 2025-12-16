# Solicitar datos del estudiante
nombre = input("Ingrese su nombre: ")

while True:
    try:
        # Pide la nota y la convierte a float
        notas = float(input("Ingrese su nota final (0-100): "))

        # Verifica que la nota esté en el rango válido
        if 0 <= notas <= 100:
            break  # Sale del bucle si la nota es válida
        else:
            print("La nota debe estar entre 0 y 100.")

    # Captura errores si el usuario no introduce un número
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

# Determinar el resultado segun la nota
if notas >= 90:
    resultado = "Aprobado con distinción"
elif notas >= 70:
    resultado = "Aprobado"
elif notas >= 50:
    resultado = "Recuperación"
else:
    resultado = "Reprobado"

# Mostrar el resultado
print("\n--- Resultado Académico ---")
print(f"Estudiante: {nombre}")
print(f"Nota: {notas}")
print(f"Estado: {resultado}")