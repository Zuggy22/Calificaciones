def calcular_dv_rut(rut_cuerpo_str: str) -> str:
    """
    Calcula el Dígito Verificador (DV) de un RUT chileno usando el algoritmo Módulo 11.

    Args:
        rut_cuerpo_str: El número base del RUT como cadena de texto (ej: "19812753").

    Returns:
        El Dígito Verificador como una cadena de texto ('0'-'9' o 'K').
    """
    suma = 0
    factor = 2

    # 1. Iterar el RUT de derecha a izquierda
    for digito_char in reversed(rut_cuerpo_str):
        # Convertir el carácter del dígito a un entero
        digito = int(digito_char)

        # 2. Multiplicación y Suma
        suma += digito * factor

        # 3. Incrementar el factor (2, 3, 4, 5, 6, 7, 2, 3...)
        factor += 1
        if factor > 7:
            factor = 2  # Reiniciar el ciclo de factores

    # 4. Módulo 11 (Obtener el Resto)
    resto = suma % 11

    # 5. Cálculo del Dígito Provisional: 11 - Resto
    dv_provisional = 11 - resto

    # 6. Definición del Dígito Verificador Final
    if dv_provisional == 11:
        return '0'
    elif dv_provisional == 10:
        return 'K'
    else:
        return str(dv_provisional)


def formatear_rut(rut_cuerpo_str: str) -> str:
    """
    Función auxiliar para formatear el RUT con puntos (ej: "12345678" -> "12.345.678").
    """
    rut_formateado = ""
    contador = 0

    # Iterar de derecha a izquierda
    for digito in reversed(rut_cuerpo_str):
        if contador > 0 and contador % 3 == 0:
            rut_formateado = "." + rut_formateado

        rut_formateado = digito + rut_formateado
        contador += 1

    return rut_formateado


def main():
    """
    Función principal para la interacción con el usuario.
    """
    print("==================================================")
    print(" CALCULADORA DE DÍGITO VERIFICADOR (DV) DEL RUT ")
    print("==================================================")

    while True:
        rut_input = input("Ingrese el cuerpo del RUT (solo números, sin puntos ni guion): ").strip()

        # 1. Validación de la entrada
        if rut_input.isdigit():
            rut_cuerpo_str = rut_input
            break
        else:
            print("ERROR: La entrada es inválida. Por favor, ingrese solo números.")

    # 2. Ejecutar el cálculo
    dv = calcular_dv_rut(rut_cuerpo_str)

    # 3. Mostrar el resultado
    rut_formateado = formatear_rut(rut_cuerpo_str)

    print("\n--------------------------------------------------")
    print("RESULTADO:")
    print(f"El Dígito Verificador (DV) para el RUT {rut_cuerpo_str} es: {dv}")
    print(f"El RUT completo y formateado es: {rut_formateado}-{dv}")
    print("--------------------------------------------------")


if __name__ == "__main__":
    main()