def calcular_resultado(nombre, notas):
    """Devuelve un dict con nombre, calificaciones, promedio y estado."""
    if not isinstance(notas, (list, tuple)) or len(notas) == 0:
        raise ValueError("Notas deben ser una lista no vacía")
    notas_f = []
    try:
        notas_f = [float(n) for n in notas]
    except (TypeError, ValueError):
        raise ValueError("Todas las notas deben ser numeros")
    promedio = sum(notas_f) / len(notas_f)
    estado = "Aprobado" if promedio >= 70 else "Reprobado"
    return {
        "nombre": nombre,
        "calificaciones": notas_f,
        "promedio": promedio,
        "estado": estado,
    }


def procesar_estudiante_simple():
    """Solicita los datos del estudiante y muestra el resultado."""
    nombre = input("Ingrese nombre estudiante: ")
    try:
        nota1 = float(input(f"Ingrese primera nota para {nombre} (0-100): "))
        nota2 = float(input(f"Ingrese segunda nota para {nombre} (0-100): "))
        nota3 = float(input(f"Ingrese tercera nota para {nombre} (0-100): "))
    except ValueError:
        print("Error: notas deben ser numeros")
        return
    resultado = calcular_resultado(nombre, [nota1, nota2, nota3])
    print("\n--- Resultado del Estudiante ---")
    print(f"Nombre: {resultado['nombre']}")
    print(f"Calificaciones: {resultado['calificaciones']}")
    print(f"Promedio: {resultado['promedio']:.2f}")
    print(f"Estado: {resultado['estado']}")


def _self_test():
    r = calcular_resultado("Ana", [80, 70, 90])
    assert abs(r["promedio"] - (80 + 70 + 90) / 3) < 1e-9
    assert r["estado"] == "Aprobado"
    r2 = calcular_resultado("Bob", [60, 60, 60])
    assert r2["estado"] == "Reprobado"
    print("Self-tests passed")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        _self_test()
    else:
        procesar_estudiante_simple()
